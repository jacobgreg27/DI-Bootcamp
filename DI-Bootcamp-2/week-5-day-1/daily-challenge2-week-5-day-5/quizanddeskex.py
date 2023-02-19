# Instructions
# Part 1 : Quizz :
# Answer the following questions

# What is a class?
#  ans : blueprint for objects

# What is an instance?
#  ans : an object based on a class

# What is encapsulation?
#  ans :Encapsulation is a way to restrict the direct access to some components of an object

# What is abstraction?
#  ans :hides all but the relevant data about an object in order to reduce complexity and increase efficiency.


# What is inheritance?
# ans: When a class derives from another class


# What is multiple inheritance?
# ans : an object or class can inherit features from more than one parent object or parent class.


# What is polymorphism?
# ans: allows a specific routine to use variables of different types at different times

# What is method resolution order or MRO?
#ans: the order in which Python looks for a method in a hierarchy of classes. 





# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.


import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                card = Card(suit, value)
                self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop()

