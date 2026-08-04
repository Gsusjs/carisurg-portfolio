# CariSurg Healthcare AI Portfolio (Weeks 0-9)

This repository documents my weekly assignments for the Mercer General Hospital Clinical AI & Innovation Unit training program, spanning clinical data cleaning, exploratory analysis, model development, and a reproducible, config-driven triage prediction pipeline for emergency care settings.

## Repository Structure

- `notebooks/` → exploratory notebooks (Weeks 0, 5, 6, 7) - see `notebooks/README.md`
- `docs/` → literature review, feasibility memo, model-selection audit trail (`model-selection.md`), handover document (`HANDOVER.md`), and Week 9 HCI/HRI design artefacts (see Week 9 Design Artefacts below)
- `src/` → the refactored pipeline: `data.py` (loading and cleaning), `features.py` (feature selection), `model.py` (training and evaluation), `utils.py` (shared helpers)
- `scripts/` → `train.py`, the single entry point that reads `config.yaml` and runs the pipeline end-to-end
- `tests/` → pytest sanity checks (data-schema check and training smoke test)
- `config.yaml` → the pinned final model, its hyperparameters, file paths, and random seed
- `data/` → dataset reference only (no raw patient data stored - see Data Governance below)

## Weekly Progress

- **Week 0** - Data cleaning (gender standardisation, DBP physiological limits) and basic visualisation.
- **Week 1** - Literature review on AI-assisted emergency triage.
- **Week 2** - Repository restructuring, reference management, updated proposal.
- **Week 5** - ED triage dataset profiling and feasibility assessment; identified ESI as the target variable, flagged leakage and fairness-sensitive variables.
- **Week 6** - Baseline models (Logistic Regression, Decision Tree) trained on an 80/20 stratified split, `random_state=42`.
- **Week 7** - Benchmarked Random Forest and Gradient Boosting against the Week 6 baseline; Logistic Regression recommended for Phase 3 on balance of performance, interpretability, and cost.
- **Week 8** - Refactored the notebook logic into a modular, config-driven `src/` pipeline; pinned the final model; added pytest sanity checks; produced the model-selection audit trail and handover document.
- **Week 9** - Designed the HCI (ED triage desk) and HRI (Observation Unit kiosk) deployment concepts; produced co-design canvases, mock-ups, a system requirements document, and a safety considerations one-pager. See Week 9 Design Artefacts below.

## Week 9 Design Artefacts

- `docs/co-design-canvas.md` / `docs/co-design-canvas.pdf` - full co-design canvas (Problem, Ethics, Guidelines, MVP, Environment, Form) for both the HCI (ED Triage Desk) and HRI (Observation Unit) settings.
- `docs/mockup-hci-triage-desk.png` - screen-based mock-up of the ED triage desk queue and AI recommendation panel.
- `docs/mockup-hri-observation-kiosk.png` - physical form-factor mock-up of the Observation Unit kiosk and its paired nurse-station alert view.
- `docs/system-requirements.md` - deployment vision, human-machine interfacing requirements, inputs/outputs, and the build-path choice with justification.
- `docs/safety-considerations.md` - three HCI-specific and three HRI-specific safety considerations, each with a specific mitigation mechanism.

## Final Model

The final model is Logistic Regression, pinned in `config.yaml`, selected on the basis of the Week 7 benchmark comparison. See `docs/model-selection.md` for the full comparison and `docs/HANDOVER.md` for the handover summary.

## How to Run

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. To explore the original analysis, open the notebooks in `notebooks/` in Jupyter Notebook or VS Code and run cells from top to bottom.
4. To train the pinned model end-to-end, run:
   ```bash
   python scripts/train.py --config config.yaml
   ```
   This loads and cleans the data, trains the pinned model, evaluates it, and writes the fitted model plus its metrics to `models/` (git-ignored).
5. To run the sanity checks:
   ```bash
   pytest tests/
   ```

## Data Governance

The clinical dataset is not stored in this repository due to healthcare data governance considerations. Dataset files, trained models, and other generated artifacts are excluded using `.gitignore`. See `docs/HANDOVER.md` for the full governance statement.

This project follows a reproducible research workflow using GitHub version control, structured documentation, and reference management (Zotero).
