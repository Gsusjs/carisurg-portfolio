"""
src/model.py

Training and evaluation functions for the ESI triage prediction
pipeline. The pinned Phase 3 model is Logistic Regression (see
config.yaml and docs/model-selection.md for the decision record).

Random Forest and Gradient Boosting builders are kept here too since
they're part of the audited model-selection history (Week 7) — but
scripts/train.py only calls the Logistic Regression path by default.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
)

from src.utils import timed


def build_logistic_regression(max_iter: int = 1000, random_state: int = 42) -> LogisticRegression:
    """Construct the pinned Logistic Regression model with committed hyperparameters."""
    return LogisticRegression(max_iter=max_iter, random_state=random_state)


def build_random_forest(n_estimators: int = 300, random_state: int = 42) -> RandomForestClassifier:
    """Construct the Random Forest model as evaluated in Week 7 (not pinned)."""
    return RandomForestClassifier(
        n_estimators=n_estimators,
        class_weight="balanced",
        random_state=random_state,
        n_jobs=-1,
    )


def build_gradient_boosting(random_state: int = 42) -> GradientBoostingClassifier:
    """Construct the Gradient Boosting model as evaluated in Week 7 (not pinned)."""
    return GradientBoostingClassifier(random_state=random_state)


def train_model(model, X_train, y_train):
    """
    Fit a model and time the training call.

    Parameters
    ----------
    model : sklearn estimator
    X_train, y_train : training data

    Returns
    -------
    (fitted model, training_time_seconds)
    """
    fitted, train_time = timed(model.fit, X_train, y_train)
    return fitted, train_time


def predict(model, X_test):
    """
    Run inference and time the prediction call.

    Parameters
    ----------
    model : fitted sklearn estimator
    X_test : test features

    Returns
    -------
    (predictions, inference_time_seconds, time_per_prediction_seconds)
    """
    preds, inference_time = timed(model.predict, X_test)
    time_per_prediction = inference_time / len(X_test)
    return preds, inference_time, time_per_prediction


def evaluate_model(y_test, y_pred) -> dict:
    """
    Compute headline classification metrics (macro-averaged, matching
    the Week 7 benchmark table).

    Parameters
    ----------
    y_test : true labels
    y_pred : predicted labels

    Returns
    -------
    dict
        accuracy, precision, recall, f1
    """
    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, average="macro", zero_division=0),
        "recall": recall_score(y_test, y_pred, average="macro", zero_division=0),
        "f1": f1_score(y_test, y_pred, average="macro", zero_division=0),
    }


def classification_report_text(y_test, y_pred, digits: int = 3) -> str:
    """Return the full per-class classification report as text (for logging)."""
    return classification_report(y_test, y_pred, digits=digits)

