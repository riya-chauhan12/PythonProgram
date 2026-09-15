''' WAP to implement Decision Tree, SVM, logistic algorithm
'''
# ============================================================
# MACHINE LEARNING LAB
# Experiment: Decision Tree, SVM and Logistic Regression
# ============================================================

# ------------------------------------------------------------
# 1. IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

# Used for handling data
import pandas as pd

# Load the built-in Iris dataset
from sklearn.datasets import load_iris

# Used to split data into training and testing sets
from sklearn.model_selection import train_test_split

# Decision Tree classification algorithm
from sklearn.tree import DecisionTreeClassifier

# Support Vector Machine classification algorithm
from sklearn.svm import SVC

# Logistic Regression classification algorithm
from sklearn.linear_model import LogisticRegression

# Used to calculate classification accuracy
from sklearn.metrics import accuracy_score


# ------------------------------------------------------------
# 2. LOAD THE IRIS DATASET
# ------------------------------------------------------------

# Load the Iris dataset
iris = load_iris()

# X contains the input features
#
# The four features are:
# 1. Sepal Length
# 2. Sepal Width
# 3. Petal Length
# 4. Petal Width

X = iris.data

# y contains the target/output.
#
# Target classes:
# 0 -> Iris Setosa
# 1 -> Iris Versicolor
# 2 -> Iris Virginica

y = iris.target


# ------------------------------------------------------------
# 3. SPLIT THE DATASET
# ------------------------------------------------------------

# Divide the dataset into:
# 70% training data
# 30% testing data
#
# random_state=42 makes the split reproducible.
# stratify=y keeps the proportion of each species similar
# in both training and testing data.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)


# ============================================================
# 4. DECISION TREE
# ============================================================

# Create a Decision Tree classifier.
#
# random_state=42 makes the result reproducible.

decision_tree = DecisionTreeClassifier(random_state=42)


# Train the Decision Tree using the training data.
decision_tree.fit(X_train, y_train)


# Predict the species of the test data.
dt_prediction = decision_tree.predict(X_test)


# Calculate the accuracy of the Decision Tree.
dt_accuracy = accuracy_score(y_test, dt_prediction)


# Display the result.
print("Decision Tree Accuracy:",
      dt_accuracy * 100, "%")


# ============================================================
# 5. SUPPORT VECTOR MACHINE (SVM)
# ============================================================

# Create an SVM classification model.
#
# kernel="linear" means we are using a linear decision boundary.

svm_model = SVC(kernel="linear")


# Train the SVM model.
svm_model.fit(X_train, y_train)


# Predict the species of the test data.
svm_prediction = svm_model.predict(X_test)


# Calculate SVM accuracy.
svm_accuracy = accuracy_score(y_test, svm_prediction)


# Display the result.
print("SVM Accuracy:",
      svm_accuracy * 100, "%")


# ============================================================
# 6. LOGISTIC REGRESSION
# ============================================================

# Create a Logistic Regression model.
#
# max_iter=200 is used to give the algorithm enough
# iterations to find the solution.

logistic_model = LogisticRegression(max_iter=200)


# Train the Logistic Regression model.
logistic_model.fit(X_train, y_train)


# Predict the species of the test data.
logistic_prediction = logistic_model.predict(X_test)


# Calculate Logistic Regression accuracy.
logistic_accuracy = accuracy_score(
    y_test,
    logistic_prediction
)


# Display the result.
print("Logistic Regression Accuracy:",
      logistic_accuracy * 100, "%")

