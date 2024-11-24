""" 
multi line comments
is necessary to learn 
in python
"""

# take imput from the keyboard
# Taking input
takenInput = input("Please type a number: ")

# Checking the data type
print("Data type of your input: ", type(takenInput))

# Converting the input to a number
try:
    # Attempt to convert to integer first
    convertedNum = int(takenInput)
    print("Converted to integer:", convertedNum)
except ValueError:
    try:
        # If conversion to integer fails, try to convert to float
        convertedNum = float(takenInput)
        print("Converted to float:", convertedNum)
    except ValueError:
        print("Error: The input is not a valid number.")


"""
[List]
(Tuples)
{Set}
{"brand": "Ford", model: "Mustang"} Dictionary
"""


# list -> Array (in js)
fruitsList = ["apples", "banana", "berry", "coconut", "chachew"]
print(fruitsList[1])


# Tuples
fruitsTuple = ("apples", "banana", "berry", "coconut", "chachew")
print(type(fruitsTuple))
print(fruitsTuple[1])

# set
fruitsSet = {"apples", "banana", "berry", "coconut", "chachew"}
print(type(fruitsSet))
print(fruitsSet)
