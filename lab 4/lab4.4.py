my_list = [2,3,2,5,3,2,6]

frequency = {}
for item in my_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Frequency of elements in the list:",frequency)
