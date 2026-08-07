"""
tools2.py
======================================
AI Home Energy Optimizer - Tool Library (Part 2)

Tools Included
--------------
11. monthly_cost
12. daily_cost
13. hourly_cost
14. cost_breakdown
15. peak_usage
16. peak_tariff_analysis
17. highest_consumption_day
18. lowest_consumption_day
19. solar_generation
20. solar_utilization

Compatible with:
- LangChain v1.x
- create_agent()

Requirements
------------
pip install pandas langchain-core

NOTE
----
This module expects the dataset to be loaded using
tools1.load_dataset().

Example

from tools1 import load_dataset
from tools2 import *

load_dataset("home_energy_dataset.csv")
"""

from __future__ import annotations

from typing import Dict, List

import pandas as pd
from langchain_core.tools import tool

# Import shared dataset from tools1
import tools1


###############################################################################
# Helper
###############################################################################

def _df() -> pd.DataFrame:
    if tools1._df is None:
        raise RuntimeError(
            "Dataset not loaded.\n"
            "Call tools1.load_dataset() first."
        )
    return tools1._df


###############################################################################
# Tool 11
###############################################################################

@tool
def monthly_cost() -> Dict:
    """
    Returns monthly electricity cost statistics.
    """

    df = _df()

    return {
        "monthly_cost_inr": round(df["Cost_INR"].sum(), 2),
        "average_daily_cost": round(
            df.groupby("Date")["Cost_INR"].sum().mean(),
            2,
        ),
        "average_hourly_cost": round(
            df["Cost_INR"].mean(),
            2,
        ),
    }


###############################################################################
# Tool 12
###############################################################################

@tool
def daily_cost() -> List[Dict]:
    """
    Returns daily electricity cost.
    """

    df = _df()

    result = (
        df.groupby("Date")
        .agg(
            Daily_Cost=("Cost_INR", "sum"),
            Daily_kWh=("Total_kWh", "sum"),
        )
        .reset_index()
    )

    result["Date"] = result["Date"].astype(str)

    return result.round(2).to_dict(orient="records")


###############################################################################
# Tool 13
###############################################################################

@tool
def hourly_cost() -> List[Dict]:
    """
    Returns average electricity cost by hour.
    """

    df = _df()

    result = (
        df.groupby("Hour")
        .agg(
            Average_Cost=("Cost_INR", "mean"),
            Average_kWh=("Total_kWh", "mean"),
        )
        .reset_index()
    )

    return result.round(2).to_dict(orient="records")


###############################################################################
# Tool 14
###############################################################################

@tool
def cost_breakdown() -> Dict:
    """
    Estimates appliance-wise electricity cost.

    Cost is distributed proportional
    to appliance energy consumption.
    """

    df = _df()

    appliance_energy = {
        appliance: df[column].sum()
        for appliance, column in tools1.APPLIANCES.items()
    }

    total_energy = sum(appliance_energy.values())

    total_cost = df["Cost_INR"].sum()

    result = {}

    for appliance, energy in appliance_energy.items():

        result[appliance] = round(
            total_cost * energy / total_energy,
            2,
        )

    return result


###############################################################################
# Tool 15
###############################################################################

@tool
def peak_usage() -> Dict:
    """
    Returns statistics during Peak Tariff hours.
    """

    df = _df()

    peak = df[df["PeakTariff"] == "Yes"]

    return {
        "peak_hours": sorted(
            peak["Hour"].unique().tolist()
        ),
        "peak_energy_kwh": round(
            peak["Total_kWh"].sum(),
            2,
        ),
        "peak_cost_inr": round(
            peak["Cost_INR"].sum(),
            2,
        ),
    }


###############################################################################
# Tool 16
###############################################################################

@tool
def peak_tariff_analysis() -> Dict:
    """
    Compares peak tariff and off-peak usage.
    """

    df = _df()

    peak = df[df["PeakTariff"] == "Yes"]

    offpeak = df[df["PeakTariff"] == "No"]

    return {

        "peak": {
            "energy_kwh": round(
                peak["Total_kWh"].sum(),
                2,
            ),
            "cost_inr": round(
                peak["Cost_INR"].sum(),
                2,
            ),
        },

        "offpeak": {
            "energy_kwh": round(
                offpeak["Total_kWh"].sum(),
                2,
            ),
            "cost_inr": round(
                offpeak["Cost_INR"].sum(),
                2,
            ),
        }

    }


###############################################################################
# Tool 17
###############################################################################

@tool
def highest_consumption_day() -> Dict:
    """
    Returns the day with highest energy consumption.
    """

    df = _df()

    daily = df.groupby("Date")["Total_kWh"].sum()

    day = daily.idxmax()

    return {

        "date": str(day.date()),

        "energy_kwh": round(
            daily.max(),
            2,
        ),

        "cost_inr": round(
            df[df["Date"] == day]["Cost_INR"].sum(),
            2,
        )

    }


###############################################################################
# Tool 18
###############################################################################

@tool
def lowest_consumption_day() -> Dict:
    """
    Returns the day with lowest energy usage.
    """

    df = _df()

    daily = df.groupby("Date")["Total_kWh"].sum()

    day = daily.idxmin()

    return {

        "date": str(day.date()),

        "energy_kwh": round(
            daily.min(),
            2,
        ),

        "cost_inr": round(
            df[df["Date"] == day]["Cost_INR"].sum(),
            2,
        )

    }


###############################################################################
# Tool 19
###############################################################################

@tool
def solar_generation() -> Dict:
    """
    Returns solar generation statistics.
    """

    df = _df()

    return {

        "total_generation_kwh": round(
            df["SolarGeneration_kWh"].sum(),
            2,
        ),

        "average_daily_generation": round(
            df.groupby("Date")[
                "SolarGeneration_kWh"
            ].sum().mean(),
            2,
        ),

        "maximum_hourly_generation": round(
            df["SolarGeneration_kWh"].max(),
            2,
        )

    }


###############################################################################
# Tool 20
###############################################################################

@tool
def solar_utilization() -> Dict:
    """
    Calculates solar contribution.
    """

    df = _df()

    solar = df["SolarGeneration_kWh"].sum()

    total = df["Total_kWh"].sum()

    coverage = solar / total * 100

    grid = total - solar

    return {

        "solar_generated_kwh": round(
            solar,
            2,
        ),

        "grid_energy_kwh": round(
            grid,
            2,
        ),

        "solar_coverage_percent": round(
            coverage,
            2,
        )

    }


###############################################################################
# Exported Tool List
###############################################################################

TOOLS = [

    monthly_cost,

    daily_cost,

    hourly_cost,

    cost_breakdown,

    peak_usage,

    peak_tariff_analysis,

    highest_consumption_day,

    lowest_consumption_day,

    solar_generation,

    solar_utilization,

]