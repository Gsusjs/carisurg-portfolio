## Table 1. Final Benchmark Comparison (Baseline vs Complex Model)

# Week 7 Model Benchmark Comparison

| Model | Accuracy | Precision | Recall | F1 | Training Time (s) | Inference Time (ms/sample) | Interpretability |
|---|---:|---:|---:|---:|---:|---:|---|
| Logistic Regression | 0.667 | 0.582 | 0.463 | 0.492 | 26.861 | 0.001 | High - individual predictions can be explained using model coefficients |
| Random Forest | 0.647 | 0.475 | 0.384 | 0.406 | 73.933 | 0.185 | Medium - individual predictions can be explored through tree structure and feature importance |
| Gradient Boosting | 0.651 | 0.476 | 0.382 | 0.407 | 100.710 | 0.011 | Medium - individual predictions can be explained using feature importance rankings |


