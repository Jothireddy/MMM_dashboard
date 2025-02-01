# Market Mix Modeling (MMM) for TV Manufacturing & Supplier Unit

This project aims to analyze the effectiveness of different marketing channels (SMS, Newspaper, Radio, TV, and Internet) and external economic factors on sales performance. The goal is to build a Market Mix Model (MMM) using Ridge Regression to identify key drivers of sales and optimize marketing spend based on ROI.

## Project Overview

### Dataset:
The dataset contains daily data for a TV Manufacturing & Supplier Unit, including:
- **Sales & Demand:** DEMAND, SALES ($), Unit Price ($), POS/ Supply Data
- **Economic Indicators:** Consumer Price Index (CPI), Consumer Confidence Index (CCI), Producer Price Index (PPI)
- **Advertising Expenses:** SMS, Newspaper, Radio, TV, Internet
- **GRP (Gross Rating Points):** For Newspaper, SMS, Radio, Internet, and TV

### Objectives:
1. Preprocess the data.
2. Perform exploratory data analysis (EDA).
3. Build a Market Mix Model to estimate the impact of different marketing channels on sales.
4. Optimize ROI based on the model's insights.
5. Deploy an interactive dashboard using Streamlit to visualize trends and optimization recommendations.

## Steps:

### 1. Install & Import Libraries
Install necessary libraries for data analysis, modeling, and visualization.

```bash
pip install pandas numpy matplotlib seaborn statsmodels sklearn streamlit


2. Load & Preprocess Data
The dataset is loaded and cleaned:

The DATE column is converted to datetime format.
Missing values are handled by filling them with the mean of respective columns.
The TV Manufacturing Brand column is dropped as it's not relevant.
3. Exploratory Data Analysis (EDA)
Sales trends over time are visualized.
A correlation matrix is generated to understand relationships between features.
4. Build Market Mix Model
A Ridge Regression model is trained to estimate the impact of marketing channels and economic factors on sales:

Features: Advertising Expenses (SMS, Newspaper, Radio, TV, Internet), CPI, CCI, PPI.
The model is evaluated using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
Feature importance is visualized to identify the most impactful marketing channels.
5. ROI Optimization Recommendations
The Return on Investment (ROI) is calculated for each marketing channel, and recommendations for optimizing marketing spend are provided.

6. Build Dashboard
An interactive dashboard is created using Streamlit to visualize:

Sales trends over time.
Feature importance in driving sales.
ROI optimization recommendations.
How to Run:
Download the dataset (MMM_data.xlsx) and place it in the appropriate directory.
Run the preprocessing and modeling code in Google Colab to generate results.
Deploy the Streamlit app

```bash
streamlit run mmm_dashboard.py

Files:
MMM_data.xlsx: The dataset containing daily sales and marketing data.
market_mix_model.py: The Python script for data preprocessing, model building, and ROI optimization.
app.py: The Streamlit app to visualize the results.
Conclusion:
This project helps in understanding the impact of different marketing channels on sales and provides actionable insights for optimizing marketing spend.

