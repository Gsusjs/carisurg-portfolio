"""
scripts/train.py — entry point.

Usage:
    python scripts/train.py --config config.yaml

Reads config.yaml, loads and cleans the data, trains the pinned final
model, evaluates it on the held-out split, and writes the fitted model
plus its metrics to models/.
"""

import argparse
import json
import os
import sys

# Ensure the repo root is on sys.path so `src` resolves regardless of
# where `python scripts/train.py` is invoked from.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from src.data import load_raw, clean
from src.features import get_xy
from src.model import build_model, train_and_time, evaluate
from src.utils import load_config


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Path to config.yaml")
    args = parser.parse_args()

    cfg = load_config(args.config)
    seed = cfg["seed"]

    raw = load_raw(cfg["data"]["raw_path"])
    df = clean(raw)
    X, y = get_xy(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=cfg["data"]["test_size"],
        stratify=y,
        random_state=seed,
    )

    model_name = cfg["final_models"][0]
    params = cfg["models"][model_name]
    model = build_model(model_name, params, seed)

    # Logistic Regression is scale-sensitive; tree-based models are not
    # (see Week 6 exercise answers).
    scaler = None
    if model_name == "logistic_regression":
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    train_time = train_and_time(model, X_train, y_train)
    metrics = evaluate(model, X_test, y_test)
    metrics["training_time_s"] = train_time

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, f"models/{model_name}.pkl")
    if scaler is not None:
        joblib.dump(scaler, f"models/{model_name}_scaler.pkl")

    with open(f"models/{model_name}_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print(f"Trained {model_name}")
    for key, value in metrics.items():
        print(f"  {key}: {value:.4f}" if isinstance(value, float) else f"  {key}: {value}")
    print(f"Model saved to models/{model_name}.pkl")


if __name__ == "__main__":
    main()
