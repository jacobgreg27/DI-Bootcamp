# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.





class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Create another cat breed named Siamese which inherits from the Cat class.
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Create instances of the three cat breeds
bengal = Bengal('Benny', 3)
chartreux = Chartreux('Charlie', 5)
siamese = Siamese('Sami', 2)



# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.

all_cats = [bengal, chartreux, siamese]

# Create a Pets instance with the list of cat instances
sara_pets = Pets(all_cats)

# Call the walk method on the all_pets instance
sara_pets.walk()


# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.


class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"
# we are calculating this first
    def run_speed(self):
        return self.weight / (self.age*10)
    

    def fight(self, other_dog):
# and using it here  
     self_dog = self.weight * self.run_speed()
# and there
     other_dogg = other_dog.weight * other_dog.run_speed()
# and comparing
     if self_dog > other_dogg: 

        return f"{self.name} won the fight!"
     
     else:
        return f"{other_dog.name} won the fight!"

dog1 = Dog("Max", 3, 20)
dog2 = Dog("Buddy", 5, 25)
dog3 = Dog("Rocky", 4, 15)

print(dog1.fight(dog2))  
print(dog2.fight(dog3))  
print(dog3.fight(dog1)) 