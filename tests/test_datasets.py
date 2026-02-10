"""Datasets testing

This module provides a set of tests to run against `treat_sim.datasets`.  
These tests are either pass or fail and no interpretation is needed. 

There are two example arrivals profiles built into the package (very small size ~380 bytes).
They are loaded from the functions load_nelson_arrivals() and load_alternative_arrivals().
The package also provides the function valid_arrival_profile() that will return True if all is 
okay with a profile format or raise exceptions if there are problems.

Tests are divided as follows

1. Dirty tests
Tests that the `treat-sim.datasets` functions fail as expected when certain invalid values.

2 Functional tests
These provide tests of the correct loading and use of internal datasets plus
#check that a scenario is created correctly when presented with a valid dataset.

"""
import numpy as np
import pandas as pd

import pytest

from treat_sim.datasets import (
    load_nelson_arrivals,
    load_alternative_arrivals,
    valid_arrival_profile,
)

from treat_sim.model import Scenario

### 1. Dirty tests
# tests to check that `treat-sim` fails as
# expected when given certain values.


def nelson_arrivals_wrong_cols():
    """Create an arrival profile with incorrect col names
    """
    df = load_nelson_arrivals()
    df.columns = ["random_col1", "random_col2"]
    return df

def nelson_arrivals_wrong_rows():
    """Create an arrival profile with incorrect num rows.
    """
    df1 = load_nelson_arrivals()
    df2 = load_nelson_arrivals()
    return pd.concat([df1,df2],ignore_index=True)

@pytest.mark.parametrize(
    "arrival_profile, exception_type",
    [
        (["period", "arrival_rate"], TypeError),
        (["random_str1", "random_str2"], TypeError),
        (np.arange(10), TypeError),
        (nelson_arrivals_wrong_cols(), ValueError),
        (nelson_arrivals_wrong_rows(), ValueError),

    ],
)
def test_invalid_profile(arrival_profile, exception_type):
    """tests that exceptions are thrown for various types
    of problems with profile
    wrong type
    wrong columns
    wrong number of rows"""
    with pytest.raises(exception_type):
        valid_arrival_profile(arrival_profile)


### 2 Functional tests
# These provide tests of the correct
# loading and use of internal datasets plus
# check that a scenario is created correctly.

@pytest.mark.parametrize(
    "arrival_profile",
    [
        (load_nelson_arrivals()),
        (load_alternative_arrivals()),
    ],
)
def test_valid_profile(arrival_profile):
    """
    Test that included datasets pass the 
    validation test.
    """
    assert valid_arrival_profile(arrival_profile)


@pytest.mark.parametrize(
    "arrival_profile",
    [
        (load_nelson_arrivals()),
        (load_alternative_arrivals()),
    ],
)
def test_scenario_accepts_valid_profile(arrival_profile):
    """
    Test that included datasets work with Scenario.
    """
    test_scenario = Scenario(arrival_profile = arrival_profile)

    assert isinstance(test_scenario, Scenario)
