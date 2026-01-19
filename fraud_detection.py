# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset (for demo)
data = {
    'amount': [100, 2000, 150, 3000, 50, 5000],
    'old_balance': [5000, 8000, 2000, 10000, 300, 15000],
    'new_balance': [4900, 6000, 1850, 7000, 250, 10000],
    'is_fraud': [0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Features and target
X = df.drop('is_fraud', axis=1)
y = df['is_fraud']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

print("Logistic Regression Accuracy:",
      accuracy_score(y_test, lr_pred))

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

print("Random Forest Accuracy:",
      accuracy_score(y_test, rf_pred))

# Classification report
print("\nRandom Forest Report:\n",
      classification_report(y_test, rf_pred))
