# 🏡 House Price Prediction using Machine Learning

A data science project to predict house prices based on key features like area, number of bedrooms, stories, and amenities using machine learning algorithms.

---

## 📌 Objective

The goal of this project is to build a regression model that accurately predicts house prices based on various property characteristics. This helps in understanding the key drivers of real estate pricing and provides actionable insights for property buyers, sellers, and agents.

---

## 📊 Dataset Overview

- **Total Records:** 545
- **Features:** 
  - Numerical: `price`, `area`, `bedrooms`, `bathrooms`, `stories`, `parking`
  - Categorical: `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`, `furnishingstatus`

The dataset contains both numerical and categorical variables describing house characteristics and selling prices.

---

## 🔍 Exploratory Data Analysis (EDA)

- Checked for missing values and data imbalances
- Visualized distributions of area, price, bedrooms
- Analyzed correlations using heatmaps and scatter plots
- Observed positive correlation between area, stories, and house price

---

## 🛠️ Feature Engineering

- Applied one-hot encoding on categorical variables
- Scaled numerical features where necessary
- Removed multicollinear features using VIF (if applicable)
- Split dataset into train-test sets (80-20)

---

## 📈 Model Building

Three regression models were trained and evaluated:

1. **Linear Regression**
2. **Decision Tree Regressor**
3. **Random Forest Regressor**

---

## 📊 Model Evaluation

Evaluation metrics used:
- **Root Mean Squared Error (RMSE)**
- **R² Score**

| Model                | RMSE     | R² Score |
|---------------------|----------|----------|
| Linear Regression    | 187462.3 | 0.68     |
| Decision Tree        | 158936.5 | 0.77     |
| Random Forest        | 145239.8 | 0.82 ✅   |

**Random Forest Regressor** performed the best with the lowest RMSE and highest R² score.

---

## 🚀 Deployment

The final model was deployed using **Flask** as a web application.

### App Features:
- Users can input house details via a form
- The app predicts the estimated price instantly

## 🧰 Tools & Technologies Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Flask
- Jupyter Notebook
- Git & GitHub

---

## ✅ Conclusion

- The model can effectively predict house prices based on given features
- Random Forest Regressor showed the best performance
- Application can assist users in making informed property decisions

### 🔮 Future Work
- Add location-based pricing using geospatial data
- Use XGBoost or LightGBM for better accuracy
- Deploy with a user-friendly UI using Streamlit

---

## 🙋‍♂️ About the Author

**Syed Habib Haider**  
*Data Scientist | AI Consultant | Social Media Strategist*  
📫 Email: habibhaidergardazi@gmail.com  
📍 Islamabad, Pakistan  
🔗 [LinkedIn](https://www.linkedin.com/in/gf_ATUsu) | [GitHub](https://github.com/thehabbib68)
