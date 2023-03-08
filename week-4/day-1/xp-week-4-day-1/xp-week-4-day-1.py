# ex1
print("Hello World\n" *4)

# ex2
print((99**3)*8)

# ex3
# 5 < 3

# # false

# 3 == 3

# #  true

# 3 == "3"

# # false

# # "3" > 3

# # false

# "Hello" == "hello"

# # false


# ex4
computer_brand = "Hauwei"

print("I have a " + computer_brand + " computer")


#ex5
name = "Jacob"

age = 19

shoe_size = 42

info = "I am " + name +  "and I am " + str(age) + "years old. " "The European scale for my shoe size is " + str(shoe_size) 

print(info)


# ex6
a = 4
b = 2

if a > b: 
    print("Hello World")

# ex7
num = int(input('What is your lucky number ?: '))

if (num % 2) == 0:
    print("Seem like your number is even")

else: print("Seems like your number is odd")




# ex8
name = input("What is your name ?: ")

if (name == "Jacob"):
 print("Hey, you stole my name")

else: print("Sorry, I am looking for someone with the same name as me")



# ex9
height_inch = int(input("What is your height in inches, please ?: "))

height_cm = (height_inch * 2.54)

if (height_cm > 145):
 print("Tall enough to ride")

else: print("grow some more to ride")