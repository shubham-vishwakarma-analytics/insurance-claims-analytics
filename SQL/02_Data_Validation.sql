---------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------Data Validation-----------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------
USE DATABASE INSURANCE_CLAIMS_DB;
USE SCHEMA CLAIMS;
USE WAREHOUSE INSURANCE_CLAIMS_WH;


-- Check tables
SHOW TABLES;


------------------------------------------------Check the Structure of tables-----------------------------------------------

DESC TABLE INSURANCE_DATA;

DESC TABLE EMPLOYEE_DATA;

DESC TABLE VENDOR_DATA;


------------------------------------------------Data row-count validation----------------------------------------------------------

SELECT 
    'Insurance_Data' AS Table_Name,
    COUNT(*)  Total_Rows
FROM  INSURANCE_DATA
UNION ALL
SELECT 
    'Employee_Data' AS Table_Name,
    COUNT(*)  Total_Rows
FROM  EMPLOYEE_DATA
UNION ALL
SELECT 
    'Vendor_Data' AS Table_Name,
    COUNT(*)  Total_Rows
FROM  VENDOR_DATA;




------------------------------------- Duplicates Checking--------------------------------------------------------------------


-- Check duplicate transactions
SELECT
    TRANSACTION_ID,
    COUNT(*) Duplicate_Count
FROM INSURANCE_DATA
GROUP BY TRANSACTION_ID
HAVING COUNT(*) > 1;


-- Check duplicate Customers
SELECT
    CUSTOMER_ID,
    COUNT(*) Duplicate_Count
FROM INSURANCE_DATA
GROUP BY CUSTOMER_ID
HAVING COUNT(*) > 1;


-- Check duplicate Policies
SELECT
    POLICY_NUMBER,
    COUNT(*) Duplicate_Count
FROM INSURANCE_DATA
GROUP BY POLICY_NUMBER
HAVING COUNT(*) > 1;


-- Check duplicate Vendors
SELECT
    VENDOR_ID,
    COUNT(*) AS DUPLICATE_COUNT
FROM VENDOR_DATA
GROUP BY VENDOR_ID
HAVING COUNT(*) > 1;


----------------------------------------------------Check Missing values---------------------------------------------------------------

SELECT
    COUNT(*) AS TOTAL_ROWS,
    SUM(IFF(CUSTOMER_ID IS NULL, 1, 0)) AS MISSING_CUSTOMER_ID,
    SUM(IFF(POLICY_NUMBER IS NULL, 1, 0)) AS MISSING_POLICY_NUMBER,
    SUM(IFF(INSURANCE_TYPE IS NULL, 1, 0)) AS MISSING_INSURANCE_TYPE,
    SUM(IFF(PREMIUM_AMOUNT IS NULL, 1, 0)) AS MISSING_PREMIUM,
    SUM(IFF(CLAIM_AMOUNT IS NULL, 1, 0)) AS MISSING_CLAIM_AMOUNT,
    SUM(IFF(AGENT_ID IS NULL, 1, 0)) AS MISSING_AGENT_ID,
    SUM(IFF(VENDOR_ID IS NULL, 1, 0)) AS MISSING_VENDOR_ID
FROM INSURANCE_DATA;



---------------------------------------Check important numeric ranges------------------------------------------------------------


SELECT
    MIN(AGE) AS MIN_AGE,
    MAX(AGE) AS MAX_AGE,
    MIN(TENURE) AS MIN_TENURE,
    MAX(TENURE) AS MAX_TENURE,
    MIN(PREMIUM_AMOUNT) AS MIN_PREMIUM,
    MAX(PREMIUM_AMOUNT) AS MAX_PREMIUM,
    MIN(CLAIM_AMOUNT) AS MIN_CLAIM,
    MAX(CLAIM_AMOUNT) AS MAX_CLAIM
FROM INSURANCE_DATA;





-------------------------------------------------Negative values Checking-----------------------------------------

SELECT 
    SUM(IFF(PREMIUM_AMOUNT < 0, 1, 0)) AS NEGATIVE_PREMIUM, 
    SUM(IFF(CLAIM_AMOUNT < 0, 1, 0)) AS NEGATIVE_CLAIM, 
    SUM(IFF(AGE <= 0, 1, 0)) AS INVALID_AGE, 
    SUM(IFF(TENURE < 0, 1, 0)) AS INVALID_TENURE 
FROM INSURANCE_DATA;


-----------------------------Check Invalid Date-------------------------------------------------------------

SELECT
    COUNT(*) AS Total_Count,
    SUM(IFF(REPORT_DT < LOSS_DT, 1, 0)) AS Invalid_Report_Date,
    SUM(IFF(POLICY_EFF_DT > LOSS_DT, 1, 0)) AS Invalid_Policy_Eff_Date
FROM INSURANCE_DATA;



-------------------------------------------------Validate Agent relationship--------------------------------------------

SELECT 
    COUNT(*) AS Invalid_Agent_References
FROM INSURANCE_DATA i 
LEFT JOIN EMPLOYEE_DATA e
         ON i.agent_id = e.agent_id
WHERE i.agent_id IS NOT NULL AND e.agent_id IS NULL;


---------------------------------------------------Validate Vendor relationship---------------------------------------------
SELECT
    COUNT(*) AS Invalid_Vendor_References
FROM INSURANCE_DATA i
LEFT JOIN VENDOR_DATA v 
         ON i.vendor_id = v.vendor_id
WHERE i.vendor_id IS NOT NULL AND v.vendor_id
IS NULL;