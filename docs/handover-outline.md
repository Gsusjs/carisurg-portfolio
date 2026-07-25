# Handover Document

## 1. Project Summary
This project predicts a patient's Emergency Severity Index (ESI, 1–5) at emergency department triage using the Yale EMMLC triage dataset to support, but not replace, clinical triage decision-making.

## 2. Final Model Decision
Logistic Regression was selected as the final model because it achieved the strongest overall performance across the evaluated metrics (accuracy, macro precision, macro recall, and macro F1) while providing better interpretability and lower computational cost than the alternative models tested. The model was selected based on the comparative evaluation conducted in Week 7. See `docs/model-selection.md` for the full comparison.

## 3. How to Run
```bash
git clone <repo-url>
cd carisurg-triage
pip install -r requirements.txt
python scripts/train.py --config config.yaml
```

## 4. Where the Data Lives (and Governance Status)
- Path: `data/raw/yaleemmlc_admissionprediction_triage.csv` (git-ignored and not committed).
- The dataset is de-identified; however, access should remain limited to the project team, and the file must not be redistributed outside the Trust.

## 5. Known Limitations
- ESI-1 recall is modest across all models evaluated (0.25 at best on a test set containing only 16 ESI-1 cases). This tool is intended to support, not replace, clinical judgement for the most critical patients.
- The model was developed using a single-site dataset (Yale EMMLC), so performance may not generalize to other hospitals or departments without further validation.
- Demographic variables (e.g., age, gender, ethnicity, race, and insurance status) were excluded during feature selection to reduce reliance on sensitive attributes and help mitigate potential fairness concerns.
