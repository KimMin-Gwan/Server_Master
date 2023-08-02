import json

with open("./json_data_test.json", 'r', encoding="UTF-8") as f:
    data = json.load(f)
    print(data)