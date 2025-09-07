def count_digits(number):
    count = 0
    while number != 0:
        number //= 10 
        count += 1
    return count

num = int(input("Enter a number: "))
if num == 0:
    print("Number of digits: 1")
else:
    print("Number of digits:", count_digits(abs(num)))  
