num = input("Enter a number: ")

negative = False
if num.startswith('-'):
    negative = True
    num = num[1:]

reversed_num = num[::-1] 

if negative:
    reversed_num = '-' + reversed_num

print("Reversed number:", reversed_num)
