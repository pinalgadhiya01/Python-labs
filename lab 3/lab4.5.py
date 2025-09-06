sentence = input("Enter a sentence: ")

words = sentence.strip().split()

last_word = words[-1]

print("Length of the last word:", len(last_word))
