"""
src/features.py — Feature selection for the ESI triage model.

Excludes variables unavailable at triage time (leakage), administrative
metadata, and demographic attributes from the modelling feature set —
the same exclusion lists used throughout Weeks 6-7.
"""

import pandas as pd

from src.data import TARGET

LEAKAGE = ["disposition", "previousdispo"]

ADMIN = [
    "dep_name",
    "arrivalmode",
    "arrivalmonth",
    "arrivalday",
    "arrivalhour_bin",
]

DEMOGRAPHICS = [
    "age",
    "gender",
    "ethnicity",
    "race",
    "lang",
    "religion",
    "maritalstatus",
    "employstatus",
    "insurance_status",
]


def select_features(df: pd.DataFrame) -> list:
    """Return the modelling feature-column list (excludes target/leakage/admin/demographics)."""
    return [
        c for c in df.columns
        if c != TARGET and c not in LEAKAGE + ADMIN + DEMOGRAPHICS
    ]


def get_xy(df: pd.DataFrame):
    """Split a cleaned dataframe into (X, y) using select_features()."""
    features = select_features(df)
    return df[features], df[TARGET]
