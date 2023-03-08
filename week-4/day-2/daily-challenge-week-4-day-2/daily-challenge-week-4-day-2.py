# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]


num = int(input("Do enter a number, please ! "))

length = int(input("Do enter a length"))


multiple_list = []

multiple = num

while len(multiple_list) < length:
      multiple_list.append(multiple)
      multiple += num
      print(multiple_list)




# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"     

word = str(input("Enter a word"))

p = ""

for x in word:
    if x not in p:
       p = p + x
print(p)