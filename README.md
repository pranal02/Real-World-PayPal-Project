# Transaction Breakdown Application 🛒

[**Access the deployed application here**](https://real-world-paypal-project-gel8tyrsw3i6i4w6hcvmhu.streamlit.app/) *(Replace `#` with your Streamlit deployment URL)*

---

## Overview
This application is designed to help you analyze transactional data efficiently and effectively. From uncovering patterns to generating detailed Excel reports, this tool streamlines transaction analysis for auditors, business analysts, and financial professionals.

---

## Features

### Data Cleaning and Analysis
- Cleans and filters transactional data for meaningful insights.
- Focuses on successful transactions by excluding incomplete ones.
- Removes unnecessary columns for better clarity.

### Key Metrics Calculation
- Provides detailed summaries:
  - Total, mean, and maximum transaction values.
  - Transaction counts and unique customer statistics.
- Breaks down refunds, chargebacks, and charges over 90 and 180 days.

### Customer Insights
- Identifies high-value transactions and customers.
- Highlights duplicate transactions on the same day by the same customer.
- Enables searching for transactions linked to a specific customer name.

### Flagged Transactions
- Detects transactions with flagged keywords (e.g., "raffle," "lottery").
- Monitors compliance and detects anomalies.

### Excel Report Generation
- Generates multi-sheet Excel workbooks:
  - Cleaned data
  - Key calculations
  - Pivot tables
  - High-value transactions and more

---

## How to Use the Application

### Input Requirements
1. **Filename**: Enter the desired name for the output Excel file.
2. **Name Search**: Input a customer's name to find related transactions.
3. **High Ticket Value**: Specify an integer threshold to identify high-value transactions.
4. **CSV File**: Upload a dataset with columns such as `Total`, `Transaction_Type`, `Customer_Name`, and `Day`.

### Steps to Use
1. **Enter Required Information**:
   - Filename
   - Customer name (optional)
   - High-value transaction threshold
2. **Upload Your Data**:
   - Click the "Upload CSV File" button.
   - Ensure the file is in CSV format.
3. **Wait for Processing**:
   - Data is cleaned and processed automatically.
   - Key metrics and analyses are displayed.
4. **Download Your Report**:
   - Click the "Download Excel Worksheets" button to access the detailed Excel report.

---

## Key Outputs
- **Cleaned Data**: Tidy dataset ready for further analysis.
- **Summary Metrics**: Total transactions, refunds, chargebacks, and more.
- **High-Value Transactions**: Transactions exceeding the specified threshold.
- **Pivot Tables**: Transaction breakdowns by customer, type, and country.
- **Flagged Notes**: Highlights transactions with flagged keywords.
- **Duplicate Transactions**: Identifies possible duplicate transactions.

---

## Chart Maker Application 📈

### Features
1. **Interactive Filters**:
   - Payment Status: All, Charge, Refund, Chargeback
   - Payment Method: Goods and Services, Friends & Family
   - Payment Application: Desktop, Tablet, Phone
   - Payment Country: All, US, UK, AU
2. **Dynamic Date Selection**:
   - Default start date: 180 days prior
   - Adjustable using date pickers
3. **Upload CSV File**:
   - Required columns: `Total`, `Transaction_Type`, `Type`, `Country`, `Source`, `Day`, `Customer_Name`, `Transaction_Notes`

### Visualizations
1. **Histogram**: Count of transactions by value.
2. **Box and Whisker Plot**: Monthly transaction distribution.
3. **Sum of Transactions by Month**:
   - X-Axis: Month (YYYYMM format)
   - Y-Axis: Sum of transaction totals
   - Color: Payment Type
4. **Count of Transactions by Month**:
   - X-Axis: Month (YYYYMM format)
   - Y-Axis: Count of transactions
   - Color: Payment Type

### Tabs
- **Histogram**: Transaction count distribution
- **Box and Whiskers**: Monthly transaction variations
- **Box Plot Sum**: Monthly transaction sums
- **Box Plot Count**: Monthly transaction counts

---

## Tips for First-Time Users
- Ensure your CSV file includes necessary columns (e.g., `Total`, `Day`, `Customer_Name`).
- Use meaningful filenames for easier report organization.
- Adjust high-ticket value thresholds based on transaction scale (e.g., `500` for small businesses, `10,000` for large enterprises).
- Explore all Excel sheets for deeper insights.

---

## Technology Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Deployment**: Streamlit Cloud

---


