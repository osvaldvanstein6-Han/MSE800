import pandas as pd
ds = pd.read_csv("dataset1.csv", header=None)
print(ds)

sum_row = ds.sum(axis=1)
avg_row = ds.mean(axis=1)

sum_col = ds.sum()
avg_col = ds.mean()

ds["sum_row"] = sum_row
ds["avg_row"] = avg_row
ds.loc["sum"] = sum_col
ds.loc["avg"] = avg_col

print(ds)
ds.to_csv("dateset_result.csv")