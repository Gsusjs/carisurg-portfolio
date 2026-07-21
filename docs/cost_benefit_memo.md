# Week 7 Cost-Benefit Memo

## Model Selection for Emergency Severity Index (ESI) Prediction

## Verdict

Logistic Regression is recommended for Phase 3 development because it provides the strongest balance between predictive performance, interpretability, computational efficiency, and operational simplicity compared with the more complex models evaluated.

---

## Dataset and Methods Recap

This evaluation used the Yale EMMLC emergency department triage dataset to predict Emergency Severity Index (ESI) levels from triage information.

The same cleaning process, feature selection strategy, and stratified train/test split from Week 6 were reused to ensure a fair comparison between models. A fixed random seed (42) was used throughout so that results are reproducible.

Three models were evaluated:

- Logistic Regression as the Week 6 baseline model.
- Random Forest as a complex tree-based classifier.
- Gradient Boosting as an ensemble learning model.

Models were assessed using the following axes:

- Accuracy, precision, recall, and F1-score.
- Training time and inference time per prediction.
- Interpretability, including whether a single prediction can be explained to a clinician in under a minute and the method used.

---

## Benchmark Table

| Model | Accuracy | Precision | Recall | F1 | Training Time (s) | Inference Time (ms/sample) | Interpretability |
|---|---:|---:|---:|---:|---:|---:|---|
| Logistic Regression | 0.667 | 0.582 | 0.463 | 0.492 | 26.861 | 0.001 | High - coefficients allow explanation |
| Random Forest | 0.647 | 0.475 | 0.384 | 0.406 | 73.933 | 0.185 | Medium - tree structure can be inspected |
| Gradient Boosting | 0.651 | 0.476 | 0.382 | 0.407 | 100.710 | 0.011 | Medium - feature importance ranking |

Logistic Regression coefficients allow a single prediction to be explained to a clinician in under a minute by examining the direction and magnitude of feature weights. Random Forest can be inspected through tree structure, while Gradient Boosting can be supported through feature importance rankings. These approaches provide useful model-level explanations but are less direct for explaining individual predictions.

---

## Arguments Supporting Logistic Regression

### 1. Strongest Benchmark Performance

Logistic Regression achieved the highest accuracy, macro precision, macro recall, and macro F1-score. The complex models did not improve predictive performance despite increased complexity.

### 2. Better Operational Efficiency

The model required less training time and had the lowest inference cost. This supports easier deployment, maintenance, and scaling within a clinical environment.

### 3. Higher Interpretability

Logistic Regression coefficients provide a transparent explanation of feature influence, and a single prediction can be talked through in under a minute. This supports clinical review and governance requirements.

---

## Arguments Against Logistic Regression

### 1. Limited Nonlinear Modelling Capability

Logistic Regression may not capture complex interactions between clinical variables as effectively as tree-based models.

### 2. Lower Flexibility

Random Forest and Gradient Boosting can automatically learn more complicated relationships from data without requiring the analyst to specify interaction terms in advance.

### 3. Class Imbalance Remains a Challenge

The model does not fully solve prediction difficulties for rare ESI categories, particularly ESI 1 and ESI 5.

---

## Risks and Unknowns

- The model has only been evaluated using one dataset. External validation using data from additional hospitals is required before clinical deployment.

- The impact of model predictions on real clinical workflows has not been measured. Further assessment is needed to determine whether the system improves triage decisions in practice.

- Model performance may change when patient populations, clinical practices, or hospital workflows differ from the Yale EMMLC dataset. Ongoing monitoring would be required to detect performance degradation after deployment.

---

## Recommendation

Logistic Regression should be carried forward into Phase 3 because it provides the best balance between predictive performance, explainability, and deployment efficiency.

However, this choice does not solve all challenges associated with automated ESI prediction. It does not remove class imbalance problems, guarantee performance across different healthcare settings, or replace clinical judgement. Further validation, monitoring, and fairness analysis are required before operational use.
