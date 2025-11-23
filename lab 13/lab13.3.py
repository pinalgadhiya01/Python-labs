import csv

file_name = 'data.csv'

with open(file_name, 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
