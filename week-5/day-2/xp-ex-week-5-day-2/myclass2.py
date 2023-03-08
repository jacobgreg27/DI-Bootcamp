# Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”. 
import random
from myclass import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)

    def train(self):
        output = self.bark()
        print(output)
        self.trained = True
    
    def play(self, *dogs):
        dog_names = [dog.name for dog in dogs]
        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        if self.train == True:
           tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"] 
           trick = random.choice(tricks)
           print(f"{self.name} {trick}")

        else: 
            print(f"{self.name} is not trained yet")   



