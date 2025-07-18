import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30]
})
print(df)
# print(json_str)
print(df.to_json(orient="index"))
print(df.to_json(orient="columns"))
print(df.to_json(orient="split"))
print(df.to_json(orient="records"))
print(df.to_json(orient="index"))
print(df.to_json(orient="columns"))
print(df.to_json(orient="values"))
print(df.to_json(orient="table"))
