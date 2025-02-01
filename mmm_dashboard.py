import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "MMM_data.xlsx"  # Make sure this file is in the same directory as the script
df = pd.read_excel(file_path)

# Convert DATE to datetime format
df["DATE"] = pd.to_datetime(df["DATE"])

# Title of the app
st.title("📊 Market Mix Modeling Dashboard")

# Sidebar
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Start Date", df["DATE"].min())
end_date = st.sidebar.date_input("End Date", df["DATE"].max())

# Filter dataset based on date range
filtered_df = df[(df["DATE"] >= pd.to_datetime(start_date)) & (df["DATE"] <= pd.to_datetime(end_date))]

# Sales Trend
st.subheader("📈 Sales Trend Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=filtered_df, x="DATE", y="SALES ($)", ax=ax)
st.pyplot(fig)

# Feature Importance
st.subheader("🎯 Advertising Impact on Sales")
X = df[
    [
        "Advertising Expenses (SMS)",
        "Advertising Expenses(Newspaper ads)",
        "Advertising Expenses(Radio)",
        "Advertising Expenses(TV)",
        "Advertising Expenses(Internet)",
        "Consumer Price Index (CPI)",
        "Consumer Confidence Index(CCI)",
        "Producer Price Index (PPI)",
    ]
]
y = df["SALES ($)"]

from sklearn.linear_model import Ridge
model = Ridge(alpha=1.0)
model.fit(X, y)

feature_importance = pd.DataFrame({"Feature": X.columns, "Coefficient": model.coef_})
feature_importance.sort_values(by="Coefficient", ascending=False, inplace=True)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=feature_importance, x="Coefficient", y="Feature", palette="viridis", ax=ax)
st.pyplot(fig)

# ROI Insights
st.subheader("💡 ROI Optimization Recommendations")
total_ad_spend = df[
    [
        "Advertising Expenses (SMS)",
        "Advertising Expenses(Newspaper ads)",
        "Advertising Expenses(Radio)",
        "Advertising Expenses(TV)",
        "Advertising Expenses(Internet)",
    ]
].sum()

roi = (feature_importance.set_index("Feature")["Coefficient"] / total_ad_spend) * 100
st.write(roi.sort_values(ascending=False))
