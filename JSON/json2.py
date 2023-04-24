import json

json_string = '{"first_name": "Bruno", "Last_name": "Salles"}'


## json para dicionario
json_dict = json.loads(json_string)
print(json_dict)
