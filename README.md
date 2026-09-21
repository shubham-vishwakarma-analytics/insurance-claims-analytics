# 🛡️ Insurance Claims Analytics

> **End-to-End Insurance Claims Analytics Project | Data Cleaning • SQL • EDA • Diagnostic Analysis • Machine Learning • Power BI • Streamlit**

An end-to-end **Insurance Claims Analytics** project that transforms raw insurance claim data into structured business insights using **Excel, Snowflake SQL, Python, Databricks, PySpark, Machine Learning, Power BI, and Streamlit**.

The project covers the complete analytics lifecycle — from **data profiling and SQL-based cleaning** to **exploratory analysis, diagnostic analysis, predictive modeling, interactive dashboards, and a Streamlit application**.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Business Objectives](#-business-objectives)
- [Project Workflow](#-project-workflow)
- [Dataset](#-dataset)
- [Dataset Relationships](#-dataset-relationships)
- [Data Quality & Cleaning](#-data-quality--cleaning)
- [SQL Data Transformation](#-sql-data-transformation)
- [Exploratory Data Analysis](#-exploratory-data-analysis)
- [Diagnostic Analysis](#-diagnostic-analysis)
- [Predictive Analysis](#-predictive-analysis)
- [Model Performance](#-model-performance)
- [Power BI Dashboards](#-power-bi-dashboards)
- [Streamlit Application](#-streamlit-application)
- [Technology Stack](#-technology-stack)
- [Project Architecture](#-project-architecture)
- [Snowflake Architecture](#-snowflake-architecture)
- [Repository Structure](#-repository-structure)
- [SQL Pipeline](#-sql-pipeline)
- [Key Business Metrics](#-key-business-metrics)
- [Key Analytical Insights](#-key-analytical-insights)
- [Data Privacy](#-data-privacy)
- [Limitations](#-limitations)
- [Project Deliverables](#-project-deliverables)
- [How to Use](#-how-to-use)
- [Skills Demonstrated](#-skills-demonstrated)
- [Author](#-author)

---

# 📊 Project Overview

Insurance claims data contains information about customers, policies, incidents, claim amounts, premiums, risk categories, incident severity, reporting behavior, agents, and vendors.

The objective of this project is to convert raw claims data into a structured analytical solution that can help understand:

- Claim volume and financial exposure
- Insurance product distribution
- Risk segmentation
- Incident severity
- Claim amount behavior
- Reporting delays
- Agent and vendor exposure
- Relationships between claim attributes
- Claim amount prediction

The project combines **data analytics, business intelligence, and machine learning** into a single end-to-end workflow.

---

# 💼 Business Problem

Insurance organizations need to understand claim behavior and financial exposure across different insurance products, risk categories, incidents, customers, agents, and vendors.

Raw claims data alone does not provide an immediate understanding of these patterns.

This project addresses the problem by:

1. Profiling and validating the raw datasets.
2. Cleaning and transforming data using SQL.
3. Creating a centralized analytical dataset.
4. Performing descriptive and diagnostic analysis.
5. Estimating claim amounts using machine learning.
6. Creating Power BI dashboards for business reporting.
7. Building a Streamlit application for interactive analytics.

---

# 🎯 Business Objectives

The main objectives of the project are:

- Analyze overall insurance claim activity.
- Understand claim distribution across insurance types.
- Analyze risk segmentation.
- Analyze incident severity.
- Understand claim amount and premium exposure.
- Examine reporting delays.
- Analyze claim exposure across agents.
- Analyze claim exposure across vendors.
- Identify relationships and patterns between claim attributes.
- Estimate claim amounts using machine learning.
- Create interactive Power BI dashboards.
- Build an interactive Streamlit analytics application.
- Provide data-driven insights for claims operations and monitoring.

---

# 🔄 Project Workflow

```text
Raw CSV Files
      │
      ▼
Excel Data Profiling
      │
      ▼
Snowflake Data Storage
      │
      ▼
SQL Data Validation
      │
      ▼
SQL Data Cleaning
      │
      ▼
SQL Data Transformation
      │
      ▼
CLAIMS_ANALYTICS_VW
      │
      ├──────────────► Python / Databricks
      │                     │
      │                     ├── EDA
      │                     ├── Diagnostic Analysis
      │                     └── Machine Learning
      │
      ├──────────────► Power BI
      │                     └── Interactive Dashboards
      │
      └──────────────► Streamlit
                            └── Interactive Analytics App
