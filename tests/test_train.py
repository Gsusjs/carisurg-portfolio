"""
tests/test_train.py — Test 2: training smoke test.

Runs the pinned final model (Logistic Regression) end to end on ~60
rows. This does not check accuracy — only that the pipeline holds
together: it fits and predicts without crashing and returns the right
number of predictions.
"""

import numpy as np
import pandas as pd

from src.data import VITAL_COLS, TARGET
from src.features import get_xy
from src.model import build_model


def _tiny_clean_df(n=60, seed=0) -> pd.DataFrame:
    """A ~60-row frame in the same shape as clean()'s output (already encoded/imputed)."""
    rng = np.random.default_rng(seed)

    data = {
        TARGET: rng.choice([1, 2, 3, 4, 5], size=n),
        "gender": rng.choice([0, 1], size=n),
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


def test_smoke_train_predict():
    df = _tiny_clean_df(60)
    X, y = get_xy(df)

    model = build_model("logistic_regression", {"max_iter": 1000}, seed=42)
    model.fit(X, y)
    preds = model.predict(X)

    assert len(preds) == len(y)
