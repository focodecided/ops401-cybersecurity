#Prompt the user to select a mode:
#Encrypt a file (mode 1)
#Decrypt a file (mode 2)
#Encrypt a message (mode 3)
#Decrypt a message (mode 4)
#If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
#If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
#Depending on the selection, perform one of the below functions. You’ll need to create four functions:

#Encrypt the target file if in mode 1.
#Delete the existing target file and replace it entirely with the encrypted version.
#Decrypt the target file if in mode 2.
#Delete the encrypted target file and replace it entirely with the decrypted version.
#Encrypt the string if in mode 3.
#Print the ciphertext to the screen.
#Decrypt the string if in mode 4.
#Print the cleartext to the screen.

#Import cryptology library--> use "pip install cryptography" in the terminal
from cryptography.fernet import Fernet

#Create a menu of options
import sys

from cryptography.fernet import Fernet
import os

# Generate a key. In a real application, you should securely store and manage this key.
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_file(filepath):
    with open(filepath, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)
    print(f"File {filepath} encrypted.")

def decrypt_file(filepath):
    with open(filepath, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(filepath, 'wb') as file:
        file.write(decrypted_data)
    print(f"File {filepath} decrypted.")

def encrypt_message(message):
    encrypted_message = cipher_suite.encrypt(message.encode())
    print(f"Encrypted message: {encrypted_message.decode()}")

def decrypt_message(encrypted_message):
    decrypted_message = cipher_suite.decrypt(encrypted_message.encode())
    print(f"Decrypted message: {decrypted_message.decode()}")

def menu():
    while True:
        print("\nChoose a mode:")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Encrypt a message")
        print("4. Decrypt a message")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            filepath = input("Enter the file path to encrypt: ")
            encrypt_file(filepath)
        elif choice == "2":
            filepath = input("Enter the file path to decrypt: ")
            decrypt_file(filepath)
        elif choice == "3":
            message = input("Enter the message to encrypt: ")
            encrypt_message(message)
        elif choice == "4":
            encrypted_message = input("Enter the encrypted message to decrypt: ")
            decrypt_message(encrypted_message)
        elif choice == "0":
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

# Run the menu
menu()