file_name = 'example.txt'

with open(file_name, 'r') as file:
    text = file.read()

# Count lines
with open(file_name, 'r') as file:
    lines = file.readlines()

line_count = len(lines)
word_count = len(text.split())
char_count = len(text)

print("Number of lines:", line_count)
print("Number of words:", word_count)
print("Number of characters:", char_count)
