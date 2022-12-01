<div align="center">
  <h1>Advanced Security</h1>
</div>

<!-- Table of Contents -->

## :notebook_with_decorative_cover: Table of Contents

- [Introduction](#introduction)
- [Applications](#closed_lock_with_key-applications)
  - [AES Algorithm](#one-aes-algorithm)
  - [Caesar Cipher](#two-caesar-cipher)
  - [Calculator](#three-calculator)
  - [Hill Cipher](#four-hill-cipher)
  - [Letter Frequency Attack on Mono-Alphabetic Substitution Cipher ](#five-letter-frequency-attack-on-mono-alphabetic-substitution-cipher)
  - [Miller-Rabin Algorithm](#six-miller-rabin-algorithm)
  - [Vigeneré Cipher](#seven-vigeneré-cipher)
- [Getting Started](#toolbox-getting-started)
- [Directory Structure](#file_folder-directory-structure)

---

<!-- Features -->

## Introduction

Implemented various encryption/decryption, number theory and cryptographic applications made using Python

---

<!-- Features -->

## :closed_lock_with_key: Applications

### :one: AES Algorithm

Symmetrical block cipher algorithm that takes plain text in blocks of 128 bits and converts them to ciphertext using keys of 128, 192, and 256 bits.

### :two: Caesar Cipher

Uses a substitution method where letters in the alphabet are shifted by some fixed number of spaces to yield an encoding alphabet

### :three: Calculator

Calculator which is able to perform the following arithmetic:

- Addition
- Subtraction
- Division
- Multiplication

The calculator has a GUI (Graphical User Interface) for ease of use

### :four: Hill Cipher

- Polygraphic substitution cipher based on linear algebra
- Keyword and plaintext turned into key matrix and column vector
- Matrix multiplication modulo the length of the alphabet (i.e. 26) is performed on each vector
- These vectors are then converted back into letters to produce the ciphertext

### :five: Letter Frequency Attack on Mono-Alphabetic Substitution Cipher

- Frequency analysis is one of the known ciphertext attacks. It is based on the study of the frequency of letters or groups of letters in a ciphertext
- Find the difference between i-th maximum occurring letter in the given string and the string T and then shift all the letters of the given string with that difference
- The string obtained will be one of the possible decrypted strings.

### :six: Miller-Rabin Algorithm

Determines whether a given number is likely to be prime

### :seven: Vigeneré Cipher

- Type of polyalphabetic substitution cipher
- Cipher alphabet is changed regularly during the encryption process, making it less vulnerable to cryptanalysis.

---

<!-- Getting Started -->

## :toolbox: Getting Started

**To set up the database:**

1. Open a new command prompt window
2. Redirect to the location of the python file you wish to run
3. Type the following command and press `Enter`:

   ```bash
   python3 name_of_application.py
   ```

---

<!-- Directory Structure -->

## :file_folder: Directory Structure

```
|-- AES Algorithm (Key Expansion)
|   '-- keyExpansionAES.py
|-- Caesar Cipher
|   '-- caesar_cipher.py
|-- Calculator
|   '-- CalculatorApp.py
|-- Hill Cipher
|   '-- main.py
|-- Letter Frequency Attack on Mono-Alphabetic Substitution Cipher
|   '-- main.py
|-- Miller-Rabin Algorithm
|   '-- millerRabinAlgorithm.py
|-- Vigeneré Cipher
|   |-- test.py
|   '-- vigenere_cipher.py
```
