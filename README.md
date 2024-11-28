# Credit_Risk_Analysis
#### By : Venkatesh Kannan
#### Project Description
#### **Title** : Credit Risk Analysis and Prediction

Overview: The Credit Risk Analysis and Prediction project aims to identify key factors contributing to loan default and predict the likelihood of default using a machine learning-based approach. By analyzing customer financial data and loan details, this project provides actionable insights for lenders to minimize risk, improve decision-making, and maximize profitability.

The project also includes a user-friendly interactive web application, built with Streamlit, that enables users to input customer data and receive real-time predictions about loan default risk. This tool is designed for banks, financial institutions, and credit providers seeking efficient ways to assess creditworthiness.

### **Project Description**

**Title:** Credit Risk Analysis and Prediction

**Overview:**
The **Credit Risk Analysis and Prediction** project aims to identify key factors contributing to loan default and predict the likelihood of default using a machine learning-based approach. By analyzing customer financial data and loan details, this project provides actionable insights for lenders to minimize risk, improve decision-making, and maximize profitability.

The project also includes a user-friendly interactive web application, built with **Streamlit**, that enables users to input customer data and receive real-time predictions about loan default risk. This tool is designed for banks, financial institutions, and credit providers seeking efficient ways to assess creditworthiness.

---

### **Objectives**
1. **Understand Key Risk Factors**:
   - Identify financial and demographic factors that contribute to the likelihood of loan default.
   
2. **Develop a Predictive Model**:
   - Build a machine learning model to predict default probabilities using customer and loan attributes.

3. **Answer Business Questions**:
   - **Q1**: What factors contribute to loan default?
   - **Q2**: What is the ideal loan-to-value (LTV) ratio for reducing risk across customer segments?
   - **Q3**: How can lenders maximize profitability while managing risk?

4. **Deploy an Interactive App**:
   - Provide a platform for users to interactively predict loan default probabilities based on input data.

---

### **Data Description**
The project uses a dataset containing customer financial and loan details, including:
- **Demographics**: Age, income, employment length, home ownership status.
- **Loan Details**: Loan amount, loan purpose, interest rate, loan grade.
- **Credit History**: Credit history length, prior defaults.

The data is preprocessed to handle missing values, normalize continuous features, and encode categorical variables. Outliers are treated to improve model accuracy.

---

### **Methodology**
1. **Exploratory Data Analysis (EDA)**:
   - Visualize data distributions, detect outliers, and examine correlations between features and loan default status.

2. **Feature Engineering**:
   - Calculate derived metrics like loan-to-income ratio and encode categorical features.

3. **Model Development**:
   - Train a Logistic Regression model for binary classification.
   - Evaluate model performance using accuracy, precision, recall, and F1-score.

4. **Deployment**:
   - Build an interactive Streamlit app for end-users to predict loan default risk.

---

### **Features of the Streamlit App**
1. **User Input**:
   - Enter customer details (age, income, loan amount, etc.) via intuitive input widgets.
   
2. **Prediction**:
   - Display whether the customer is likely to default, along with the probability.
   
3. **Insights**:
   - Provide business insights and risk mitigation strategies based on model outputs.

---

### **Key Insights**
1. **Factors Contributing to Loan Default**:
   - High loan-to-income ratios, shorter credit histories, and higher interest rates are strong predictors of default.

2. **Optimal Loan-to-Value Ratios**:
   - Default rates are lowest for LTV ratios below 40%.

3. **Profitability Strategies**:
   - Increase interest rates for high-risk customers, limit loan amounts, and require collateral to reduce financial exposure.

---

### **Conclusion**
This project provides a comprehensive framework for analyzing and predicting credit risk, enabling lenders to make data-driven decisions. The integration of a predictive model with a Streamlit-based app ensures accessibility and usability for financial professionals.

---

