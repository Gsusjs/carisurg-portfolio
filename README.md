# carisurg-portfolio

Overview
Assignment One at Mercer General Hospital’s Clinical AI & Innovation Unit focused on the importance of data cleaning and preprocessing to prepare a triage dataset for accurate analysis and machine learning tasks. The activity used the file EmergencyTriageDataset_Reduced_Dirty.csv, where the Gender column contained inconsistent values that could lead to inaccurate results if left uncleaned. The main objective was to improve data quality, ensure consistency, and prevent analytical errors by standardizing the values into a single binary format.

The following mappings were applied during the cleaning process:

1. `Male`, `MALE`, and `1` were converted to `1`
2. `Female`, `FEMALE`, and `0` were converted to `0`

This process demonstrated how inconsistent entries, capitalization differences, numeric encodings, and missing data in a triage AI context can affect the reliability of a dataset and weaken statistical or machine learning models. Clear and readable Python code was used to load the CSV file, clean the Gender column, and document each transformation step so the workflow could be easily understood and reproduced.

