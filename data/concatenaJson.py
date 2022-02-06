import pandas as pd
import glob, os, json
from pandas.io.json import json_normalize



json_pattern = os.path.join('*.json')
file_list = glob.glob(json_pattern)

dfs = []
for file in file_list:
    with open(file) as f:
        json_data = pd.json_normalize(json.loads(f.read()))
        json_data['site'] = file.rsplit("/", 1)[-1]
    dfs.append(json_data)
df = pd.concat(dfs)
print(df)
df.to_csv("unido.csv")