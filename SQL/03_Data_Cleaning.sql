---------------------------------------------------------------------------------------------------------------------------
-----------------------------------------SQL DATA CLEANING----------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------

USE DATABASE INSURANCE_CLAIMS_DB;
USE SCHEMA CLAIMS;
USE WAREHOUSE INSURANCE_CLAIMS_WH;

SHOW TABLES;

------------------------------------------------------------------------------------------------------------------
----------------------------------------------------Clean Employee Data-------------------------------------------
------------------------------------------------------------------------------------------------------------------

CREATE OR REPLACE TABLE EMPLOYEE_CLEANED AS
SELECT
    TRIM(AGENT_ID) AS AGENT_ID,
    TRIM(AGENT_NAME) AS AGENT_NAME,
    DATE_OF_JOINING,
    TRIM(ADDRESS_LINE1) AS ADDRESS_LINE1,
    COALESCE(NULLIF(TRIM(ADDRESS_LINE2), ''), 'Not Provided') AS ADDRESS_LINE2,
    COALESCE(NULLIF(TRIM(CITY), ''), 'Not Provided') AS CITY,
    TRIM(STATE) AS STATE,
    POSTAL_CODE,
    EMP_ROUTING_NUMBER,
    TRIM(EMP_ACCT_NUMBER) AS EMP_ACCT_NUMBER
FROM EMPLOYEE_DATA;



--------------------------------------Check that the table was created--------------------------------------------
SELECT 
    COUNT(*) AS ROW_COUNT
FROM EMPLOYEE_CLEANED;

SELECT TOP 10
    *
FROM EMPLOYEE_CLEANED;


--------------------------------Check whether missing values were cleaned--------------------------------------
SELECT 
    SUM(IFF(ADDRESS_LINE2 = 'Not Provided', 1, 0)) AS ADDRESS_LINE2_NOT_PROVIDED,
    SUM(IFF(CITY = 'Not Provided', 1, 0)) AS CITY_NOT_PROVIDED
FROM EMPLOYEE_CLEANED;



------------------------------------Compare Raw vs Clean---------------------------------------
SELECT
    (SELECT COUNT(*) FROM EMPLOYEE_DATA) AS RAW_ROWS,
    (SELECT COUNT(*) FROM EMPLOYEE_CLEANED) AS CLEANED_ROWS;



--------------------------------------------------------------------------------------------------
----------------------------------------Clean Insurance Data-------------------------------------
----------------------------------------------------------------------------------------------------

CREATE OR REPLACE TABLE INSURANCE_CLEANED AS
SELECT
    TXN_DATE_TIME,
    TRIM(TRANSACTION_ID) AS TRANSACTION_ID,
    TRIM(CUSTOMER_ID) AS CUSTOMER_ID,
    TRIM(POLICY_NUMBER) AS POLICY_NUMBER,
    POLICY_EFF_DT,
    LOSS_DT,
    REPORT_DT,
    TRIM(INSURANCE_TYPE) AS INSURANCE_TYPE,
    PREMIUM_AMOUNT,
    CLAIM_AMOUNT,
    TRIM(CUSTOMER_NAME) AS CUSTOMER_NAME,
    TRIM(ADDRESS_LINE1) AS ADDRESS_LINE1,
    COALESCE(NULLIF(TRIM(ADDRESS_LINE2), ''), 'Not Provided') AS ADDRESS_LINE2,
    COALESCE(NULLIF(TRIM(CITY), ''), 'Not Provided') AS CITY,
    TRIM(STATE) AS STATE,
    POSTAL_CODE,
    TRIM(SSN) AS SSN,
    TRIM(MARITAL_STATUS) AS MARITAL_STATUS,
    AGE,
    TENURE,
    TRIM(EMPLOYMENT_STATUS) AS EMPLOYMENT_STATUS,
    NO_OF_FAMILY_MEMBERS,
    TRIM(RISK_SEGMENTATION) AS RISK_SEGMENTATION,
    TRIM(HOUSE_TYPE) AS HOUSE_TYPE,
    TRIM(SOCIAL_CLASS) AS SOCIAL_CLASS,
    ROUTING_NUMBER,
    TRIM(ACCT_NUMBER) AS ACCT_NUMBER,
    COALESCE(NULLIF(TRIM(CUSTOMER_EDUCATION_LEVEL), ''), 'Not Provided') AS CUSTOMER_EDUCATION_LEVEL,
    TRIM(CLAIM_STATUS) AS CLAIM_STATUS,
    TRIM(INCIDENT_SEVERITY) AS INCIDENT_SEVERITY,
    COALESCE(NULLIF(TRIM(AUTHORITY_CONTACTED), ''), 'Not Provided') AS AUTHORITY_CONTACTED,
    ANY_INJURY,
    POLICE_REPORT_AVAILABLE,
    TRIM(INCIDENT_STATE) AS INCIDENT_STATE,
    COALESCE(NULLIF(TRIM(INCIDENT_CITY), ''), 'Not Provided') AS INCIDENT_CITY,
    INCIDENT_HOUR_OF_THE_DAY,
    TRIM(AGENT_ID) AS AGENT_ID,
    VENDOR_ID
FROM INSURANCE_DATA;

-------------------------------------Check row count--------------------------------------------
SELECT 
    COUNT(*) AS ROW_COUNT
FROM INSURANCE_CLEANED;


-----------------------------------Check the new table--------------------------------------------

SELECT TOP 10
    *
FROM INSURANCE_CLEANED;


----------------------------------Compare RAW vs CLEANED--------------------------------------

SELECT
    (SELECT COUNT(*) FROM INSURANCE_DATA) AS RAW_ROWS,
    (SELECT COUNT(*) FROM INSURANCE_CLEANED) AS CLEANED_ROWS;



-------------------------------------Check missing values after cleaning-------------------------------

SELECT
    SUM(IFF(ADDRESS_LINE2 = 'Not Provided', 1, 0)) AS ADDRESS_LINE2_NOT_PROVIDED,
    SUM(IFF(CITY = 'Not Provided' ,1, 0)) AS CITY_NOT_PROVIDED,
    SUM(IFF(INCIDENT_CITY = 'Not Provided', 1, 0))  AS INCIDENT_CITY_NOT_PROVIDED,
    SUM(IFF(CUSTOMER_EDUCATION_LEVEL = 'Not Provided',1, 0)) AS EDUCATION_NOT_PROVIDED,
    SUM(IFF(AUTHORITY_CONTACTED = 'Not Provided', 1, 0)) AS AUTHORITY_NOT_PROVIDED,
    SUM(IFF(VENDOR_ID IS NULL, 1, 0)) AS MISSING_VENDOR_ID
FROM INSURANCE_CLEANED;


--------------------------------Check duplicates after cleaning----------------------------------------

SELECT
    TRANSACTION_ID,
    COUNT(*) AS DUPLICATE_COUNT
FROM INSURANCE_CLEANED
GROUP BY TRANSACTION_ID
HAVING COUNT(*) > 1;



------------------------------------------Check numerical values after cleaning---------------------------------------
SELECT
    SUM(IFF(PREMIUM_AMOUNT < 0, 1, 0)) AS NEGATIVE_PREMIUM,
    SUM(IFF(CLAIM_AMOUNT < 0, 1, 0)) AS NEGATIVE_CLAIM,
    SUM(IFF(AGE <= 0, 1, 0)) AS INVALID_AGE,
    SUM(IFF(TENURE < 0, 1, 0)) AS INVALID_TENURE
FROM INSURANCE_CLEANED;


----------------------------------------------------------------------------------------------------------------------
----------------------------------------CLEAN VENDOR_CLEANED-------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------

CREATE OR REPLACE TABLE VENDOR_CLEANED AS
SELECT
    TRIM(VENDOR_ID) AS VENDOR_ID,
    TRIM(VENDOR_NAME) AS VENDOR_NAME,
    TRIM(ADDRESS_LINE1) AS ADDRESS_LINE1,
    COALESCE(NULLIF(TRIM(ADDRESS_LINE2), ''), 'Not Provided') AS ADDRESS_LINE2,
    COALESCE(NULLIF(TRIM(CITY), ''), 'Not Provided') AS CITY,
    TRIM(STATE) AS STATE,
    POSTAL_CODE
FROM VENDOR_DATA;


------------------------------------Check Row Count------------------------------------

SELECT 
    COUNT(*) AS ROW_COUNT
FROM VENDOR_CLEANED;


--------------------------------------Check the Cleaned Data-----------------------------------------

SELECT TOP 10
    *
FROM VENDOR_CLEANED;


---------------------------------------Validate Missing Values-------------------------------------------

SELECT
    SUM(IFF(ADDRESS_LINE2 = 'Not Provided', 1, 0)) AS ADDRESS_LINE2_NOT_PROVIDED,
    SUM(IFF(CITY = 'Not Provided',1 ,0)) AS CITY_NOT_PROVIDED,
    SUM(IFF(VENDOR_ID IS NULL, 1, 0)) AS MISSING_VENDOR_ID
FROM VENDOR_CLEANED;


-----------------------------------------Check Duplicate Vendor IDs--------------------

SELECT
    VENDOR_ID,
    COUNT(*) AS DUPLICATE_COUNT
FROM VENDOR_CLEANED
GROUP BY VENDOR_ID
HAVING COUNT(*) > 1;



-------------------------------------------Check Missing Vendor Names-----------------------------

SELECT
    SUM(IFF(VENDOR_NAME IS NULL OR VENDOR_NAME = '', 1, 0)) AS MISSING_VENDOR_NAME
FROM VENDOR_CLEANED;



---------------------------------------Compare Raw vs Cleaned---------------------------------------

SELECT
    (SELECT COUNT(*) FROM VENDOR_DATA) AS RAW_ROWS,
    (SELECT COUNT(*) FROM VENDOR_CLEANED) AS CLEANED_ROWS;




-----------------------------------------Final Vendor Cleaning Validation----------------------

SELECT
    COUNT(*) AS TOTAL_ROWS,
    SUM(IFF(VENDOR_ID IS NULL,1 ,0)) AS MISSING_VENDOR_ID,
    SUM(IFF(VENDOR_NAME IS NULL OR VENDOR_NAME = '',1 ,0)) AS MISSING_VENDOR_NAME,
    SUM(IFF(ADDRESS_LINE2 = 'Not Provided',1 ,0)) AS ADDRESS_LINE2_NOT_PROVIDED,
    SUM(IFF(CITY = 'Not Provided',1 ,0)) AS CITY_NOT_PROVIDED
FROM VENDOR_CLEANED;

