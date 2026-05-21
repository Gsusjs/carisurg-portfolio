# carisurg-portfolio

### Overview

Week 0 – Assignment 1 focused on cleaning the `Gender` column in a dataset for Mercer General Hospital’s Clinical AI & Innovation Unit. The purpose of the activity was to demonstrate the importance of data cleaning and preprocessing before performing analysis or using machine learning models. The dataset used was *EmergencyTriageDataset_Reduced_Dirty.csv*, where the `Gender` column contained inconsistent values that could lead to inaccurate results if left uncleaned.

The following mappings were used to standardize the data:

1. `Male`, `MALE`, and `1` were converted to `1`
2. `Female`, `FEMALE`, and `0` were converted to `0`

This cleaning process improved consistency, reduced errors, and made the dataset more reliable for analysis. It also showed how differences in capitalization, numeric values, and missing data can affect data quality. Clear and readable Python code was used to load the CSV file, clean the `Gender` column, and document each step so the process could be easily understood and repeated.
