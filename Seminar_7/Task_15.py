"""Чтение CSV в словарь"""

import csv
with open('for_task14.csv', 'r', newline='') as f:
  csv_file = csv.DictReader(f, fieldnames=["name", "sex",
"age", "height", "weight", "office"], restkey="new", restval="Main Office", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
  for line in csv_file:
    print(f'{line = }')
  print(f'{line["name"] = }\t{line["age"] = }')