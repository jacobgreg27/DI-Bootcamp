# Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

import random

def roll_dice(num):
    rand_num = random.randint(1, 100)
    if rand_num == num:
        print("Congratulations! You rolled the same number!")
    else:
        print("Better luck next time!")


# Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

import string
import random

def generate_random_string():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(5))

print(generate_random_string())


# Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

from datetime import datetime

def current_date():
    now = datetime.now()
    print("Today's date is", now.strftime("%Y-%m-%d"))
    
current_date()


# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

from datetime import datetime

def time_until_january_1st():
    now = datetime.now()
    january_1st = datetime(now.year + 1, 1, 1)
    time_left = january_1st - now
    print("The 1st of January is in", time_left.days, "days and", time_left.seconds // 3600, "hours.")
    
time_until_january_1st()


# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), 
# then displays a message stating how many minutes the user lived in his life.

from datetime import datetime

def minutes_lived(birthdate):
    now = datetime.now()
    birth = datetime.strptime(birthdate, "%Y-%m-%d")
    delta = now - birth
    minutes = delta.days * 1440 + delta.seconds // 60
    print("You have lived for", minutes, "minutes.")
    
minutes_lived("1990-05-15")


# Exercise 7 : Upcoming Holiday
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.

from datetime import datetime

def upcoming_holiday():
    now = datetime.now()
    holiday = datetime(now.year, 12, 25)
    if holiday < now:
        holiday = holiday.replace(year=now.year + 1)
    time_left = holiday - now
    print("The next holiday is Christmas, which is in", time_left.days, "days and", time_left.seconds // 3600, "hours.")
    
upcoming_holiday()


# Exercise 8 : How Old Are You On Jupiter?
# Instructions
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.

def calculate_age_on_jupiter(age_in_seconds):
    earth_year = 365.25 * 24 * 60 * 60
    mercury_year = 0.2408467 * earth_year
    venus_year = 0.61519726 * earth_year
    mars_year = 1.8808158 * earth_year
    jupiter_year = 11.862615 * earth_year
    saturn_year = 29.447498 * earth_year
    uranus_year = 84.016846 * earth_year
    neptune_year = 164.79132 * earth_year
    
    age_on_earth = age_in_seconds / earth_year
    age_on_jupiter = age_on_earth / jupiter_year
    return age_on_jupiter


# Exercise 9 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. 
# Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.
from faker import Faker

fake = Faker()

users = []

for i in range(1):
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)

print(users)


