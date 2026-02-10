# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Dates formatted as YYYY-MM-DD as per [ISO standard](https://www.iso.org/iso-8601-date-and-time-format.html).

Consistent identifier (represents all versions, resolves to latest): [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10026326.svg)](https://doi.org/10.5281/zenodo.10026326)

## [v2.2.0](https://github.com/pythonhealthdatascience/stars-treat-sim/releases/tag/v2.2.0) - 2024-08-01

### Added

* All model classes and functions now have python type hints
* `treat_sim.datasets` module with `load_nelson_arrivals`, `load_alternative_arrivals` and `valid_arrival_profile` functions
* `tests/test_datasets.py` contains functional and dirty tests for loading and using internal arrival profile datasets.

### Changed

* `Scenario` defaults to the time dependent arrival profile given in Nelson (2013), but also accepts `arrival_profile` a `pandas.DataFrame` parameter for scenario analysis. 
* Default arrival profile is sourced from local package rather than GitHub URL.

### Fixed

* MODEL: thinning algorithm: `np.Inf` -> `np.inf` for compatibility with `numpy>=2`

## [v2.1.0](https://github.com/pythonhealthdatascience/stars-treat-sim/releases/tag/v2.1.0) - 2024-05-30 - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11396022.svg)](https://doi.org/10.5281/zenodo.11396022)

### Changes

* TESTS: added automated unit tests under `tests/`
* README: updated to recommend miniforge and mamba instead of anaconda/conda.

## [v2.0.0](https://github.com/pythonhealthdatascience/stars-treat-sim/releases/tag/v2.0.0) - 2024-05-17 - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11210422.svg)](https://doi.org/10.5281/zenodo.11210422)

### Changed

* MODEL: Examination distribution modified to truncated normal distribution (minimum 0.5)
* Mitgrated package build to `pyproject.toml` and `hatch`. 
* Updated local conda virtual environment to python 3.10.x 
* Tested model in python 3.11 and 3.12 and added to supported versions.

### Removed

* Removed redundant `setup.py`, `requirements.txt`, `MANIFEST.in`


## [v1.2.0](https://github.com/pythonhealthdatascience/stars-treat-sim/releases/tag/v1.2.0) - 2024-05-08 - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11146209.svg)](https://doi.org/10.5281/zenodo.11146209)

### Changed

* `CHANGES.md` uses Keep a Changelog formatting, and includes release links, DOIs, and first release.
* `CITATION.cff` includes references, new author, and spelling/grammar fixes.
* `README.md` updated repo overview and spelling/grammar fixes
* Full author list in `__init__`

### Fixed

* Model uses data from this repository (rather than external)

### Removed

* Duplicate `ed_arrivals.csv`

## [v1.1.1](https://github.com/pythonhealthdatascience/stars-treat-sim/releases/tag/v1.1.1) - 2024-05-01 - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11098944.svg)](https://doi.org/10.5281/zenodo.11098944)

### Fixed

* Trauma patient treatment fixed to use correct distribution and parameters.

## [v1.1.0](https://github.com/pythonhealthdatascience/stars-treat-sim/releases/tag/v1.1.0) - 2024-04-06 - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10936052.svg)](https://doi.org/10.5281/zenodo.10936052)

### Changed

* Upgraded internal implementation of generating non-overlapping random number streams. This is now implemented to use `np.random.SeedSequence`. See [https://numpy.org/doc/stable/reference/random/parallel.html](https://numpy.org/doc/stable/reference/random/parallel.html).

### Fixed

* `setup.py` now links to correct Github URL

## [v1.0.0](https://github.com/pythonhealthdatascience/stars-treat-sim/releases/tag/v1.0.0) - 2023-10-20 - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10026327.svg)](https://doi.org/10.5281/zenodo.10026327)

:seedling: First release.
