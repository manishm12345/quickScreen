from cryptography.fernet import Fernet
import os.path
from os import path
from simplecrypt import encrypt, decrypt

from Crypto.Cipher import XOR
import base64

password_key = 'Trutech1'


def encrypt(plaintext):
    cipher = XOR.new(password_key)
    return base64.b64encode(cipher.encrypt(plaintext)).decode()


def decrypt(ciphertext):
    cipher = XOR.new(password_key)
    return cipher.decrypt(base64.b64decode(ciphertext)).decode()


'''
def simple_encryption(string_to_encrypt):
    return encrypt(password_key, string_to_encrypt)


def simple_decryption(string_to_decrypt):
    return decrypt(password_key, string_to_decrypt)

DEPRICATED COMPLEX ENCRYPTION DECRYPTION CODE

# Create an encryption for storing mobile number of user
def return_encryption_key():

    # check if a key already exists in the program
    if path.exists("encryption.key"):
        file = open('encryption.key', 'rb')
        key = file.read()  # The key will be type bytes
        file.close()
    else:
        key = Fernet.generate_key()
        file = open('encryption.key', 'wb')
        file.write(key)  # The key is type bytes still
        file.close()

    fern = Fernet(key)

    return fern


# Code that encrypts the data
def encrypt_data(string_to_encrypt):
    fern_key = return_encryption_key()
    return fern_key.encrypt(string_to_encrypt.encode())


# Code that decrypts the data
def decrypt_data(string_to_decrypt):
    fern_key = return_encryption_key()
    return fern_key.encrypt(string_to_decrypt)
'''