# 🎯 Student Math Score Prediction (Machine Learning Project)

## 📌 Project Overview

This project uses Machine Learning to predict a student's **math score** based on various academic and demographic features such as reading score, writing score, lunch type, and test preparation course.

The goal is to understand how different factors influence student performance and build a regression model to make predictions.

---

## 📊 Dataset

The dataset contains student performance data with features like:

* Gender
* Race/Ethnicity
* Parental level of education
* Lunch type
* Test preparation course
* Reading score
* Writing score
* Math score (target variable)

---

## 🧹 Data Preprocessing

Steps performed:

* Handled categorical variables using **One-Hot Encoding**
* Converted all features into numerical format
* Checked correlations between features
* Selected important features for training

---

## 🤖 Model Used

* Linear Regression (Scikit-learn)

---

## 📈 Evaluation

The model was evaluated using **R² score**:

* Initial model score: ~0.56
* Improved model score: ~0.87 – 0.90

This shows a strong relationship between selected features and math score.

---

## 🔥 Key Insights

* Reading and writing scores have the highest impact on math score
* Demographic features have weaker influence
* Academic performance is strongly correlated across subjects

---

## 🛠️ Tech Stack

* Python
* Pandas
* Matplotlib
* Scikit-learn

---

## 🚀 How to Run

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install pandas numpy matplotlib scikit-learn
   ```
3. Run the Jupyter Notebook
4. Train the model and test predictions

---

## 📌 Future Improvements

* Add more feature engineering
* Deploy as a small web app
* Improve generalization on unseen data

---

## 👨‍💻 Author

Beginner Machine Learning Project for learning and practice purposes.
