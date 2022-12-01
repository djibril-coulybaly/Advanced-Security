# Alphabet string
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Function to encrypt the plaintext
def encrypt_plaintext(plaintext, key):
    # Creating the plaintext matrix
    plaintext_matrix = matrix(plaintext)
    print("--------------------------------------------\n")
    print("Plaintext Matrix: ",plaintext_matrix)

    # Creating the key matrix
    key_matrix = matrix(key)
    print("Key Matrix: ",key_matrix)

    #Creating the ciphertext matrix
    cipher_matrix = multiply_matrix(key_matrix, plaintext_matrix)
    print("Ciphertext Matrix: ",cipher_matrix)

    final_ciphertext = ""

    # Creating the ciphertext using the ciphertext matrix and mod 26
    for i in range(2):
        for j in range(2):
            final_ciphertext += alphabet[cipher_matrix[i][j] % 26]
    return final_ciphertext


# Function to create a 2x2 matrix based on the key/plaintext
def matrix(text):
    # Initializing empty matrix
    init_matrix = [[0, 0],
              [0, 0]]

    # Getting numerical value of letter and add it to the matrix
    for i in range(2):
        for j in range(2):
            init_matrix[i][j] = alphabet.index(text[(i + j) + 1 * i])
    return init_matrix


# Function to create the ciphertext matrix based on the multiplication of the key and plaintext matrix
def multiply_matrix(key_matrix, plaintext_matrix):
    ciphertext_matrix = [[0] * 2 for i in range(2)]

    # Multiplying the two matrices
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ciphertext_matrix[i][j] += key_matrix[i][k] * plaintext_matrix[k][j]
    return ciphertext_matrix


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    response = "Y"
    while response == "Y" or response == "y":
        print("--------------------------------------------")
        print("Hill Cipher Encoder")
        print("--------------------------------------------\n")

        key = str(input("Please enter key: "))
        plaintext = str(input("Please enter plaintext: ")).lower()

        if len(plaintext) != 4 or len(key) != 4:
            print("The plaintext and key must be 4 characters each, please try again!")
        else:
            ciphertext = encrypt_plaintext(plaintext, key)
            print("Encrypted message: ",ciphertext)
            print("\n--------------------------------------------\n")
        response = input("Do you want to encode another text? [Y/N]: ")