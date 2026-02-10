
# 💫 Towards Sharing Tools, and Artifacts, for Reusable Simulation (STARS): a minimal model example

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pythonhealthdatascience/stars-treat-sim/HEAD)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/pypi/pyversions/treat_sim)](https://pypi.org/project/treat_sim/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10026326.svg)](https://doi.org/10.5281/zenodo.10026326)
[![PyPI version fury.io](https://badge.fury.io/py/treat-sim.svg)](https://pypi.org/project/treat-sim/)
[<img src="https://img.shields.io/static/v1?label=dockerhub&message=images&color=important?style=for-the-badge&logo=docker">](https://hub.docker.com/r/tommonks01/treat_sim)

## Overview

The materials and methods in this repository support work towards developing the STARShealthcare framework (**S**haring **T**ools and **A**rtifacts for **R**eusable **S**imulations in healthcare).  The code and written materials here demonstrate the application of STARS version 1 to sharing a `SimPy` discrete-event simulation model and associated research artifacts.  

* All artifacts in this repository are linked to study researchers via ORCIDs;
* Model code is made available under an MIT license;
* Python dependencies are managed through `mamba`;
* Documentation of the model is enhanced using a simple Jupyter notebook.
* The python model itself can be viewed and executed in Jupyter notebooks via [Binder](https://mybinder.org); 
* The materials are deposited and made citable using Zenodo;
* The model is sharable with other researchers and the NHS without the need to install software.
* A full suite of automated tests are provided with the model. 

## Author ORCIDs

[![ORCID: Harper](https://img.shields.io/badge/Alison_Harper_ORCID-0000--0001--5274--5037-brightgreen)](https://orcid.org/0000-0001-5274-5037)
[![ORCID: Monks](https://img.shields.io/badge/Tom_Monks_ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481)
[![ORCID: Heather](https://img.shields.io/badge/Amy_Heather_ORCID-0000--0002--6596--3479-brightgreen)](https://orcid.org/0000-0002-6596-3479)

## Funding

This code is part of independent research supported by the National Institute for Health Research Applied Research Collaboration South West Peninsula. The views expressed in this publication are those of the author(s) and not necessarily those of the National Institute for Health Research or the Department of Health and Social Care.

## Instructions to run the model

### Install from PyPI

If you do not wish to view the code or would like to use the model as part of your own work you can install the model as a python package.

```bash
pip install treat-sim
```

### Online Notebooks via Binder

The python code for the model has been setup to run online in Jupyter notebooks via binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pythonhealthdatascience/stars-treat-sim/HEAD)

> mybinder.org is a free tier service.  If it has not been used in a while Binder will need to re-containerise the code repository, and push to BinderHub. This will take several minutes. After that the online environment will be quick to load.

### To download code and run locally

#### Downloading the code

Either clone the repository using git or click on the green "code" button and select "Download Zip".

```bash
git clone https://github.com/pythonhealthdatascience/stars-treat-sim
```

#### Installing dependencies

[![Python](https://img.shields.io/pypi/pyversions/treat_sim)](https://pypi.org/project/treat_sim/)

All dependencies can be found in [`binder/environment.yml`]() and are pulled from conda-forge.  To run the code locally, we recommend installing [miniforge](https://github.com/conda-forge/miniforge);

> miniforge is FOSS alternative to Anaconda and miniconda that uses conda-forge as the default channel for packages. It installs both conda and mamba (a drop in replacement for conda) package managers.  We recommend mamba for faster resolving of dependencies and installation of packages. 

navigating your terminal (or cmd prompt) to the directory containing the repo and issuing the following command:

```
mamba env create -f binder/environment.yml
```

Activate the mamba environment using the following command:

```
mamba activate stars_treat_sim
```

#### Running the model

To run 50 multiple replications across a number of example experiments, use the following code:

```python
from treat_sim.model import (get_scenarios, run_scenario_analysis,
                             scenario_summary_frame, 
                             DEFAULT_RESULTS_COLLECTION_PERIOD)

if __name__ == '__main__':

    results = run_scenario_analysis(get_scenarios(), 
                                    DEFAULT_RESULTS_COLLECTION_PERIOD,
                                    n_reps=50)

    results_summary = scenario_summary_frame(results)
    print(results_summary)

```

Alternative you can design and execute individual experiments by creating a `Scenario` object:

```python
from treat_sim.model import Scenario, multiple_replications

if __name__ == '__main__':

    # use all default parameter values
    base_case = Scenario()

    results = multiple_replications(base_case).describe().round(2).T
    print(results)

```

The model can be run with different time dependent arrival profiles. By default the model runs with the arrival profile taken from Nelson (2013). The `datasets` module provides access to an alternative example dataset where arrivals are slightly skewed towards the end of the working day.  

```python

from treat_sim.model import Scenario, multiple_replications
from treat_sim.datasets import load_alternative_arrivals

if __name__ == '__main__':

    # set the arrival profile to later in the day
    scenario1 = Scenario(arrival_profile=load_alternative_arrivals())

    alternative_results = multiple_replications(scenario1).describe().round(2).T
    print(alternative_results)
```

#### Testing the model

> See our [online documentation](https://pythonhealthdatascience.github.io/stars-simpy-example-docs/content/02_model_code/05_testing.html) for an overview of testing

To run tests activate the virtual environment and entre the following command:

```bash
pytest
```

Alternatively to recieve a test coverage estimate issue the following command

```bash
pytest --cov=treat_sim tests/
```


## Repo overview

```
.
├── binder
│   └── environment.yml
├── CHANGES.md
├── CITATION.cff
├── LICENSE
├── notebooks
│   └── test_package.ipynb
├── pyproject.toml
├── README.md
├── tests
│   └── test_datasets.ipynb
│   └── test_model.ipynb
└── treat_sim
    ├── data
    │   └── ed_arrivals.csv
    │   └── ed_arrivals_scenario1.csv
    ├── __init__.py
    ├── datasets.py
    ├── distributions.py
    └── model.py
```

* `binder/` - contains the environment.yml file (sim) and all dependencies managed via conda, used to set-up the notebooks on Binder.
* `CHANGES.md` - changelog with record of notable changes to project between versions.
* `CITATION.cff` - citation information for the package.
* `LICENSE` - details of the MIT permissive license of this work.
* `notebooks/` - contains a notebook to run the model and provides basic enhanced model documentation.
* `pyproject.toml` - used to build and distribute python package inc. managing a list of package dependencies.
* `README.md` - what you are reading now!
* `tests/` - contains automated testing code
* `treat_sim/` - contains packaged version of the model.
    * `data/` - directory containing data file used by package.
    * `__init__.py` - required as part of package - contains author and version.
    * `datasets.py` - functions to load example dataset for parameterising the model.
    * `distributions.py` - distribution classes.
    * `model.py` - example SimPy model.


## Citation

If you use the materials within this repository we would appreciate a citation.

```
Monks, T., Harper, A., & Heather, A. (2024). Towards Sharing Tools, and Artifacts, for Reusable Simulation: a minimal model example (v2.1.0). Zenodo. https://doi.org/10.5281//zenodo.10026326
```

```bibtex
@software{stars_treat_sim,
  author       = {Thomas Monks, Alison Harper and Amy Heather},
  title        = {{Towards Sharing Tools, and Artifacts, for Reusable 
                   Simulation: a minimal model example}},
  month        = May,
  year         = 2024,
  publisher    = {Zenodo},
  version      = {v2.2.0},
  doi          = {10.5281//zenodo.10026326.},
  url          = {https://doi.org/10.5281//zenodo.10026326}
}
```

