import streamlit as st
import joblib
import pandas as pd

# Load trained salary prediction model
model = joblib.load("salary_prediction_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Glassdoor Salary Prediction",
    page_icon="💼",
    layout="centered"
)

# App title
st.title("💼 Glassdoor Job Salary Prediction")
st.write("Enter the job details below to predict the average salary.")

# Job details
st.subheader("Enter Job Details")

job_title = st.text_input("Job Title", "Data Scientist")
rating = st.number_input("Company Rating", 0.0, 5.0, 3.5, 0.1)
location = st.text_input("Location", "New York, NY")
headquarters = st.text_input("Headquarters", "New York, NY")

size = st.selectbox(
    "Company Size",
    ["-1", "1 to 50", "51 to 200", "201 to 500", "501 to 1000",
     "1001 to 5000", "5001 to 10000", "10000+"]
)

founded = st.number_input(
    "Year Founded",
    min_value=0,
    max_value=2026,
    value=2000
)

ownership = st.text_input(
    "Type of Ownership",
    "Company - Private"
)

industry = st.text_input(
    "Industry",
    "IT Services"
)

sector = st.text_input(
    "Sector",
    "Information Technology"
)

revenue = st.text_input(
    "Revenue",
    "Unknown / Non-Applicable"
)

competitors = st.text_input(
    "Competitors",
    "-1"
)

# Create input data for prediction
input_data = {
    "Job Title": job_title,
    "Rating": rating,
    "Location": location,
    "Headquarters": headquarters,
    "Size": size,
    "Founded": founded,
    "Type of ownership": ownership,
    "Industry": industry,
    "Sector": sector,
    "Revenue": revenue,
    "Competitors": competitors
}
#convert dictionary to a 2d data frame
input_df = pd.DataFrame([input_data])
# Predict salary
if st.button("💰 Predict Salary"):

    prediction = model.predict(input_df)

    st.success(
        f"Predicted Average Salary: ${prediction[0]:,.2f}"
    )