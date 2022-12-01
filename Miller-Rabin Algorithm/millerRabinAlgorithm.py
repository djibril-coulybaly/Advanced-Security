# Importing the random module
import random


# Function to test the primality of an integer number
def miller_rabin(number):
    if number < 0 or number % 2 == 0:
        return "inconclusive"

    k, q = find_integers(number - 1)

    a = random.randint(2, number - 2)

    if a ** q % number == 1:
        return "inconclusive"

    for j in range(k):
        if a ** (2 ** j * q) % number == number - 1:
            return "inconclusive"

    return "composite"


# Function to find integers k and q as per the algorithm
def find_integers(number):
    k = 0
    while number % 2 == 0:
        k += 1
        number /= 2
    q = number
    return k, q


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    response = "Y"
    while response == "Y" or response == "y":
        print("--------------------------------------------")
        print("Miller Rabin Algorithm")
        print("--------------------------------------------\n")

        integer = int(input("Please enter an integer: "))

        if not int(integer):
            print("The value entered must be an integer number, please try again!")
        else:
            print("The value", integer, "that you've entered is", miller_rabin(integer))
            print("\n--------------------------------------------\n")
        response = input("Do you want to try another integer? [Y/N]: ")
