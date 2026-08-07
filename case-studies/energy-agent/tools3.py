"""
tools3.py
======================================
AI Home Energy Optimizer - Tool Library (Part 3)

Tools Included
--------------
21. solar_vs_grid
22. occupancy_statistics
23. temperature_statistics
24. hvac_temperature_correlation
25. ev_charging_analysis
26. water_heater_analysis
27. washing_machine_analysis
28. weekend_vs_weekday
29. find_anomalies
30. recommendation_statistics
31. energy_report

Compatible with
---------------
- LangChain v1.x
- create_agent()

Requirements
------------
pip install pandas langchain-core

NOTE
----
Uses the shared dataframe loaded by:

tools1.load_dataset(...)
"""

from __future__ import annotations

from typing import Dict, List

import pandas as pd
from langchain_core.tools import tool

import tools1
import tools2


###############################################################################
# Shared Dataset
###############################################################################

def _df() -> pd.DataFrame:
    if tools1._df is None:
        raise RuntimeError(
            "Dataset not loaded.\n"
            "Call tools1.load_dataset() first."
        )

    return tools1._df


###############################################################################
# Tool 21
###############################################################################

@tool
def solar_vs_grid() -> Dict:
    """
    Compare solar generation against
    grid electricity usage.
    """

    df = _df()

    solar = df["SolarGeneration_kWh"].sum()

    total = df["Total_kWh"].sum()

    grid = max(total - solar, 0)

    return {

        "solar_generation_kwh": round(solar, 2),

        "grid_consumption_kwh": round(grid, 2),

        "solar_percentage": round(
            solar / total * 100,
            2,
        ),

        "grid_percentage": round(
            grid / total * 100,
            2,
        )

    }


###############################################################################
# Tool 22
###############################################################################

@tool
def occupancy_statistics() -> Dict:
    """
    Analyze occupancy statistics.
    """

    df = _df()

    return {

        "average_occupancy": round(
            df["Occupancy"].mean(),
            2,
        ),

        "maximum_occupancy": int(
            df["Occupancy"].max()
        ),

        "minimum_occupancy": int(
            df["Occupancy"].min()
        ),

        "average_energy_per_person": round(
            df["Total_kWh"].sum() /
            max(df["Occupancy"].sum(), 1),
            3,
        )

    }


###############################################################################
# Tool 23
###############################################################################

@tool
def temperature_statistics() -> Dict:
    """
    Outdoor temperature statistics.
    """

    df = _df()

    return {

        "minimum_temperature": round(
            df["OutdoorTemp_C"].min(),
            1,
        ),

        "maximum_temperature": round(
            df["OutdoorTemp_C"].max(),
            1,
        ),

        "average_temperature": round(
            df["OutdoorTemp_C"].mean(),
            1,
        )

    }


###############################################################################
# Tool 24
###############################################################################

@tool
def hvac_temperature_correlation() -> Dict:
    """
    Correlation between HVAC usage
    and outdoor temperature.
    """

    df = _df()

    corr = df["HVAC_kWh"].corr(
        df["OutdoorTemp_C"]
    )

    if corr > 0.8:
        level = "Very Strong"

    elif corr > 0.6:
        level = "Strong"

    elif corr > 0.3:
        level = "Moderate"

    else:
        level = "Weak"

    return {

        "correlation": round(corr, 3),

        "relationship": level

    }


###############################################################################
# Tool 25
###############################################################################

@tool
def ev_charging_analysis() -> Dict:
    """
    Analyze EV charging.
    """

    df = _df()

    ev = df[df["EVCharging_kWh"] > 0]

    return {

        "charging_hours": sorted(
            ev["Hour"].unique().tolist()
        ),

        "energy_used_kwh": round(
            ev["EVCharging_kWh"].sum(),
            2,
        ),

        "estimated_cost": round(
            ev["Cost_INR"].sum(),
            2,
        )

    }


###############################################################################
# Tool 26
###############################################################################

@tool
def water_heater_analysis() -> Dict:
    """
    Water heater usage.
    """

    df = _df()

    energy = df["WaterHeater_kWh"].sum()

    return {

        "energy_kwh": round(
            energy,
            2,
        ),

        "average_daily_kwh": round(
            energy / df["Date"].nunique(),
            2,
        )

    }


###############################################################################
# Tool 27
###############################################################################

@tool
def washing_machine_analysis() -> Dict:
    """
    Washing machine usage.
    """

    df = _df()

    energy = df["WashingMachine_kWh"].sum()

    return {

        "energy_kwh": round(
            energy,
            2,
        ),

        "usage_hours": sorted(
            df[
                df["WashingMachine_kWh"] > 0
            ]["Hour"].unique().tolist()
        )

    }


###############################################################################
# Tool 28
###############################################################################

@tool
def weekend_vs_weekday() -> Dict:
    """
    Compare weekend and weekday
    energy usage.
    """

    df = _df().copy()

    df["Weekend"] = (
        df["Date"]
        .dt.dayofweek >= 5
    )

    result = (
        df.groupby("Weekend")[
            "Total_kWh"
        ].sum()
    )

    return {

        "weekday_kwh": round(
            result.get(False, 0),
            2,
        ),

        "weekend_kwh": round(
            result.get(True, 0),
            2,
        )

    }


###############################################################################
# Tool 29
###############################################################################

@tool
def find_anomalies(
    threshold: float = 2.5
) -> List[Dict]:
    """
    Detect unusually high
    electricity consumption.
    """

    df = _df()

    mean = df["Total_kWh"].mean()

    std = df["Total_kWh"].std()

    anomalies = df[
        df["Total_kWh"] >
        mean + threshold * std
    ]

    return anomalies[
        [
            "Date",
            "Hour",
            "Total_kWh",
            "Cost_INR",
        ]
    ].to_dict(
        orient="records"
    )


###############################################################################
# Tool 30
###############################################################################

@tool
def recommendation_statistics() -> Dict:
    """
    Returns all important
    statistics for the LLM.

    This tool should be used
    before generating
    recommendations.
    """

    return {

        "monthly_summary":
            tools1.monthly_summary.invoke({}),

        "top_consumers":
            tools1.top_energy_consumers.invoke({}),

        "cost_breakdown":
            tools2.cost_breakdown.invoke({}),

        "peak_usage":
            tools2.peak_usage.invoke({}),

        "solar":
            solar_vs_grid.invoke({}),

        "temperature":
            temperature_statistics.invoke({}),

        "occupancy":
            occupancy_statistics.invoke({}),

        "correlation":
            hvac_temperature_correlation.invoke({})

    }


###############################################################################
# Tool 31
###############################################################################

@tool
def energy_report() -> str:
    """
    Generate a Markdown
    energy report.
    """

    monthly = tools1.monthly_summary.invoke({})

    top = tools1.top_energy_consumers.invoke({})

    peak = tools2.peak_usage.invoke({})

    solar = solar_vs_grid.invoke({})

    report = f"""
# Home Energy Optimization Report

## Monthly Summary

- Total Energy: {monthly['total_energy_kwh']} kWh
- Total Cost: ₹{monthly['total_cost_inr']}
- Average Daily Usage: {monthly['average_daily_kwh']} kWh

## Top Energy Consumers

"""

    for item in top:

        report += (
            f"- {item['appliance']} : "
            f"{item['energy_kwh']} kWh\n"
        )

    report += f"""

## Peak Usage

Peak Hours:
{peak['peak_hours']}

Peak Energy:
{peak['peak_energy_kwh']} kWh

## Solar

Solar Contribution:
{solar['solar_percentage']} %

Grid Contribution:
{solar['grid_percentage']} %

## Recommendation

Use the recommendation_statistics()
tool to generate personalized
energy-saving suggestions.
"""

    return report


###############################################################################
# Exported Tool List
###############################################################################

TOOLS = [

    solar_vs_grid,

    occupancy_statistics,

    temperature_statistics,

    hvac_temperature_correlation,

    ev_charging_analysis,

    water_heater_analysis,

    washing_machine_analysis,

    weekend_vs_weekday,

    find_anomalies,

    recommendation_statistics,

    energy_report,

]