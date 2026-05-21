# carisurg-portfolio

### Overview

Week 0 - Assignment 1

## Assignment 1 (Gender Column Cleaning)

Assignment 1 focused on cleaning the `Gender` column in a dataset for Mercer General Hospital’s Clinical AI & Innovation Unit. The purpose of the activity was to demonstrate the importance of data cleaning and preprocessing before performing analysis or using machine learning models. The dataset used was *EmergencyTriageDataset_Reduced_Dirty.csv*, where the `Gender` column contained inconsistent values that could lead to inaccurate results if left uncleaned.

The following mappings were used to standardize the data:

1. `Male`, `MALE`, and `1` were converted to `1`
2. `Female`, `FEMALE`, and `0` were converted to `0`

This cleaning process improved consistency, reduced errors, and made the dataset more reliable for analysis. It also showed how differences in capitalization, numeric values, and missing data can affect data quality. Clear and readable Python code was used to load the CSV file, clean the `Gender` column, and document each step so the process could be easily understood and repeated.



Week 0 - Assignment 2

## Assignment 2: Advanced Cleaning (DBP Column)

# Assignment: Cleaning the DBP Column

## Overview

This notebook focuses on cleaning the **DBP (Diastolic Blood Pressure)** column in the dataset. DBP represents the pressure in the arteries when the heart rests between beats and is important for accurate clinical analysis and MAP calculations.

---

## Cleaning Steps

### 1. Import Libraries

`pandas` and `numpy` were imported for data handling and cleaning.

### 2. Load Dataset

The dataset was loaded directly from Google Drive using `pd.read_csv()`.
`df_raw.info()` was used to inspect column types and missing values.

### 3. Convert DBP to Numeric

```python id="e1d6um"
df_raw['DBP'] = pd.to_numeric(df_raw['DBP'], errors='coerce')
```

This converted invalid or non-numeric entries into `NaN` values for easier cleaning.

### 4. Identify and Handle Outliers

DBP values outside the clinical range of **30–150 mmHg** were treated as outliers and replaced with `NaN`.

```python id="8tkr8v"
df_raw.loc[(df_raw['DBP'] < 30) | (df_raw['DBP'] > 150), 'DBP'] = np.nan
```

### 5. Impute Missing Values

Missing values were filled using the median because the median is less affected by extreme values.

```python id="9n2b6o"
median_value = df_raw['DBP'].median()
df_raw['DBP'] = df_raw['DBP'].fillna(median_value)
```

### 6. Verify Cleaning Results

`describe()` and `isnull().sum()` were used to confirm the column was cleaned successfully.

---

## Screenshot Included

* `dbp_cleaned_summary.png`

The screenshot shows the cleaned DBP summary statistics after handling missing values and outliers.

---

## Deliverables

* Cleaning notebook with comments explaining decisions
* Screenshot shared on Discord
* Notebook uploaded to the `carisurg-portfolio` GitHub repository

### Commit Message

```bash id="v5rr1y"
Cleaned DBP column: handled NaNs, outliers, and imputed with median
```
