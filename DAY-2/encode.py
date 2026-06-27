import pandas as pd
df=pd.read_csv("encodedata.csv")
print("ORIGINAL DATA")
print(df)
df["gender"]=df["gender"].map({"male":0,"female":1})
print("GENDER ENCODING")
print(df)
df["name"]=pd.factorize(df["name"])[0]
print("NAME ENCODING")
print(df)