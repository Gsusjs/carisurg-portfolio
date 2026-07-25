"""
src/data.py — Data loading and cleaning for the ESI triage model.

Refactored from the Week 6 and Week 7 exploratory notebooks. The cleaning
logic itself is unchanged from the notebooks (Week 7's clean_triage_data,
which reused Week 6's rules) — only restructured into functions with
explicit signatures instead of notebook globals.
"""

import pandas as pd
import numpy as np

TARGET = "esi"

VITAL_COLS = [
    "triage_vital_hr",
    "triage_vital_sbp",
    "triage_vital_dbp",
    "triage_vital_rr",
    "triage_vital_o2",
    "triage_vital_temp",
    "triage_glucose",
]

# Variables unavailable at triage time / that would leak the outcome,
# and columns intentionally excluded from modelling (see Week 6/7).
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


def load_raw(path: str) -> pd.DataFrame:
    """Load the raw Yale EMMLC triage CSV from `path`."""
    return pd.read_csv(path)


def clean(raw: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the raw triage dataframe.

    Mirrors the Week 6/7 notebook cleaning exactly:
      - drops stray 'Unnamed' index columns
      - coerces vitals and esi to numeric
      - drops rows with an invalid ESI label (keeps only 1-5)
      - nulls out physiologically impossible temp/o2 readings
      - encodes gender as 0/1 (male/m -> 0, female/f -> 1)
      - median-imputes vitals, age, and gender
    """
    df = raw.copy()

    df = df.drop(
        columns=[c for c in df.columns if c.startswith("Unnamed")],
        errors="ignore",
    )

    for col in VITAL_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df[TARGET] = pd.to_numeric(df[TARGET], errors="coerce")
    df = df[df[TARGET].isin([1, 2, 3, 4, 5])]

    df.loc[
        (df["triage_vital_temp"] < 90) | (df["triage_vital_temp"] > 110),
        "triage_vital_temp",
    ] = np.nan

    df.loc[df["triage_vital_o2"] > 100, "triage_vital_o2"] = np.nan

    df["gender"] = (
        df["gender"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map({"male": 0, "m": 0, "female": 1, "f": 1})
    )

    for col in VITAL_COLS + ["age", "gender"]:
        df[col] = df[col].fillna(df[col].median())

    df[TARGET] = df[TARGET].astype(int)

    return df


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
