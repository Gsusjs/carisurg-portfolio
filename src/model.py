"""
src/model.py — Model construction and evaluation.

Refactored from the Week 6/7 notebooks (Dummy baseline, Logistic
Regression, Decision Tree, Random Forest, Gradient Boosting). No
modelling logic is changed — only wrapped into build_model() /
evaluate() with explicit signatures instead of notebook globals.
"""

import time

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

MODEL_REGISTRY = {
    "dummy": DummyClassifier,
    "logistic_regression": LogisticRegression,
    "decision_tree": DecisionTreeClassifier,
    "random_forest": RandomForestClassifier,
    "gradient_boosting": GradientBoostingClassifier,
}


def build_model(name: str, params: dict, seed: int):
    """
    Construct an sklearn estimator by name using the given hyperparameters.

    `name` must be a key in MODEL_REGISTRY (see config.yaml `models:`
    section). `seed` is injected as random_state so every model in the
    comparison table is trained with the same reproducible seed.
    """
    if name not in MODEL_REGISTRY:
        raise ValueError(f"Unknown model '{name}'. Options: {list(MODEL_REGISTRY)}")

    cls = MODEL_REGISTRY[name]
    kwargs = dict(params or {})
    kwargs.setdefault("random_state", seed)
    return cls(**kwargs)


def train_and_time(model, X_train, y_train) -> float:
    """Fit `model` in place and return training time in seconds."""
    start = time.time()
    model.fit(X_train, y_train)
    return time.time() - start


def evaluate(model, X_test, y_test) -> dict:
    """
    Score a fitted model on held-out data.

    Returns accuracy, macro precision/recall/F1, and per-sample inference
    time in milliseconds — the same headline metrics used in the Week 7
    benchmark table (docs/model-selection.md).
    """
    start = time.time()
    preds = model.predict(X_test)
    inference_time = time.time() - start

    return {
        "accuracy": accuracy_score(y_test, preds),
        "precision": precision_score(y_test, preds, average="macro", zero_division=0),
        "recall": recall_score(y_test, preds, average="macro", zero_division=0),
        "f1": f1_score(y_test, preds, average="macro", zero_division=0),
        "inference_time_ms_per_sample": (inference_time / len(X_test)) * 1000,
    }
