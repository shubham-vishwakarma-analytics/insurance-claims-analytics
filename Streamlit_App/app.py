# ============================================================
# INSURANCE CLAIMS ANALYTICS
# STREAMLIT APPLICATION
# ============================================================


# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import streamlit as st
import snowflake.connector
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ============================================================
# 2. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Insurance Claims Analytics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# 3. CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    h1 {
        font-weight: 700;
    }

    h2 {
        font-weight: 600;
    }

    h3 {
        font-weight: 600;
    }

    [data-testid="stMetric"] {
        padding: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 4. LOAD DATA FROM SNOWFLAKE
# ============================================================

@st.cache_data
def load_data():

    connection = None

    try:

        connection = snowflake.connector.connect(

            account=st.secrets["snowflake"]["account"],

            user=st.secrets["snowflake"]["user"],

            password=st.secrets["snowflake"]["password"],

            warehouse=st.secrets["snowflake"]["warehouse"],

            database=st.secrets["snowflake"]["database"],

            schema=st.secrets["snowflake"]["schema"]

        )

        query = """
        SELECT *
        FROM INSURANCE_CLAIMS_DB.CLAIMS.CLAIMS_ANALYTICS_VW
        """

        insurance_df = pd.read_sql(
            query,
            connection
        )

        return insurance_df

    except Exception as e:

        st.error(
            "Unable to load insurance claims data from Snowflake."
        )

        st.error(
            f"Error details: {e}"
        )

        st.stop()

    finally:

        if connection is not None:

            connection.close()


# ============================================================
# 5. LOAD DATA
# ============================================================

with st.spinner(
    "Loading insurance claims data..."
):

    insurance_df = load_data()


# ============================================================
# 6. PREPARE DATA TYPES
# ============================================================

numeric_columns = [

    "CLAIM_AMOUNT",

    "PREMIUM",

    "AGE",

    "TENURE",

    "REPORTING_DELAY_DAYS",

    "INCIDENT_HOUR_OF_THE_DAY"

]

for column in numeric_columns:

    if column in insurance_df.columns:

        insurance_df[column] = pd.to_numeric(
            insurance_df[column],
            errors="coerce"
        )


# ============================================================
# 7. REQUIRED COLUMN VALIDATION
# ============================================================

required_columns = [

    "CLAIM_AMOUNT",

    "INSURANCE_TYPE",

    "RISK_SEGMENTATION",

    "INCIDENT_SEVERITY",

    "REPORTING_DELAY_DAYS",

    "CUSTOMER_ID"

]

missing_columns = [

    column

    for column in required_columns

    if column not in insurance_df.columns

]


if missing_columns:

    st.error(
        "Required columns are missing from "
        "CLAIMS_ANALYTICS_VW."
    )

    st.write(
        missing_columns
    )

    st.stop()


# ============================================================
# 8. OPTIONAL PREMIUM COLUMN CHECK
# ============================================================

has_premium = (
    "PREMIUM"
    in insurance_df.columns
)


# ============================================================
# 9. SIDEBAR BRANDING
# ============================================================

st.sidebar.markdown(
    "### Insurance Claims Analytics"
)

st.sidebar.caption(
    "Claims Operations Dashboard"
)

st.sidebar.divider()


# ============================================================
# 10. NAVIGATION
# ============================================================

st.sidebar.subheader(
    "Navigation"
)

page = st.sidebar.radio(

    "Select Analysis",

    [
        "Overview",
        "Descriptive Analysis",
        "Diagnostic Analysis",
        "Predictive Analysis",
        "About Project"
    ]

)


# ============================================================
# 11. SIDEBAR FILTERS
# ============================================================

st.sidebar.divider()

st.sidebar.subheader(
    "Filters"
)


insurance_types = sorted(

    insurance_df[
        "INSURANCE_TYPE"
    ]
    .dropna()
    .unique()
    .tolist()

)


risk_segments = sorted(

    insurance_df[
        "RISK_SEGMENTATION"
    ]
    .dropna()
    .unique()
    .tolist()

)


severities = sorted(

    insurance_df[
        "INCIDENT_SEVERITY"
    ]
    .dropna()
    .unique()
    .tolist()

)


selected_insurance_type = st.sidebar.selectbox(

    "Insurance Type",

    ["All"] + insurance_types

)


selected_risk_segment = st.sidebar.selectbox(

    "Risk Segment",

    ["All"] + risk_segments

)


selected_severity = st.sidebar.selectbox(

    "Incident Severity",

    ["All"] + severities

)


# ============================================================
# 12. FILTER DATA
# ============================================================

filtered_df = insurance_df.copy()


if selected_insurance_type != "All":

    filtered_df = filtered_df[
        filtered_df["INSURANCE_TYPE"]
        == selected_insurance_type
    ]


if selected_risk_segment != "All":

    filtered_df = filtered_df[
        filtered_df["RISK_SEGMENTATION"]
        == selected_risk_segment
    ]


if selected_severity != "All":

    filtered_df = filtered_df[
        filtered_df["INCIDENT_SEVERITY"]
        == selected_severity
    ]


# ============================================================
# 13. SIDEBAR FILTER SUMMARY
# ============================================================

st.sidebar.divider()

st.sidebar.write(
    f"Showing **{len(filtered_df):,}** claims"
)


# ============================================================
# 14. OVERVIEW PAGE
# ============================================================

if page == "Overview":

    st.title(
        "Insurance Claims Analytics"
    )

    st.caption(
        "Claims Operations | Interactive Data Analytics Dashboard"
    )


    # --------------------------------------------------------
    # EMPTY DATA CHECK
    # --------------------------------------------------------

    if len(filtered_df) == 0:

        st.warning(
            "No claims match the selected filters."
        )

        st.stop()


    st.info(
        f"Currently analyzing {len(filtered_df):,} claims "
        "based on the selected filters."
    )


    # --------------------------------------------------------
    # KPI CALCULATIONS
    # --------------------------------------------------------

    total_claims = len(
        filtered_df
    )


    total_claim_amount = (
        filtered_df[
            "CLAIM_AMOUNT"
        ].sum()
    )


    average_claim_amount = (
        filtered_df[
            "CLAIM_AMOUNT"
        ].mean()
    )


    high_risk_claims = (

        filtered_df[
            "RISK_SEGMENTATION"
        ]
        .eq("High")
        .sum()

    )


    high_value_claims = (

        filtered_df[
            "CLAIM_AMOUNT"
        ]
        .ge(50000)
        .sum()

    )


    same_day_claims = (

        filtered_df[
            "REPORTING_DELAY_DAYS"
        ]
        .eq(0)
        .sum()

    )


    total_customers = (

        filtered_df[
            "CUSTOMER_ID"
        ]
        .nunique()

    )


    # --------------------------------------------------------
    # KPI ROW 1
    # --------------------------------------------------------

    st.subheader(
        "Claims Overview"
    )


    if has_premium:

        average_premium = (

            filtered_df[
                "PREMIUM"
            ].mean()

        )


        col1, col2, col3, col4 = st.columns(4)


        with col1:

            st.metric(
                "Total Claims",
                f"{total_claims:,}"
            )


        with col2:

            st.metric(
                "Total Claim Amount",
                f"₹{total_claim_amount:,.0f}"
            )


        with col3:

            st.metric(
                "Average Claim",
                f"₹{average_claim_amount:,.2f}"
            )


        with col4:

            st.metric(
                "Average Premium",
                f"₹{average_premium:,.2f}"
            )

    else:

        col1, col2, col3, col4 = st.columns(4)


        with col1:

            st.metric(
                "Total Claims",
                f"{total_claims:,}"
            )


        with col2:

            st.metric(
                "Total Claim Amount",
                f"₹{total_claim_amount:,.0f}"
            )


        with col3:

            st.metric(
                "Average Claim",
                f"₹{average_claim_amount:,.2f}"
            )


        with col4:

            st.metric(
                "Customers",
                f"{total_customers:,}"
            )


    # --------------------------------------------------------
    # KPI ROW 2
    # --------------------------------------------------------

    st.divider()


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "High-Risk Claims",
            f"{high_risk_claims:,}"
        )


    with col2:

        st.metric(
            "High-Value Claims",
            f"{high_value_claims:,}"
        )


    with col3:

        st.metric(
            "Same-Day Claims",
            f"{same_day_claims:,}"
        )


    with col4:

        st.metric(
            "Customers",
            f"{total_customers:,}"
        )


    # --------------------------------------------------------
    # CLAIM AMOUNT SUMMARY
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Claim Amount Summary"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Minimum Claim",
            f"₹{filtered_df['CLAIM_AMOUNT'].min():,.2f}"
        )


    with col2:

        st.metric(
            "Median Claim",
            f"₹{filtered_df['CLAIM_AMOUNT'].median():,.2f}"
        )


    with col3:

        st.metric(
            "Maximum Claim",
            f"₹{filtered_df['CLAIM_AMOUNT'].max():,.2f}"
        )


    # --------------------------------------------------------
    # INSURANCE TYPE
    # --------------------------------------------------------

    insurance_type_counts = (

        filtered_df[
            "INSURANCE_TYPE"
        ]
        .value_counts()
        .sort_values(
            ascending=False
        )

    )


    # --------------------------------------------------------
    # RISK
    # --------------------------------------------------------

    risk_counts = (

        filtered_df[
            "RISK_SEGMENTATION"
        ]
        .value_counts()

    )


    col1, col2 = st.columns(2)


    with col1:

        st.subheader(
            "Claims by Insurance Type"
        )

        st.bar_chart(
            insurance_type_counts
        )


    with col2:

        st.subheader(
            "Claims by Risk Segment"
        )

        st.bar_chart(
            risk_counts
        )


    # --------------------------------------------------------
    # SEVERITY
    # --------------------------------------------------------

    st.subheader(
        "Claims by Incident Severity"
    )


    severity_counts = (

        filtered_df[
            "INCIDENT_SEVERITY"
        ]
        .value_counts()

    )


    st.bar_chart(
        severity_counts
    )


    # --------------------------------------------------------
    # OBSERVATIONS
    # --------------------------------------------------------

    st.subheader(
        "Key Observations"
    )


    top_insurance_type = (

        filtered_df[
            "INSURANCE_TYPE"
        ]
        .value_counts()
        .idxmax()

    )


    top_risk_segment = (

        filtered_df[
            "RISK_SEGMENTATION"
        ]
        .value_counts()
        .idxmax()

    )


    top_severity = (

        filtered_df[
            "INCIDENT_SEVERITY"
        ]
        .value_counts()
        .idxmax()

    )


    st.info(

        f"""
        - Most frequent insurance type: **{top_insurance_type}**
        - Most frequent risk segment: **{top_risk_segment}**
        - Most frequent incident severity: **{top_severity}**
        """

    )


    # --------------------------------------------------------
    # DATA PREVIEW
    # --------------------------------------------------------

    st.subheader(
        "Filtered Claims Data"
    )


    st.dataframe(

        filtered_df.head(20),

        use_container_width=True,

        hide_index=True

    )


# ============================================================
# 15. DESCRIPTIVE ANALYSIS
# ============================================================

elif page == "Descriptive Analysis":

    st.title(
        "Descriptive Analysis"
    )

    st.caption(
        "Summary statistics and distributions of insurance claims."
    )


    if len(filtered_df) == 0:

        st.warning(
            "No claims match the selected filters."
        )

        st.stop()


    # --------------------------------------------------------
    # OVERALL SUMMARY
    # --------------------------------------------------------

    st.subheader(
        "Overall Summary"
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Claims",
            f"{len(filtered_df):,}"
        )


    with col2:

        st.metric(
            "Total Claim Amount",
            f"₹{filtered_df['CLAIM_AMOUNT'].sum():,.0f}"
        )


    with col3:

        st.metric(
            "Average Claim",
            f"₹{filtered_df['CLAIM_AMOUNT'].mean():,.2f}"
        )


    with col4:

        st.metric(
            "Median Claim",
            f"₹{filtered_df['CLAIM_AMOUNT'].median():,.2f}"
        )


    # --------------------------------------------------------
    # INSURANCE TYPE ANALYSIS
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Insurance Type Analysis"
    )


    insurance_summary = (

        filtered_df
        .groupby(
            "INSURANCE_TYPE"
        )
        .agg(

            Claims=(
                "CLAIM_AMOUNT",
                "count"
            ),

            Total_Claim_Amount=(
                "CLAIM_AMOUNT",
                "sum"
            ),

            Average_Claim_Amount=(
                "CLAIM_AMOUNT",
                "mean"
            )

        )
        .sort_values(
            "Claims",
            ascending=False
        )

    )


    # --------------------------------------------------------
    # ADD PREMIUM ONLY IF AVAILABLE
    # --------------------------------------------------------

    if has_premium:

        premium_summary = (

            filtered_df
            .groupby(
                "INSURANCE_TYPE"
            )["PREMIUM"]
            .mean()
            .rename(
                "Average_Premium"
            )

        )


        insurance_summary = (

            insurance_summary
            .join(
                premium_summary
            )

        )


    st.dataframe(

        insurance_summary.style.format(

            {
                "Total_Claim_Amount":
                    "₹{:,.2f}",

                "Average_Claim_Amount":
                    "₹{:,.2f}",

                "Average_Premium":
                    "₹{:,.2f}"

            }

        ),

        use_container_width=True

    )


    st.bar_chart(
        insurance_summary[
            "Claims"
        ]
    )


    # --------------------------------------------------------
    # RISK ANALYSIS
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Risk Segment Analysis"
    )


    risk_summary = (

        filtered_df
        .groupby(
            "RISK_SEGMENTATION"
        )
        .agg(

            Claims=(
                "CLAIM_AMOUNT",
                "count"
            ),

            Total_Claim_Amount=(
                "CLAIM_AMOUNT",
                "sum"
            ),

            Average_Claim_Amount=(
                "CLAIM_AMOUNT",
                "mean"
            )

        )
        .sort_values(
            "Claims",
            ascending=False
        )

    )


    st.dataframe(

        risk_summary.style.format(

            {

                "Total_Claim_Amount":
                    "₹{:,.2f}",

                "Average_Claim_Amount":
                    "₹{:,.2f}"

            }

        ),

        use_container_width=True

    )


    st.bar_chart(
        risk_summary[
            "Claims"
        ]
    )


    # --------------------------------------------------------
    # INCIDENT SEVERITY
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Incident Severity Analysis"
    )


    severity_summary = (

        filtered_df
        .groupby(
            "INCIDENT_SEVERITY"
        )
        .agg(

            Claims=(
                "CLAIM_AMOUNT",
                "count"
            ),

            Total_Claim_Amount=(
                "CLAIM_AMOUNT",
                "sum"
            ),

            Average_Claim_Amount=(
                "CLAIM_AMOUNT",
                "mean"
            )

        )
        .sort_values(
            "Claims",
            ascending=False
        )

    )


    st.dataframe(

        severity_summary.style.format(

            {

                "Total_Claim_Amount":
                    "₹{:,.2f}",

                "Average_Claim_Amount":
                    "₹{:,.2f}"

            }

        ),

        use_container_width=True

    )


    st.bar_chart(
        severity_summary[
            "Claims"
        ]
    )


    # --------------------------------------------------------
    # CLAIM AMOUNT ANALYSIS
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Claim Amount Analysis"
    )


    claim_statistics = pd.DataFrame(

        {

            "Statistic": [

                "Minimum",

                "25th Percentile",

                "Median",

                "Mean",

                "75th Percentile",

                "Maximum"

            ],

            "Claim Amount": [

                filtered_df[
                    "CLAIM_AMOUNT"
                ].min(),

                filtered_df[
                    "CLAIM_AMOUNT"
                ].quantile(0.25),

                filtered_df[
                    "CLAIM_AMOUNT"
                ].median(),

                filtered_df[
                    "CLAIM_AMOUNT"
                ].mean(),

                filtered_df[
                    "CLAIM_AMOUNT"
                ].quantile(0.75),

                filtered_df[
                    "CLAIM_AMOUNT"
                ].max()

            ]

        }

    )


    st.dataframe(

        claim_statistics.style.format(

            {
                "Claim Amount":
                    "₹{:,.2f}"
            }

        ),

        use_container_width=True,

        hide_index=True

    )


    st.write(
        "Claim Amount Distribution"
    )


    st.bar_chart(

        filtered_df[
            "CLAIM_AMOUNT"
        ]
        .value_counts()
        .sort_index()
        .head(50)

    )


    # --------------------------------------------------------
    # DEMOGRAPHIC ANALYSIS
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Demographic Analysis"
    )


    col1, col2 = st.columns(2)


    with col1:

        if "AGE" in filtered_df.columns:

            st.write(
                "Age Distribution"
            )

            st.bar_chart(

                filtered_df[
                    "AGE"
                ]
                .value_counts()
                .sort_index()

            )


    with col2:

        if "SOCIAL_CLASS" in filtered_df.columns:

            st.write(
                "Social Class Distribution"
            )

            st.bar_chart(

                filtered_df[
                    "SOCIAL_CLASS"
                ]
                .value_counts()

            )


    col1, col2 = st.columns(2)


    with col1:

        if "EMPLOYMENT_STATUS" in filtered_df.columns:

            st.write(
                "Employment Status"
            )

            st.bar_chart(

                filtered_df[
                    "EMPLOYMENT_STATUS"
                ]
                .value_counts()

            )


    with col2:

        if "MARITAL_STATUS" in filtered_df.columns:

            st.write(
                "Marital Status"
            )

            st.bar_chart(

                filtered_df[
                    "MARITAL_STATUS"
                ]
                .value_counts()

            )


    # --------------------------------------------------------
    # REPORTING ANALYSIS
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Reporting Analysis"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(

            "Average Reporting Delay",

            f"{filtered_df['REPORTING_DELAY_DAYS'].mean():.2f} days"

        )


    with col2:

        same_day_percentage = (

            filtered_df[
                "REPORTING_DELAY_DAYS"
            ]
            .eq(0)
            .mean()
            * 100

        )


        st.metric(

            "Same-Day Reporting",

            f"{same_day_percentage:.2f}%"

        )


    st.write(
        "Reporting Delay Distribution"
    )


    st.bar_chart(

        filtered_df[
            "REPORTING_DELAY_DAYS"
        ]
        .value_counts()
        .sort_index()

    )


# ============================================================
# 16. DIAGNOSTIC ANALYSIS
# ============================================================

elif page == "Diagnostic Analysis":

    st.title(
        "Diagnostic Analysis"
    )

    st.caption(
        "Relationships and patterns across claim characteristics."
    )


    if len(filtered_df) == 0:

        st.warning(
            "No claims match the selected filters."
        )

        st.stop()


    # --------------------------------------------------------
    # RISK × SEVERITY
    # --------------------------------------------------------

    st.subheader(
        "Risk Segment × Incident Severity"
    )


    risk_severity = pd.crosstab(

        filtered_df[
            "RISK_SEGMENTATION"
        ],

        filtered_df[
            "INCIDENT_SEVERITY"
        ]

    )


    st.dataframe(

        risk_severity,

        use_container_width=True

    )


    st.bar_chart(
        risk_severity
    )


    # --------------------------------------------------------
    # INSURANCE TYPE × RISK
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Insurance Type × Risk Segment"
    )


    insurance_risk = pd.crosstab(

        filtered_df[
            "INSURANCE_TYPE"
        ],

        filtered_df[
            "RISK_SEGMENTATION"
        ]

    )


    st.dataframe(

        insurance_risk,

        use_container_width=True

    )


    st.bar_chart(
        insurance_risk
    )


    # --------------------------------------------------------
    # INSURANCE TYPE × SEVERITY
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Insurance Type × Incident Severity"
    )


    insurance_severity = pd.crosstab(

        filtered_df[
            "INSURANCE_TYPE"
        ],

        filtered_df[
            "INCIDENT_SEVERITY"
        ]

    )


    st.dataframe(

        insurance_severity,

        use_container_width=True

    )


    st.bar_chart(
        insurance_severity
    )


    # --------------------------------------------------------
    # RISK × CLAIM AMOUNT
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Average Claim Amount by Risk Segment"
    )


    risk_claim_amount = (

        filtered_df
        .groupby(
            "RISK_SEGMENTATION"
        )[
            "CLAIM_AMOUNT"
        ]
        .mean()
        .sort_values(
            ascending=False
        )

    )


    st.bar_chart(
        risk_claim_amount
    )


    # --------------------------------------------------------
    # SEVERITY × CLAIM AMOUNT
    # --------------------------------------------------------

    st.subheader(
        "Average Claim Amount by Incident Severity"
    )


    severity_claim_amount = (

        filtered_df
        .groupby(
            "INCIDENT_SEVERITY"
        )[
            "CLAIM_AMOUNT"
        ]
        .mean()
        .sort_values(
            ascending=False
        )

    )


    st.bar_chart(
        severity_claim_amount
    )


    # --------------------------------------------------------
    # INJURY × SEVERITY
    # --------------------------------------------------------

    if "ANY_INJURY" in filtered_df.columns:

        st.divider()

        st.subheader(
            "Injury × Incident Severity"
        )


        injury_severity = pd.crosstab(

            filtered_df[
                "ANY_INJURY"
            ],

            filtered_df[
                "INCIDENT_SEVERITY"
            ]

        )


        st.dataframe(

            injury_severity,

            use_container_width=True

        )


        st.bar_chart(
            injury_severity
        )


    # --------------------------------------------------------
    # POLICE REPORT × SEVERITY
    # --------------------------------------------------------

    if "POLICE_REPORT_AVAILABLE" in filtered_df.columns:

        st.divider()

        st.subheader(
            "Police Report × Incident Severity"
        )


        police_severity = pd.crosstab(

            filtered_df[
                "POLICE_REPORT_AVAILABLE"
            ],

            filtered_df[
                "INCIDENT_SEVERITY"
            ]

        )


        st.dataframe(

            police_severity,

            use_container_width=True

        )


        st.bar_chart(
            police_severity
        )


    # --------------------------------------------------------
    # REPORTING DELAY × CLAIM AMOUNT
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Reporting Delay × Average Claim Amount"
    )


    delay_claim = (

        filtered_df
        .groupby(
            "REPORTING_DELAY_DAYS"
        )[
            "CLAIM_AMOUNT"
        ]
        .mean()
        .sort_index()

    )


    st.bar_chart(
        delay_claim
    )


    # --------------------------------------------------------
    # AGENT ANALYSIS
    # --------------------------------------------------------

    if "AGENT_ID" in filtered_df.columns:

        st.divider()

        st.subheader(
            "Agent Analysis"
        )


        agent_summary = (

            filtered_df
            .groupby(
                "AGENT_ID"
            )
            .agg(

                Claims=(
                    "CLAIM_AMOUNT",
                    "count"
                ),

                Total_Claim_Amount=(
                    "CLAIM_AMOUNT",
                    "sum"
                ),

                Average_Claim_Amount=(
                    "CLAIM_AMOUNT",
                    "mean"
                )

            )
            .sort_values(
                "Claims",
                ascending=False
            )
            .head(20)

        )


        st.dataframe(

            agent_summary.style.format(

                {

                    "Total_Claim_Amount":
                        "₹{:,.2f}",

                    "Average_Claim_Amount":
                        "₹{:,.2f}"

                }

            ),

            use_container_width=True

        )


    # --------------------------------------------------------
    # VENDOR ANALYSIS
    # --------------------------------------------------------

    if "VENDOR_ID" in filtered_df.columns:

        st.divider()

        st.subheader(
            "Vendor Analysis"
        )


        vendor_data = filtered_df[
            filtered_df[
                "VENDOR_ID"
            ].notna()
        ]


        if len(vendor_data) > 0:

            vendor_summary = (

                vendor_data
                .groupby(
                    "VENDOR_ID"
                )
                .agg(

                    Claims=(
                        "CLAIM_AMOUNT",
                        "count"
                    ),

                    Total_Claim_Amount=(
                        "CLAIM_AMOUNT",
                        "sum"
                    ),

                    Average_Claim_Amount=(
                        "CLAIM_AMOUNT",
                        "mean"
                    )

                )
                .sort_values(
                    "Claims",
                    ascending=False
                )
                .head(20)

            )


            st.dataframe(

                vendor_summary.style.format(

                    {

                        "Total_Claim_Amount":
                            "₹{:,.2f}",

                        "Average_Claim_Amount":
                            "₹{:,.2f}"

                    }

                ),

                use_container_width=True

            )

        else:

            st.info(
                "No non-null vendor records are available "
                "for the selected filters."
            )


# ============================================================
# 17. PREDICTIVE ANALYSIS
# ============================================================

elif page == "Predictive Analysis":

    st.title(
        "Predictive Analysis"
    )

    st.caption(
        "Machine learning models for insurance claim amount prediction."
    )


    st.subheader(
        "Prediction Problem"
    )


    st.write(
        "The objective is to predict CLAIM_AMOUNT using "
        "selected customer, policy, risk, incident, and "
        "reporting characteristics."
    )


    st.info(
        "This is a supervised regression problem because "
        "CLAIM_AMOUNT is a continuous numerical target."
    )


    # --------------------------------------------------------
    # MODEL FEATURES
    # --------------------------------------------------------

    model_columns = [

        "INSURANCE_TYPE",

        "AGE",

        "TENURE",

        "RISK_SEGMENTATION",

        "INCIDENT_SEVERITY",

        "MARITAL_STATUS",

        "EMPLOYMENT_STATUS",

        "HOUSE_TYPE",

        "SOCIAL_CLASS",

        "CUSTOMER_EDUCATION_LEVEL",

        "ANY_INJURY",

        "POLICE_REPORT_AVAILABLE",

        "INCIDENT_HOUR_OF_THE_DAY",

        "REPORTING_DELAY_DAYS"

    ]


    categorical_columns = [

        "INSURANCE_TYPE",

        "RISK_SEGMENTATION",

        "INCIDENT_SEVERITY",

        "MARITAL_STATUS",

        "EMPLOYMENT_STATUS",

        "HOUSE_TYPE",

        "SOCIAL_CLASS",

        "CUSTOMER_EDUCATION_LEVEL",

        "ANY_INJURY",

        "POLICE_REPORT_AVAILABLE"

    ]


    numerical_columns = [

        "AGE",

        "TENURE",

        "INCIDENT_HOUR_OF_THE_DAY",

        "REPORTING_DELAY_DAYS"

    ]


    # --------------------------------------------------------
    # CHECK MODEL COLUMNS
    # --------------------------------------------------------

    missing_model_columns = [

        column

        for column in model_columns

        if column not in insurance_df.columns

    ]


    if missing_model_columns:

        st.error(
            "The following ML columns are missing "
            "from CLAIMS_ANALYTICS_VW:"
        )

        st.write(
            missing_model_columns
        )

        st.stop()


    # --------------------------------------------------------
    # TRAINING FUNCTION
    # --------------------------------------------------------

    @st.cache_resource
    def train_models(data):

        X = data[
            model_columns
        ].copy()


        y = data[
            "CLAIM_AMOUNT"
        ].copy()


        X_train, X_test, y_train, y_test = (

            train_test_split(

                X,

                y,

                test_size=0.20,

                random_state=42

            )

        )


        # ----------------------------------------------------
        # NUMERICAL PIPELINE
        # ----------------------------------------------------

        numeric_transformer = Pipeline(

            steps=[

                (
                    "imputer",

                    SimpleImputer(
                        strategy="median"
                    )

                )

            ]

        )


        # ----------------------------------------------------
        # CATEGORICAL PIPELINE
        # ----------------------------------------------------

        categorical_transformer = Pipeline(

            steps=[

                (
                    "imputer",

                    SimpleImputer(
                        strategy="most_frequent"
                    )

                ),

                (
                    "encoder",

                    OneHotEncoder(
                        handle_unknown="ignore"
                    )

                )

            ]

        )


        # ----------------------------------------------------
        # PREPROCESSOR
        # ----------------------------------------------------

        preprocessor = ColumnTransformer(

            transformers=[

                (
                    "num",

                    numeric_transformer,

                    numerical_columns

                ),

                (
                    "cat",

                    categorical_transformer,

                    categorical_columns

                )

            ]

        )


        # ----------------------------------------------------
        # LINEAR REGRESSION
        # ----------------------------------------------------

        linear_model = Pipeline(

            steps=[

                (
                    "preprocessor",

                    preprocessor

                ),

                (
                    "model",

                    LinearRegression()

                )

            ]

        )


        # ----------------------------------------------------
        # RANDOM FOREST
        # ----------------------------------------------------

        random_forest_model = Pipeline(

            steps=[

                (
                    "preprocessor",

                    preprocessor

                ),

                (
                    "model",

                    RandomForestRegressor(

                        n_estimators=200,

                        random_state=42,

                        n_jobs=-1

                    )

                )

            ]

        )


        # ----------------------------------------------------
        # TRAIN
        # ----------------------------------------------------

        linear_model.fit(
            X_train,
            y_train
        )


        random_forest_model.fit(
            X_train,
            y_train
        )


        # ----------------------------------------------------
        # PREDICTIONS
        # ----------------------------------------------------

        linear_predictions = (

            linear_model.predict(
                X_test
            )

        )


        random_forest_predictions = (

            random_forest_model.predict(
                X_test
            )

        )


        # ----------------------------------------------------
        # LINEAR REGRESSION METRICS
        # ----------------------------------------------------

        linear_mae = (

            mean_absolute_error(

                y_test,

                linear_predictions

            )

        )


        linear_rmse = np.sqrt(

            mean_squared_error(

                y_test,

                linear_predictions

            )

        )


        linear_r2 = (

            r2_score(

                y_test,

                linear_predictions

            )

        )


        # ----------------------------------------------------
        # RANDOM FOREST METRICS
        # ----------------------------------------------------

        rf_mae = (

            mean_absolute_error(

                y_test,

                random_forest_predictions

            )

        )


        rf_rmse = np.sqrt(

            mean_squared_error(

                y_test,

                random_forest_predictions

            )

        )


        rf_r2 = (

            r2_score(

                y_test,

                random_forest_predictions

            )

        )


        # ----------------------------------------------------
        # RESULTS
        # ----------------------------------------------------

        results = pd.DataFrame(

            {

                "Model": [

                    "Linear Regression",

                    "Random Forest"

                ],

                "MAE": [

                    linear_mae,

                    rf_mae

                ],

                "RMSE": [

                    linear_rmse,

                    rf_rmse

                ],

                "R2": [

                    linear_r2,

                    rf_r2

                ]

            }

        )


        return (

            linear_model,

            random_forest_model,

            results,

            X_test,

            y_test,

            linear_predictions,

            random_forest_predictions

        )


    # --------------------------------------------------------
    # TRAINING
    # --------------------------------------------------------

    with st.spinner(
        "Training prediction models..."
    ):

        (

            linear_model,

            random_forest_model,

            model_results,

            X_test,

            y_test,

            linear_predictions,

            random_forest_predictions

        ) = train_models(
            insurance_df
        )


    # --------------------------------------------------------
    # MODEL COMPARISON
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Model Performance Comparison"
    )


    display_results = (
        model_results.copy()
    )


    display_results["MAE"] = (

        display_results[
            "MAE"
        ]
        .round(2)

    )


    display_results["RMSE"] = (

        display_results[
            "RMSE"
        ]
        .round(2)

    )


    display_results["R2"] = (

        display_results[
            "R2"
        ]
        .round(4)

    )


    st.dataframe(

        display_results,

        use_container_width=True,

        hide_index=True

    )


    # --------------------------------------------------------
    # MODEL METRICS
    # --------------------------------------------------------

    linear_row = (

        model_results[
            model_results["Model"]
            == "Linear Regression"
        ]
        .iloc[0]

    )


    rf_row = (

        model_results[
            model_results["Model"]
            == "Random Forest"
        ]
        .iloc[0]

    )


    col1, col2 = st.columns(2)


    with col1:

        st.markdown(
            "### Linear Regression"
        )


        st.metric(
            "MAE",
            f"₹{linear_row['MAE']:,.2f}"
        )


        st.metric(
            "RMSE",
            f"₹{linear_row['RMSE']:,.2f}"
        )


        st.metric(
            "R²",
            f"{linear_row['R2']:.4f}"
        )


    with col2:

        st.markdown(
            "### Random Forest"
        )


        st.metric(
            "MAE",
            f"₹{rf_row['MAE']:,.2f}"
        )


        st.metric(
            "RMSE",
            f"₹{rf_row['RMSE']:,.2f}"
        )


        st.metric(
            "R²",
            f"{rf_row['R2']:.4f}"
        )


    # --------------------------------------------------------
    # MODEL SELECTION
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Model Selection"
    )


    st.write(
        "Linear Regression is used as the final prediction "
        "model because it achieved lower RMSE and higher "
        "R² on the test data."
    )


    st.info(
        "Random Forest achieved a slightly lower MAE, "
        "while Linear Regression achieved lower RMSE "
        "and higher R²."
    )


    # --------------------------------------------------------
    # ACTUAL VS PREDICTED
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Actual vs Predicted Claim Amount"
    )


    prediction_comparison = pd.DataFrame(

        {

            "Actual Claim Amount":
                y_test.values,

            "Linear Regression":
                linear_predictions,

            "Random Forest":
                random_forest_predictions

        }

    )


    st.dataframe(

        prediction_comparison.head(20),

        use_container_width=True,

        hide_index=True

    )


    st.line_chart(

        prediction_comparison.head(50)

    )


    # --------------------------------------------------------
    # FEATURE IMPORTANCE
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "Random Forest Feature Importance"
    )


    feature_names = (

        random_forest_model
        .named_steps[
            "preprocessor"
        ]
        .get_feature_names_out()

    )


    feature_importances = (

        random_forest_model
        .named_steps[
            "model"
        ]
        .feature_importances_

    )


    feature_importance_df = pd.DataFrame(

        {

            "Feature":
                feature_names,

            "Importance":
                feature_importances

        }

    ).sort_values(

        "Importance",

        ascending=False

    )


    st.dataframe(

        feature_importance_df.head(15),

        use_container_width=True,

        hide_index=True

    )


    st.bar_chart(

        feature_importance_df
        .head(15)
        .set_index(
            "Feature"
        )

    )


    st.caption(
        "Feature importance indicates model contribution "
        "to prediction and does not establish causation."
    )


    # ========================================================
    # INTERACTIVE PREDICTION
    # ========================================================

    st.divider()

    st.subheader(
        "Interactive Claim Amount Prediction"
    )


    st.write(
        "Enter claim characteristics to estimate "
        "the claim amount."
    )


    # --------------------------------------------------------
    # INPUTS
    # --------------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        prediction_insurance_type = st.selectbox(

            "Insurance Type",

            sorted(

                insurance_df[
                    "INSURANCE_TYPE"
                ]
                .dropna()
                .unique()

            ),

            key="prediction_insurance"

        )


    with col2:

        prediction_risk = st.selectbox(

            "Risk Segment",

            sorted(

                insurance_df[
                    "RISK_SEGMENTATION"
                ]
                .dropna()
                .unique()

            ),

            key="prediction_risk"

        )


    with col1:

        prediction_severity = st.selectbox(

            "Incident Severity",

            sorted(

                insurance_df[
                    "INCIDENT_SEVERITY"
                ]
                .dropna()
                .unique()

            ),

            key="prediction_severity"

        )


    with col2:

        prediction_age = st.number_input(

            "Age",

            min_value=25,

            max_value=64,

            value=40,

            key="prediction_age"

        )


    with col1:

        prediction_tenure = st.number_input(

            "Tenure",

            min_value=6,

            max_value=119,

            value=60,

            key="prediction_tenure"

        )


    with col2:

        prediction_marital = st.selectbox(

            "Marital Status",

            sorted(

                insurance_df[
                    "MARITAL_STATUS"
                ]
                .dropna()
                .unique()

            ),

            key="prediction_marital"

        )


    with col1:

        prediction_employment = st.selectbox(

            "Employment Status",

            sorted(

                insurance_df[
                    "EMPLOYMENT_STATUS"
                ]
                .dropna()
                .unique()

            ),

            key="prediction_employment"

        )


    with col2:

        prediction_house = st.selectbox(

            "House Type",

            sorted(

                insurance_df[
                    "HOUSE_TYPE"
                ]
                .dropna()
                .unique()

            ),

            key="prediction_house"

        )


    with col1:

        prediction_social = st.selectbox(

            "Social Class",

            sorted(

                insurance_df[
                    "SOCIAL_CLASS"
                ]
                .dropna()
                .unique()

            ),

            key="prediction_social"

        )


    with col2:

        prediction_education = st.selectbox(

            "Customer Education Level",

            sorted(

                insurance_df[
                    "CUSTOMER_EDUCATION_LEVEL"
                ]
                .dropna()
                .unique()

            ),

            key="prediction_education"

        )


    with col1:

        prediction_injury = st.selectbox(

            "Any Injury",

            sorted(

                insurance_df[
                    "ANY_INJURY"
                ]
                .dropna()
                .unique()

            ),

            key="prediction_injury"

        )


    with col2:

        prediction_police = st.selectbox(

            "Police Report Available",

            sorted(

                insurance_df[
                    "POLICE_REPORT_AVAILABLE"
                ]
                .dropna()
                .unique()

            ),

            key="prediction_police"

        )


    with col1:

        prediction_hour = st.number_input(

            "Incident Hour",

            min_value=0,

            max_value=23,

            value=12,

            key="prediction_hour"

        )


    with col2:

        prediction_delay = st.number_input(

            "Reporting Delay (Days)",

            min_value=0,

            max_value=5,

            value=2,

            key="prediction_delay"

        )


    # --------------------------------------------------------
    # PREDICTION INPUT DATAFRAME
    # --------------------------------------------------------

    prediction_input = pd.DataFrame(

        {

            "INSURANCE_TYPE": [
                prediction_insurance_type
            ],

            "AGE": [
                prediction_age
            ],

            "TENURE": [
                prediction_tenure
            ],

            "RISK_SEGMENTATION": [
                prediction_risk
            ],

            "INCIDENT_SEVERITY": [
                prediction_severity
            ],

            "MARITAL_STATUS": [
                prediction_marital
            ],

            "EMPLOYMENT_STATUS": [
                prediction_employment
            ],

            "HOUSE_TYPE": [
                prediction_house
            ],

            "SOCIAL_CLASS": [
                prediction_social
            ],

            "CUSTOMER_EDUCATION_LEVEL": [
                prediction_education
            ],

            "ANY_INJURY": [
                prediction_injury
            ],

            "POLICE_REPORT_AVAILABLE": [
                prediction_police
            ],

            "INCIDENT_HOUR_OF_THE_DAY": [
                prediction_hour
            ],

            "REPORTING_DELAY_DAYS": [
                prediction_delay
            ]

        }

    )


    # --------------------------------------------------------
    # PREDICT BUTTON
    # --------------------------------------------------------

    if st.button(

        "Predict Claim Amount",

        type="primary"

    ):

        predicted_amount = (

            linear_model.predict(

                prediction_input

            )[0]

        )


        st.success(

            f"Estimated Claim Amount: "
            f"₹{predicted_amount:,.2f}"

        )


        st.caption(

            "This is a model-generated estimate based on "
            "the selected input characteristics and should "
            "not be treated as an actual claim settlement value."

        )


# ============================================================
# 18. ABOUT PROJECT
# ============================================================

elif page == "About Project":

    st.title(
        "About the Project"
    )


    st.caption(
        "Insurance Claims Analytics | Claims Operations"
    )


    # --------------------------------------------------------
    # PROJECT OVERVIEW
    # --------------------------------------------------------

    st.subheader(
        "Project Overview"
    )


    st.write(

        "This project analyzes insurance claims data to "
        "understand claim patterns, financial exposure, "
        "risk segments, incident severity, customer "
        "characteristics, and operational reporting patterns."

    )


    # --------------------------------------------------------
    # BUSINESS OBJECTIVES
    # --------------------------------------------------------

    st.subheader(
        "Business Objectives"
    )


    st.markdown(

        """
        - Analyze insurance claim volumes and financial exposure.
        - Understand risk and incident severity patterns.
        - Examine relationships between claim characteristics.
        - Analyze customer and operational attributes.
        - Predict insurance claim amounts using machine learning.
        """

    )


    # --------------------------------------------------------
    # PROJECT WORKFLOW
    # --------------------------------------------------------

    st.subheader(
        "Project Workflow"
    )


    st.code(

        """
Raw Insurance Data
        ↓
Excel Data Profiling
        ↓
Snowflake
        ↓
SQL Cleaning & Transformation
        ↓
CLAIMS_ANALYTICS_VW
        ↓
Python / Databricks
        ↓
EDA + Diagnostic Analysis + ML
        ↓
Power BI
        ↓
Streamlit
        ↓
Interactive Analytics Application
        """

    )


    # --------------------------------------------------------
    # TECHNOLOGY STACK
    # --------------------------------------------------------

    st.subheader(
        "Technology Stack"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.markdown(

            """
            **Data & Database**

            - Excel
            - Snowflake
            - SQL

            **Data Analysis**

            - Python
            - Pandas
            - NumPy
            - Matplotlib
            - Seaborn
            """

        )


    with col2:

        st.markdown(

            """
            **Business Intelligence**

            - Power BI

            **Machine Learning**

            - Scikit-learn
            - Linear Regression
            - Random Forest

            **Application**

            - Streamlit
            """

        )


    # --------------------------------------------------------
    # DATASET INFORMATION
    # --------------------------------------------------------

    st.subheader(
        "Dataset Information"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(

            "Insurance Records",

            f"{len(insurance_df):,}"

        )


    with col2:

        st.metric(

            "Analytical Columns",

            f"{insurance_df.shape[1]:,}"

        )


    with col3:

        st.metric(

            "Insurance Types",

            f"{insurance_df['INSURANCE_TYPE'].nunique():,}"

        )


    # --------------------------------------------------------
    # ANALYTICAL COMPONENTS
    # --------------------------------------------------------

    st.subheader(
        "Analytical Components"
    )


    st.markdown(

        """
        **Descriptive Analysis**

        Understand claim volumes, financial values,
        insurance types, risk segments, severity,
        demographics, and reporting patterns.


        **Diagnostic Analysis**

        Explore relationships between risk, severity,
        insurance type, injury, police reports,
        reporting delay, agents, and vendors.


        **Predictive Analysis**

        Predict claim amounts using Linear Regression
        and Random Forest Regression.
        """

    )


# ============================================================
# 19. FOOTER
# ============================================================

st.divider()

st.caption(

    "Insurance Claims Analytics | Claims Operations Data Analytics Project"

)