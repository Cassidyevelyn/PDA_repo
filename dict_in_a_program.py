# A dictionary of butterfly species and their scientific names
butterflies = {
    "Monarch": "Danaus plexippus",
    "Swallowtail": "Papilio machaon",
    "Painted Lady": "Vanessa cardui",
    "Blue Morpho": "Morpho peleides"
}

# A function that takes a dictionary as input and prints each key-value pair
def print_dict_items(dct):
    for key in dct:  # Iterate over the keys in the dictionary
        value = dct[key]  # Access the value corresponding to the key
        print(key + ": " + str(value))  # Print the key-value pair

# Call the function with the butterflies dictionary
print_dict_items(butterflies)

# Result of the function running:

# Monarch: Danaus plexippus
# Swallowtail: Papilio machaon
# Painted Lady: Vanessa cardui
# Blue Morpho: Morpho peleides

# Dictionaries are used to store key-value pairs in Python.
# In the code above, we have a dictionary called 'butterflies' 
# that maps butterfly species to their scientific names.
# The function 'print_dict_items' iterates through the key-value 
# pairs in a given dictionary and prints them.
# When the function is called with the 'butterflies' dictionary, 
# it prints each butterfly species along with its scientific name.
# Dictionaries are sometimes used for data retrieval based on keys.



