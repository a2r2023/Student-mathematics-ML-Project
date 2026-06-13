import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("StudentsPerformance.csv")
df["gender"] = df["gender"].map({
    "male":1,
    "female":0
})
df["race/ethnicity"] = df["race/ethnicity"].map({
    "group A":1,
    "group B":2,
    "group C":3,
    "group D":4,
    "group E":5
})
df = pd.get_dummies(df, columns=["parental level of education"],dtype=int)
df["test preparation course"] = df["test preparation course"].map({
    "none":0,
    "completed":1
})
df["lunch"] = df["lunch"].map({
    "standard":1,
    "free/reduced":0
})
corr = df.corr(numeric_only=True)["math score"]

X = df.drop("math score",axis=1)
y = df["math score"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model = LinearRegression()
model.fit(X,y)
prediction = model.predict(X_test)
print("Actual:")
print(y_test.values[:5])
print("predicted:")
print(prediction[:5])

print("The R^2 test value is: " , round(r2_score(prediction,y_test) , 1))