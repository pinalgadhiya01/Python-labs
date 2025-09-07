def multiply_list_items(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result 

my_list = [2, 3, 4, 5]
product = multiply_list_items(my_list)
print("The product of all items in the list is:", product)
