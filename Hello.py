import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations
def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Load Lottie animation
lottie_animation = load_lottie_url("https://assets6.lottiefiles.com/packages/lf20_jv3fpaxx.json")  # Replace with your preferred animation URL

# Page Configurations
st.set_page_config(
    page_title="Welcome to PayPal Reviews",
    page_icon="👋",
    layout="centered",
)

# Center the logo and reduce its size
image_url = "https://cdn-icons-png.flaticon.com/512/5932/5932535.png"  # Replace with your banner/logo URL
st.markdown(
    f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <img src="{image_url}" alt="PayPal Logo" style="width: 150px; height: auto;">
    </div>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Welcome to PayPal Reviews 🎉")

# Animation Section
if lottie_animation:
    st_lottie(lottie_animation, height=300, key="intro")

# Introduction Section
st.markdown(
    """
    <div style="background-color:#f4f4f9; padding: 20px; border-radius: 8px;">
    <h3 style="color:#0d6efd;">📊 Explore Our Applications</h3>
    <p style="font-size:16px;">These two applications (Transactions and Graphs) are designed to help you review PayPal-related customer transactions with ease and efficiency.</p>
    <h4 style="color:#0d6efd;">👈 Select an app from the sidebar to get started.</h4>
    </div>
    """, 
    unsafe_allow_html=True
)

# Info Message with Enhancements
st.info(
    """
    **⚠️ Notice: Application May Take a Few Moments to Load**

    Thank you for accessing this application! Please note that the server hosting this app 
    is currently in a **sleep mode** due to resource optimizations. When the app is not 
    actively used, it temporarily enters a hibernation state to conserve resources.

    As a result, the app may take **10–30 seconds** to wake up and fully load after you access it. 
    Once active, it will run smoothly without further delays.

    We appreciate your patience and understanding. If you experience any issues, 
    feel free to refresh the page or try again later.
    """
)

# Add More Engagement Options
st.markdown(
    """
    <div style="background-color:#e9ecef; padding: 20px; border-radius: 8px; margin-top: 20px;">
        <h4 style="color:#0d6efd;">Check Out</h4>
        <ul style="font-size:16px;">
            <li><a href="https://github.com/pranal02/Real-World-PayPal-Project.git" target="_blank">GitHub Link</a></li>
            <li><a href="https://drive.google.com/file/d/17Th5ZMelGhmWn-4qxie-q9gBF2ZbRPno/view?usp=sharing" target="_blank">Download this Dataset to get an overview about the application [Dataset in CSV Format]</a></li>
        </ul>
    </div>
    """, 
    unsafe_allow_html=True
)


st.markdown("""
# Welcome to the Transaction Breakdown Application! 🛒

This application is designed to help you analyze transactional data efficiently and effectively. Whether you are looking to uncover patterns, flag specific transactions, or generate detailed Excel reports, this tool has you covered.

---

## What Does This Application Do?

### **Data Cleaning and Analysis**
- Cleans and filters your transaction data for meaningful insights.
- Focuses on successful transactions by excluding incomplete ones.
- Removes unnecessary columns and organizes data for better clarity.

### **Key Metrics Calculation**
- Provides detailed summaries like total, mean, and maximum transaction values.
- Calculates transaction counts and unique customer statistics.
- Breaks down refunds, chargebacks, and charges over 90 and 180 days.

### **Customer Insights**
- Identifies high-value transactions and customers.
- Highlights duplicate transactions on the same day by the same customer.
- Allows you to search for transactions linked to a specific customer name.

### **Flagged Transactions**
- Detects transactions with specific flagged keywords (e.g., "raffle," "lottery").
- Helps monitor compliance and detect anomalies.

### **Excel Report Generation**
- Automatically generates a multi-sheet Excel workbook.
- Includes clean data, key calculations, pivot tables, high-value transactions, and more.

---

## How to Use the Application

### **Enter Required Information**
- **Filename**: Enter the desired name for the output Excel file.
- **Name Search**: Input a customer's name to find related transactions.
- **High Ticket Value**: Specify a value (integer only) to identify high-value transactions.

### **Upload Your Data**
- Click on the **"Upload CSV File"** button and upload your dataset. The file must be in CSV format.

### **Wait for Processing**
- Once the file is uploaded, the application cleans and processes the data automatically.
- You will see a summary of key metrics and analyses.

### **Download Your Report**
- Click the **Download Excel Worksheets** button to get a detailed Excel report.

---

## What You Need to Provide
- **CSV File**: A dataset with transaction details, including columns like `Total`, `Transaction_Type`, `Customer_Name`, and `Day`.
- **High Ticket Value**: An integer threshold for identifying large transactions.
- **Customer Name**: (Optional) A specific name to search within the dataset.

---

## Key Outputs

- **Cleaned Data**: A tidy dataset ready for further analysis.
- **Summary Metrics**: Total transactions, refunds, chargebacks, and more.
- **High-Value Transactions**: Identifies transactions that exceed your specified threshold.
- **Pivot Tables**: Transaction breakdowns by customer, type, and country.
- **Flagged Notes**: Highlights transactions with flagged keywords.
- **Duplicate Transactions**: Identifies possible duplicate transactions.

---

## Tips for First-Time Users
- Ensure your CSV file includes all necessary columns (e.g., `Total`, `Day`, `Customer_Name`, etc.).
- Use meaningful filenames for easier organization of downloaded reports.
- Adjust the high-ticket value based on the scale of your transactions (e.g., $500 for small businesses, $10,000 for large enterprises).
- Explore all generated Excel sheets for deeper insights.

---

This application streamlines transaction analysis, making it ideal for auditors, business analysts, and financial professionals. **Enjoy exploring your data!** 😊
""")





st.markdown("""
# Chart Maker Application 📈

Welcome to the **Chart Maker Application**! This tool allows you to explore and visualize your transaction data with ease. You can filter data by various criteria, generate insightful charts, and analyze transaction patterns over time.

---

## Features
- **Interactive Filters**: Filter data by payment status, method, application, and country.
- **Dynamic Date Selection**: Choose start and end dates for analysis.
- **Upload Your CSV File**: Analyze local transaction data in a structured way.
- **Visualize Insights**: Generate:
  - **Histogram of Transactions**
  - **Box and Whisker Plots**
  - **Sum and Count Plots by Month**

---

## How to Use
1. **Choose Filters**:
    - **Payment Status**: Select from `All`, `Charge`, `Refund`, or `Chargeback`.
    - **Payment Method**: Filter by `Goods and Services` or `Friends & Family`.
    - **Payment Application**: View data from `Desktop`, `Tablet`, or `Phone`.
    - **Payment Country**: Choose between `All`, `US`, `UK`, or `AU`.

2. **Select Date Range**:
    - Start Date defaults to 180 days prior.
    - Adjust as needed using the date pickers.

3. **Upload CSV File**:
    - Click the **Upload CSV File** button and provide a dataset. The file must include:
        - `Total`, `Transaction_Type`, `Type`, `Country`, `Source`, `Day`, `Customer_Name`, and `Transaction_Notes`.

4. **Explore Charts**:
    - Analyze transaction distributions with a histogram.
    - Examine variations with box and whisker plots.
    - Explore monthly transaction sums and counts.

---

## Charts Available
### 1. Histogram: Count of Transactions
- **X-Axis**: Total transaction value (binned).
- **Y-Axis**: Count of transactions.

### 2. Box and Whisker Plot: Transaction Distribution by Month
- **X-Axis**: Month (YYYYMM format).
- **Y-Axis**: Transaction Total.

### 3. Sum of Transactions by Month
- **X-Axis**: Month (YYYYMM format).
- **Y-Axis**: Sum of Transaction Totals.
- **Color**: Payment Type.

### 4. Count of Transactions by Month
- **X-Axis**: Month (YYYYMM format).
- **Y-Axis**: Count of Transactions.
- **Color**: Payment Type.

---

## Tabs
Explore different visualizations using the tabs:
1. **Histogram**: View transaction count distribution.
2. **Box and Whiskers**: Analyze monthly transaction variations.
3. **Box Plot Sum**: Visualize monthly transaction sums.
4. **Box Plot Count**: Examine transaction counts per month.

---

### Start exploring your transaction data and uncover valuable insights!
""")


