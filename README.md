# Insurance Claims Analytics

> **End-to-End Insurance Claims Analytics | Excel | SQL | Snowflake | Python | Machine Learning | Power BI | Streamlit | GitHub**

An end-to-end insurance claims analytics project that transforms raw claim data into business-ready insights through data profiling, SQL cleaning and transformation, exploratory analysis, diagnostic analysis, predictive modeling, Power BI dashboards, and a Streamlit application.

## Project Overview

This project analyzes insurance claims to understand claim volume, financial exposure, insurance products, risk segmentation, incident severity, reporting behavior, agents, vendors, and claim amount prediction.

## Business Objectives

| #  | Objective                                                    |
| -- | ------------------------------------------------------------ |
| 1  | Analyze overall insurance claim activity                     |
| 2  | Understand claim distribution across insurance types         |
| 3  | Analyze risk segmentation and incident severity              |
| 4  | Analyze claim amount and premium exposure                    |
| 5  | Examine reporting delays and reporting behavior              |
| 6  | Analyze claim exposure across agents and vendors             |
| 7  | Identify relationships and patterns between claim attributes |
| 8  | Estimate claim amounts using machine learning                |
| 9  | Build interactive Power BI dashboards                        |
| 10 | Develop an interactive Streamlit analytics application       |

## End-to-End Workflow

```text
Raw CSV Data
    ↓
Excel Data Profiling
    ↓
Snowflake Data Storage
    ↓
SQL Validation
    ↓
SQL Cleaning
    ↓
SQL Transformation
    ↓
CLAIMS_ANALYTICS_VW
    ↓
Python
    ├── EDA
    ├── Diagnostic Analysis
    └── Machine Learning
    ↓
Power BI Dashboards
    ↓
Streamlit Application
    ↓
Business Insights & Reporting
```

## Dataset

| Dataset        |       Rows | Columns | Purpose                      |
| -------------- | ---------: | ------: | ---------------------------- |
| Insurance Data |     10,000 |      38 | Main claim-level analysis    |
| Employee Data  |      1,200 |      10 | Agent/employee information   |
| Vendor Data    |        600 |       7 | Vendor information           |
| **Total**      | **11,800** |  **55** | **Complete project dataset** |

## Dataset Relationships

| Relationship         | Key         | Purpose                               |
| -------------------- | ----------- | ------------------------------------- |
| Employee → Insurance | `AGENT_ID`  | Connects agents/employees with claims |
| Vendor → Insurance   | `VENDOR_ID` | Connects vendors with claims          |

**Agent:** the insurance representative associated with a policy or claim. `AGENT_ID` is used for claim volume and claim exposure analysis.

**Vendor:** an external service provider associated with a claim when available. `VENDOR_ID` is used for claim volume and claim exposure analysis.

## Data Quality & Cleaning

Data profiling was performed in Excel. Main cleaning and transformation were performed using SQL in Snowflake.

| Data Quality Check                 |          Result |
| ---------------------------------- | --------------: |
| Full-row duplicates                | None identified |
| Invalid Agent References           |               0 |
| Invalid non-null Vendor References |               0 |
| Policy Effective Date > Loss Date  |               0 |
| Report Date < Loss Date            |               0 |
| Negative Claim Amounts             |               0 |
| Negative Premiums                  |               0 |

### Important Missing Values

| Column                     | Missing Records | Missing % |
| -------------------------- | --------------: | --------: |
| `ADDRESS_LINE2`            |           8,505 |    85.05% |
| `VENDOR_ID`                |           3,245 |    32.45% |
| `AUTHORITY_CONTACTED`      |           1,945 |    19.45% |
| `CUSTOMER_EDUCATION_LEVEL` |             529 |     5.29% |
| `CITY`                     |              54 |     0.54% |
| `INCIDENT_CITY`            |              46 |     0.46% |

Descriptive missing values were standardized where appropriate. Missing `VENDOR_ID` values were retained when no reliable vendor information was available.

## Sensitive Data Handling

| Sensitive Field | Analytical Layer |
| --------------- | ---------------- |
| SSN             | Excluded         |
| Account Number  | Excluded         |
| Routing Number  | Excluded         |

Credentials and secrets should never be committed to GitHub.

## Snowflake Platform

| Component            | Value                 |
| -------------------- | --------------------- |
| Database             | `INSURANCE_CLAIMS_DB` |
| Schema               | `CLAIMS`              |
| Warehouse            | `INSURANCE_CLAIMS_WH` |
| Main Analytical View | `CLAIMS_ANALYTICS_VW` |

## SQL Data Transformation

`CLAIMS_ANALYTICS_VW` is the centralized analytical layer used by Python, Power BI, and Streamlit.

| Derived Field            | Purpose                                |
| ------------------------ | -------------------------------------- |
| `REPORTING_DELAY_DAYS`   | Days between loss date and report date |
| `CLAIM_TO_PREMIUM_RATIO` | Claim amount relative to premium       |
| `AGE_GROUP`              | Customer age segmentation              |
| `TENURE_GROUP`           | Tenure segmentation                    |
| `CLAIM_AMOUNT_BUCKET`    | Claim amount categorization            |
| `REPORTING_CATEGORY`     | Reporting delay categorization         |
| `CLAIM_VALUE_CATEGORY`   | Claim value categorization             |
| `LOSS_YEAR`              | Year from loss date                    |
| `LOSS_MONTH`             | Month from loss date                   |
| `LOSS_MONTH_NAME`        | Month name from loss date              |

## Exploratory Data Analysis

| Analysis Area     | Variables / Metrics                   |
| ----------------- | ------------------------------------- |
| Claim Amount      | Minimum, maximum, mean, median, total |
| Premium           | Minimum, maximum, mean, total         |
| Insurance Type    | Claim distribution                    |
| Risk              | Low, Medium, High                     |
| Incident Severity | Minor Loss, Major Loss, Total Loss    |
| Customer          | Age, tenure, demographics             |
| Reporting         | Reporting delay, same-day reporting   |
| Agent             | Claim volume and exposure             |
| Vendor            | Claim volume and exposure             |

## Key Descriptive Metrics

| Metric                            |        Value |
| --------------------------------- | -----------: |
| Total Claims                      |       10,000 |
| Total Claim Amount                | ₹165,638,300 |
| Average Claim Amount              |   ₹16,563.83 |
| Median Claim Amount               |       ₹7,000 |
| Minimum Claim Amount              |         ₹100 |
| Maximum Claim Amount              |     ₹100,000 |
| Total Premium                     |  ₹885,085.95 |
| Average Premium                   |       ₹88.51 |
| Minimum Premium                   |           ₹6 |
| Maximum Premium                   |         ₹200 |
| Average Reporting Delay           |    3.21 days |
| Reporting Delay Range             |     0–5 days |
| Same-Day Claims                   |        1,565 |
| Total Customers                   |       10,000 |
| Total Agents                      |        1,200 |
| Unique Non-null Vendors in Claims |          407 |
| Insurance Types                   |            6 |

## Insurance Type Distribution

| Insurance Type | Claims |
| -------------- | -----: |
| Property       |  1,692 |
| Mobile         |  1,692 |
| Health         |  1,690 |
| Life           |  1,682 |
| Travel         |  1,670 |
| Motor          |  1,574 |

## Risk Segmentation

| Risk Segment |     Claims |
| ------------ | ---------: |
| Low          |      4,395 |
| Medium       |      4,150 |
| High         |      1,455 |
| **Total**    | **10,000** |

Risk segmentation is a source-data category and is not treated as a fraud label.

## Incident Severity

| Incident Severity |     Claims |
| ----------------- | ---------: |
| Total Loss        |      3,390 |
| Major Loss        |      3,317 |
| Minor Loss        |      3,293 |
| **Total**         | **10,000** |

| Attribute         | Meaning                                             |
| ----------------- | --------------------------------------------------- |
| Risk Segmentation | Assigned risk category                              |
| Incident Severity | Level/category of loss associated with the incident |

## Diagnostic Analysis

| #  | Relationship / Analysis        | Method                |
| -- | ------------------------------ | --------------------- |
| 1  | Risk × Incident Severity       | Cross-tabulation      |
| 2  | Insurance Type × Risk          | Cross-tabulation      |
| 3  | Insurance Type × Severity      | Cross-tabulation      |
| 4  | Risk × Claim Amount            | GroupBy + Aggregation |
| 5  | Severity × Claim Amount        | GroupBy + Aggregation |
| 6  | Injury × Incident Severity     | Cross-tabulation      |
| 7  | Police Report × Severity       | Cross-tabulation      |
| 8  | Reporting Delay × Claim Amount | GroupBy + Aggregation |
| 9  | Agent Analysis                 | GroupBy + Aggregation |
| 10 | Vendor Analysis                | GroupBy + Aggregation |

| Method           | Purpose                           |
| ---------------- | --------------------------------- |
| Cross-tabulation | Examine categorical relationships |
| GroupBy          | Compare groups                    |
| Count            | Measure records                   |
| Mean             | Compare averages                  |
| Median           | Compare central values            |
| Sum              | Compare financial exposure        |

> **Diagnostic analysis identifies relationships and patterns in claim data. It does not establish causation.**

## Predictive Analysis

### Target

| Target Variable | Description                  |
| --------------- | ---------------------------- |
| `CLAIM_AMOUNT`  | Claim amount to be estimated |

### Numerical Features

| Feature                    |
| -------------------------- |
| `AGE`                      |
| `TENURE`                   |
| `INCIDENT_HOUR_OF_THE_DAY` |
| `REPORTING_DELAY_DAYS`     |

### Categorical Features

| Feature                    |
| -------------------------- |
| `INSURANCE_TYPE`           |
| `RISK_SEGMENTATION`        |
| `INCIDENT_SEVERITY`        |
| `MARITAL_STATUS`           |
| `EMPLOYMENT_STATUS`        |
| `HOUSE_TYPE`               |
| `SOCIAL_CLASS`             |
| `CUSTOMER_EDUCATION_LEVEL` |
| `ANY_INJURY`               |
| `POLICE_REPORT_AVAILABLE`  |

## Machine Learning Pipeline

| Stage                | Approach                |
| -------------------- | ----------------------- |
| Target               | `CLAIM_AMOUNT`          |
| Train/Test Split     | 80% / 20%               |
| Random State         | 42                      |
| Missing Values       | Simple Imputation       |
| Categorical Encoding | One-Hot Encoding        |
| Preprocessing        | `ColumnTransformer`     |
| Model 1              | Linear Regression       |
| Model 2              | Random Forest Regressor |
| Evaluation           | MAE, RMSE, R²           |

## Model Performance

| Model             |      MAE |      RMSE |     R² |
| ----------------- | -------: | --------: | -----: |
| Linear Regression | 6,935.15 | 11,976.84 | 0.7066 |
| Random Forest     | 6,903.99 | 12,250.86 | 0.6930 |

| Comparison           | Result            |
| -------------------- | ----------------- |
| Lower MAE            | Random Forest     |
| Lower RMSE           | Linear Regression |
| Higher R²            | Linear Regression |
| Final Selected Model | Linear Regression |

Linear Regression was selected based on the combined test-set performance across MAE, RMSE, and R². An R² of 0.7066 means the model explains approximately 70.66% of the variation in test-set claim amounts; it is not 70.66% prediction accuracy.

## Power BI Dashboards

| Dashboard                       | Main Focus                            | Key Components                                            |
| ------------------------------- | ------------------------------------- | --------------------------------------------------------- |
| 01 - Claims Overview            | Overall claims and financial exposure | KPIs, monthly trend, insurance type, premium              |
| 02 - Risk & Severity            | Risk and incident severity            | Risk, severity, risk × severity, exposure, age            |
| 03 - Operations & Investigation | Operational claim behavior            | Reporting delay, high-value claims, agent/vendor exposure |

## Streamlit Application

| Section              | Main Content                              |
| -------------------- | ----------------------------------------- |
| Overview             | KPIs, claim summary, charts               |
| Descriptive Analysis | Distribution and category analysis        |
| Diagnostic Analysis  | Relationships and operational analysis    |
| Predictive Analysis  | Claim amount prediction and model results |
| About Project        | Project information and technology stack  |

### Interactive Filters

| Filter            |
| ----------------- |
| Insurance Type    |
| Risk Segment      |
| Incident Severity |

## Streamlit Architecture

```text
Snowflake
    ↓
CLAIMS_ANALYTICS_VW
    ↓
Streamlit
    ↓
Pandas
    ├── Filters
    ├── KPIs
    ├── Charts
    └── ML Prediction
```

## Technology Stack

| Technology      | Category                | Purpose                                        |
| --------------- | ----------------------- | ---------------------------------------------- |
| Microsoft Excel | Data Analytics          | Data profiling and preparation                 |
| Snowflake       | Cloud Data Warehouse    | Data storage and SQL analytics                 |
| SQL             | Data Analytics          | Validation, cleaning, transformation, analysis |
| Python          | Programming             | EDA, visualization, machine learning           |
| Pandas          | Python Library          | Data manipulation                              |
| NumPy           | Python Library          | Numerical operations                           |
| Matplotlib      | Python Library          | Visualization                                  |
| Seaborn         | Python Library          | Statistical visualization                      |
| Scikit-learn    | Machine Learning        | Regression and evaluation                      |
| Power BI        | Business Intelligence   | Interactive dashboards                         |
| Streamlit       | Application Development | Interactive analytics application              |
| Git             | Version Control         | Source control                                 |
| GitHub          | Collaboration           | Repository and documentation                   |

## Project Architecture

| Layer           | Technology   | Responsibility                          |
| --------------- | ------------ | --------------------------------------- |
| Data Source     | CSV          | Raw insurance, employee and vendor data |
| Profiling       | Excel        | Data profiling and quality assessment   |
| Storage         | Snowflake    | Centralized cloud data storage          |
| Cleaning        | SQL          | Data cleaning and standardization       |
| Transformation  | SQL          | Analytical fields and views             |
| Analytics       | Python       | EDA and diagnostic analysis             |
| ML              | Scikit-learn | Claim amount prediction                 |
| BI              | Power BI     | Business dashboards                     |
| Application     | Streamlit    | Interactive analytics                   |
| Version Control | GitHub       | Project management and documentation    |

## Snowflake Architecture

```text
INSURANCE_CLAIMS_DB
│
└── CLAIMS
    ├── INSURANCE_DATA
    ├── EMPLOYEE_DATA
    ├── VENDOR_DATA
    ├── INSURANCE_CLEANED
    ├── EMPLOYEE_CLEANED
    ├── VENDOR_CLEANED
    ├── INSURANCE_ANALYTICS
    └── Analytical Views
        ├── CLAIMS_ANALYTICS_VW
        ├── CLAIMS_SUMMARY_VW
        ├── INSURANCE_TYPE_VW
        ├── RISK_SEGMENT_VW
        ├── INCIDENT_SEVERITY_VW
        ├── AGENT_PERFORMANCE_VW
        ├── VENDOR_PERFORMANCE_VW
        ├── MONTHLY_CLAIMS_TREND_VW
        ├── STATE_CLAIMS_VW
        └── CLAIM_INVESTIGATION_PRIORITY_VW
```

## Repository Structure

```text
insurance-claims-analytics/
│
├── Dataset/
│   ├── employee_data.csv
│   ├── insurance_data.csv
│   └── vendor_data.csv
│
├── Excel/
├── PowerBI/
├── Python/
├── Reports/
├── SQL/
│   ├── 01_Database_Setup.sql
│   ├── 02_Raw_Data_Validation.sql
│   ├── 03_Data_Cleaning.sql
│   ├── 04_Cleaned_Data_Validation.sql
│   ├── 05_Data_Transformation.sql
│   ├── 06_EDA_Business_Analysis.sql
│   └── 07_Final_Views.sql
│
├── Streamlit_App/
└── README.md
```

## SQL Pipeline

| File                             | Stage            | Purpose                                  |
| -------------------------------- | ---------------- | ---------------------------------------- |
| `01_Database_Setup.sql`          | Database Setup   | Creates database objects and environment |
| `02_Raw_Data_Validation.sql`     | Raw Validation   | Validates raw datasets                   |
| `03_Data_Cleaning.sql`           | Data Cleaning    | Cleans and standardizes data             |
| `04_Cleaned_Data_Validation.sql` | Validation       | Validates cleaned datasets               |
| `05_Data_Transformation.sql`     | Transformation   | Creates analytical fields                |
| `06_EDA_Business_Analysis.sql`   | Analysis         | SQL EDA and business analysis            |
| `07_Final_Views.sql`             | Analytical Layer | Creates reusable analytical views        |

## Final Analytical Views

| View                              | Purpose                           |
| --------------------------------- | --------------------------------- |
| `CLAIMS_ANALYTICS_VW`             | Central analytical dataset        |
| `CLAIMS_SUMMARY_VW`               | Overall claims summary            |
| `INSURANCE_TYPE_VW`               | Insurance type analysis           |
| `RISK_SEGMENT_VW`                 | Risk segment analysis             |
| `INCIDENT_SEVERITY_VW`            | Severity analysis                 |
| `AGENT_PERFORMANCE_VW`            | Agent-level claim exposure        |
| `VENDOR_PERFORMANCE_VW`           | Vendor-level claim exposure       |
| `MONTHLY_CLAIMS_TREND_VW`         | Monthly claim trend               |
| `STATE_CLAIMS_VW`                 | State-level claim analysis        |
| `CLAIM_INVESTIGATION_PRIORITY_VW` | Rule-based investigation analysis |

## Key Analytical Insights

| Area               | Insight                                                                     |
| ------------------ | --------------------------------------------------------------------------- |
| Claim Amount       | Average ₹16,563.83 vs median ₹7,000, indicating a right-skewed distribution |
| Risk               | 1,455 claims are categorized as High Risk                                   |
| Severity           | Claims are distributed across Minor, Major and Total Loss                   |
| Reporting          | Reporting delays range from 0 to 5 days                                     |
| Same-Day Reporting | 1,565 claims were reported on the same day                                  |
| Agents             | Agent-level analysis shows claim volume and financial exposure              |
| Vendors            | Vendor-level analysis shows claim volume and financial exposure             |
| Prediction         | Linear Regression achieved R² of 0.7066 on the test set                     |

## Analytical Limitations

| Limitation                | Explanation                                            |
| ------------------------- | ------------------------------------------------------ |
| No explicit fraud label   | Dataset does not contain a dedicated fraud target      |
| No supervised fraud model | Fraud classification was therefore not implemented     |
| Diagnostic analysis       | Identifies patterns but does not prove causation       |
| Agent/Vendor exposure     | Exposure alone does not establish service quality      |
| ML predictions            | Predictions are estimates, not guaranteed claim values |
| Missing Vendor IDs        | Retained when reliable information was unavailable     |
| Model performance         | Depends on the available dataset and test split        |

## Security & Privacy

| Item               | Handling                           |
| ------------------ | ---------------------------------- |
| Snowflake Password | Store securely outside source code |
| Streamlit Secrets  | Store in `.streamlit/secrets.toml` |
| API Keys           | Never commit                       |
| SSN                | Excluded from analytical outputs   |
| Account Number     | Excluded from analytical outputs   |
| Routing Number     | Excluded from analytical outputs   |

Recommended `.gitignore`:

```text
.streamlit/secrets.toml
__pycache__/
*.pyc
```

## How to Run

### 1. Clone Repository

```bash
git clone https://github.com/shubham-vishwakarma-analytics/insurance-claims-analytics.git
cd insurance-claims-analytics
```

### 2. Install Python Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit snowflake-connector-python
```

### 3. Configure Streamlit Secrets

Create:

```text
.streamlit/secrets.toml
```

Store the required Snowflake credentials securely. Do not commit this file.

### 4. Run Streamlit

```bash
streamlit run Streamlit_App/app.py
```

Update the entry-file path if the application uses a different filename.

## Project Deliverables

| Deliverable               | Status    |
| ------------------------- | --------- |
| Excel Data Profiling      | Completed |
| Excel Data Preparation    | Completed |
| Snowflake Database Setup  | Completed |
| Raw Data Validation       | Completed |
| SQL Data Cleaning         | Completed |
| Cleaned Data Validation   | Completed |
| SQL Data Transformation   | Completed |
| SQL Business Analysis     | Completed |
| Final SQL Views           | Completed |
| Python Analysis           | Completed |
| Exploratory Data Analysis | Completed |
| Diagnostic Analysis       | Completed |
| Machine Learning          | Completed |
| Model Evaluation          | Completed |
| Power BI Dashboards       | Completed |
| Streamlit Application     | Completed |
| Project Presentation      | Completed |
| Project Reports           | Completed |
| GitHub Repository         | Completed |

## Skills Demonstrated

| Skill Area       | Skills                                                                           |
| ---------------- | -------------------------------------------------------------------------------- |
| Data Analytics   | Profiling, Cleaning, Transformation, EDA, Diagnostic Analysis, Business Analysis |
| SQL              | Validation, Cleaning, Joins, GroupBy, Aggregations, CASE, Date Functions, Views  |
| Python           | Pandas, NumPy, Matplotlib, Seaborn                                               |
| Machine Learning | Regression, Feature Selection, Encoding, Imputation, MAE, RMSE, R²               |
| Power BI         | KPI Cards, Slicers, Charts, Dashboards, Business Reporting                       |
| Snowflake        | Cloud Data Warehouse, SQL Analytics, Analytical Views                            |
| Streamlit        | Interactive filters, KPIs, charts, ML integration                                |
| Git/GitHub       | Version control, repository organization, documentation                          |

## Project Outcome

The project demonstrates the complete analytics lifecycle:

```text
DATA
 ↓
PROFILE
 ↓
CLEAN
 ↓
VALIDATE
 ↓
TRANSFORM
 ↓
ANALYZE
 ↓
VISUALIZE
 ↓
MODEL
 ↓
PREDICT
 ↓
REPORT
 ↓
INTERACT
```

The final solution combines **Excel, Snowflake SQL, Python, Machine Learning, Power BI, Streamlit, and GitHub** to transform raw insurance claims data into a structured analytics solution for understanding claims behavior, risk, severity, financial exposure, reporting patterns, and claim amount estimation.

## Author

**Shubham Vishwakarma**
B.Tech Information Technology — 2026
**Data Analytics | SQL | Python | Power BI | Snowflake | Machine Learning**
