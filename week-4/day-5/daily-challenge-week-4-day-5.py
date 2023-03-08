# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world


def sort_words(words):
    words = words.split(',')
    sorted_words = sorted(words)
    sorted_string = ""
    for word in sorted_words:
        sorted_string += word + ","
    return sorted_string[:-1]

input_words = input("Enter a comma-separated sequence of words: ")
sorted_words = sort_words(input_words)
print("Sorted sequence:", sorted_words)
