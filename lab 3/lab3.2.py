text = input("Enter a string: ")

text = text.lower()

# Reverse the string
reversed_text = text[::-1]

if text == reversed_text:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
