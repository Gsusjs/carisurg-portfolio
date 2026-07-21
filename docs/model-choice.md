# Week 7 Model Choice Decision Journal

## Context

- Week 7 focused on comparing complex machine learning classifiers (Random Forest and Gradient Boosting) against the Week 6 Logistic Regression baseline for predicting Emergency Severity Index (ESI) levels using the Yale EMMLC emergency department triage dataset.

- Random Forest and Gradient Boosting were evaluated using the same cleaned dataset, feature selection process, and stratified train/test split as the baseline. This ensured that differences in performance were caused by model choice rather than changes in data preparation.

## Alternatives Considered

- **Logistic Regression baseline classifier**  
  Carried forward from Week 6 as the reference model for comparison.

- **Random Forest classifier**  
  Evaluated to determine whether a tree-based ensemble could capture nonlinear relationships between triage variables and ESI level.

- **Gradient Boosting classifier**  
  Evaluated as a sequential boosting approach to determine whether it could improve performance compared with Logistic Regression and Random Forest.

## Decision

Logistic Regression will be recommended as the preferred model for Phase 3 because it achieved the strongest balance between predictive performance, interpretability, and computational efficiency.

## Reasoning

- Logistic Regression achieved the highest macro F1-score (0.492) compared with Random Forest (0.406) and Gradient Boosting (0.407).

- Logistic Regression had the lowest inference time at 0.001 ms/sample, compared with Random Forest (0.185 ms/sample) and Gradient Boosting (0.011 ms/sample).

- Logistic Regression provides clearer explanations through model coefficients, allowing a single prediction to be explained to a clinician in under a minute and supporting clinical governance review.

## Things Not Yet Known

- Performance on external hospital datasets has not been evaluated, so it is unknown whether the benchmark results generalise beyond the Yale EMMLC dataset.

- The effect of deploying the model on real clinical workflows and triage decisions remains unknown and requires further evaluation.
