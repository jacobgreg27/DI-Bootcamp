# Exercise 1: Cats
# Instructions
# Using this class

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.



class Cat():
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Tom", 2)
cat2 = Cat("Jerry", 3)
cat3 = Cat("Spike", 4)

cats = [cat1, cat2, cat3]

def oldest_cat(cats):
    oldest_age = 0
    oldest_cat = None
    for cat in cats:
        if cat.age > oldest_age:
            oldest_age = cat.age
            oldest_cat = cat
    return oldest_cat
oldest_cat_found = oldest_cat(cats)
print(f"The oldest cat is {oldest_cat_found.name} and is {oldest_cat_found.age}")            




# Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height

      

    def bark(self):
        print(f"{self.name} goes woof !")

    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high !")  


davids_dog = Dog("Rex", 50) 
sarahs_dog = Dog("Teacup", 20)


print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")

davids_dog.bark()
davids_dog.jump()            


print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
            print(f"{davids_dog.name}")

else:
            print(f"{sarahs_dog.name}")  




# Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven 


class Song():
    def __init__(self, lyrics):
         self.lyrics = lyrics

    def sing_me_a_song(self):
         for line in self.lyrics:
              print(line)
stairway =  Song(["There’s a lady who's sure",
                  "all that glitters is gold", 
                  "and she’s buying a stairway to heaven"])   
stairway.sing_me_a_song()           



# Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# # Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to the zoo.")
        else:
            print(f"{new_animal} is already in the zoo.")
    
    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(f"- {animal}")
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")
    
    def sort_animals(self):
        self.animals.sort()
    
    def get_groups(self):
        animal_groups = {}
        for animal in self.animals:
            if animal[0] in animal_groups:
                animal_groups[animal[0]].append(animal)
            else:
                animal_groups[animal[0]] = [animal]
        print("Animals grouped by first letter:")
        for letter, animals in animal_groups.items():
            animal_list = ", ".join(animals)
            print(f"{letter}: {animal_list}")
ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Tiger") # in
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Bear")
ramat_gan_safari.sell_animal("Giraffe") # not in
ramat_gan_safari.add_animal("Gazelle")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()


  