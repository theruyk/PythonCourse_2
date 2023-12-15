import csv
with open('for_task13.csv', 'r', newline='') as f:
  csv_file = csv. reader (f)
  for line in csv_file:
    print (line)
  print (type(line))