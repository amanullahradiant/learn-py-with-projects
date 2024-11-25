import string
import random 

def genPass():
    string1 = string.ascii_uppercase
    # print(string1)
    string2 = string.ascii_lowercase
    # print(string2)
    string3 = string.digits
    # print(string3)
    string4 = string.punctuation
    # print(string4)

    passLen = int(input("Enter the length of password: \n"))

    accumulatedString = []

    accumulatedString.extend(list(string1))
    accumulatedString.extend(list(string2))
    accumulatedString.extend(list(string3))
    accumulatedString.extend(list(string4))

    # print(accumulatedString)

    random.shuffle(accumulatedString)
    # print(accumulatedString)

    myPass = ("".join(accumulatedString[0:passLen]))

    print(myPass)

genPass()