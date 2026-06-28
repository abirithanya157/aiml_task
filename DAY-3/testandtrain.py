import pandas as pd
from sklearn.model_selection import train_test_split
df=pd.read_csv("data2.csv")
df["gender"]=df["gender"].map({"male":0,"female":1})
X=df[["gender"]]
y=df["salary"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print("Training input(X_train)")
print(X_train)
print("\nTraining input(y_train)")
print(y_train)
print("Training input(X_test)")
print(X_test)
print("Training input(y_test)")
print(y_test)
