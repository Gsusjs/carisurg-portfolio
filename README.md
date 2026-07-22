# CariSurg Healthcare AI Portfolio (Weeks 0–2)

## Overview
This repository documents my work on the CariSurg Healthcare AI Program, focusing on clinical data cleaning, exploratory analysis, and early-stage AI-assisted triage system design in emergency care settings.

The project bridges healthcare and data science by applying structured data cleaning, visualisation, and simple decision-support logic to emergency department datasets.

---

## Repository Structure

- `notebooks/` → Week 0 EDA and analysis notebooks + Week 5 emergency department dataset exploration and data-quality dashboard
- `docs/` → Week 1 literature review, Week 2 updated proposal, and Week 5 feasibility memo
- `data/` → Dataset reference (no raw patient data stored)

---

## Key Outputs

- Week 0: Data cleaning (Gender, DBP) + visualisations + triage algorithm  
- Week 1: Literature review on AI-assisted emergency triage  
- Week 2: Repository restructuring + reference management + updated proposal
- Week 5: Emergency department dataset exploration, data-quality dashboard, feasibility memo, and clinical feature shortlist
- Week 6: Baseline models were trained using a fixed random seed (42) with an 80/20 stratified train-test split on the ESI target variable to ensure reproducible results
- Week 7: Evaluated ESI prediction models; delivered benchmarks, memo, and decision journal.





---

## How to Run

1. Clone the repository  
2. Install dependencies:

pip install -r requirements.txt

3. Open notebooks in Jupyter Notebook or VS Code  
4. Run cells from top to bottom  

---

## Data Governance

The clinical dataset is not stored in this repository due to healthcare data governance considerations.

Dataset files are excluded using `.gitignore`.


---

## How to Run

1. Clone the repository  
2. Install dependencies:
   pip install -r requirements.txt  
3. Open notebooks/week0 in Jupyter Notebook or VS Code  
4. Run cells from top to bottom
This project follows a reproducible research workflow using GitHub version control, structured documentation, and reference management (Zotero).
