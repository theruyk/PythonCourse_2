"""Преобразование JSON в Python"""

import json

with open('for_task7.json', 'r', encoding='utf-8') as f:
  json_file = json.load (f)

print (f'{type (json_file) = }\n {json_file = }')
print (f'{json_file["name"] = }')
print (f'{json_file["address"]["geo"] = }')
print (f'{json_file["email"] = }')