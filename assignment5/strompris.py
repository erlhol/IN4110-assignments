#!/usr/bin/env python3
"""
Fetch data from https://www.hvakosterstrommen.no/strompris-api
and visualize it.

Assignment 5
"""

import datetime
import warnings

import altair as alt
import pandas as pd
import requests
import requests_cache

# install an HTTP request cache
# to avoid unnecessary repeat requests for the same data
# this will create the file http_cache.sqlite
requests_cache.install_cache()

# suppress a warning with altair 4 and latest pandas
warnings.filterwarnings("ignore", ".*convert_dtype.*", FutureWarning)


# task 5.1:


def fetch_day_prices(date: datetime.date = None, location: str = "NO1") -> pd.DataFrame:
    """Fetch one day of data for one location from hvakosterstrommen.no API

    Make sure to document arguments and return value...
    ...
    """
    if date is None:
        date = datetime.datetime.now()

    # construct the date format for the GET-request
    date_format = (
        str(date.year) + "/" + zero_pad(str(date.month)) + "-" + zero_pad(str(date.day))
    )

    # Construct the url with the date format and location
    url = (
        f"https://www.hvakosterstrommen.no/api/v1/prices/{date_format}_{location}.json"
    )
    # Make a GET-request
    r = requests.get(url)
    if r.status_code != 200:
        return None

    # Parse the get request to json-format
    data = r.json()
    df = pd.DataFrame.from_dict(data)

    # Filter out to only include NOK_per_kWh and time_start
    df = df[["NOK_per_kWh", "time_start"]]

    # Convert to correct timezone (from write-up)
    df["time_start"] = pd.to_datetime(df["time_start"], utc=True).dt.tz_convert(
        "Europe/Oslo"
    )
    # Convert to float if not already
    df["NOK_per_kWh"] = df["NOK_per_kWh"].astype("float")
    return df


# LOCATION_CODES maps codes ("NO1") to names ("Oslo")
LOCATION_CODES = {
    "NO1": "Oslo",
    "NO2": "Kristiansand",
    "NO3": "Trondheim",
    "NO4": "Tromsø",
    "NO5": "Bergen",
}

# task 1:


def fetch_prices(
    end_date: datetime.date = None,
    days: int = 7,
    locations: list[str] = tuple(LOCATION_CODES.keys()),
) -> pd.DataFrame:
    """Fetch prices for multiple days and locations into a single DataFrame

    Make sure to document arguments and return value...
    ...
    """

    if end_date is None:
        end_date = datetime.datetime.now()

    total_df = None
    # traverse in reverse order, from the oldest to the most recent day
    for n in range(days - 1, -1, -1):
        for location in locations:
            td = end_date - datetime.timedelta(n)
            df = fetch_day_prices(td, location)
            df["location_code"] = location
            df["location"] = LOCATION_CODES[location]
            if total_df is None:
                total_df = df
                continue
            total_df = pd.concat([total_df, df])
    return total_df


# task 5.1:


def plot_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot energy prices over time

    x-axis should be time_start
    y-axis should be price in NOK
    each location should get its own line

    Make sure to document arguments and return value...
    """
    # TODO!
    return (
        alt.Chart(df)
        .mark_line()
        .encode(x="time_start", y="NOK_per_kWh", color="location")
    )


# Task 5.4


def plot_daily_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot the daily average price

    x-axis should be time_start (day resolution)
    y-axis should be price in NOK

    You may use any mark.

    Make sure to document arguments and return value...
    """
    ...


# Task 5.6

ACTIVITIES = {
    # activity name: energy cost in kW
    ...
}


def plot_activity_prices(
    df: pd.DataFrame, activity: str = "shower", minutes: float = 10
) -> alt.Chart:
    """
    Plot price for one activity by name,
    given a data frame of prices, and its duration in minutes.

    Make sure to document arguments and return value...
    """
    raise NotImplementedError("Remove me when you implemnt this optional task")

    ...


def zero_pad(n: str):
    """zero-pad a number string

    turns '2' into '02'

    """
    if len(n) == 2:
        return n
    return "0" + n


def main():
    """Allow running this module as a script for testing."""
    df = fetch_prices()
    chart = plot_prices(df)
    # showing the chart without requiring jupyter notebook or vs code for example
    # requires altair viewer: `pip install altair_viewer`
    chart.show()


if __name__ == "__main__":
    main()
