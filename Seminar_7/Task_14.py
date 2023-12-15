import csv
with open('for_task14.csv', 'r', newline = '') as f:
  csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
  for line in csv_file:
    print(line)
  print(type (line))