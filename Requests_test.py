import requests as req
import csv
import pandas as p

r = req.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E&for=state:*')

print(r.text)
print(r.json())

with open("commuter_data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(r.json())

commuter_dataframe = p.read_csv("commuter_data.csv")
commuter_dataframe.columns = ['State', 'Commuters', 'Code']
print(commuter_dataframe.head())
