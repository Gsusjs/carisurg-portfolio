# Clinical Data Cleaning & Visualization Portfolio

This repository documents my weekly assignments for the Mercer General Hospital Clinical AI & Innovation Unit training program. Each week focuses on data cleaning, preprocessing, and visualization tasks using Python, pandas, and matplotlib.

## Week 0 Highlights
- **Assignment 1 – Gender Column Cleaning**  
  Standardized inconsistent values (`Male`, `MALE`, `1` → 1; `Female`, `FEMALE`, `0` → 0) to improve dataset reliability.

- **Assignment 2 – DBP Column Cleaning**  
  Applied physiological limits (30–150 mmHg), converted invalid entries to `NaN`, and imputed missing values with the median for clinical accuracy.

- **Assignment 3 – Basic Visualization**  
  Created histograms of DBP distribution and scatter plots of DBP vs Age, with reference lines for hypotension/hypertension thresholds.

---


## Week 5 — Clinical Data Profiling & Feasibility Assessment  
Focused on understanding and evaluating an ED triage dataset before modelling, with emphasis on data quality, structure, and clinical meaning.

### Tutorial 1 – Clinical Data Literacy  
- Understood dataset structure and clinical meaning of features  
- Identified vitals, demographics, chief complaints, and ESI target  
- Highlighted leakage risks and fairness-sensitive variables  

### Tutorial 2 – Data Profiling  
- Used `.info()`, `.describe()`, `.shape`, and dtype audit  
- Quantified missing values (counts + percentages)  
- Identified outliers and data type issues  
- Explored relationships between features and ESI  

### Tutorial 3 – Exploratory Visualization  
- Visualised ESI distribution and demographic breakdowns  
- Explored missingness and chief complaint patterns  
- Examined relationships between vitals and acuity  

### Outcome  
Produced a data profiling report and feasibility summary to assess readiness for predictive modelling.
