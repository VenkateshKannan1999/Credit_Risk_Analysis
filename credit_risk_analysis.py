# -*- coding: utf-8 -*-
"""Credit_Risk_Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Symy8jfPoPk4pe4w75NxMRme6t-2Ioj-
"""

# Importing necessary libraries
import pandas as pd #data Maipulation
import numpy as np #numerical calculation
import matplotlib.pyplot as plt #Data Visulaisation
import seaborn as sns #statistical Visulisation
from sklearn.model_selection import train_test_split #splitting data for model training and testing
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
Credit_risk_analysis = pd.read_csv('credit_risk_dataset.csv')

Credit_risk_analysis.info()

# Encoding  categorical features using MAP function and assigning the Categorical features with Numerical Values
Credit_risk_analysis['person_home_ownership'] = Credit_risk_analysis['person_home_ownership'].map({'RENT': 0, 'MORTGAGE': 1, 'OWN': 2, 'OTHER': 3})
Credit_risk_analysis['loan_intent'] = Credit_risk_analysis['loan_intent'].map({'HOMEIMPROVEMENTS': 0, 'EDUCATION': 1, 'MEDICAL': 2, 'VENTURE': 3,'DEBTCONSOLIDATION': 4})
Credit_risk_analysis['loan_grade'] = Credit_risk_analysis['loan_grade'].map({'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6})
Credit_risk_analysis['cb_person_default_on_file'] = Credit_risk_analysis['cb_person_default_on_file'].map({'Y': 1, 'N': 0})

Credit_risk_analysis.info()

#Finding Missing Values
Credit_risk_analysis.isnull().sum()

# Fill missing values for 'person_emp_length','loan_int_rate' with the median
Credit_risk_analysis['person_emp_length'] = Credit_risk_analysis['person_emp_length'].fillna(Credit_risk_analysis['person_emp_length'].median())
Credit_risk_analysis['loan_int_rate'] = Credit_risk_analysis['loan_int_rate'].fillna(Credit_risk_analysis['loan_int_rate'].median())
Credit_risk_analysis['loan_intent'] = Credit_risk_analysis['loan_intent'].fillna(Credit_risk_analysis['loan_intent'].mode()[0])
print(Credit_risk_analysis.isnull().sum())

Credit_risk_analysis.isnull().sum()

# Exploratory Data Analysis
print(Credit_risk_analysis.describe())

# Ploting histograms for all features
Credit_risk_analysis.hist(bins=20, figsize=(15, 10), edgecolor='black')
plt.hist("Histograms of All Features")
plt.show()

# Distribution of loan amounts grouped by loan intent
plt.figure(figsize=(15,9))
sns.countplot(data = Credit_risk_analysis, x = 'loan_intent', hue = 'loan_status')
plt.title("Loan Intent Distribution by Loan Status")
plt.xlabel("Loan Intent(0=Personal, 1=Education, 2=Medical, 3=Venture, 4=Debt Consolidation)")
plt.ylabel("Loan Distribution(0=No Default,1=Defautl)")
plt.show()

#histogram for loan_status (0 = No Default, 1 = Default)
import plotly.express as px
fig2 = px.histogram(
    Credit_risk_analysis,
    x="loan_grade",
    color="loan_status",
    title="Loan Grade Distribution by Loan Status",
    labels={
        "loan_grade": "Loan Grade (Encoded)",
        "loan_status": "Loan Status (0=No Default, 1=Default)"
    },
    barmode="group"
)
fig2.update_layout(
    legend_title="Loan Status",
    title=dict(x=0.5),  # Center align title
    xaxis_title="Loan Grade",
    yaxis_title="Loan Distribution"
)
fig2.show()

fig3 = px.box(
    Credit_risk_analysis,
    x="loan_intent",
    y="loan_amnt",
    color="loan_status",
    title="Loan Amount Distribution by Loan Intent and Loan Status",
    labels={
        "loan_intent": "Loan Intent (Encoded)",
        "loan_amnt": "Loan Amount",
        "loan_status": "Loan Status (0=No Default, 1=Default)"
    }
)
fig3.update_layout(
    legend_title="Loan Status",
    title=dict(x=0.5),  # Center align title
    xaxis_title="Loan Intent",
    yaxis_title="Loan Amount"
)
fig3.show()

fig4 = px.scatter(
    Credit_risk_analysis,
    x="loan_amnt",
    y="loan_int_rate",
    color="loan_status",
    title="Loan Interest Rate vs Loan Amount by Loan Status",
    labels={
        "loan_amnt": "Loan Amount",
        "loan_int_rate": "Loan Interest Rate",
        "loan_status": "Loan Status (0=No Default, 1=Default)"
    }
)
fig4.update_layout(
    legend_title="Loan Status",
    title=dict(x=0.5),  # Center align title
    xaxis_title="Loan Amount",
    yaxis_title="Loan Interest Rate"
)
fig4.show()

#dealing with Outliers
# Define continuous numerical columns
continuous_columns = ['person_age', 'person_income', 'loan_amnt', 'loan_int_rate', 'cb_person_cred_hist_length']

#clipping outliers to the 2th and 75th percentiles
for column in continuous_columns:
    Q1 = Credit_risk_analysis[column].quantile(0.25)
    Q3 = Credit_risk_analysis[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    Credit_risk_analysis[column] = np.clip(Credit_risk_analysis[column], lower_bound, upper_bound)

for column in continuous_columns:
    plt.figure(figsize=(8, 4))
    sns.boxplot(Credit_risk_analysis[column])
    plt.title(f"Boxplot of {column} after Outlier Clipping")
    plt.show()

# Compute and visualize the correlation matrix
plt.figure(figsize=(12, 8))
correlation_matrix = Credit_risk_analysis.corr()
sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5
)
plt.title("Correlation Matrix after Outlier Handling")
plt.xlabel("Features")
plt.ylabel("Features")
plt.show()



for feature in Credit_risk_analysis:
    plt.figure(figsize=(10, 5))
    sns.histplot(Credit_risk_analysis[feature], kde=True, bins=30)
    plt.title(f"Distribution of {feature}")
    plt.show()

# Define feature set (X) and target variable (y)
X = Credit_risk_analysis.drop(['loan_status'], axis=1)  # Drop target columns from features
# Changed: Pass a list of column names ['loan_status', 'loan_grade'] instead of a tuple within a list.
y = Credit_risk_analysis['loan_status']  # Target variable

# Split the dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler

# Define continuous columns
continuous_columns = [ 'person_age','person_income', 'loan_amnt','loan_int_rate','cb_person_cred_hist_length', 'person_emp_length']

# Apply StandardScaler to continuous features
scaler = StandardScaler()
X_train[continuous_columns] = scaler.fit_transform(X_train[continuous_columns]) # Use continuous_columns instead of Credit_risk_analysis
X_test[continuous_columns] = scaler.transform(X_test[continuous_columns]) # Use continuous_columns instead of Credit_risk_analysis

from sklearn.linear_model import LogisticRegression

# Train Logistic Regression model
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)[:, 1]  # Probabilities for ROC-AUC calculation

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# ROC-AUC Score
# Get probabilities for the positive class only
y_pred_prob = model.predict_proba(X_test)[:, 1]  # Probabilities for the positive class

# Calculate ROC-AUC for binary classification
roc_auc = roc_auc_score(y_test, y_pred_prob)

print(f"ROC-AUC Score: {roc_auc:.2f}")

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=['No Default', 'Default'], yticklabels=['No Default', 'Default'])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc:.2f})", color="blue")
plt.plot([0, 1], [0, 1], linestyle="--", color="red")
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# Define new customer data
new_customer = pd.DataFrame({
    'person_age': [21],
    'person_income': [10000],
    'person_home_ownership': [2],
    'person_emp_length': [6.0],
    'loan_intent': [3],
    'loan_grade': [0],
    'loan_amnt': [35000],
    'loan_int_rate': [11.11],
    'loan_status': [1],
    'loan_percent_income': [0.44],
    'cb_person_default_on_file': [0],
    'cb_person_cred_hist_length': [4]

}, index=[0]) # Create a DataFrame with an index

# Get the feature names used during training
training_features = model.feature_names_in_

# Ensure all training features are present in new_customer
for feature in training_features:
    if feature not in new_customer.columns:
        new_customer[feature] = np.nan  # Add missing columns with NaN

# Reorder the columns of new_customer to match the training data
new_customer = new_customer[training_features]

# Impute missing values using the mean strategy
imputer = SimpleImputer(strategy='mean') # Create an imputer with your desired strategy

# Fit the imputer on your training data and transform the new customer data
new_customer_imputed = imputer.fit_transform(new_customer) # Fit and transform using the imputer


new_prediction_prob = model.predict_proba(new_customer_imputed)[:, 1]

print(f"Will the customer default? {'Yes' if new_prediction[0] == 1 else 'No'}")
print(f"Probability of Default: {new_prediction_prob[0] * 100:.2f}%")

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
# Assuming 'model' holds your trained Logistic Regression model from previous cells:
logistic_model = model

# Define new customer data with correct column names from X_train
new_customer = pd.DataFrame([{
    'person_age': 42,
    'person_income': 9600,
    'person_home_ownership': 0,
    'person_emp_length': 5.0,
    'loan_intent': 0,
    'loan_grade': 1,
    'loan_amnt': 1000.0,
    'loan_int_rate': 11.14,
    'cb_person_default_on_file': 1,
    'cb_person_cred_hist_length': 5,
    # Include the missing column with a value
    'loan_percent_income': 0.104  # Example value, adjust as needed
}])
# Reorder columns in new_customer to match X_train
new_customer = new_customer[X_train.columns]
# Normalize continuous features
continuous_columns = ['person_age', 'person_income', 'loan_amnt', 'loan_int_rate', 'cb_person_cred_hist_length', 'person_emp_length']
new_customer[continuous_columns] = scaler.transform(new_customer[continuous_columns])

# Make predictions
new_prediction = logistic_model.predict(new_customer)
new_prediction_prob = logistic_model.predict_proba(new_customer)[:, 1]

# Display results
print(f"Will the customer default? {'Yes' if new_prediction[0] == 1 else 'No'}")
print(f"Probability of Default: {new_prediction_prob[0] * 100:.2f}%")

import joblib
joblib.dump(model, 'Credit_risk_analysis_model')

!pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib  # To load the trained model and scaler

# Load your trained model and scaler
# model_path = os.path.join(os.path.dirname(__file__), 'Credit_risk_analysis_model')  # __file__ is not defined in Streamlit
# Use a relative path assuming the model is in the same directory as the script
model_path = 'Credit_risk_analysis_model'
model = joblib.load(model_path)


# App title
st.title("Credit Default Prediction App")
st.write("""
This app predicts whether a customer is likely to default on their loan based on their financial and loan-related information.
""")

# Sidebar for user input
st.sidebar.header("Enter Customer Details")

# Input fields
person_age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=30, step=1)
person_income = st.sidebar.number_input("Income", min_value=0, max_value=1_000_000, value=50_000, step=1_000)
person_home_ownership = st.sidebar.selectbox("Home Ownership", options=["RENT", "MORTGAGE", "OWN", "OTHER"])
person_emp_length = st.sidebar.number_input("Employment Length (years)", min_value=0.0, max_value=50.0, value=5.0, step=0.1)
loan_intent = st.sidebar.selectbox("Loan Intent", options=["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "DEBTCONSOLIDATION"])
loan_grade = st.sidebar.selectbox("Loan Grade", options=["A", "B", "C", "D", "E", "F", "G"])
loan_amnt = st.sidebar.number_input("Loan Amount", min_value=0.0, max_value=100_000.0, value=10_000.0, step=100.0)
loan_int_rate = st.sidebar.number_input("Interest Rate (%)", min_value=0.0, max_value=100.0, value=10.0, step=0.1)
loan_percent_income = st.sidebar.number_input("Loan to Income Ratio", min_value=0.0, max_value=1.0, value=0.1, step=0.01)
cb_person_default_on_file = st.sidebar.selectbox("Previous Default on File", options=["Yes", "No"])
cb_person_cred_hist_length = st.sidebar.number_input("Credit History Length (years)", min_value=0, max_value=50, value=10, step=1)

# Encode categorical features
home_ownership_map = {"RENT": 0, "MORTGAGE": 1, "OWN": 2, "OTHER": 3}
loan_intent_map = {"PERSONAL": 0, "EDUCATION": 1, "MEDICAL": 2, "VENTURE": 3, "DEBTCONSOLIDATION": 4}
loan_grade_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
default_on_file_map = {"Yes": 1, "No": 0}

# Prepare data for prediction
input_data = pd.DataFrame([{
    'person_age': person_age,
    'person_income': person_income,
    'person_home_ownership': home_ownership_map[person_home_ownership],
    'person_emp_length': person_emp_length,
    'loan_intent': loan_intent_map[loan_intent],
    'loan_grade': loan_grade_map[loan_grade],
    'loan_amnt': loan_amnt,
    'loan_int_rate': loan_int_rate,
    'loan_percent_income': loan_percent_income,
    'cb_person_default_on_file': default_on_file_map[cb_person_default_on_file],
    'cb_person_cred_hist_length': cb_person_cred_hist_length
}])
# Display user inputs
st.subheader("Customer Details")
st.write(input_data)

# Predict default
if st.button("Predict Default"):
    prediction = model.predict(input_data)
    prediction_prob = model.predict_proba(input_data)[:, 1]

    if prediction[0] == 1:
        st.error(f"The customer is likely to default! (Probability: {prediction_prob[0] * 100:.2f}%)")
    else:
        st.success(f"The customer is unlikely to default. (Probability: {prediction_prob[0] * 100:.2f}%)")