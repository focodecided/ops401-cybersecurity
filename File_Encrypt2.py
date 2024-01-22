#!/usr/bin/env python3
# Title: Recursive Encryption/Decryption Tool
# Purpose: This script provides a simple command-line interface to encrypt and decrypt files or messages.
#          It can also recursively encrypt or decrypt all files within a specified folder.


# Import cryptology library --> use "pip install cryptography" in the terminal
from cryptography.fernet import Fernet
import sys
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

def encrypt_folder(folderpath):
    for root, dirs, files in os.walk(folderpath):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path)

def decrypt_folder(folderpath):
    for root, dirs, files in os.walk(folderpath):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path)

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
        print("5. Encrypt a folder")
        print("6. Decrypt a folder")
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
        elif choice == "5":
            folderpath = input("Enter the folder path to encrypt: ")
            encrypt_folder(folderpath)
        elif choice == "6":
            folderpath = input("Enter the folder path to decrypt: ")
            decrypt_folder(folderpath)
        elif choice == "0":
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

# Run the menu
menu()
