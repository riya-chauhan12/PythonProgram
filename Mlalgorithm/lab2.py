'''Construct the classification model by using K-NN algorithm using Iris species data set.
 Take the value of k=3 , train the model by using 70 % data also print the classification accuracy.  '''

 # ============================================================
# MACHINE LEARNING LAB
# Experiment: K-NN Classification using Iris Dataset
# ============================================================

# Import required libraries

# pandas is used for handling the dataset
import pandas as pd

# Load the Iris dataset from sklearn
from sklearn.datasets import load_iris

# Used to divide the dataset into training and testing data
from sklearn.model_selection import train_test_split

# K-Nearest Neighbors classification algorithm
from sklearn.neighbors import KNeighborsClassifier

# Used to calculate the classification accuracy
from sklearn.metrics import accuracy_score


# ------------------------------------------------------------
# 1. LOAD THE IRIS DATASET
# ------------------------------------------------------------

# Load the built-in Iris dataset
iris = load_iris()


# ------------------------------------------------------------
# 2. CREATE A DATAFRAME
# ------------------------------------------------------------

# Convert the feature data into a Pandas DataFrame.
#
# Iris dataset contains four features:
# 1. Sepal Length
# 2. Sepal Width
# 3. Petal Length
# 4. Petal Width

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

# Add the target/species column to the DataFrame.
df["Species"] = iris.target


# Display the first five records
print("First five records of Iris dataset:")
print(df.head())


# ------------------------------------------------------------
# 3. SEPARATE FEATURES AND TARGET
# ------------------------------------------------------------

# X contains the input features used by the model.
#
# These four measurements are used to predict the
# species of the Iris flower.

X = iris.data


# y contains the target/output.
#
# The target represents the species of the Iris flower.
#
# 0 -> Setosa
# 1 -> Versicolor
# 2 -> Virginica

y = iris.target


# ------------------------------------------------------------
# 4. SPLIT THE DATASET INTO TRAINING AND TESTING DATA
# ------------------------------------------------------------

# We use 70% of the data for training
# and 30% for testing.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)


# Display the number of records in training and testing data
print("\nTraining data size:", len(X_train))
print("Testing data size:", len(X_test))


# ------------------------------------------------------------
# 5. CREATE THE K-NN CLASSIFICATION MODEL
# ------------------------------------------------------------

# Create a K-Nearest Neighbors classifier.
#
# n_neighbors=3 means k = 3.
#
# For each new flower, the algorithm looks at the
# 3 nearest training examples and predicts the class
# based on their majority class.

knn = KNeighborsClassifier(n_neighbors=3)


# ------------------------------------------------------------
# 6. TRAIN THE MODEL
# ------------------------------------------------------------

# Train the K-NN model using the training data.

knn.fit(X_train, y_train)


# ------------------------------------------------------------
# 7. MAKE PREDICTIONS
# ------------------------------------------------------------

# Use the trained model to predict the species
# of flowers in the test dataset.

y_pred = knn.predict(X_test)


# ------------------------------------------------------------
# 8. CALCULATE CLASSIFICATION ACCURACY
# ------------------------------------------------------------

# Compare the actual species (y_test)
# with the predicted species (y_pred).

accuracy = accuracy_score(y_test, y_pred)


# Display the classification accuracy
print("\nClassification Accuracy:", accuracy)

# Display accuracy as a percentage
print("Classification Accuracy: {:.2f}%".format(accuracy * 100))

