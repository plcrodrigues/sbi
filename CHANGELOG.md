# Changelog

## v0.24.0

### ✨ Highlights

- feat: add `CategoricalMADE` by @jnsbck in https://github.com/sbi-dev/sbi/pull/1269  **(Major New Feature)**
- tests: `mini-sbibm` by @manuelgloeckler in https://github.com/sbi-dev/sbi/pull/1335 **(Major New Feature)**
- feat: Score-based iid sampling by @manuelgloeckler in https://github.com/sbi-dev/sbi/pull/1381 **(Major New Feature)**
- Drop python3.9 support, fix ci by @janfb in https://github.com/sbi-dev/sbi/pull/1412 **(Python Version Support Change)**
- additional features for NPSE by @gmoss13 in https://github.com/sbi-dev/sbi/pull/1370 **(Enhancement)**

### 🐛 Bug Fixes

- #1350 leakage correction breaks consistency of log prob vs log prob batched by @manuelgloeckler in https://github.com/sbi-dev/sbi/pull/1355
- fix #1343 device handling in mog_log_prob by @janfb in https://github.com/sbi-dev/sbi/pull/1356
- Fix failing tutorials, change MNLE default for log_transform to False by @janfb in https://github.com/sbi-dev/sbi/pull/1367
- Fix conditional posterior shape and device bugs. by @janfb in https://github.com/sbi-dev/sbi/pull/1373
- fix: type fix in VI subclasses. xfail pymc tests. by @janfb in https://github.com/sbi-dev/sbi/pull/1390
- Temporary Wrappers to fix MADE by @gmoss13 in https://github.com/sbi-dev/sbi/pull/1398
- Fix mnle tests, MCMC init pbar, sir batch size. by @janfb in https://github.com/sbi-dev/sbi/pull/1410
- fix mnle tests by @janfb in https://github.com/sbi-dev/sbi/pull/1415
- fix: protocol and refactor for custom potential by @janfb in https://github.com/sbi-dev/sbi/pull/1409
- fix docs workflow by @janfb in https://github.com/sbi-dev/sbi/pull/1419
- fix: gpu-handling for CategoricalMADE by @janfb in https://github.com/sbi-dev/sbi/pull/1448

### 🛠️ Maintenance & Improvements

- increase tutorial test timeout by @janfb in https://github.com/sbi-dev/sbi/pull/1360
- add nan check to _loss method. by @janfb in https://github.com/sbi-dev/sbi/pull/1361
- Update and pin pre commit and ruff to recent version. by @janfb in https://github.com/sbi-dev/sbi/pull/1358
- add nan handling in diagnostics by @janfb in https://github.com/sbi-dev/sbi/pull/1359
- Improve tests to detect circular imports and resolve all of them by @manuelgloeckler in https://github.com/sbi-dev/sbi/pull/1357
- docs: add details about zuko density estimators by @janfb in https://github.com/sbi-dev/sbi/pull/1387
- fix: duplication of 'large number' in warning by @turnmanh in https://github.com/sbi-dev/sbi/pull/1391
- improve PR and issue templates by @janfb in https://github.com/sbi-dev/sbi/pull/1399
- perf: speed up CI with uv by @janfb in https://github.com/sbi-dev/sbi/pull/1400
- tests: add pytest testmon plugin to speed up CI by @janfb in https://github.com/sbi-dev/sbi/pull/1402
- small fixes to score methods by @janfb in https://github.com/sbi-dev/sbi/pull/1404
- docs: Corrected python version in installation document (Revised) by @VijaySamant4368 in https://github.com/sbi-dev/sbi/pull/1423
- docs: Markdown formatting compliant to Markdown Linter (solves #1434) by @nMaax in https://github.com/sbi-dev/sbi/pull/1443

### 🎉 New Contributors

- @VijaySamant4368 made their first contribution in https://github.com/sbi-dev/sbi/pull/1423
- @nMaax made their first contribution in https://github.com/sbi-dev/sbi/pull/1443

**Full Changelog**: https://github.com/sbi-dev/sbi/compare/v0.23.3...v0.24.0

## v0.23.3

### Highlights 🤩

- docs: Add conda-forge install instructions by @matthewfeickert in <https://github.com/sbi-dev/sbi/pull/1340>
- feat: `NLE` with multiple iid conditions by @janfb in <https://github.com/sbi-dev/sbi/pull/1331>

### What's Changed 🚧

- fix: Correted typo in y-axis label by @turnmanh in <https://github.com/sbi-dev/sbi/pull/1296>
- docs: update embedding networks notebook by @emmanuel-ferdman in <https://github.com/sbi-dev/sbi/pull/1297>
- fix pickle issues in MCMC posterior + test by @manuelgloeckler in <https://github.com/sbi-dev/sbi/pull/1291>
- Minor fix for EnsemblePosterior weights.setter by @CompiledAtBirth in <https://github.com/sbi-dev/sbi/pull/1299>
- Remove deprecated neural_net access from `utils` by @tvwenger in <https://github.com/sbi-dev/sbi/pull/1302>
- [test] add tests for ensemble posterior weights by @samadpls in <https://github.com/sbi-dev/sbi/pull/1307>
- Clarify last round behavior of SNPE-A by @michaeldeistler in <https://github.com/sbi-dev/sbi/pull/1323>
- expose batched sampling option; error handling by @janfb in <https://github.com/sbi-dev/sbi/pull/1321>
- Fix #1316: remove sample_dim docstring for condition. by @janfb in <https://github.com/sbi-dev/sbi/pull/1338>
- docs: fix tutorial typos by @janfb in <https://github.com/sbi-dev/sbi/pull/1341>
- docs: run and seed SBC tutorial by @manuel-morales-a in <https://github.com/sbi-dev/sbi/pull/1336>

### New Contributors 🎉

- @emmanuel-ferdman made their first contribution in <https://github.com/sbi-dev/sbi/pull/1297>
- @CompiledAtBirth made their first contribution in <https://github.com/sbi-dev/sbi/pull/1299>
- @tvwenger made their first contribution in <https://github.com/sbi-dev/sbi/pull/1302>
- @matthewfeickert made their first contribution in <https://github.com/sbi-dev/sbi/pull/1340>
- @manuel-morales-a made their first contribution in <https://github.com/sbi-dev/sbi/pull/1336>

**Full Changelog**: <https://github.com/sbi-dev/sbi/compare/v0.23.2...v0.23.3>

## v0.23.2

### Bug Fixes

- fixup for failing hmc test by @michaeldeistler (#1247)
- fix: make RestrictedPrior a distribution to enable log_prob @janfb (#1257)
- fix: npe iid handling by @janfb (#1262)
- fix: tutorials test error handling, fix bugs in tutorials by @janfb (#1264)
- fix #1260: include points in plotting limits by @janfb (#1265)
- fix: conditioned potential error handling by @janfb, @michaeldeistler (#1275, #1289)
- fix: Allow 1D pytorch distributions by @michaeldeistler (#1286)

### Documentation

- Rename SNPE to NPE in the README by @michaeldeistler (#1248)
- update pickling FAQ by @michaeldeistler (#1255)
- Adding example for custom DataLoader to tutorial 18 by @psteinb (#1256)
- docs: add readme intro to docs landing page by @janfb (#1272)
- Change sampling method for LC2ST to `sample_batched()` by @JuliaLinhart (#1279)

### Maintenance

- Refactor simulate_for_sbi location by @samadpls (#1253)
- build: devcontainer update by @janfb (#1252)
- fix: docker notebook python version by @janfb (#1258)
- refactor: remove outputs except plots from tutorials. by @janfb (#1266)
- build: automatic nb stripping and pypi upload by @janfb (#1267)
- refactor: remove deprecated x_shape where not needed by @janfb (#1271)
- more explicit error message for CNN shapes by @Ankush7890 (#1281)

## v0.23.1

- fix: include `score` folder by adding `__init__.py` (#1245 #1246)

## v0.23.0

### Announcements

- Re-licensing: license change from
  [AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html) to
  [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) (see #997 for
  details)
- `sbi` is now affiliated with [`NumFOCUS`](https://numfocus.org) 🎉
- New contributors 🎉: @anastasiakrouglova, @theogruner, @felixp8, @Matthijspals,
  @jsvetter, @pfuhr, @turnmanh, @fariedabuzaid, @augustes, @zinastef, @Baschdl,
  @danielmk, @lisahaxel, @janko-petkovic, @samadpls, @ThomasGesseyJonesPX, @schroedk

### Major Changes

- internal renaming of all inference classes from, e.g., `SNPE` to `NPE` (i.e., we
  removed the `S` prefix). The functionality of the classes remains the same. The NPE
  class handles both the amortized and sequential versions of neural posterior
  estimation. An alias for SNPE (and other sequential methods) still exists for
  backwards compatibility (#1238) (@michaeldeistler).
- change `sbi` default parameters: `training_batch_size=200`, `num_chains=20` (#1221)
  (@janfb)
- change imports of `posterior_nn`, `likelihood_nn`, and `classifier_nn`. They should
  now be imported from `sbi.neural_nets`, not from `sbi.utils` (#994) (@famura)
- big refactoring of plotting utilities, new tutorial (#1084) (@Matthijspals)
- improved tutorials and website documentation (#1012, #1051, #1073) (@augustes,
  @zinaStef, @lisahaxel, @psteinb)
- improved website structure and contribution guides (#1019) (@tomMoral, @janfb)
- drop support for python3.8 and torch1.12 (#1233)
- refactor folder structure and naming of `neural_nets` (#1237) (@michaeldeistler)

### New Features

- full flexibility over the training loop (#983) (@michaeldeistler)
- unified density estimator classes (#952, #965, #979, #1151) (@michaeldeistler,
  @gmoss13, @tomMoral, @manualgloeckler)
- vectorized sampling and log_prob for `(S)NPE` given batches of x (#1153)
  (@manuelgloeckler, @michaeldeistler)
- batched sampling for vectorized MCMC samplers (#1176, #1210) (@gmoss13, @janfb)
- support @zuko as a backend for normalizing flows (#1088, #1116)
  (@anastasiakrouglova)
- local c2st metric (#1109) (@JuliaLinhart)
- tarp coverage metric (#1106) (@psteinb)
- add interface for @PyMC samplers (#1053) (@famura, @felixp8)
- flow matching density estimators (#1049) (@turnmanh, @fariedabuzaid, @janfb)
- score matching density estimators (#1015) (@rdgao, @jsvetter, @pfuhr,
  @manuelgloeckler, @michaeldeistler, @janfb)
- ABC methods for trial-based data using statistical distances (#1104)
  (@theogruner)
- support Apple MPS as gpu device (#912) (@janfb)
- dev container for using `sbi` in codespaces on GitHub (#1070) (@turnmanh)
- enable importance sampling for likelihood-based estimators (#1183) (@manuelgloeckler)
- refactoring and unified shape handling for `RatioEstimator` (#1097) (@bkmi)
- faster sbc and tarp calibration checks via batched sampling (#1196) (@janfb)
- batched sampling and embedding net support for `MNLE` (#1203) (@janfb)
- adapt `MNLE` to new densitye stimator abstraction (#1089) (@coschroeder)
- better plotting options for coverage plots (#1039, #1212) (@janfb)
- allow for potential_fn to be a Callable (#943) (@michaeldeistler)

### Bug Fixes

- bugfix for embedding net tutorial (#1159) (@deismic)
- Fixup for process_x in EnsemblePosterior (#1148) (@deismic)
- fixed notebook by changing MCMC parameters (#1058) (@zinaStef)
- fix: add NeuralPosteriorEnsemble to utils.__init__ (#1002) (@jnsbck)
- fix: print_false_positive_rate (#976) (@danielmk)
- fix: make VIPosterior pickable (#951) (@manuelgloeckler)
- fix: bug in importance sampled posterior (#1081) (@max-dax)
- fix: embedding device and warning handling (#1186) (@janfb)
- fix: c2st with constant features (#1204) (@janfb)
- fix: erroneous warnings about different devices (#1225, @ThomasGesseyJonesPX)
- fix: type annotation in class `ConditionedPotential` (#1222) (@schroedk)

### Maintenance and other changes

- add pre-commit hooks (#955) (@janfb)
- add ruff to replace `isort`, `black`, `flake` (#960, #978, #1113) (@janfb)
- switch to `pyproject.toml` for package specification (#941) (@janfb)
- Split the GitHub workflow in CI and CD (#1063) (@famura)
- split linting process from the CI/CD workflow (#1164) (@tomMoral)
- Switch to the newest `pyright` and fix all typing errors (#1045, #1108) (@Baschdl)
- introduce two docs versions: `latest` pointing to latest release at
  <https://sbi-dev.github.io/sbi/latest/> and `dev` pointing to the latest version on
  `main` <https://sbi-dev.github.io/sbi/dev/>

## v0.22.0

### API change

- We have moved `sbi` to an new github organization: `https://github.com/sbi-dev/sbi`
- We have changed the website of the `sbi` docs: `https://sbi-dev.github.io/sbi/`.
- `sbi.analysis.pairplot`: `upper` was replaced by `offdiag` and will be deprecated in a future release.

### Features and enhancements

- size-invariant embedding nets for amortized inference with iid-data (@janfb, #808)
- option for new using MAF with rational quadratic splines (thanks to @ImahnShekhzadeh, #819)
- improved docstring for `process_prior` (thanks to @musoke, #813)
- extended tutorial for SBI with iid data (@janfb, #857)
- new tutorial for SBI with experimental conditions and mixed data (@janfb, #829)
- New options for `pairplot`:
  - `upper` is now called `offdiag` to match other kwargs.
  - alternating colors for `samples` and `points`
  - option to add a `legend` and pass `kwargs` for the legend.

### Bug fixes

- fixed memory leak in in `append_simulations` (thanks to @VictorSven, #803)
- bug fix for CNRE (thanks to @bkmi, #815)
- bug fix for iid-inference with posterior ensembles (@janfb, #826)
- bug fix for simulation-based calibration with VI posteriors (@janfb, #834, #838)
- bug fix for BoxUniform device handling (@janfb, #854, #856)
- bug fix for MAP estimates with independent priors (@janfb, #867)
- bug fix for tutorial on SBC (@michaeldeistler, #891)
- fix spurious seeding for `simulate_for_sbi` (@jan-matthis, #876)
- bump python version of github action tests to `3.9.13` (@michaeldeistler, #888, #900)

## v0.21.0

- implementation of ["Contrastive Neural Ratio Estimation"](https://openreview.net/forum?id=kOIaB1hzaLe) (thanks to @bkmi, #787)
- implementation of ["Balanced Neural Ratio Estimation"](https://openreview.net/forum?id=o762mMj4XK) (thanks to @ADelau, #779)
- bugfixes for SBC, device handling and iid-data (#793, #789, #780)

## v0.20.0

### Major changes and bug fixes

- implementation of ["Truncated proposals for scalable and hassle-free sbi"](https://openreview.net/forum?id=QW98XBAqNRa) (#754)
- sample-based expected coverage tests (#754)
- permutation invariant embedding to allow iid data in SNPE (thanks @coschroeder, #751)
- convolutional neural network embedding (thanks @coschroeder, #745, #751, #769)
- disallow invalid simulations when using SNLE, SNRE, or atomic SNPE-C (#768)

### Enhancements

- add tutorial on all available methods (#754)
- allow seeding of `simulate_for_sbi` on multiple workers (#762)
- expose `enable_transforms` in sampler interface (#756)
- bugfix for building the transformation of transformed distributions (#756)

## v0.19.2

- Rely on new version of `pyknos` with bugfix for APT with MDNs (#734)
- bugfix: atomic SNPE-C now allows any kind of proposal (#732)
- bugfix for SNPE with implicit prior on GPU (#730)
- SNPE-A has `force_first_round_loss=True` as default (#729)

## v0.19.1

- bug fix for `ArviZ` integration (#727)

## v0.19.0

### Major changes and bug fixes

- new option to sample posterior using importance sampling (#692)
- new option to use `arviz` for posterior plotting and MCMC diagnostics (#546, #607, thanks to @sethaxen)
- fixes for using the `VIPosterior` with `MultipleIndependent` prior, a51e93b
- bug fix for sir (sequential importance reweighting) for MCMC initialization (#692)
- bug fix for SNPE-A 565082c
- bug fix for validation loader batch size (#674, thanks to @bkmi)
- small bug fixes for `pairplot` and MCMC kwargs

### Enhancements

- improved and new tutorials:
  - Tutorial for simulation-based calibration (SBC) (#629, thanks to @psteinb)
  - Tutorial for sampling the conditional posterior (#667)
- new option to use first-round loss in all rounds
- simulated data is now stored as `Dataset` to reduce memory load and add flexibility
  with large data sets (#685, thanks to @tbmiller-astro)
- refactoring of summary write for better training logs with tensorboard (#704)
- new option to find peaks of 1D posterior marginals without gradients (#707, #708, thanks to @Ziaeemehr)
- new option to not use parameter transforms in `DirectPosterior` for more flexibility with custom priors (#714)

## v0.18.0

### Breaking changes

- Posteriors saved under `sbi` `v0.17.2` or older can not be loaded under `sbi`
`v0.18.0` or newer.
- `sample_with` can no longer be passed to `.sample()`. Instead, the user has to rerun
`.build_posterior(sample_with=...)`. (#573)
- the `posterior` no longer has the the method `.sample_conditional()`. Using this
  feature now requires using the `sampler interface` (see tutorial
  [here](https://sbi-dev.github.io/sbi/tutorial/07_conditional_distributions/)) (#573)
- `retrain_from_scratch_each_round` is now called `retrain_from_scratch` (#598, thanks to @jnsbck)
- API changes that had been introduced in `sbi v0.14.0` and `v0.15.0` are not enforced. Using the interface prior to
  those changes leads to an error (#645)
- prior passed to SNPE / SNLE / SNRE must be a PyTorch distribution (#655), see FAQ-7 for how to pass use custom prior.

### Major changes and bug fixes

- new `sampler interface` (#573)
- posterior quality assurance with simulation-based calibration (SBC) (#501)
- added `Sequential Neural Variational Inference (SNVI)` (Glöckler et al. 2022) (#609, thanks to @manuelgloeckler)
- bugfix for SNPE-C with mixture density networks (#573)
- bugfix for sampling-importance resampling (SIR) as `init_strategy` for MCMC (#646)
- new density estimator for neural likelihood estimation with mixed data types (MNLE, #638)
- MCMC can now be parallelized across CPUs (#648)
- improved device check to remove several GPU issues (#610, thanks to @LouisRouillard)

### Enhancements

- pairplot takes `ax` and `fig` (#557)
- bugfix for rejection sampling (#561)
- remove warninig when using multiple transforms with NSF in single dimension (#537)
- Sampling-importance-resampling (SIR) is now the default `init_strategy` for MCMC (#605)
- change `mp_context` to allow for multi-chain pyro samplers (#608, thanks to @sethaxen)
- tutorial on posterior predictive checks (#592, thanks to @LouisRouillard)
- add FAQ entry for using a custom prior (#595, thanks to @jnsbck)
- add methods to plot tensorboard data (#593, thanks to @lappalainenj)
- add option to pass the support for custom priors (#602)
- plotting method for 1D marginals (#600, thanks to @guymoss)
- fix GPU issues for `conditional_pairplot` and `ActiveSubspace` (#613)
- MCMC can be performed in unconstrained space also when using a `MultipleIndependent` distribution as prior (#619)
- added z-scoring option for structured data (#597, thanks to @rdgao)
- refactor c2st; change its default classifier to random forest (#503, thanks to @psteinb)
- MCMC `init_strategy` is now called `proposal` instead of `prior` (#602)
- inference objects can be serialized with `pickle` (#617)
- preconfigured fully connected embedding net (#644, thanks to @JuliaLinhart #624)
- posterior ensembles (#612, thanks to @jnsbck)
- remove gradients before returning the `posterior` (#631, thanks to @tomMoral)
- reduce batchsize of rejection sampling if few samples are left (#631, thanks to @tomMoral)
- tutorial for how to use SBC (#629, thanks to @psteinb)
- tutorial for how to use SBI with trial-based data and mixed data types (#638)
- allow to use a `RestrictedPrior` as prior for `SNPE` (#642)
- optional pre-configured embedding nets (#568, #644, thanks to @JuliaLinhart)

## v0.17.2

### Minor changes

- bug fix for transforms in KDE (#552)

## v0.17.1

### Minor changes

- improve kwarg handling for rejection abc and smcabc
- typo and link fixes (#549, thanks to @pitmonticone)
- tutorial notebook on crafting summary statistics with sbi (#511, thanks to @ybernaerts)
- small fixes and improved documenentation for device handling (#544, thanks to @milagorecki)

## v0.17.0

### Major changes

- New API for specifying sampling methods (#487). Old syntax:

```python
posterior = inference.build_posterior(sample_with_mcmc=True)
```

New syntax:

```python
posterior = inference.build_posterior(sample_with="mcmc")  ## or "rejection"
```

- Rejection sampling for likelihood(-ratio)-based posteriors (#487)
- MCMC in unconstrained and z-scored space (#510)
- Prior is now allowed to lie on GPU. The prior has to be on the same device as the one
  passed for training (#519).
- Rejection-ABC and SMC-ABC now return the accepted particles / parameters by default,
  or a KDE fit on those particles (`kde=True`) (#525).
- Fast analytical sampling, evaluation and conditioning for `DirectPosterior` trained
  with MDNs (thanks @jnsbck #458).

### Minor changes

- `scatter` allowed for diagonal entries in pairplot (#510)
- Changes to default hyperparameters for `SNPE_A` (thanks @famura, #496, #497)
- bugfix for `within_prior` checks (#506)

## v0.16.0

### Major changes

- Implementation of SNPE-A (thanks @famura and @theogruner, #474, #478, #480, #482)
- Option to do inference over iid observations with SNLE and SNRE (#484, #488)

### Minor changes

- Fixed unused argument `num_bins` when using `nsf` as density estimator (#465)
- Fixes to adapt to the new support handling in `torch` `v1.8.0` (#469)
- More scalars for monitoring training progress (thanks @psteinb #471)
- Fixed bug in `minimal.py` (thanks @psteinb, #485)
- Depend on `pyknos` `v0.14.2`

## v0.15.1

- add option to pass `torch.data.DataLoader` kwargs to all inference methods (thanks @narendramukherjee, #445)
- fix bug due to release of `torch` `v1.8.0` (#451)
- expose `leakage_correction` parameters for `log_prob` correction in unnormalized
  posteriors (thanks @famura, #454)

## v0.15.0

### Major changes

- Active subspaces for sensitivity analysis (#394, [tutorial](https://sbi-dev.github.io/sbi/tutorial/09_sensitivity_analysis/))
- Method to compute the maximum-a-posteriori estimate from the posterior (#412)

### API changes

- `pairplot()`, `conditional_pairplot()`, and `conditional_corrcoeff()` should now be imported from `sbi.analysis` instead of `sbi.utils` (#394).
- Changed `fig_size` to `figsize` in pairplot (#394).
- moved `user_input_checks` to `sbi.utils` (#430).

### Minor changes

- Depend on new `joblib=1.0.0` and fix progress bar updates for multiprocessing (#421).
- Fix for embedding nets with `SNRE` (thanks @adittmann, #425).
- Is it now optional to pass a prior distribution when using SNPE (#426).
- Support loading of posteriors saved after `sbi v0.15.0` (#427, thanks @psteinb).
- Neural network training can be resumed (#431).
- Allow using NSF to estimate 1D distributions (#438).
- Fix type checks in input checks (thanks @psteinb, #439).
- Bugfix for GPU training with SNRE_A (thanks @glouppe, #442).

## v0.14.3

- Fixup for conditional correlation matrix (thanks @JBeckUniTb, #404)
- z-score data using only the training data (#411)

## v0.14.2

- Small fix for SMC-ABC with semi-automatic summary statistics (#402)

## v0.14.1

- Support for training and sampling on GPU including fixes from `nflows` (#331)
- Bug fix for SNPE with neural spline flow and MCMC (#398)
- Small fix for SMC-ABC particles covariance
- Small fix for rejection-classifier (#396)

## v0.14.0

- New flexible interface API (#378). This is going to be a breaking change for users of
the flexible interface and you will have to change your code. Old syntax:

```python
from sbi.inference import SNPE, prepare_for_sbi

simulator, prior = prepare_for_sbi(simulator, prior)
inference = SNPE(simulator, prior)

## Simulate, train, and build posterior.
posterior = inference(num_simulation=1000)
```

New syntax:

```python
from sbi.inference import SNPE, prepare_for_sbi, simulate_for_sbi

simulator, prior = prepare_for_sbi(simulator, prior)
inference = SNPE(prior)

theta, x = simulate_for_sbi(simulator, proposal=prior, num_simulations=1000)
density_estimator = inference.append_simulations(theta, x).train()
posterior = inference.build_posterior(density_estimator)  ## MCMC kwargs go here.
```

More information can be found here [here](https://sbi-dev.github.io/sbi/tutorial/02_flexible_interface/).

- Fixed typo in docs for `infer` (thanks @glouppe, #370)
- New `RestrictionEstimator` to learn regions of bad simulation outputs (#390)
- Improvements for and new ABC methods (#395)
  - Linear regression adjustment as in Beaumont et al. 2002 for both MCABC and SMCABC
  - Semi-automatic summary statistics as in Fearnhead & Prangle 2012 for both MCABC and SMCABC
  - Small fixes to perturbation kernel covariance estimation in SMCABC.

## v0.13.2

- Fix bug in SNRE (#363)
- Fix warnings for multi-D x (#361)
- Small improvements to MCMC, verbosity and continuing of chains (#347, #348)

## v0.13.1

- Make logging of vectorized numpy slice sampler slightly less verbose and address NumPy future warning (#347)
- Allow continuation of MCMC chains (#348)

## v0.13.0

- Conditional distributions and correlations for analysing the posterior (#321)
- Moved rarely used arguments from pairplot into kwargs (#321)
- Sampling from conditional posterior (#327)
- Allow inference with multi-dimensional x when appropriate embedding is passed (#335)
- Fixes a bug with clamp_and_warn not overriding num_atoms for SNRE and the warning message itself (#338)
- Compatibility with Pyro 1.4.0 (#339)
- Speed up posterior rejection sampling by introducing batch size (#340, #343)
- Allow vectorized evaluation of numpy potentials (#341)
- Adds vectorized version of numpy slice sampler which allows parallel log prob evaluations across all chains (#344)

## v0.12.2

- Bug fix for zero simulations in later rounds (#318)
- Bug fix for sbi.utils.sbiutils.Standardize; mean and std are now registered in state dict (thanks @plcrodrigues, #325)
- Tutorials on embedding_net and presimulated data (thanks @plcrodrigues, #314, #318)
- FAQ entry for pickling error

## v0.12.1

- Bug fix for broken NSF (#310, thanks @tvwenger).

## v0.12.0

- Add FAQ (#293)
- Fix bug in embedding_net when output dimension does not equal input dimension (#299)
- Expose arguments of functions used to build custom networks (#299)
- Implement non-atomic APT (#301)
- Depend on pyknos 0.12 and nflows 0.12
- Improve documentation (#302, #305, thanks to @agramfort)
- Fix bug for 1D uniform priors (#307).

## v0.11.2

- Fixed pickling of SNRE by moving StandardizeInputs (#291)
- Added check to ensure correct round number when presimulated data is provided
- Subclassed Posterior depending on inference algorithm (#282, #285)
- Pinned pyro to v1.3.1 as a temporary workaround (see #288)
- Detaching weights for MCMC SIR init immediately to save memory (#292)

## v0.11.1

- Bug fix for log_prob() in SNRE (#280)

## v0.11.0

- Changed the API to do multi-round inference (#273)
- Allow to continue inference (#273)

## v0.10.2

- Added missing type imports (#275)
- Made compatible for Python 3.6 (#275)

## v0.10.1

- Added `mcmc_parameters` to init methods of inference methods (#270)
- Fixed detaching of `log_weights` when using `sir` MCMC init (#270)
- Fixed logging for SMC-ABC

## v0.10.0

- Added option to pass external data (#264)
- Added setters for MCMC parameters (#267)
- Added check for `density_estimator` argument (#263)
- Fixed `NeuralPosterior` pickling error (#265)
- Added code coverage reporting (#269)

## v0.9.0

- Added ABC methods (#250)
- Added multiple chains for MCMC and new init strategy (#247)
- Added options for z-scoring for all inference methods (#256)
- Simplified swapping out neural networks (#256)
- Improved tutorials
- Fixed device keyword argument (#253)
- Removed need for passing x-shapes (#259)

## v0.8.0

- First public version
