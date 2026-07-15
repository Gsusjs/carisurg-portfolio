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


# Week 5 — Clinical Data Profiling & Feasibility Assessment

This week focused on understanding and evaluating an Emergency Department (ED) triage dataset prior to modelling. The emphasis was on data quality, structure, and clinical interpretation to determine readiness for predictive modelling.

---

## Objective
To assess the feasibility of building a predictive model for ED triage acuity (ESI) by performing exploratory data analysis, identifying data quality issues, and evaluating clinical relevance.

---

## Work Completed

### 1. Clinical Data Understanding
- Interpreted dataset structure and clinical meaning of variables
- Identified key feature groups:
  - Vital signs (heart rate, blood pressure, respiratory rate, oxygen saturation, temperature, glucose)
  - Demographics (age, gender, ethnicity, race, insurance status)
  - Chief complaints (~200 binary indicators)
- Recognised Emergency Severity Index (ESI) as the target variable
- Highlighted potential data leakage risks and fairness-sensitive variables

---

### 2. Data Profiling & Quality Assessment
- Used `df.info()`, `df.describe()`, and `df.shape` for initial profiling
- Performed dtype audit to identify incorrect or inconsistent data types
- Quantified missing values (both counts and percentages per column)
- Identified outliers and implausible physiological values in vital signs
- Assessed sparsity in high-dimensional chief complaint features

---

### 3. Exploratory Data Visualization
- Visualised ESI distribution across patient population
- Explored missingness patterns across features
- Analysed relationships between vital signs and acuity levels
- Examined demographic distributions (race, gender, age)

---

## Model Reproducibility

The Week 6 baseline models use a fixed random seed of 42.

The dataset was divided into:
- 80% training data
- 20% testing data

The split used stratification on the ESI target variable to maintain the distribution of triage levels between the training and testing sets.

Using the same random seed allows the model results to be reproduced by other reviewers.

---

## Key Outputs
- Data profiling notebook (`/notebooks`)
- Missingness visualisation and analysis (`/docs`)
- Clinical feasibility memo assessing dataset readiness for modelling (`/docs`)



---

## Outcome
A structured exploratory analysis was completed to evaluate the dataset’s suitability for predictive modelling. The results informed a feasibility assessment outlining strengths, limitations, and data quality concerns relevant to clinical deployment.

The dataset is considered suitable for exploratory modelling following appropriate preprocessing, feature engineering, and fairness-aware evaluation.
