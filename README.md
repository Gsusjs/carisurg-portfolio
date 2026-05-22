# carisurg-portfolio

### Overview
---



---

Week 0 - Assignment 1

## Assignment 1 (Gender Column Cleaning)

Assignment 1 focused on cleaning the `Gender` column in a dataset for Mercer General Hospital’s Clinical AI & Innovation Unit. The purpose of the activity was to demonstrate the importance of data cleaning and preprocessing before performing analysis or using machine learning models. The dataset used was *EmergencyTriageDataset_Reduced_Dirty.csv*, where the `Gender` column contained inconsistent values that could lead to inaccurate results if left uncleaned.

The following mappings were used to standardize the data:

1. `Male`, `MALE`, and `1` were converted to `1`
2. `Female`, `FEMALE`, and `0` were converted to `0`

This cleaning process improved consistency, reduced errors, and made the dataset more reliable for analysis. It also showed how differences in capitalization, numeric values, and missing data can affect data quality. Clear and readable Python code was used to load the CSV file, clean the `Gender` column, and document each step so the process could be easily understood and repeated.

## Gender Column Cleaning Output

## Assignment 2: DBP Cleaning Output

![DBP cleaned summary](screenshots/week_0/Assignment_2/dbp_cleaned_summary.png)

---
Week 0 - Assignment 2

## Assignment 2: Advanced Cleaning (DBP Column)

# Assignment: Cleaning the DBP Column

## Overview

I chose the **DBP (Diastolic Blood Pressure)** column for cleaning. DBP represents the pressure in the arteries when the heart rests between beats and is important for accurate clinical analysis and MAP calculations. The DBP column was selected because accurate diastolic blood pressure values are essential for patient assessment and reliable analysis results.

## What Was Done and Why

* Imported `pandas` and `numpy` for data handling and numerical operations.
* Loaded the dataset from Google Drive using its file ID for reliable access in Colab.
* Defined physiological DBP limits (`30–150 mmHg`) to identify unrealistic values.
* Converted DBP values to numeric using `errors='coerce'`, replacing invalid entries with `NaN`.
* Replaced out-of-range values with `NaN` because they are not clinically valid.
* Imputed missing values using the median, since it is resistant to outliers.
* Printed the number of corrected outliers, summary statistics, and remaining `NaN` values to verify successful cleaning.

This approach demonstrates correct handling of invalid data, clinical understanding through the use of realistic physiological limits, and readable code through clear variable names and concise outputs.

## DBP Cleaning Output

## Assignment 2: DBP Cleaning Output

![DBP cleaned summary](screenshots/week_0/Assignment_2/dbp_cleaned_summary.png)
