# Healthcare AI Risk Management and Algorithmic Equity Assessment

This risk register identifies the principal AI-technical, operational, ethical and equity risks associated with deploying an AI-assisted emergency department triage system across the Saint Cedric public hospital network.

| Risk Name | Category | Likelihood | Impact | Mitigation Strategy | Signal of Success |
|---|---|---|---|---|---|
| Training-distribution shift between Mercer urban data and rural/outbreak cohorts | AI-Technical | High | High | Clinical AI Lead monitors model drift weekly and validates quarterly against holdout datasets. A recall reduction greater than 3 percentage points triggers model review and suspension until revalidated. | Recall remains within ±3 percentage points (pp) across all sites. |
| Model performance drift over time due to changing disease patterns | AI-Technical | Medium | High | Continuous monitoring with scheduled annual retraining. Performance falling below the validation baseline triggers immediate model review and retraining. | AUROC and sensitivity remain above validation baseline. |
| Alert fatigue leading to clinician dismissal of critical notifications | Operational | High | High | Clinical Operations Lead reviews alert thresholds monthly. A clinical action rate below 15% triggers a mandatory redesign of the alert interface. | >15% of alerts result in documented clinical action. |
