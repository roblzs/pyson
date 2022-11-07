import json

data = {"key1": "value1", "key2": "value2", "key3": "value3"}

JSON_data = json.dumps(data)

JSON_dotais = json.loads(JSON_data)

key2 = JSON_dotais["key2"]

print(key2)

print_JSON = json.dumps(data, indent=2, separators=(",", "="))

print(print_JSON)

sort_data = {"id": 1, "name": "value2", "age": 29}

save_JSON = json.dumps(sort_data, sort_keys=True)

with open("sample.json", "w") as outfile:
    outfile.write(save_JSON)

company_data = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

company_JSON = json.loads(company_data)

salary = company_JSON["company"]["employee"]["payble"]["salary"]

print(salary)