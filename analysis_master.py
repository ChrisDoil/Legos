import pandas
import json
import requests

import pandas as pd

print("hello")

res = requests.get("https://rebrickable.com/api/v3/lego/colors/?key=a33b0190e72500634fa56d408e217d12")

print(res.headers)

j = res.json()

filename = 'temp.csv'
df = pd.DataFrame(j['results'])

print(df.head())
print()

df.to_csv(filename)