class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        kwargs['is_child'] = True
        self.members.append(kwargs)
        print(f"Congratulations on the birth of {kwargs['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"{self.last_name}:")
        for member in self.members:
            print(member['name'])

# Create a family
family = Family('Smith', [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
])

# Test the born method
family.born(name='John', age=0, gender='Male')
print(family.members) # should print a list containing 3 dictionaries

# Test the is_18 method
print(family.is_18('Michael')) # should print True
print(family.is_18('John')) # should print False

# Test the family_presentation method
family.family_presentation() # should print "The Smith family members are: Michael Sarah John"





# didnt know how to tackle this part
# class TheIncredibles(Family):
    
#     def use_power(self, name):
#         for member in self.members:
#             if member['name'] == name:
#                 if member['age'] >= 18:
#                     print(f"{name}'s power is: {member['power']}")
#                 else:




