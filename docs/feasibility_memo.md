# Feasibility Memo – ED Triage Dataset

## 1. One-sentence verdict
The dataset is suitable for predictive modelling of triage acuity (ESI), but only after addressing missingness, feature sparsity, and data quality issues such as outliers, inconsistent formatting, and potential bias.

---

## 2. Dataset summary
This dataset contains de-identified emergency department triage encounters, including patient demographics, arrival vital signs, and approximately 200 binary chief complaint indicators.

The target variable is the Emergency Severity Index (ESI), a 5-level clinical acuity scale used at triage (1 = most urgent, 5 = least urgent).

### Key feature groups:
- **Demographics:** age, gender, ethnicity, race, insurance status  
- **Vitals:** heart rate, blood pressure, respiratory rate, oxygen saturation, temperature (°F), glucose  
- **Chief complaints:** sparse binary indicators grouped across body systems (~200 features)  

The dataset is high-dimensional and reflects real-world ED workflow where feature availability varies at point of care.

---

## 3. Top 3 data quality concerns

### 1. Missing data in structured variables
As observed in the missingness analysis, several structured fields (including vitals and demographics) contain >20% missing values. This may introduce bias if missingness is not random (e.g., sicker patients receiving more complete measurements).

### 2. High-dimensional sparse complaint features
The chief complaint section contains ~200 binary variables, most of which are rarely activated. This sparsity reduces signal strength and may require aggregation into clinically meaningful groups to improve interpretability and performance.

### 3. Outliers, inconsistent formatting, and data type issues
Exploratory analysis shows physiologically implausible values in vital signs (e.g., extreme blood pressure or temperature readings), suggesting recording or entry errors. In addition, several numeric variables are stored as strings and require standardisation before modelling.

---

## 4. Top 3 reasons to proceed

### 1. Strong physiological signal in triage vitals
Vital signs (heart rate, oxygen saturation, respiratory rate, blood pressure) are directly linked to physiological instability and are well-established predictors of clinical acuity.

### 2. Broad clinically relevant feature coverage
The dataset integrates physiological measurements, demographic variables, and presenting complaints, enabling a multi-dimensional representation of patient status at triage.

### 3. Well-defined and clinically meaningful target (ESI)
The Emergency Severity Index provides a structured and interpretable outcome aligned with real-world triage decision-making, making it suitable for supervised learning.

---

## 5. Key caveats

- This dataset is US-based and may not generalise to other healthcare systems due to differences in population, resources, and ED workflows  
- Certain variables (e.g., insurance status) may encode systemic bias and require fairness-aware evaluation before inclusion in modelling  
- Temporal ordering must be strictly respected: only features available at triage should be used to avoid data leakage from post-triage outcomes  
- Temperature is recorded in Fahrenheit and must be standardised prior to analysis  
- Missingness likely reflects clinical workflow rather than random absence, limiting naive imputation strategies  

---

## Conclusion
The dataset is suitable for exploratory triage prediction modelling following appropriate preprocessing, feature engineering, and bias evaluation. Any model developed should be considered exploratory and intended for clinical decision-support only, rather than deployment-ready.
