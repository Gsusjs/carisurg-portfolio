"""
src/data.py

Data loading and cleaning functions for the ESI triage prediction pipeline.

Refactored from the Week 6 baseline notebook and reused unchanged in Week 7
to keep the baseline vs. complex-model comparison fair. Logic is preserved
exactly from the notebook cells — this module only restructures it into
importable, testable functions.
"""

import os
import pandas as pd
import numpy as np

VITAL_COLS = [
    "triage_vital_hr",
    "triage_vital_sbp",
    "triage_vital_dbp",
    "triage_vital_rr",
    "triage_vital_o2",
    "triage_vital_temp",
    "triage_glucose",
]

TARGET = "esi"

LEAKAGE = [
    "disposition",
    "previousdispo",
]

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


def resolve_data_path(raw_filename: str, drive_dir: str = "/content/drive/MyDrive/CariSurg/") -> str:
    """
    Resolve the dataset path, preferring a mounted Google Drive copy
    (Colab workflow) and falling back to a local copy alongside the
    code (GitHub / new-hire workflow).

    Parameters
    ----------
    raw_filename : str
        Name of the raw CSV file.
    drive_dir : str
        Google Drive directory used in the original Colab workflow.

    Returns
    -------
    str
        The resolved path to use with pandas.read_csv.
    """
    drive_path = os.path.join(drive_dir, raw_filename)
    return drive_path if os.path.exists(drive_path) else raw_filename


def load_raw_data(path: str) -> pd.DataFrame:
    """
    Load the raw triage CSV from disk.

    Parameters
    ----------
    path : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Raw, unprocessed dataframe.
    """
    return pd.read_csv(path)


def clean_triage_data(raw: pd.DataFrame) -> pd.DataFrame:
    """
    Apply the Week 6 cleaning rules to the raw triage dataframe.

    Steps:
      - drop stray "Unnamed" index columns
      - coerce vital sign columns and target to numeric
      - keep only valid ESI classes (1-5)
      - null out physiologically implausible temperature / o2 readings
      - normalise gender to a binary numeric column
      - median-impute vitals, age and gender
      - cast esi to int

    Parameters
    ----------
    raw : pd.DataFrame
        Raw dataframe as returned by load_raw_data.

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe ready for feature selection.
    """
    df = raw.copy()

    df = df.drop(
        columns=[c for c in df.columns if c.startswith("Unnamed")],
        errors="ignore",
    )

    for col in VITAL_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["esi"] = pd.to_numeric(df["esi"], errors="coerce")

    df = df[df["esi"].isin([1, 2, 3, 4, 5])]

    df.loc[
        (df["triage_vital_temp"] < 90) | (df["triage_vital_temp"] > 110),
        "triage_vital_temp",
    ] = np.nan

    df.loc[df["triage_vital_o2"] > 100, "triage_vital_o2"] = np.nan

    # .str.strip() before .str.lower() -- stops values like " Female "
    # from falling through the map() as missing.
    df["gender"] = (
        df["gender"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map({"male": 0, "m": 0, "female": 1, "f": 1})
    )

    for col in VITAL_COLS + ["age", "gender"]:
        df[col] = df[col].fillna(df[col].median())

    df["esi"] = df["esi"].astype(int)

    return df


def get_feature_columns(df: pd.DataFrame) -> list:
    """
    Return the list of feature columns available at triage time,
    excluding the target, known leakage columns, admin/logistics
    columns, and demographic columns.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned dataframe.

    Returns
    -------
    list
        Ordered list of feature column names.
    """
    excluded = set([TARGET] + LEAKAGE + ADMIN + DEMOGRAPHICS)
    return [c for c in df.columns if c not in excluded]

