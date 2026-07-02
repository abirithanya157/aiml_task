import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
data = {
    "Hours": [1,2,3,4,5,6,7,8,2,5],
    "Attendance": [50,55,60,70,75,80,90,95,65,85],
    "Assignments": [1,2,3,4,5,5,6,7,2,6],
    "Result": ["Fail","Fail","Fail","Pass","Pass","Pass","Pass","Pass","Fail","Pass"]
}
df = pd.DataFrame(data)
X = df[["Hours", "Attendance", "Assignments"]]
y = df["Result"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy :", accuracy)
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
new_student = pd.DataFrame({
    "Hours": [5],
    "Attendance": [82],
    "Assignments": [5]
})
prediction = model.predict(new_student)
print("\nPrediction :", prediction[0])