# Insurance Analytics EDA

This repository contains exploratory data analysis (EDA) for historical car insurance claim data from **AlphaCare Insurance Solutions (ACIS)**. The goal of this analysis is to optimize marketing strategies and identify "low-risk" clients to attract new business by offering competitive premiums.

---

## Project Objectives

- Understand the structure and distribution of the data.
- Explore patterns and relationships among key variables.
- Segment clients into risk profiles (e.g., high-risk and low-risk).
- Provide actionable insights for optimizing insurance marketing strategies.

---

## Dataset Overview

The dataset includes historical insurance data from **February 2014** to **August 2015**, covering various client demographics, vehicle details, and insurance claims.

### Key Columns

- **Policy Details**: `UnderwrittenCoverID`, `PolicyID`, `TransactionMonth`
- **Client Information**: `IsVATRegistered`, `Citizenship`, `LegalType`, `Gender`, `Province`, `MaritalStatus`
- **Vehicle Information**: `VehicleType`, `RegistrationYear`, `Make`, `Model`, `CubicCapacity`
- **Insurance Plan**: `SumInsured`, `CalculatedPremiumPerTerm`, `CoverType`, `TotalPremium`, `TotalClaims`

---

## Analysis Steps

1. **Data Cleaning**: Handle missing values and ensure consistency in data types.
2. **Exploratory Analysis**:
   - Distribution of premiums, claims, and insured sums.
   - Relationships between variables (e.g., `TotalPremium` vs. `TotalClaims`).
   - Client segmentation by demographics, geography, and risk.
3. **Visualization**:
   - Histograms, scatter plots, bar charts, and heatmaps.
4. **Insights**:
   - Identify high-risk and low-risk clients.
   - Regional trends in claims and premiums.
   - Correlations between client attributes and claim rates.

---

## Repository Structure

```plaintext
.
├── data/                     # Dataset (not included for privacy)
├── notebooks/                # Jupyter notebooks for EDA
├── scripts/                  # Python scripts for data preprocessing and visualization
├── src/                      # Source code for the project
│   ├── __init__.py           # Initialize the src module
│   ├── data_preprocessing.py # Data preprocessing scripts
│   ├── visualization.py      # Visualization scripts
│   └── analysis.py           # Analysis scripts
├── tests/                    # Unit tests for the project
│   ├── __init__.py           # Initialize the tests module
│   ├── test_data_preprocessing.py # Unit tests for data preprocessing
│   ├── test_visualization.py      # Unit tests for visualization
│   └── test_analysis.py           # Unit tests for analysis
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
