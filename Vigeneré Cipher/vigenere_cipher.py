import sys


def main():
    menu()


def menu():
    key_index_dict = create_index_dict()
    table = create_table()

    print("------------------------------------------------")
    print("Vigenere Cipher Demonstration")
    print("------------------------------------------------\n")

    choice = input("""A: Add Plaintext, Key and Display Cipertext 
E: End Program  
Please enter your choice: """)

    if choice == "A" or choice == "a":
        print("\n------------------------------------------------")
        plaintext = input("Please enter the plaintext you wish to encrypt: ")
        key = input("Please enter the key value you wish to use: ")
        ciphertext = display_ciphertext(key_index_dict, table, plaintext, key)
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


def create_row():
    row = []
    for i in range(ord('A'), ord('Z') + 1):
        row.append(chr(i))
    for i in range(ord('a'), ord('z') + 1):
        row.append(chr(i))
    for i in range(ord('0'), ord('9') + 1):
        row.append(chr(i))
    row.append(' ')
    return row


def create_index_dict():
    index_map = {}
    index = 0
    for c in create_row():
        index_map[c] = index
        index += 1
    return index_map


def create_table():
    table = []
    row = create_row()
    length = len(row)
    for i in range(length):
        r = row[i:] + row[:i]
        table.append(r)
    return table


def display_ciphertext(key_index_dict, table, p, k):
    finalCiphertext = []
    count = 0
    for i in p:
        indexOfKey = k[count % len(k)]
        text_index = key_index_dict[i]
        key_index = key_index_dict[indexOfKey]
        finalCiphertext.append(table[text_index][key_index])
        count += 1
    return "".join(finalCiphertext)


def end_program():
    sys.exit("The program has ended gracefully!")


# the program is initiated, so to speak, here
main()
