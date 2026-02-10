"""
Datasets

treat_sim bundles small datasets that can be used by the model for experimentation. 
Datasets are returned as pandas dataframes. 
"""

from pathlib import Path

import pandas as pd

# path to Nelson arrival profile CSV file
DEFAULT_NSPP_PROFILE_FILE = "ed_arrivals.csv"
SCENARIO_NSPP_PROFILE_FILE = "ed_arrivals_scenario1.csv"


def load_nelson_arrivals() -> pd.DataFrame:
    """Default time dependent arrival profile from Nelson 2013

    Arrival rates between between 6am and 12am broken down into
    60 minute intervals.  Duration of day is 1080 minutes (18 hours * 60 mins).

    Returns a pd.DataFrame with 2 columns: period and arrival_rate

    Returns:
    -------
    pd.DataFrame
    """
    path_to_file = Path(__file__).parent.joinpath("data", DEFAULT_NSPP_PROFILE_FILE)
    return pd.read_csv(path_to_file)


def load_alternative_arrivals() -> pd.DataFrame:
    """An example alternative arrival profile.

    In this scenario the Treatment Centre has number of arrivals overall
     as the default scenario, but their is a shift in numbers towards later in the day
      with a higher peak at 6pm

    Arrival rates between between 6am and 12am broken down into
    60 minute intervals.  Duration of day is 1080 minutes (18 hours * 60 mins).

    Returns a pd.DataFrame with 2 columns: period and arrival_rate

    Returns:
    -------
    pd.DataFrame
    """
    path_to_file = Path(__file__).parent.joinpath("data", SCENARIO_NSPP_PROFILE_FILE)
    return pd.read_csv(path_to_file)


def valid_arrival_profile(arrival_profile: pd.DataFrame) -> bool:
    """
    Provides a simple check that a dataframe containing an arrival
    profile is in a valid format.

    Raise an exception if invalid
    """

    if not isinstance(arrival_profile, pd.DataFrame):
        raise TypeError(
            "Invalid arrival profile. arrival_profile must a DataFrame in the correct format."
        )

    if not {"period", "arrival_rate"}.issubset(arrival_profile.columns):
        raise ValueError(
            "Invalid arrival profile. DataFrame must contain period and arrival_rate columns"
        )

    if arrival_profile.shape[0] != 18:
        raise ValueError(
            f"Invalid arrival profile. Profile should contain 18 period.  But selected DataFrame contains {arrival_profile.shape[0]} rows."
        )

    return True
