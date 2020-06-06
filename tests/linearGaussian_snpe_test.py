import pytest
import torch
from torch import zeros, ones, eye
from torch.distributions import MultivariateNormal

import sbi.utils as utils
from tests.test_utils import (
    check_c2st,
    get_dkl_gaussian_prior,
    get_prob_outside_uniform_prior,
    get_normalization_uniform_prior,
)
from sbi.inference import SNPE_B
from sbi.inference import SNPE_C
from sbi.simulators.linear_gaussian import (
    true_posterior_linear_gaussian_mvn_prior,
    samples_true_posterior_linear_gaussian_uniform_prior,
    linear_gaussian,
    samples_true_posterior_linear_gaussian_mvn_prior_different_dims,
)

# Use cpu by default.
torch.set_default_tensor_type("torch.FloatTensor")
# Seeding:
# Some tests in this module have "set_seed" as an argument. This argument points to
# tests/conftest.py to seed the test with the seed set in conftext.py.


@pytest.mark.parametrize(
    "num_dim, prior_str", ((2, "gaussian"), (2, "uniform"), (1, "gaussian"),),
)
def test_c2st_snpe_on_linearGaussian(
    num_dim: int, prior_str: str, set_seed,
):
    """Test whether SNPE C infers well a simple example with available ground truth.

    Args:
        set_seed: fixture for manual seeding
    """

    x_o = zeros(1, num_dim)
    num_samples = 1000

    # likelihood_mean will be likelihood_shift+theta
    likelihood_shift = -1.0 * ones(num_dim)
    likelihood_cov = 0.3 * eye(num_dim)

    if prior_str == "gaussian":
        prior_mean = zeros(num_dim)
        prior_cov = eye(num_dim)
        prior = MultivariateNormal(loc=prior_mean, covariance_matrix=prior_cov)
        gt_posterior = true_posterior_linear_gaussian_mvn_prior(
            x_o[0], likelihood_shift, likelihood_cov, prior_mean, prior_cov
        )
        target_samples = gt_posterior.sample((num_samples,))
    else:
        prior = utils.BoxUniform(-2.0 * ones(num_dim), 2.0 * ones(num_dim))
        target_samples = samples_true_posterior_linear_gaussian_uniform_prior(
            x_o, likelihood_shift, likelihood_cov, prior=prior, num_samples=num_samples
        )

    simulator = lambda theta: linear_gaussian(theta, likelihood_shift, likelihood_cov)

    infer = SNPE_C(
        simulator=simulator,
        density_estimator=None,  # Use default MAF.
        prior=prior,
        z_score_x=True,
        simulation_batch_size=10,
        retrain_from_scratch_each_round=False,
        discard_prior_samples=False,
        show_progressbar=False,
        num_atoms=None,
        sample_with_mcmc=False,
    )

    posterior = infer(num_rounds=1, num_simulations_per_round=2000)  # type: ignore
    posterior.freeze(x_o=x_o)
    samples = posterior.sample(num_samples, x=x_o)

    # Compute the c2st and assert it is near chance level of 0.5.
    check_c2st(samples, target_samples, alg="snpe_c")

    # Checks for log_prob()
    if prior_str == "gaussian":
        # For the Gaussian prior, we compute the KLd between ground truth and posterior.
        dkl = get_dkl_gaussian_prior(
            posterior, x_o[0], likelihood_shift, likelihood_cov, prior_mean, prior_cov
        )

        max_dkl = 0.1 if num_dim == 1 else 0.8

        assert (
            dkl < max_dkl
        ), f"D-KL={dkl} is more than 2 stds above the average performance."

    elif prior_str == "uniform":
        # Check whether the returned probability outside of the support is zero.
        posterior_prob = get_prob_outside_uniform_prior(posterior, num_dim)
        assert (
            posterior_prob == 0.0
        ), "The posterior probability outside of the prior support is not zero"

        # Check whether normalization (i.e. scaling up the density due
        # to leakage into regions without prior support) scales up the density by the
        # correct factor.
        (
            posterior_likelihood_unnorm,
            posterior_likelihood_norm,
            acceptance_prob,
        ) = get_normalization_uniform_prior(posterior, prior, x_o)
        # The acceptance probability should be *exactly* the ratio of the unnormalized
        # and the normalized likelihood. However, we allow for an error margin of 1%,
        # since the estimation of the acceptance probability is random (based on
        # rejection sampling).
        assert (
            acceptance_prob * 0.99
            < posterior_likelihood_unnorm / posterior_likelihood_norm
            < acceptance_prob * 1.01
        ), "Normalizing the posterior density using the acceptance probability failed."


def test_c2st_snpe_on_linearGaussian_different_dims(set_seed):
    """Test whether SNPE B/C infer well a simple example with available ground truth.

    This example has different number of parameters theta than number of x. Also
    this implicitly tests simulation_batch_size=1.

    Args:
        set_seed: fixture for manual seeding
    """

    theta_dim = 3
    x_dim = 2
    discard_dims = theta_dim - x_dim

    x_o = zeros(1, x_dim)
    num_samples = 1000

    # likelihood_mean will be likelihood_shift+theta
    likelihood_shift = -1.0 * ones(x_dim)
    likelihood_cov = 0.3 * eye(x_dim)

    prior_mean = zeros(theta_dim)
    prior_cov = eye(theta_dim)
    prior = MultivariateNormal(loc=prior_mean, covariance_matrix=prior_cov)
    target_samples = samples_true_posterior_linear_gaussian_mvn_prior_different_dims(
        x_o[0],
        likelihood_shift,
        likelihood_cov,
        prior_mean,
        prior_cov,
        num_discarded_dims=discard_dims,
        num_samples=num_samples,
    )

    simulator = lambda theta: linear_gaussian(
        theta, likelihood_shift, likelihood_cov, num_discarded_dims=discard_dims
    )

    snpe_common_args = dict(
        simulator=simulator,
        density_estimator=None,  # Use default MAF.
        prior=prior,
        z_score_x=True,
        simulation_batch_size=1,
        retrain_from_scratch_each_round=False,
        discard_prior_samples=False,
        show_progressbar=False,
    )

    infer = SNPE_C(sample_with_mcmc=False, **snpe_common_args)

    posterior = infer(num_rounds=1, num_simulations_per_round=2000)  # type: ignore
    samples = posterior.sample(num_samples, x=x_o)

    # Compute the c2st and assert it is near chance level of 0.5.
    check_c2st(samples, target_samples, alg="snpe_c")


# Test multi-round SNPE.
@pytest.mark.slow
@pytest.mark.parametrize(
    "algorithm_str",
    (
        pytest.param(
            "snpe_b",
            marks=pytest.mark.xfail(
                raises=NotImplementedError, reason="""SNPE-B not implemented""",
            ),
        ),
        "snpe_c",
    ),
)
def test_c2st_multi_round_snpe_on_linearGaussian(algorithm_str: str, set_seed):
    """Test whether SNPE B/C infer well a simple example with available ground truth.

    Args:
        set_seed: fixture for manual seeding.
    """

    num_dim = 2
    x_o = zeros((1, num_dim))
    num_samples = 1000

    # likelihood_mean will be likelihood_shift+theta
    likelihood_shift = -1.0 * ones(num_dim)
    likelihood_cov = 0.3 * eye(num_dim)

    prior_mean = zeros(num_dim)
    prior_cov = eye(num_dim)
    prior = MultivariateNormal(loc=prior_mean, covariance_matrix=prior_cov)
    gt_posterior = true_posterior_linear_gaussian_mvn_prior(
        x_o[0], likelihood_shift, likelihood_cov, prior_mean, prior_cov
    )
    target_samples = gt_posterior.sample((num_samples,))

    simulator = lambda theta: linear_gaussian(theta, likelihood_shift, likelihood_cov)

    snpe_common_args = dict(
        simulator=simulator,
        density_estimator=None,  # Use default MAF.
        prior=prior,
        z_score_x=True,
        retrain_from_scratch_each_round=False,
        show_progressbar=False,
    )

    if algorithm_str == "snpe_b":
        infer = SNPE_B(simulation_batch_size=10, **creation_args)
        posterior = infer(**call_args)
    elif algorithm_str == "snpe_c":
        infer = SNPE_C(
            simulation_batch_size=50, sample_with_mcmc=False, **creation_args
        )
        posterior = infer(num_atoms=10, **call_args)

    posterior = infer(num_rounds=2, x_o=x_o, num_simulations_per_round=1000)  # type: ignore
    samples = posterior.sample(num_samples)

    # Compute the c2st and assert it is near chance level of 0.5.
    check_c2st(samples, target_samples, alg=algorithm_str)


_fail_reason_deterministic_sim = """If the simulator has truely deterministic (even
partial) outputs, the inference can succeed with z_score_std > 0, but the log posterior
will have infinites, which we reject."""


@pytest.mark.slow
@pytest.mark.parametrize(
    "z_score_min_std",
    (
        pytest.param(
            0.0,
            marks=pytest.mark.xfail(
                raises=NotImplementedError, reason=_fail_reason_deterministic_sim,
            ),
        ),
        pytest.param(
            1e-7,
            marks=pytest.mark.xfail(
                raises=NotImplementedError, reason="""SNPE-B not implemented""",
            ),
        ),
    ),
)
def test_multi_round_snpe_deterministic_simulator(set_seed, z_score_min_std):
    """Test if a deterministic simulator breaks inference for SNPE-C.

    Args:
        set_seed: fixture for manual seeding
    """

    num_dim = 3
    x_o = zeros((1, num_dim))

    # likelihood_mean will be likelihood_shift+theta
    likelihood_shift = -1.0 * ones(num_dim)
    likelihood_cov = 0.3 * eye(num_dim)

    prior_mean = zeros(num_dim)
    prior_cov = eye(num_dim)
    prior = MultivariateNormal(loc=prior_mean, covariance_matrix=prior_cov)

    simulator = lambda theta: linear_gaussian(theta, likelihood_shift, likelihood_cov)

    def deterministic_simulator(theta):
        """Simulator with deterministic last output dimension (across batches)."""
        result = simulator(theta)
        result[:, num_dim - 1] = 1.0

        return result

    infer = SNPE_C(
        simulator=deterministic_simulator,
        density_estimator=None,  # Use default MAF.
        prior=prior,
        z_score_x=True,
        retrain_from_scratch_each_round=False,
        simulation_batch_size=10,
        z_score_min_std=z_score_min_std,
        show_progressbar=False,
    )

    infer(num_rounds=2, x_o=x_o, num_simulations_per_round=1000)


# Testing rejection and mcmc sampling methods.
@pytest.mark.slow
@pytest.mark.parametrize(
    "sample_with_mcmc, mcmc_method, prior_str",
    (
        (True, "slice_np", "gaussian"),
        (True, "slice", "gaussian"),
        # XXX (True, "slice", "uniform"),
        # XXX takes very long. fix when refactoring pyro sampling
        (False, "rejection", "uniform"),
    ),
)
def test_api_snpe_c_posterior_correction(
    sample_with_mcmc, mcmc_method, prior_str, set_seed
):
    """Test that leakage correction applied to sampling works, with both MCMC and
    rejection.

    Args:
        set_seed: fixture for manual seeding
    """

    num_dim = 2
    x_o = zeros(1, num_dim)

    # likelihood_mean will be likelihood_shift+theta
    likelihood_shift = -1.0 * ones(num_dim)
    likelihood_cov = 0.3 * eye(num_dim)

    if prior_str == "gaussian":
        prior_mean = zeros(num_dim)
        prior_cov = eye(num_dim)
        prior = MultivariateNormal(loc=prior_mean, covariance_matrix=prior_cov)
    else:
        prior = utils.BoxUniform(-2.0 * ones(num_dim), 2.0 * ones(num_dim))

    simulator = lambda theta: linear_gaussian(theta, likelihood_shift, likelihood_cov)

    infer = SNPE_C(
        simulator=simulator,
        density_estimator=None,  # Use default MAF.
        prior=prior,
        num_atoms=None,
        z_score_x=True,
        simulation_batch_size=50,
        use_combined_loss=False,
        retrain_from_scratch_each_round=False,
        discard_prior_samples=False,
        sample_with_mcmc=sample_with_mcmc,
        mcmc_method=mcmc_method,
        show_progressbar=False,
    )

    posterior = infer(num_rounds=1, num_simulations_per_round=1000, max_num_epochs=5)

    # Posterior should be corrected for leakage even if num_rounds just 1.
    samples = posterior.sample(10, x=x_o)

    # Evaluate the samples to check correction factor.
    posterior.log_prob(samples, x=x_o)
