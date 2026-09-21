# Insurance Claims Analytics

An end-to-end Insurance Claims Analytics project focused on analyzing claim patterns, risk segmentation, financial exposure, operational behavior, and claim amount prediction.

## Project Overview

This project analyzes insurance claims data using Excel, Snowflake SQL, Python, Databricks, PySpark, Power BI, and Streamlit.

The project follows an end-to-end analytics workflow:

Raw Data → Excel Profiling → Snowflake → SQL Cleaning → SQL Transformation → Python/Databricks → EDA → Diagnostic Analysis → Machine Learning → Power BI → Streamlit

## Business Objectives

- Analyze overall insurance claim activity.
- Understand claim distribution across insurance types.
- Analyze risk segmentation and incident severity.
- Analyze claim amount and premium exposure.
- Examine reporting delays and reporting behavior.
- Analyze claim exposure across agents and vendors.
- Identify relationships and patterns between claim attributes.
- Estimate claim amounts using machine learning.
- Build interactive Power BI dashboards.
- Develop an interactive Streamlit analytics application.

## Dataset

The project contains three datasets:

| Dataset | Rows | Columns |
|---|---:|---:|
| Insurance | 10,000 | 38 |
| Employee | 1,200 | 10 |
| Vendor | 600 | 7 |

Total records: **11,800**

### Main Relationships

```text
EMPLOYEE_DATA.AGENT_ID
        ↓
INSURANCE_DATA.AGENT_ID

VENDOR_DATA.VENDOR_ID
        ↓
INSURANCE_DATA.VENDOR_ID
