"""
src/features.py

Feature/target preparation and train-test splitting for the ESI
triage prediction pipeline. Reuses the exact Week 6 split
(test_size=0.20, stratified, random_state=42) so results stay
comparable across weeks.
"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from src.data import get_feature_columns, TARGET


def build_feature_matrix(df):
    """
    Split a cleaned dataframe into feature matrix X and target vector y.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned dataframe (output of src.data.clean_triage_data).

    Returns
    -------
    (pd.DataFrame, pd.Series)
        X, y
    """
    features = get_feature_columns(df)
    X = df[features]
    y = df[TARGET]
    return X, y


def train_test_split_data(X, y, test_size: float = 0.20, random_state: int = 42):
    """
    Stratified train/test split, matching the Week 6 configuration
    exactly so every model is evaluated on the same patient groups.

    Parameters
    ----------
    X : pd.DataFrame
    y : pd.Series
    test_size : float
    random_state : int

    Returns
    -------
    X_train, X_test, y_train, y_test
    """
    return train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=random_state
    )


def scale_features(X_train, X_test):
    """
    Fit a StandardScaler on the training set and apply it to both
    train and test sets. Only used by Logistic Regression — the
    tree-based models train on unscaled features, matching the
    Week 7 notebook.

    Parameters
    ----------
    X_train : pd.DataFrame
    X_test : pd.DataFrame

    Returns
    -------
    (np.ndarray, np.ndarray, StandardScaler)
        X_train_scaled, X_test_scaled, fitted scaler
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler

