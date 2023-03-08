# #Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {2, 5, 7}

my_fav_numbers.update([10], [11])

my_fav_numbers.remove(11)

friend_fav_numbers = {4, 6}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)




# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# answer : tuples cannot be changed and is not mutable. but we could type-cast it to a list, change the list and convert it back into a tuple.




# Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)


list_basket = ["Banana", "Apples", "Oranges", "Blueberries"]

list_basket.remove("Banana")

list_basket.remove("Blueberries")

list_basket.insert(0, "Kiwi")

list_basket.append("Apples")

list_basket = list_basket.count("Apples")

# list_basket = []

print(list_basket)





# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?


# Ans 1/ Basically, floats are decimal numbers while integers are whole numbers with no decimal.

start, step = 1.5, 0.5

stop = 5

sequence = []

current = start
 
while current <= stop:
    sequence.append(current)
    current += step
print(sequence)    

# or we can initialize the list with its values directly as follows

my_little_list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]





# Exercise 5: For Loop
# Instructions
# # Use a for loop to print all numbers from 1 to 20, inclusive.
# # Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.


for i in range(1, 21):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

name = "Jacob"

while True:
    user_name = input("What's your name? ")
    if user_name == name:
        break
    else:
        print("That's not my name.")




# Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

fav_fruits = input("What is your fav fruit(s) with a space between each fruits ?: ")

fav_fruties = fav_fruits.split()

print("Your favourite fruits are: ", fav_fruties)

new_fruits = input("Enter a name of any fruit: ")

if new_fruits in fav_fruties:
    print("You chose one of your favorite fruits! Enjoy! ")
else: 
    print("You chose a new fruit. I hope you enjoy ")



# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

toppings = []
while True:
    topping = input("Enter a topping for your pizza (and/or type 'quit' to stop): ")
    if topping == 'quit':
        break
    toppings.append(topping)

print("Your pizza will have the following toppings:", toppings)

total_price = 10 + 2.5 * len(toppings)
print("The total price for your pizza is $%.2f" % total_price)




# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.


family = []
total_cost = 0

while True:
    age = int(input("Enter the age of a person in the family or (0 to stop): "))
    if age == 0:
        break
    family.append(age)

for age in family:
    if age < 3:
        print("The ticket is free.")
    elif age >= 3 and age <= 12:
        print("The ticket is $10.")
        total_cost += 10
    else:
        print("The ticket is $15.")
        total_cost += 15

print("The total cost for the family's tickets is $%d." % total_cost)


# Exercise 10 : Sandwich Orders
# Instructions
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.




sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

finished_sandwiches = []

for sandwich in sandwich_orders:
    finished_sandwich = sandwich
    finished_sandwiches.append(sandwich)
    print("I made your " + finished_sandwich)
print("All sandwiches made : " + str(finished_sandwiches))    

      


# Exercise 11 : Sandwich Orders#2
# Instructions
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.


sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

while True:
    sandwich_orders.count("Pastrami sandwich") < 3
    sandwich_orders.append("Pastrami sandwich")

    # had some difficulties with that last one :/


    
