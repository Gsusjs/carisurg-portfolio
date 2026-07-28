"""
tests/test_data.py — Test 1: data-schema check.

After cleaning, is the data the shape the model expects? These are not
meant to prove the pipeline is perfect — they are meant to make it fail
loudly if a future change (e.g. to clean()) silently corrupts the data.
"""

import numpy as np
import pandas as pd

from src.data import clean, VITAL_COLS, TARGET
from src.features import select_features


def _raw_sample(n=60, seed=42) -> pd.DataFrame:
    """A small synthetic raw frame with the columns clean() expects."""
    rng = np.random.default_rng(seed)

    data = {
        "Unnamed: 0": np.arange(n),
        TARGET: rng.choice([1, 2, 3, 4, 5], size=n),
        "gender": rng.choice(["Male", "Female", " male ", "F"], size=n),
        "age": rng.integers(18, 90, size=n).astype(float),
        "ethnicity": rng.choice(["Hispanic or Latino", "Non-Hispanic"], size=n),
        "race": rng.choice(["White or Caucasian", "Other"], size=n),
        "dep_name": rng.choice(["A", "B"], size=n),
        "disposition": rng.choice(["Admit", "Discharge"], size=n),
        "cc_chestpain": rng.choice([0.0, 1.0], size=n),
    }
    for col in VITAL_COLS:
        data[col] = rng.normal(loc=80, scale=10, size=n)

    return pd.DataFrame(data)


def test_clean_produces_valid_schema():
    raw = _raw_sample()
    df = clean(raw)

    # only valid ESI labels remain
    assert df[TARGET].isin([1, 2, 3, 4, 5]).all()

    # no gaps left in the vitals after imputation
    for col in VITAL_COLS:
        assert df[col].isna().sum() == 0

    # gender is encoded to 0/1, not left as free text
    assert set(df["gender"].unique()) <= {0, 1}

    # cleaning didn't silently drop every row
    assert len(df) > 0

    # stray index columns are gone
    assert not any(c.startswith("Unnamed") for c in df.columns)


def test_select_features_excludes_leakage_admin_demographics():
    raw = _raw_sample()
    df = clean(raw)
    features = select_features(df)

    for excluded in ["disposition", "race", "ethnicity", "dep_name", "age", "gender"]:
        assert excluded not in features

    assert TARGET not in features
    assert "cc_chestpain" in features
