# Glassdoor Jobs Salary Prediction

## 📌 Project Overview

This project analyzes Glassdoor job postings to understand salary trends in the data science and technology job market and builds a machine learning model to predict the average salary for a job posting.

The project covers:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Statistical Analysis
* Feature Engineering
* Machine Learning Regression
* Model Evaluation
* Cross-Validation
* Model Saving and Prediction

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Clean and preprocess the Glassdoor job salary dataset.
2. Explore salary patterns across different job-related features.
3. Analyze relationships between salary and categorical/numerical variables.
4. Build regression models to predict average salary.
5. Compare model performance using appropriate evaluation metrics.
6. Select the best-performing model.
7. Save the final trained model for future predictions.

---

## 📂 Dataset

The project uses a Glassdoor job postings dataset containing information such as:

* Job Title
* Location
* Company
* Company Size
* Company Rating
* Industry
* Sector
* Employment Type
* Salary Estimate
* Other job-related attributes

The salary estimate is processed to extract:

* Minimum Salary
* Maximum Salary
* Average Salary

`Average Salary` is used as the target variable for the regression model.

---

## 🔍 Exploratory Data Analysis

The project performs EDA to understand salary patterns and relationships.

Some of the analyses include:

* Salary distribution
* Job title vs. salary
* Location vs. salary
* Company size vs. salary
* Company rating vs. salary
* Missing-value analysis
* Duplicate-value analysis

---

## 📊 Statistical Analysis

Statistical analysis is performed to investigate relationships between salary and categorical variables.

The project includes:

* Pearson correlation analysis
* ANOVA for Company Size
* ANOVA for Job Title
* Tukey HSD post-hoc analysis

---

## 🤖 Machine Learning

Two regression models are developed and compared:

### 1. Linear Regression

A Linear Regression pipeline is used with preprocessing for categorical and numerical features.

### 2. Random Forest Regression

A Random Forest Regressor is trained with:

* `n_estimators = 300`
* `max_depth = 10`
* `min_samples_split = 5`
* `min_samples_leaf = 2`
* `random_state = 42`

Categorical variables are encoded using `OneHotEncoder`.

---

## ⚙️ Model Evaluation

The models are evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

5-fold cross-validation is also used to compare model performance.

---

## 💾 Saved Model

The final trained machine learning pipeline is saved using Joblib:

```text
salary_prediction_model.pkl
```

The saved pipeline contains the preprocessing and trained model, allowing it to be loaded later for making predictions on new job data.

---

## 📁 Project Structure

```text
Glassdoor-Job-Salary-Prediction/
│
├── Glassdoor_job_salary_prediction.ipynb
├── salary_prediction_model.pkl
└── README.md
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* SciPy
* Statsmodels
* Joblib
* Google Colab
* Git
* GitHub

---

## 👩‍💻 Project Type

**Data Science + Exploratory Data Analysis + Machine Learning Regression**

**Contribution:** Individual Project

---

## 🌐 Streamlit Web Application

The trained salary prediction model is deployed as a Streamlit web application.

The application allows users to enter job-related information such as:

- Job Title
- Company Rating
- Location
- Headquarters
- Company Size
- Year Founded
- Type of Ownership
- Industry
- Sector
- Revenue
- Competitors

The application then predicts the estimated average salary for the job.

### ▶️ Run the Application Locally

```bash
streamlit run app.py

The application will open in the browser at:
http://localhost:8501

The application can be deployed using Streamlit Community Cloud directly from the GitHub repository.

