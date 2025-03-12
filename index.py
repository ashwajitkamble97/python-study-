# Description: This script loads the Titanic dataset, handles missing values, removes outliers, normalizes the 'Age' and 'Fare' columns, performs feature engineering, and visualizes the data.
import pandas as pd # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
from sklearn.preprocessing import MinMaxScaler # type: ignore

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
try:
	df = pd.read_csv(url)
except Exception as e:
	print(f"Error loading dataset: {e}")
	exit()
if "Cabin" in df.columns:
	# Handle missing values
	df["Age"].fillna(df["Age"].median(), inplace=True)
	df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
	# Remove outliers in 'Fare' using IQR
	Q1, Q3 = df["Fare"].quantile([0.25, 0.75])
	IQR = Q3 - Q1
	lower_bound, upper_bound = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
	df = df[(df["Fare"] >= lower_bound) & (df["Fare"] <= upper_bound)]

# Normalize Age and Fare
scaler = MinMaxScaler()
df[["Fare", "Age"]] = scaler.fit_transform(df[["Fare", "Age"]])

# Feature Engineering
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

# Visualizations
plt.figure(figsize=(6, 4))
sns.histplot(df["Age"], bins=20, kde=True)
plt.title("Age Distribution After Cleaning")
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(x=df["Survived"], palette="coolwarm")
plt.title("Survival Count")
plt.show()

plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()
