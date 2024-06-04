# Project-4--Industrial-Copper-Modeling
Industrial Copper Modeling
Project Overview
Project Title
Industrial Copper Modeling

Domain
Manufacturing

Skills Acquired
Python Scripting
Data Preprocessing
Exploratory Data Analysis (EDA)
Streamlit for Interactive Web Apps
Problem Statement
The copper industry deals with sales and pricing data that can be skewed and noisy, making manual predictions challenging and time-consuming. A machine learning approach can optimize pricing and lead classification by using techniques such as data normalization, feature scaling, and outlier detection.

Solution Steps
Data Understanding: Identify variable types and distributions.
Data Preprocessing: Handle missing values, treat outliers, address skewness, and encode categorical variables.
EDA: Visualize outliers and skewness using boxplots, distplots, and violin plots.
Feature Engineering: Create new features and remove highly correlated columns.
Model Building and Evaluation:
Train and evaluate models.
Optimize model hyperparameters.
Interpret model results.
Model Deployment: Create a Streamlit page for interactive prediction.
Dataset Description
id: Unique identifier for each transaction.
item_date: Date of the transaction.
quantity tons: Quantity of the item in tons.
customer: Customer identifier.
country: Customer's country.
status: Current status of the transaction (e.g., Draft, Won).
item type: Category of the items.
application: Specific use of the items.
thickness: Thickness of the items.
width: Width of the items.
material_ref: Reference for the material used.
product_ref: Reference for the specific product.
delivery date: Expected or actual delivery date.
selling_price: Selling price of the items.
Approach
Data Understanding and Preprocessing
Identify variable types and distributions.
Handle missing values using mean/median/mode.
Treat outliers using IQR or Isolation Forest.
Address skewness with log or boxcox transformations.
Encode categorical variables.
Exploratory Data Analysis (EDA)
Visualize outliers and skewness using Seaborn's boxplots, distplots, and violin plots.
Feature Engineering
Create new features if applicable.
Remove highly correlated columns using a heatmap.
Model Building and Evaluation
Regression Model: Predicts 'Selling_Price'.
Classification Model: Predicts 'Status' (WON or LOST).
Classification Algorithms: ExtraTreesClassifier and RandomForestClassifier.
Model Selection: RandomForestClassifier chosen for its good interpretability and high testing accuracy.
Evaluate models using metrics such as accuracy, precision, recall, F1 score, and AUC curve.
Optimize model hyperparameters using cross-validation and grid search.
Model Deployment
Streamlit Page:
Task input (Regression or Classification).
Input fields for each column value except 'Selling_Price' for regression and 'Status' for classification.
Perform feature engineering and scaling.
Predict and display results.
