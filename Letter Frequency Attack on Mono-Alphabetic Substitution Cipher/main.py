import sys

# Function to perform a letter frequency attack on a mono-alphabetic substitution cipher
def wordFrequency(ciphertext, ciphertextLength):
    plaintext = [None] * 5
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    letterFrequency = [0] * 26
    letterFrequencySorted = [None] * 26
    usedAlphabet = [0] * 26

    # Counting the frequency of each letter
    for i in range(ciphertextLength):
        if ciphertext[i] != ' ':
            letterFrequency[ord(ciphertext[i]) - 65] += 1

    print("\n--------------------------------------------------------")
    print("Calculating Word Frequency")
    for letter in range(len(alphabet)):
        print(alphabet[letter], ": ", letterFrequency[letter])

    print("--------------------------------------------------------\n")

    # Making a copy of the letter frequency list to sort it
    for i in range(26):
        letterFrequencySorted[i] = letterFrequency[i]

    # Letters by frequency of appearance in English
    T = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    # Sort the copied letter frequency list in descending order
    letterFrequencySorted.sort(reverse=True)

    # Finding the top 5 possible plaintext
    for i in range(5):
        match = -1

        for j in range(26):
            if letterFrequencySorted[i] == letterFrequency[j] and usedAlphabet[j] == 0:
                usedAlphabet[j] = 1
                match = j
                break

        if match == -1:
            break

        numLetterEquivalent = ord(T[i]) - 65
        numLetterEquivalent = numLetterEquivalent - match
        tempString = ""

        for index in range(ciphertextLength):
            if ciphertext[index] == ' ':
                tempString += " "
                continue

            # Shift letter of the cipher
            shiftLetter = ord(ciphertext[index]) - 65
            shiftLetter += numLetterEquivalent

            if shiftLetter < 0:
                shiftLetter += 26
            if shiftLetter > 25:
                shiftLetter -= 26

            tempString += chr(shiftLetter + 65)

        plaintext[i] = tempString

    return plaintext


# Function to end the program
def end_program():
    sys.exit("The program has ended gracefully!")


# Function to display the top 5 possible plaintext
def showPossiblePlaintext(plaintext):
    print("\n--------------------------------------------------------")
    print("Top 5 possible plaintexts")
    for i in range(5):
        print(plaintext[i])
    print("--------------------------------------------------------\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("--------------------------------------------------------")
    print("Letter Frequency Attack on Mono-Alphabetic Substitution Cipher ")
    print("--------------------------------------------------------\n")

    choice = "A"
    possible_plaintext = [None] * 5

    while choice != "E" or choice != "e":
        choice = input("""A: Enter Cipertext
P: List the Top 5 Possible Plaintexts   
E: End Program  
Please enter your choice: """)

        if choice == "A" or choice == "a":
            ciphertext = input("Enter the text :")
            ciphertextLength = len(ciphertext)
            possible_plaintext = wordFrequency(ciphertext.upper(), ciphertextLength)
        elif choice == "P" or choice == "p":
            if possible_plaintext is None:
                print("Please enter a ciphertext first before selecting this option")
            else:
                showPossiblePlaintext(possible_plaintext)
        elif choice == "E" or choice == "e":
            end_program()
        else:
            print("\n--------------------------------------------------------")
            print("You must only select either A, K, D or E")
            print("Please try again")
            print("--------------------------------------------------------\n")
