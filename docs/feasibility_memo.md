# Feasibility Memo — ED Triage AI System

## (a) One-sentence verdict
Proceed with development with caveats due to strong predictive signal in vital signs but significant missingness and inconsistency in laboratory and secondary clinical features.

---

## (b) Dataset summary
This dataset contains emergency department (ED) triage records designed for clinical risk stratification modelling.

- Approximately 225 clinical features per patient
- Includes:
  - Patient demographics (e.g. age, sex, ethnicity)
  - Vital signs (e.g. heart rate, blood pressure, respiratory rate, temperature)
  - Laboratory measurements (e.g. blood chemistry, haematology markers)
  - Chief complaints and presenting symptoms
- Target variable: `Triage_Level`
- Data reflects real-world ED workflows where not all clinical measurements are consistently recorded at point of triage

The dataset is clinically rich but structurally heterogeneous, with variable completeness across feature types.

---

## (c) Top 3 data quality concerns

### 1. High and uneven missingness in laboratory features
A large proportion of laboratory variables are missing, likely due to selective ordering of tests based on initial clinical judgment. This introduces potential selection bias and limits their reliability in early triage prediction.

### 2. Data type inconsistencies across features
Several variables that are expected to be numeric are stored as object/string types, suggesting parsing issues or inconsistent recording formats. This may require significant preprocessing before modelling.

### 3. Potential mismatch between recorded features and triage decision timing
Some variables may represent information collected after initial triage classification, raising the risk of data leakage if used in predictive modelling.

---

## (d) Top 3 reasons to proceed

### 1. Strong signal in vital signs
Core physiological variables such as heart rate, respiratory rate, blood pressure, and temperature are consistently available and are clinically validated indicators of patient acuity.

### 2. High clinical richness of feature space
The dataset includes a broad range of clinical inputs (demographics, symptoms, labs), enabling the possibility of building a multi-factor triage prediction model.

### 3. Structured and usable target variable
The `Triage_Level` outcome is clearly defined and suitable for supervised learning, enabling model training and evaluation.

---

## (e) Key caveats and risks
- Missingness is not random and likely reflects clinical decision-making patterns, introducing potential bias
- Single-site dataset limits generalisability to other hospitals or healthcare systems
- Some variables may not be available at true point-of-triage, which may lead to unrealistic model assumptions if not carefully filtered
- Data preprocessing burden is significant due to mixed types and inconsistent formatting

---

## Final interpretation
While the dataset contains strong clinically relevant signals, particularly in physiological measurements, careful preprocessing and feature selection will be required. A model built on this dataset should initially be considered a decision-support prototype rather than a fully deployable clinical system.

