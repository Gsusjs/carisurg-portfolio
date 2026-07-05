# Feasibility Memo – ED Triage Dataset

## 1. One-sentence verdict
The dataset is suitable for predictive modelling of triage acuity (ESI), but only after addressing missingness, feature sparsity, and potential data quality inconsistencies.

---

## 2. Dataset summary
This dataset contains de-identified emergency department triage encounters, including patient demographics, arrival vital signs, and approximately 200 binary chief complaint indicators.

The target variable is the Emergency Severity Index (ESI), a 5-level clinical acuity scale used at triage (1 = most urgent, 5 = least urgent).

Key feature groups:
- **Demographics:** age, gender, ethnicity, race, insurance status
- **Vitals:** heart rate, blood pressure, respiratory rate, oxygen saturation, temperature (°F), glucose
- **Chief complaints:** sparse binary indicators grouped across body systems (~200 features)
- **Outcome variable:** disposition (admit/discharge) — not usable for triage prediction due to post-triage timing

Overall, the dataset is high-dimensional, clinically rich, and structured around real ED workflow.

---

## 3. Top 3 data quality concerns

### 1. Missing data in structured variables
Several structured fields (including vitals and demographics) contain missing values. This may introduce bias if missingness is not random (e.g. sicker patients receiving more complete measurements).

### 2. High-dimensional sparse complaint features
The chief complaint section contains ~200 binary variables, most of which are rarely activated. This sparsity may dilute predictive signal unless aggregated into clinical categories.

### 3. Potential data type inconsistencies and outliers
Some numeric fields require validation for correct typing and range constraints. Outliers exist that may reflect recording error or physiological extremes requiring careful handling.

---

## 4. Top 3 reasons to proceed

### 1. Strong clinical signal in triage vitals
Vital signs (heart rate, oxygen saturation, respiratory rate, blood pressure) are directly linked to physiological instability and are strong predictors of acuity.

### 2. Well-defined and clinically meaningful target (ESI)
The Emergency Severity Index provides a structured, standardised, and clinically interpretable prediction target aligned with real triage decision-making.

### 3. Rich real-world clinical structure
The dataset reflects authentic ED workflows, including symptoms, observations, and triage decisions, making it suitable for applied clinical machine learning development.

---

## 5. Key caveats

- This dataset is US-based and may not directly generalise to Caribbean ED populations due to differences in case mix, resources, and patient demographics.
- Some variables (e.g. insurance status) may encode systemic bias and require fairness-aware handling.
- Temporal ordering is critical: only features available at triage should be used; post-triage outcomes such as disposition must be excluded to avoid data leakage.
- Temperature is recorded in Fahrenheit and requires careful interpretation to avoid unit errors.
- Missingness patterns may reflect clinical workflow rather than random absence.

---

## Conclusion
While the dataset is suitable for building a triage prediction model, success depends on careful preprocessing, feature consolidation, and strict prevention of data leakage. The next step is systematic data cleaning and transformation prior to modelling.
