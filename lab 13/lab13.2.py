file_name = 'example.txt'

lines_list = []

with open(file_name, 'r') as file:
    for line in file:
        lines_list.append(line.strip())  

print("List of lines:")
print(lines_list)
