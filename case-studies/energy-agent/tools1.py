"""
tools1.py
======================================
AI Home Energy Optimizer - Tool Library (Part 1)

Tools Included
--------------
1. load_dataset
2. dataset_info
3. monthly_summary
4. daily_summary
5. hourly_summary
6. weekly_summary
7. appliance_usage
8. top_energy_consumers
9. least_energy_consumers
10. appliance_percentage

Compatible with:
- LangChain v1.x
- create_agent()

Requirements
------------
pip install pandas langchain-core
"""

from __future__ import annotations

from typing import Dict, List

import pandas as pd
from langchain_core.tools import tool

###############################################################################
# Global Dataset
###############################################################################

_df: pd.DataFrame | None = None

APPLIANCES = {
    "HVAC": "HVAC_kWh",
    "Lighting": "Lighting_kWh",
    "Kitchen": "Kitchen_kWh",
    "Washing Machine": "WashingMachine_kWh",
    "Water Heater": "WaterHeater_kWh",
    "EV Charging": "EVCharging_kWh",
}


###############################################################################
# Helper Functions
###############################################################################

def _require_dataset():
    """Raise an exception if dataset has not been loaded."""

    global _df

    if _df is None:
        raise RuntimeError(
            "Dataset not loaded.\n"
            "Call load_dataset('home_energy_dataset.csv') first."
        )


###############################################################################
# Tool 1
###############################################################################

@tool
def load_dataset(csv_path: str) -> str:
    """
    Load the Home Energy CSV dataset.

    Parameters
    ----------
    csv_path : str
        Path to CSV file.

    Returns
    -------
    str
        Status message.
    """

    global _df

    _df = pd.read_csv(csv_path)

    _df["Date"] = pd.to_datetime(_df["Date"])

    return (
        f"Dataset loaded successfully.\n"
        f"Rows : {_df.shape[0]}\n"
        f"Columns : {_df.shape[1]}"
    )


###############################################################################
# Tool 2
###############################################################################

@tool
def dataset_info() -> Dict:
    """
    Returns basic information about the dataset.
    """

    _require_dataset()

    return {
        "rows": len(_df),
        "columns": len(_df.columns),
        "column_names": list(_df.columns),
        "date_range": {
            "start": str(_df["Date"].min().date()),
            "end": str(_df["Date"].max().date()),
        },
        "appliances": list(APPLIANCES.keys()),
    }


###############################################################################
# Tool 3
###############################################################################

@tool
def monthly_summary() -> Dict:
    """
    Returns overall monthly statistics.
    """

    _require_dataset()

    return {
        "total_energy_kwh": round(_df["Total_kWh"].sum(), 2),
        "total_cost_inr": round(_df["Cost_INR"].sum(), 2),
        "average_daily_kwh": round(
            _df.groupby("Date")["Total_kWh"].sum().mean(),
            2,
        ),
        "average_hourly_kwh": round(
            _df["Total_kWh"].mean(),
            2,
        ),
    }


###############################################################################
# Tool 4
###############################################################################

@tool
def daily_summary() -> List[Dict]:
    """
    Returns daily energy usage.
    """

    _require_dataset()

    summary = (
        _df.groupby("Date")
        .agg(
            Total_kWh=("Total_kWh", "sum"),
            Cost_INR=("Cost_INR", "sum"),
        )
        .reset_index()
    )

    summary["Date"] = summary["Date"].astype(str)

    return summary.round(2).to_dict(orient="records")


###############################################################################
# Tool 5
###############################################################################

@tool
def hourly_summary() -> List[Dict]:
    """
    Returns average hourly consumption.
    """

    _require_dataset()

    summary = (
        _df.groupby("Hour")
        .agg(
            Average_kWh=("Total_kWh", "mean"),
            Average_Cost=("Cost_INR", "mean"),
        )
        .reset_index()
    )

    return summary.round(2).to_dict(orient="records")


###############################################################################
# Tool 6
###############################################################################

@tool
def weekly_summary() -> List[Dict]:
    """
    Returns week-wise statistics.
    """

    _require_dataset()

    df = _df.copy()

    df["Week"] = df["Date"].dt.isocalendar().week

    summary = (
        df.groupby("Week")
        .agg(
            Total_kWh=("Total_kWh", "sum"),
            Total_Cost=("Cost_INR", "sum"),
        )
        .reset_index()
    )

    return summary.round(2).to_dict(orient="records")


###############################################################################
# Tool 7
###############################################################################

@tool
def appliance_usage() -> Dict:
    """
    Returns total energy consumed by each appliance.
    """

    _require_dataset()

    result = {}

    for appliance, column in APPLIANCES.items():
        result[appliance] = round(_df[column].sum(), 2)

    return result


###############################################################################
# Tool 8
###############################################################################

@tool
def top_energy_consumers(top_n: int = 3) -> List[Dict]:
    """
    Returns the top N appliances consuming the most energy.
    """

    usage = appliance_usage.invoke({})

    ranking = sorted(
        usage.items(),
        key=lambda x: x[1],
        reverse=True,
    )

    return [
        {
            "appliance": k,
            "energy_kwh": v,
        }
        for k, v in ranking[:top_n]
    ]


###############################################################################
# Tool 9
###############################################################################

@tool
def least_energy_consumers(bottom_n: int = 3) -> List[Dict]:
    """
    Returns the lowest energy consuming appliances.
    """

    usage = appliance_usage.invoke({})

    ranking = sorted(
        usage.items(),
        key=lambda x: x[1],
    )

    return [
        {
            "appliance": k,
            "energy_kwh": v,
        }
        for k, v in ranking[:bottom_n]
    ]


###############################################################################
# Tool 10
###############################################################################

@tool
def appliance_percentage() -> Dict:
    """
    Returns percentage contribution of every appliance.
    """

    usage = appliance_usage.invoke({})

    total = sum(usage.values())

    return {
        appliance: round(value * 100 / total, 2)
        for appliance, value in usage.items()
    }


###############################################################################
# Exported Tool List
###############################################################################

TOOLS = [
    load_dataset,
    dataset_info,
    monthly_summary,
    daily_summary,
    hourly_summary,
    weekly_summary,
    appliance_usage,
    top_energy_consumers,
    least_energy_consumers,
    appliance_percentage,
]