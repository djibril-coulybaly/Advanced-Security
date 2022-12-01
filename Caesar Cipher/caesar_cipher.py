import sys


def main():
    menu()


def menu():
    print("------------------------------------------------")
    print("Caesar Cipher Demonstration")
    print("------------------------------------------------\n")

    choice = input("""A: Add Plaintext, Key and Display Cipertext 
E: End Program  
Please enter your choice: """)

    if choice == "A" or choice == "a":
        print("\n------------------------------------------------")
        plaintext = input("Please enter the plaintext you wish to encrypt: ")
        key = int(input("Please enter the key value you wish to use: "))
        ciphertext = display_ciphertext(plaintext, key)
        print("\n------------------------------------------------")
        print("Plaintext: ", plaintext)
        print("Key: ", key)
        print("Ciphertext: ", ciphertext)
        print()
        menu()
    elif choice == "E" or choice == "e":
        end_program()
    else:
        print("\n------------------------------------------------")
        print("You must only select either A, K, D or E")
        print("Please try again")
        print("------------------------------------------------\n")
        menu()


def display_ciphertext(p, k):
    finalCiphertext = ""
    for i in range(len(p)):
        charOfPlaintext = p[i]
        if charOfPlaintext == " ":
            finalCiphertext += ' '
        elif charOfPlaintext.isupper():
            finalCiphertext += chr((ord(charOfPlaintext) + k - 65) % 26 + 65)
        else:
            finalCiphertext += chr((ord(charOfPlaintext) + k - 97) % 26 + 97)
    return finalCiphertext


def end_program():
    sys.exit("The program has ended gracefully!")


# the program is initiated, so to speak, here
main()
