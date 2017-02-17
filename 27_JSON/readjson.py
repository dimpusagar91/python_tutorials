import json
json_data = open("colors.json")
data = json.load(json_data)
print(data.keys())
