
'''write a program to read the trian_loan.csv dataset handle missing value mean and mode and 
apply different Machine learning algroithms to find the best accuracy score'''

# ============================================================
# MACHINE LEARNING LAB
# Loan Prediction using Machine Learning Algorithms
# ============================================================

# ------------------------------------------------------------
# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score


# ------------------------------------------------------------
# 2. READ THE DATASET
# ------------------------------------------------------------

df = pd.read_csv("train_loan.csv")

print("First 5 rows:")
print(df.head())


# ------------------------------------------------------------
# 3. BASIC EDA
# ------------------------------------------------------------

# Check number of rows and columns
print("\nDataset Shape:")
print(df.shape)


# Check column names
print("\nColumn Names:")
print(df.columns)


# Check data types
print("\nData Types:")
print(df.dtypes)


# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())


# Check basic statistical information
print("\nStatistical Summary:")
print(df.describe())


# Check duplicate rows
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())


# ------------------------------------------------------------
# 4. HANDLE MISSING VALUES
# ------------------------------------------------------------

# Numerical columns
# Replace missing numerical values with the mean.

df["LoanAmount"] = df["LoanAmount"].fillna(
    df["LoanAmount"].mean()
)

df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(
    df["Loan_Amount_Term"].mean()
)


# Credit_History is numerical (0/1),
# so replace missing values with its mean.

df["Credit_History"] = df["Credit_History"].fillna(
    df["Credit_History"].mean()
)


# Categorical columns
# Replace missing values with the mode.

df["Gender"] = df["Gender"].fillna(
    df["Gender"].mode()[0]
)

df["Married"] = df["Married"].fillna(
    df["Married"].mode()[0]
)

df["Dependents"] = df["Dependents"].fillna(
    df["Dependents"].mode()[0]
)

df["Self_Employed"] = df["Self_Employed"].fillna(
    df["Self_Employed"].mode()[0]
)


# Check missing values again
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# ------------------------------------------------------------
# 5. BASIC VISUALIZATION
# ------------------------------------------------------------

# Count how many loans were approved and rejected.

df["Loan_Status"].value_counts().plot(
    kind="bar"
)

plt.title("Loan Approval Status")
plt.xlabel("Loan Status")
plt.ylabel("Number of Applicants")

plt.show()


# ------------------------------------------------------------
# 6. VISUALIZE LOAN AMOUNT
# ------------------------------------------------------------

df["LoanAmount"].plot(
    kind="hist",
    bins=20
)

plt.title("Distribution of Loan Amount")
plt.xlabel("Loan Amount")
plt.ylabel("Frequency")

plt.show()


# ------------------------------------------------------------
# 7. REMOVE UNNECESSARY COLUMN
# ------------------------------------------------------------

# Loan_ID is only an identification number.
# It is not useful for predicting loan approval.

df = df.drop("Loan_ID", axis=1)


# ------------------------------------------------------------
# 8. ENCODE CATEGORICAL DATA
# ------------------------------------------------------------

# Machine learning algorithms need numerical input.
# LabelEncoder converts categorical values into numbers.

encoder = LabelEncoder()


df["Gender"] = encoder.fit_transform(df["Gender"])

df["Married"] = encoder.fit_transform(df["Married"])

df["Dependents"] = encoder.fit_transform(df["Dependents"])

df["Education"] = encoder.fit_transform(df["Education"])

df["Self_Employed"] = encoder.fit_transform(df["Self_Employed"])

df["Property_Area"] = encoder.fit_transform(df["Property_Area"])

df["Loan_Status"] = encoder.fit_transform(df["Loan_Status"])


# Display cleaned dataset
print("\nCleaned Dataset:")
print(df.head())


# ------------------------------------------------------------
# 9. SEPARATE FEATURES AND TARGET
# ------------------------------------------------------------

# X = input features
# y = target/output

X = df.drop("Loan_Status", axis=1)

y = df["Loan_Status"]


# ------------------------------------------------------------
# 10. SPLIT DATA INTO TRAINING AND TESTING
# ------------------------------------------------------------

# 70% data -> training
# 30% data -> testing

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)


# ============================================================
# 11. LOGISTIC REGRESSION
# ============================================================

logistic = LogisticRegression(max_iter=1000)

# Train the model
logistic.fit(X_train, y_train)

# Make predictions
logistic_pred = logistic.predict(X_test)

# Calculate accuracy
logistic_accuracy = accuracy_score(
    y_test,
    logistic_pred
)

print(
    "\nLogistic Regression Accuracy:",
    logistic_accuracy * 100,
    "%"
)


# ============================================================
# 12. K-NEAREST NEIGHBORS
# ============================================================

knn = KNeighborsClassifier(n_neighbors=5)

# Train the model
knn.fit(X_train, y_train)

# Make predictions
knn_pred = knn.predict(X_test)

# Calculate accuracy
knn_accuracy = accuracy_score(
    y_test,
    knn_pred
)

print(
    "K-NN Accuracy:",
    knn_accuracy * 100,
    "%"
)


# ============================================================
# 13. DECISION TREE
# ============================================================

decision_tree = DecisionTreeClassifier(
    random_state=42
)

# Train the model
decision_tree.fit(X_train, y_train)

# Make predictions
dt_pred = decision_tree.predict(X_test)

# Calculate accuracy
dt_accuracy = accuracy_score(
    y_test,
    dt_pred
)

print(
    "Decision Tree Accuracy:",
    dt_accuracy * 100,
    "%"
)


# ============================================================
# 14. RANDOM FOREST
# ============================================================

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
random_forest.fit(X_train, y_train)

# Make predictions
rf_pred = random_forest.predict(X_test)

# Calculate accuracy
rf_accuracy = accuracy_score(
    y_test,
    rf_pred
)

print(
    "Random Forest Accuracy:",
    rf_accuracy * 100,
    "%"
)


# ============================================================
# 15. SUPPORT VECTOR MACHINE
# ============================================================

svm = SVC()

# Train the model
svm.fit(X_train, y_train)

# Make predictions
svm_pred = svm.predict(X_test)

# Calculate accuracy
svm_accuracy = accuracy_score(
    y_test,
    svm_pred
)

print(
    "SVM Accuracy:",
    svm_accuracy * 100,
    "%"
)


# ============================================================
# 16. NAIVE BAYES
# ============================================================

naive_bayes = GaussianNB()

# Train the model
naive_bayes.fit(X_train, y_train)

# Make predictions
nb_pred = naive_bayes.predict(X_test)

# Calculate accuracy
nb_accuracy = accuracy_score(
    y_test,
    nb_pred
)

print(
    "Naive Bayes Accuracy:",
    nb_accuracy * 100,
    "%"
)


# ============================================================
# 17. COMPARE ALL ACCURACIES
# ============================================================

accuracy_results = {
    "Logistic Regression": logistic_accuracy,
    "K-NN": knn_accuracy,
    "Decision Tree": dt_accuracy,
    "Random Forest": rf_accuracy,
    "SVM": svm_accuracy,
    "Naive Bayes": nb_accuracy
}


print("\n======================================")
print("MODEL ACCURACY COMPARISON")
print("======================================")


for model, accuracy in accuracy_results.items():

    print(
        model,
        ":",
        round(accuracy * 100, 2),
        "%"
    )


# ------------------------------------------------------------
# 18. FIND THE BEST MODEL
# ------------------------------------------------------------

best_model = max(
    accuracy_results,
    key=accuracy_results.get
)

best_accuracy = accuracy_results[best_model]


print("\n======================================")
print("BEST MODEL")
print("======================================")

print("Model:", best_model)

print(
    "Accuracy:",
    round(best_accuracy * 100, 2),
    "%"
)

