file1 = 'file1.txt'
file2 = 'file2.txt'
merged_file = 'merged.txt'

with open(merged_file, 'w') as outfile:
    # Read and write contents of file1
    with open(file1, 'r') as f1:
        outfile.write(f1.read())
        outfile.write("\n") 

    # Read and write contents of file2
    with open(file2, 'r') as f2:
        outfile.write(f2.read())

print("Files merged successfully into merged.txt")
