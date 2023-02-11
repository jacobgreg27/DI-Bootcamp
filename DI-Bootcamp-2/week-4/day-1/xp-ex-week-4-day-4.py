

# -----------------------------ex 1-------------------------------




def display_message():

   print("learning about coding and stuffs")

display_message()


# -----------------------------ex 2 --------------------------------


def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("The Help")    

#------------------------------ex 3 ----------------------------------



def describe_city(city, country = "some unknown places"):
    print(f"{city} is in {country} :) ")
describe_city("California")    


# -----------------------------ex 4------------------------------------
import random

def compare_number(n):

    random_integer = random.randint(1, 100)

    if n == random_integer:
        print("Success, how did you guess the number ?", n)
    else:
        print("You failed, your number is not the same as the random one. Your number :", n, "Generated number :", random_integer)    
    
compare_number(10)    

# ----------------------------ex5--------------------------------------


def make_shirt(size = "L", text = "I love Python"):

    print(f"The size of the shirt is {size} and the text is : '{text}'")

make_shirt()

make_shirt("M")

make_shirt("S", "Stop Reading My Shirt")

make_shirt(size = "XS", text = "Python is more readable")


# -----------------------------ex 6-------------------------------------

def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    for i in range(len(names)):
        names[i] = names[i] + ", the Great"     

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
make_great(magician_names)
show_magicians(magician_names)  


# ------------------------------ex 7 --------------------------------------
import random

def get_random_temp(season):
    if season == "Winter":
        return round(random.randint(-10, 16), 1)
    if season == "Spring":
        return round(random.randint(0, 20), 1)
    if season == "Summer":
        return round(random.randint(20, 40), 1)
    if season == "Autumn":
        return round(random.randint(10, 30), 1)          


def main():

    month = int(input("Enter the number of the month (1 = January, 12 = December): "))
    if month in [12, 1, 2]:
        season = "Winter"
    elif month in [3, 4, 5]:
        season = "Spring"
    elif month in [6, 7, 8]:
        season = "Summer"
    elif month in [9, 10, 11]:
        season = "Autumn"


    temperature = get_random_temp(season)
    
    print(f"The temperature right now is", temperature  ,"degrees Celsius.")

    if temperature < 0:
      print("Brrr, that’s freezing! Wear some extra layers today")
    elif temperature >= 0 and temperature <=16:
      print("Quite chilly! Don’t forget your coat")
    elif temperature > 16 and temperature <= 23:
      print("Let's go breathe in some fresh air !")
    elif temperature >= 23 and temperature <= 32:
      print("Let's go to the beach !")
    elif temperature > 32 and temperature <= 40:  
      print("Very high UV : Stay inside !") 

main()   


#------------------ happy face xd ------------------------


        


