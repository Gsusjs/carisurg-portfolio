# Model Selection

All models were trained and evaluated using the same Week 6/7 stratified 80/20 train-test split (`random_state=42`) of the Yale EMMLC triage dataset.

| Model | Key Hyperparameters | Accuracy | Precision (macro) | Recall (macro) | F1 (macro) | ESI-1 Recall | Training Time (s) | Inference Time (ms/sample) |
|---|---|---|---|---|---|---|---|---|
| Dummy Baseline | `strategy=stratified`, `random_state=42` | 0.375 | – | – | 0.204 | 0.00 | – | – |
| Decision Tree | `max_depth=5`, `random_state=42` | 0.556 | 0.265 | 0.245 | 0.216 | 0.00 | – | – |
| **Logistic Regression** | **`max_iter=1000`, `random_state=42`, StandardScaler applied** | **0.667** | **0.582** | **0.463** | **0.492** | **0.25** | 26.86 | **0.001** |
| Random Forest | `n_estimators=300`, `class_weight=balanced`, `random_state=42` | 0.647 | 0.475 | 0.384 | 0.406 | 0.00 | 73.93 | 0.185 |
| Gradient Boosting | Default scikit-learn parameters, `random_state=42` | 0.651 | 0.476 | 0.382 | 0.407 | 0.00 | 100.71 | 0.011 |

## Final Model Selection

The highlighted model was selected as the final model because it achieved the strongest overall performance across the evaluated metrics, including accuracy and macro-averaged precision, recall, and F1 score. It also provided the fastest inference time and greater interpretability compared with the tree-based models evaluated.

The model coefficients provide clearer insight into how individual features influence predictions, making it more suitable for an audit-ready clinical decision-support system.

## ESI-1 Recall Consideration

The test set contained only 16 ESI-1 cases. As a result, ESI-1 recall values should be interpreted cautiously because small changes in a small number of predictions can substantially affect this metric. The model is intended to support clinical triage decisions rather than replace clinical judgement, particularly for the most critical patients.
