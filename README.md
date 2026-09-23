# Insurance Claims Analytics

> End-to-end insurance claims analytics project using Excel, SQL, Snowflake, Python, Machine Learning, Power BI, Streamlit, and GitHub.

![Insurance Claims Analytics](Reports/Insurance_Claims_Analytics.pdf)

**Author:** Shubham Vishwakarma  
**Project Type:** End-to-End Data Analytics & Machine Learning  
**Domain:** Insurance / Claims Analytics

## Live Project

### [View Live Streamlit App — Insurance Claims Risk Analytics](https://insurance-claims-risk-analytics.streamlit.app/)

> Interactive Streamlit application for exploring insurance claims, financial exposure, risk segmentation, incident severity, reporting behavior, agent and vendor analysis, and claim amount prediction.

### [View Final Project Report](Reports/Insurance_Claims_Analytics.pdf)

> Complete project report covering the business problem, data quality, Snowflake architecture, SQL analysis, Python EDA, diagnostic analysis, machine learning, Power BI dashboards, Streamlit application, key findings, and business recommendations.

---

## Project Overview

Insurance Claims Analytics is an end-to-end analytics project that transforms raw insurance claim data into a structured analytical solution using Excel, Snowflake SQL, Python, Machine Learning, Power BI, and Streamlit.

The project analyzes:

- Claim volume
- Financial exposure
- Insurance types
- Risk segmentation
- Incident severity
- Customer characteristics
- Reporting behavior
- Agents
- Vendors
- Claim amount prediction

The project covers the complete analytics lifecycle:

```text
Raw Insurance Data
        ↓
Excel Data Profiling
        ↓
Snowflake Data Storage
        ↓
SQL Validation
        ↓
SQL Cleaning & Transformation
        ↓
Analytical Views
        ↓
Python EDA
        ↓
Diagnostic Analysis
        ↓
Machine Learning
        ↓
Power BI Dashboards
        ↓
Streamlit Application
        ↓
Business Insights
        ↓
Recommendations
```

---

## Business Objectives

| # | Objective |
|---|---|
| 1 | Analyze overall insurance claim activity |
| 2 | Understand claim distribution across insurance types |
| 3 | Analyze risk segmentation and incident severity |
| 4 | Analyze claim amount and premium exposure |
| 5 | Examine reporting delays and reporting behavior |
| 6 | Analyze claim exposure across agents and vendors |
| 7 | Identify relationships and patterns between claim attributes |
| 8 | Estimate claim amounts using machine learning |
| 9 | Build interactive Power BI dashboards |
| 10 | Develop an interactive Streamlit analytics application |

---

## Project at a Glance

| KPI | Result |
|---|---:|
| Total Claims | 10,000 |
| Total Claim Amount | ₹165.64M |
| Average Claim Amount | ₹16,563.83 |
| Median Claim Amount | ₹7,000 |
| Total Premium | ₹885,085.95 |
| Average Premium | ₹88.51 |
| Average Reporting Delay | 3.21 days |
| Same-Day Claims | 1,565 |
| Insurance Types | 6 |
| Total Agents | 1,200 |
| Unique Non-null Vendors | 407 |
| Linear Regression R² | 0.7066 |

---

## End-to-End Workflow

```text
Raw CSV Data
        ↓
Excel Data Profiling
        ↓
Snowflake
        ↓
SQL Data Validation
        ↓
SQL Data Cleaning
        ↓
SQL Data Transformation
        ↓
CLAIMS_ANALYTICS_VW
        ↓
Python
    ├── EDA
    ├── Diagnostic Analysis
    └── Machine Learning
        ↓
Power BI
    ├── Claims Overview
    ├── Risk & Severity
    └── Claims Operations & Review
        ↓
Streamlit
    ├── Overview
    ├── Descriptive Analysis
    ├── Diagnostic Analysis
    └── Predictive Analysis
        ↓
Business Insights
        ↓
Recommendations
```

---

# Dataset

The project uses three core datasets.

| Dataset | Rows | Columns | Purpose |
|---|---:|---:|---|
| Insurance Data | 10,000 | 38 | Main claim-level analysis |
| Employee Data | 1,200 | 10 | Agent/employee information |
| Vendor Data | 600 | 7 | Vendor information |
| **Total** | **11,800** | **55** | **Complete project dataset** |

## Source Tables

```text
INSURANCE_DATA
EMPLOYEE_DATA
VENDOR_DATA
```

---

# Dataset Relationships

| Relationship | Key | Purpose |
|---|---|---|
| Employee → Insurance | `AGENT_ID` | Connects agents/employees with claims |
| Vendor → Insurance | `VENDOR_ID` | Connects vendors with claims |

**Agent:** the insurance representative associated with a policy or claim. `AGENT_ID` is used for claim volume and claim exposure analysis.

**Vendor:** an external service provider associated with a claim when available. `VENDOR_ID` is used for claim volume and claim exposure analysis.

---

# Data Quality & Cleaning

Data profiling was performed in Excel, while the main cleaning and transformation workflow was performed using SQL in Snowflake.

## Data Quality Checks

| Data Quality Check | Result |
|---|---:|
| Full-row duplicates | None identified |
| Invalid Agent References | 0 |
| Invalid non-null Vendor References | 0 |
| Policy Effective Date > Loss Date | 0 |
| Report Date < Loss Date | 0 |
| Negative Claim Amounts | 0 |
| Negative Premiums | 0 |

## Important Missing Values

| Column | Missing Records | Missing % |
|---|---:|---:|
| `ADDRESS_LINE2` | 8,505 | 85.05% |
| `VENDOR_ID` | 3,245 | 32.45% |
| `AUTHORITY_CONTACTED` | 1,945 | 19.45% |
| `CUSTOMER_EDUCATION_LEVEL` | 529 | 5.29% |
| `CITY` | 54 | 0.54% |
| `INCIDENT_CITY` | 46 | 0.46% |

Descriptive missing values were standardized where appropriate.

Missing `VENDOR_ID` values were retained when no reliable vendor information was available.

---

# Sensitive Data Handling

Sensitive fields were excluded from the analytical layer.

| Sensitive Field | Analytical Layer |
|---|---|
| SSN | Excluded |
| Account Number | Excluded |
| Routing Number | Excluded |

Credentials and secrets should never be committed to GitHub.

---

# Snowflake Platform

Snowflake is used as the centralized cloud data warehouse and SQL analytics layer.

| Component | Value |
|---|---|
| Database | `INSURANCE_CLAIMS_DB` |
| Schema | `CLAIMS` |
| Warehouse | `INSURANCE_CLAIMS_WH` |
| Main Analytical View | `CLAIMS_ANALYTICS_VW` |

## Snowflake Architecture

```text
INSURANCE_CLAIMS_DB
│
└── CLAIMS
    │
    ├── INSURANCE_DATA
    ├── EMPLOYEE_DATA
    ├── VENDOR_DATA
    │
    ├── INSURANCE_CLEANED
    ├── EMPLOYEE_CLEANED
    ├── VENDOR_CLEANED
    │
    ├── INSURANCE_ANALYTICS
    │
    └── Analytical Views
        │
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

---

# SQL Data Transformation

`CLAIMS_ANALYTICS_VW` acts as the centralized analytical layer used by Python, Power BI, and the Snowflake-connected Streamlit application.

## Derived Analytical Fields

| Derived Field | Purpose |
|---|---|
| `REPORTING_DELAY_DAYS` | Days between loss date and report date |
| `CLAIM_TO_PREMIUM_RATIO` | Claim amount relative to premium |
| `AGE_GROUP` | Customer age segmentation |
| `TENURE_GROUP` | Tenure segmentation |
| `CLAIM_AMOUNT_BUCKET` | Claim amount categorization |
| `REPORTING_CATEGORY` | Reporting delay categorization |
| `CLAIM_VALUE_CATEGORY` | Claim value categorization |
| `LOSS_YEAR` | Year from loss date |
| `LOSS_MONTH` | Month from loss date |
| `LOSS_MONTH_NAME` | Month name from loss date |

---

# Exploratory Data Analysis

The project performs descriptive and exploratory analysis across claims, customers, insurance products, risk, severity, reporting behavior, agents, and vendors.

## Analysis Areas

| Analysis Area | Variables / Metrics |
|---|---|
| Claim Amount | Minimum, maximum, mean, median, total |
| Premium | Minimum, maximum, mean, total |
| Insurance Type | Claim distribution |
| Risk | Low, Medium, High |
| Incident Severity | Minor Loss, Major Loss, Total Loss |
| Customer | Age, tenure, demographics |
| Reporting | Reporting delay, same-day reporting |
| Agent | Claim volume and exposure |
| Vendor | Claim volume and exposure |

---

# Key Descriptive Metrics

| Metric | Value |
|---|---:|
| Total Claims | 10,000 |
| Total Claim Amount | ₹165,638,300 |
| Average Claim Amount | ₹16,563.83 |
| Median Claim Amount | ₹7,000 |
| Minimum Claim Amount | ₹100 |
| Maximum Claim Amount | ₹100,000 |
| Total Premium | ₹885,085.95 |
| Average Premium | ₹88.51 |
| Minimum Premium | ₹6 |
| Maximum Premium | ₹200 |
| Average Reporting Delay | 3.21 days |
| Reporting Delay Range | 0–5 days |
| Same-Day Claims | 1,565 |
| Total Customers | 10,000 |
| Total Agents | 1,200 |
| Unique Non-null Vendors | 407 |
| Insurance Types | 6 |

---

# Insurance Type Distribution

| Insurance Type | Claims |
|---|---:|
| Property | 1,692 |
| Mobile | 1,692 |
| Health | 1,690 |
| Life | 1,682 |
| Travel | 1,670 |
| Motor | 1,574 |

---

# Risk Segmentation

| Risk Segment | Claims |
|---|---:|
| Low | 4,395 |
| Medium | 4,150 |
| High | 1,455 |
| **Total** | **10,000** |

Risk segmentation is a source-data category and is not treated as a fraud label.

---

# Incident Severity

| Incident Severity | Claims |
|---|---:|
| Total Loss | 3,390 |
| Major Loss | 3,317 |
| Minor Loss | 3,293 |
| **Total** | **10,000** |

| Attribute | Meaning |
|---|---|
| Risk Segmentation | Assigned risk category |
| Incident Severity | Level/category of loss associated with the incident |

---

# Diagnostic Analysis

Diagnostic analysis examines relationships between claim attributes to identify patterns and differences across groups.

| # | Relationship / Analysis | Method |
|---|---|---|
| 1 | Risk × Incident Severity | Cross-tabulation |
| 2 | Insurance Type × Risk | Cross-tabulation |
| 3 | Insurance Type × Severity | Cross-tabulation |
| 4 | Risk × Claim Amount | GroupBy + Aggregation |
| 5 | Severity × Claim Amount | GroupBy + Aggregation |
| 6 | Injury × Incident Severity | Cross-tabulation |
| 7 | Police Report × Severity | Cross-tabulation |
| 8 | Reporting Delay × Claim Amount | GroupBy + Aggregation |
| 9 | Agent Analysis | GroupBy + Aggregation |
| 10 | Vendor Analysis | GroupBy + Aggregation |

## Analytical Methods

| Method | Purpose |
|---|---|
| Cross-tabulation | Examine categorical relationships |
| GroupBy | Compare groups |
| Count | Measure records |
| Mean | Compare averages |
| Median | Compare central values |
| Sum | Compare financial exposure |

> Diagnostic analysis identifies relationships and patterns in claim data. It does not establish causation.

---

# Predictive Analysis

A regression-based machine-learning approach was developed to estimate claim amounts.

## Target Variable

```text
CLAIM_AMOUNT
```

The model estimates the expected claim amount based on selected customer, incident, reporting, risk, and insurance attributes.

---

# Machine Learning Features

## Numerical Features

| Feature |
|---|
| `AGE` |
| `TENURE` |
| `INCIDENT_HOUR_OF_THE_DAY` |
| `REPORTING_DELAY_DAYS` |

## Categorical Features

| Feature |
|---|
| `INSURANCE_TYPE` |
| `RISK_SEGMENTATION` |
| `INCIDENT_SEVERITY` |
| `MARITAL_STATUS` |
| `EMPLOYMENT_STATUS` |
| `HOUSE_TYPE` |
| `SOCIAL_CLASS` |
| `CUSTOMER_EDUCATION_LEVEL` |
| `ANY_INJURY` |
| `POLICE_REPORT_AVAILABLE` |

---

# Machine Learning Pipeline

| Stage | Approach |
|---|---|
| Target | `CLAIM_AMOUNT` |
| Train/Test Split | 80% / 20% |
| Random State | 42 |
| Missing Values | Simple Imputation |
| Categorical Encoding | One-Hot Encoding |
| Preprocessing | `ColumnTransformer` |
| Model 1 | Linear Regression |
| Model 2 | Random Forest Regressor |
| Evaluation | MAE, RMSE, R² |

## Pipeline

```text
Insurance Data
      ↓
Feature Selection
      ↓
Train / Test Split
      ↓
Missing Value Imputation
      ↓
Categorical Encoding
      ↓
ColumnTransformer
      ↓
Linear Regression
      +
Random Forest
      ↓
Claim Amount Prediction
      ↓
MAE / RMSE / R²
```

---

# Model Performance

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 6,935.15 | 11,976.84 | 0.7066 |
| Random Forest | 6,903.99 | 12,250.86 | 0.6930 |

## Model Comparison

| Metric | Result |
|---|---|
| Lower MAE | Random Forest |
| Lower RMSE | Linear Regression |
| Higher R² | Linear Regression |
| Selected Model | Linear Regression |

Linear Regression was selected based on the combined test-set performance across MAE, RMSE, and R².

An R² of **0.7066** means the model explains approximately **70.66% of the variation in test-set claim amounts**. It does not represent 70.66% prediction accuracy.

Predictions are estimates of claim amounts and should not be interpreted as guaranteed claim settlements.

---

# Power BI Dashboards

Three Power BI dashboards were developed for interactive insurance claims analysis.

## 01. Claims Overview

Provides a high-level view of:

- Total claims
- Total claim amount
- Average claim
- High-value claims
- Same-day claims
- Monthly claim amount trends
- Claim exposure by insurance type
- Claim volume by insurance type
- Risk filters
- Insurance type filters

The dashboard provides an overall business-level view of claim activity and financial exposure.

## 02. Risk & Severity

Analyzes:

- Claims by risk segment
- Claims by incident severity
- Claim exposure by risk
- Claims by age group
- Risk × incident severity
- Insurance type
- Risk segment
- Incident severity

Low and Medium risk segments account for most claims, while High Risk represents **14.55%** of total claims.

## 03. Claims Operations & Review

Analyzes:

- Total claims
- High-value claims
- Average reporting delay
- Same-day claims
- Same-day vs delayed reporting
- Agent claim exposure
- Risk segmentation
- Vendor claim exposure

**84.35% of claims are reported after the loss date**, with an average reporting delay of **3.21 days**.

Agent and vendor exposure reflects claim workload and financial exposure and should not be interpreted as a measure of individual performance quality.

---

# Streamlit Analytics Application

The project includes an interactive Streamlit analytics application.

### [View Live Streamlit Application](https://insurance-claims-risk-analytics.streamlit.app/)

The application provides an interactive interface for exploring insurance claims analytics and predictive modeling.

## Application Sections

| Section | Main Content |
|---|---|
| Overview | KPIs, claim summary, charts |
| Descriptive Analysis | Distribution and category analysis |
| Diagnostic Analysis | Relationships and operational analysis |
| Predictive Analysis | Claim amount prediction and model results |
| About Project | Project information and technology stack |

## Interactive Filters

| Filter |
|---|
| Insurance Type |
| Risk Segment |
| Incident Severity |

## Streamlit Architecture

The deployed standalone application uses the project dataset directly and does not require an active Snowflake session at runtime.

```text
Insurance Dataset
      ↓
Streamlit Application
      ↓
Pandas
      ├── Filters
      ├── KPIs
      ├── Charts
      └── ML Prediction
```

The repository also contains the Snowflake-connected application architecture.

```text
Snowflake
    ↓
CLAIMS_ANALYTICS_VW
    ↓
Streamlit_App
    ↓
Pandas
    ├── Filters
    ├── KPIs
    ├── Charts
    └── ML Prediction
```

---

# Technology Stack

| Technology | Category | Purpose |
|---|---|---|
| Microsoft Excel | Data Analytics | Data profiling and preparation |
| Snowflake | Cloud Data Warehouse | Data storage and SQL analytics |
| SQL | Data Analytics | Validation, cleaning, transformation and analysis |
| Python | Programming | EDA, visualization and machine learning |
| Pandas | Python Library | Data manipulation |
| NumPy | Python Library | Numerical operations |
| Matplotlib | Python Library | Visualization |
| Seaborn | Python Library | Statistical visualization |
| Scikit-learn | Machine Learning | Regression and evaluation |
| Power BI | Business Intelligence | Interactive dashboards |
| Streamlit | Application Development | Interactive analytics application |
| Git | Version Control | Source control |
| GitHub | Collaboration | Repository and documentation |

---

# Project Architecture

| Layer | Technology | Responsibility |
|---|---|---|
| Data Source | CSV | Raw insurance, employee and vendor data |
| Profiling | Excel | Data profiling and quality assessment |
| Storage | Snowflake | Centralized cloud data storage |
| Cleaning | SQL | Data cleaning and standardization |
| Transformation | SQL | Analytical fields and views |
| Analytics | Python | EDA and diagnostic analysis |
| Machine Learning | Scikit-learn | Claim amount prediction |
| BI | Power BI | Business dashboards |
| Application | Streamlit | Interactive analytics |
| Version Control | GitHub | Project management and documentation |

---

# SQL Pipeline

| File | Stage | Purpose |
|---|---|---|
| `01_Database_Setup.sql` | Database Setup | Creates database objects and environment |
| `02_Raw_Data_Validation.sql` | Raw Validation | Validates raw datasets |
| `03_Data_Cleaning.sql` | Data Cleaning | Cleans and standardizes data |
| `04_Cleaned_Data_Validation.sql` | Validation | Validates cleaned datasets |
| `05_Data_Transformation.sql` | Transformation | Creates analytical fields |
| `06_EDA_Business_Analysis.sql` | Analysis | SQL EDA and business analysis |
| `07_Final_Views.sql` | Analytical Layer | Creates reusable analytical views |

---

# Final Analytical Views

| View | Purpose |
|---|---|
| `CLAIMS_ANALYTICS_VW` | Central analytical dataset |
| `CLAIMS_SUMMARY_VW` | Overall claims summary |
| `INSURANCE_TYPE_VW` | Insurance type analysis |
| `RISK_SEGMENT_VW` | Risk segment analysis |
| `INCIDENT_SEVERITY_VW` | Severity analysis |
| `AGENT_PERFORMANCE_VW` | Agent-level claim exposure |
| `VENDOR_PERFORMANCE_VW` | Vendor-level claim exposure |
| `MONTHLY_CLAIMS_TREND_VW` | Monthly claim trend |
| `STATE_CLAIMS_VW` | State-level claim analysis |
| `CLAIM_INVESTIGATION_PRIORITY_VW` | Rule-based investigation analysis |

---

# Key Business Insights

## Financial Exposure

The project contains **10,000 claims** with total claim exposure of approximately **₹165.64M**.

The average claim is **₹16,563.83**, while the median is **₹7,000**, indicating a right-skewed claim amount distribution.

## Insurance Type

Six insurance types are represented:

```text
Property
Mobile
Health
Life
Travel
Motor
```

Claim volume is distributed relatively evenly across the six categories, while financial exposure differs across insurance types.

## Risk Distribution

```text
Low Risk      = 4,395
Medium Risk   = 4,150
High Risk     = 1,455
```

High Risk represents **14.55%** of the claims.

Risk segmentation is treated as a source-data category and not as a fraud classification.

## Incident Severity

```text
Total Loss    = 3,390
Major Loss    = 3,317
Minor Loss    = 3,293
```

The three severity categories have relatively similar claim counts.

## Reporting Behaviour

```text
Average Reporting Delay = 3.21 days
Same-Day Claims         = 1,565
Reporting Delay Range   = 0–5 days
```

Approximately **84.35% of claims are reported after the loss date**.

## Agent and Vendor Exposure

Agent and vendor analysis is used to understand:

- Claim volume
- Financial exposure
- Operational workload
- Claim distribution

Exposure metrics should be interpreted as workload and financial exposure rather than direct measures of service quality.

## Predictive Modeling

Linear Regression achieved:

```text
MAE  = ₹6,935.15
RMSE = ₹11,976.84
R²   = 0.7066
```

The model provides an analytical estimate of claim amounts and can support exposure planning and segmentation analysis.

---

# Business Recommendations

| Area | Recommendation |
|---|---|
| Claim Exposure | Monitor high-value claims and financial exposure by insurance type |
| Risk Monitoring | Combine risk segmentation with incident severity for operational review |
| Reporting | Monitor reporting delays and same-day reporting patterns |
| Agent Analysis | Monitor claim workload and financial exposure across agents |
| Vendor Analysis | Monitor claim workload and exposure across vendors |
| Predictive Analytics | Use claim amount prediction as a supporting planning and estimation tool |
| Model Improvement | Continuously validate predictions against future claim outcomes |

---

# Project Report

### [View Final Insurance Claims Analytics Report](Reports/Insurance_Claims_Analytics.pdf)

The final report documents:

- Business understanding
- Project objectives
- Data architecture
- Data quality
- Snowflake implementation
- SQL cleaning and transformation
- Exploratory analysis
- Diagnostic analysis
- Machine learning
- Power BI dashboards
- Streamlit application
- Key business insights
- Recommendations
- Project conclusion

---

# Repository Structure

```text
insurance-claims-analytics/
│
├── Dataset/
│   ├── employee_data.csv
│   ├── insurance_data.csv
│   └── vendor_data.csv
│
├── Excel/
│
├── PowerBI/
│
├── Python/
│
├── Reports/
│   └── Insurance_Claims_Analytics.pdf
│
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
│   └── app.py
│
├── Streamlit/
│   └── app.py
│
├── .gitignore
├── LICENSE
└── README.md
```

---

# How to Run

## 1. Clone Repository

```bash
git clone https://github.com/shubham-vishwakarma-analytics/insurance-claims-analytics.git

cd insurance-claims-analytics
```

## 2. Install Python Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit snowflake-connector-python
```

## 3. Configure Snowflake

For the Snowflake-connected application, configure the required credentials securely through:

```text
.streamlit/secrets.toml
```

Do not commit this file to GitHub.

## 4. Run the Snowflake-Connected Streamlit Application

```bash
streamlit run Streamlit_App/app.py
```

## 5. Run the Standalone Streamlit Application

The standalone version does not require an active Snowflake connection.

```bash
streamlit run Streamlit/app.py
```

---

# Project Deliverables

| Deliverable | Location |
|---|---|
| Excel Data Profiling | `Excel/` |
| Dataset | `Dataset/` |
| Snowflake Database Setup | Snowflake |
| SQL Data Validation | `SQL/02_Raw_Data_Validation.sql` |
| SQL Data Cleaning | `SQL/03_Data_Cleaning.sql` |
| Cleaned Data Validation | `SQL/04_Cleaned_Data_Validation.sql` |
| SQL Data Transformation | `SQL/05_Data_Transformation.sql` |
| SQL Business Analysis | `SQL/06_EDA_Business_Analysis.sql` |
| Final SQL Views | `SQL/07_Final_Views.sql` |
| Python Analysis | `Python/` |
| Machine Learning | `Python/` |
| Power BI Dashboards | `PowerBI/` |
| Streamlit Application | `Streamlit/` |
| Snowflake Streamlit Application | `Streamlit_App/` |
| Final Project Report | `Reports/Insurance_Claims_Analytics.pdf` |
| Project Documentation | `README.md` |

---

# Data Availability

The project uses three primary datasets:

```text
employee_data.csv
insurance_data.csv
vendor_data.csv
```

The main insurance dataset contains:

```text
10,000 rows
38 columns
```

Employee data contains:

```text
1,200 rows
10 columns
```

Vendor data contains:

```text
600 rows
7 columns
```

Sensitive or restricted information should not be exposed in a public repository.

---

# Security & Data Handling

Never commit:

```text
Database Passwords
API Keys
Snowflake Credentials
Connection Strings
Private Credentials
Sensitive Business Data
.streamlit/secrets.toml
```

Recommended `.gitignore` entries:

```text
.streamlit/secrets.toml
.env
*.env
__pycache__/
*.pyc
.ipynb_checkpoints/
```

Sensitive fields such as:

```text
SSN
Account Number
Routing Number
```

are excluded from the analytical outputs.

---

# Skills Demonstrated

## Excel / Data Analytics

- Data profiling
- Data quality analysis
- Missing-value analysis
- Data validation
- Data preparation
- Pivot-based analysis

## SQL / Snowflake

- SQL validation
- Data cleaning
- Data transformation
- Joins
- Aggregations
- CASE expressions
- Date functions
- Analytical views
- KPI development
- Descriptive analysis
- Diagnostic analysis
- Business analysis

## Python

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Data manipulation
- Data validation
- Exploratory data analysis
- Statistical analysis
- Visualization

## Machine Learning

- Regression
- Linear Regression
- Random Forest Regressor
- Train/test split
- Feature selection
- Missing-value imputation
- One-Hot Encoding
- ColumnTransformer
- MAE
- RMSE
- R²
- Model comparison

## Power BI

- Power Query
- Data modeling
- DAX
- KPI cards
- Interactive filters
- Time-series analysis
- Risk analysis
- Severity analysis
- Claims analysis
- Financial exposure analysis
- Business dashboards

## Streamlit

- Interactive filters
- Dynamic KPIs
- Data visualization
- Descriptive analysis
- Diagnostic analysis
- Predictive analysis
- Machine-learning integration
- Snowflake integration

## Tools

- Microsoft Excel
- Snowflake
- SQL
- Python
- Jupyter
- Power BI
- Streamlit
- Git
- GitHub

---

# Analytical Limitations

| Limitation | Explanation |
|---|---|
| No explicit fraud label | Dataset does not contain a dedicated fraud target |
| No supervised fraud model | Fraud classification was therefore not implemented |
| Diagnostic analysis | Identifies patterns but does not prove causation |
| Agent/Vendor exposure | Exposure alone does not establish service quality |
| ML predictions | Predictions are estimates, not guaranteed claim values |
| Missing Vendor IDs | Retained when reliable information was unavailable |
| Model performance | Depends on the available dataset and test split |
| Sensitive data | Sensitive fields are excluded from analytical outputs |

---

# Final Conclusion

This project demonstrates an end-to-end insurance claims analytics workflow, from raw data profiling and quality assessment through SQL-based data preparation, Python analysis, machine learning, business intelligence, and interactive application development.

The complete workflow is:

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

The project provides visibility into:

- Claim financial exposure
- Insurance type distribution
- Risk segmentation
- Incident severity
- Customer characteristics
- Reporting behavior
- Agent exposure
- Vendor exposure
- Claim amount prediction

The final solution combines:

```text
Excel
+
Snowflake
+
SQL
+
Python
+
Machine Learning
+
Power BI
+
Streamlit
+
GitHub
```

to transform raw insurance claims data into a structured analytics solution for business analysis, reporting, visualization, and predictive estimation.

---

# Author

**Shubham Vishwakarma**

**Data Analyst | SQL | Python | Power BI | Snowflake | Machine Learning**

GitHub: `shubham-vishwakarma-analytics`
