# AI Project 2 - Data Classification Using AI

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Loading the dataset
iris = load_iris()

# Features and target values
X = iris.data
y = iris.target

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Creating the classification model
classifier = DecisionTreeClassifier()

# Training the model
classifier.fit(X_train, y_train)

# Making predictions
predictions = classifier.predict(X_test)

# Checking accuracy
accuracy = accuracy_score(y_test, predictions)

print("\n===== AI Classification Project =====")
print(f"Model Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Testing with a sample flower
sample_flower = [[5.1, 3.5, 1.4, 0.2]]

result = classifier.predict(sample_flower)

flower_names = iris.target_names

print("\nSample Prediction:")
print("Predicted Flower Type:", flower_names[result[0]])
