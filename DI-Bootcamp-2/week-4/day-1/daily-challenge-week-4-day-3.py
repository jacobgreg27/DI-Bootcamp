# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }

# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}


word = input("Enter a word ! ")

your_word = {}

for keys, index in enumerate(word):
    if index in your_word:
        your_word[index].append(keys)
    else:
        your_word[index] = [keys]    
print(your_word)





# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.


items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = int(input("Wallet Amount ?: "))

# ----------------------------------------------------------------------
items_purchase = {item: int(price[1:]) for item, price in items_purchase.items()}

affordable_items = [item for item, price in items_purchase.items() if price <= wallet]


if affordable_items:
    affordable_items.sort()
# ----------------------------------------------------------------------
    print("Affordable items:", ", ".join(affordable_items))
else:
    print("nOtHiNg :/ ")    