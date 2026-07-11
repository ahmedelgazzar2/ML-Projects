🏠 #ML House Price Prediction

📌 Overview

This project builds an end-to-end Machine Learning pipeline to predict house prices using demographic and housing-related features from the California Housing dataset.

The project covers the complete Machine Learning workflow, including data preprocessing, exploratory data analysis, model selection, hyperparameter tuning, evaluation, and UI Interaction using Streamlit.

📊 ## Dataset :
  - Dataset: Housing Dataset
  - Rows: 20,640
  - Target Variable: median_house_value

## Features :

------------------------------------------------
| Feature            | Description              |
| ------------------ | ------------------------ |
| longitude          | House longitude          |
| latitude           | House latitude           |
| housing_median_age | Median age of houses     |
| total_rooms        | Total number of rooms    |
| total_bedrooms     | Total number of bedrooms |
| population         | Population in the area   |
| households         | Number of households     |
| median_income      | Median income            |
| ocean_proximity    | Distance from the ocean  |
-------------------------------------------------

📈 ## Exploratory Data Analysis (EDA) :

  #### The following analyses were performed:

    - Missing Values Analysis
    - Feature Distribution
    - Correlation Heatmap
    - Outlier Detection
    - Target Distribution
    - Residual Analysis

<img width="854" height="543" alt="Untitled5" src="https://github.com/user-attachments/assets/bda5a52a-ed44-467f-8be9-eff857cba32a" />
<img width="843" height="543" alt="Untitled4" src="https://github.com/user-attachments/assets/4e9b3f85-12e4-4f1b-a97c-bb0b7f8091af" />
<img width="854" height="543" alt="Untitled1" src="https://github.com/user-attachments/assets/eaf2e184-8140-40d2-9644-7a339ba1b6e0" />
<img width="880" height="632" alt="Untitled" src="https://github.com/user-attachments/assets/a4e37edd-c48a-4e3e-b46a-59be3d522a6f" />


⚙️ ## Data Preprocessing :

  #### The preprocessing pipeline includes:

    - Missing Value Imputation
    - One-Hot Encoding
    - Standard Scaling
    - ColumnTransformer
    - Scikit-learn Pipeline


🤖 ## Models Evaluated :

---------------------------------------------------------------------
| Model                         |    RMSE   |     MAE   |     R²    |
| ----------------------------- | --------- | --------- | --------- |
| HistGradientBoostingRegressor | **0.230** |     0.162 | **0.836** |
| RandomForestRegressor         |     0.233 | **0.161** |     0.832 |
| Ridge Regression              |     0.328 |     0.248 |     0.667 |
| Linear Regression             |     0.328 |     0.248 |     0.667 |
| Lasso Regression              |     0.569 |     0.461 |     0.000 |
--------------------------------------------------------------------


🔍 ## Model Selection :

  #### The models were compared using:

    - K-Fold Cross Validation
    - GridSearchCV
    - RMSE
    - MAE
    - R² Score

  The best-performing model was **HistGradientBoostingRegressor**


💻 ## Streamlit Application :

  A Streamlit web application was developed to allow users to:

    - Enter house information.
    - Predict the house price instantly.
    - Interact with the trained Machine Learning model through a simple user interface.

<img width="1851" height="846" alt="WhatsApp Image 2026-07-11 at 9 16 10 AM" src="https://github.com/user-attachments/assets/f064595c-f591-4214-ac2c-ba4c4e35d70b" />

🛠️ ## Technologies Used :
  - Python
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
  - Scikit-learn
  - Streamlit

## 📁 Project Structure

```text
House-Price-Prediction/
│
├── data/
│   └── housing.csv
│
├── notebooks/
│   └── House_Price_Prediction.ipynb
│
├── models/
│   └── house_price_model.pkl
│
├── app/
│   └── app.py
│
└── README.md
```


📷 Screenshots :

<img width="1851" height="846" alt="WhatsApp Image 2026-07-11 at 9 16 10 AM" src="https://github.com/user-attachments/assets/906d6434-1559-4d45-bc0f-bd51c4636267" />
<img width="1693" height="929" alt="ChatGPT Image Jul 11, 2026, 05_57_40 PM" src="https://github.com/user-attachments/assets/e33a6619-a575-43c1-8781-1191e1f0bbe1" />

⭐ # Repository

## If you found this project useful, feel free to ⭐ the repository.
