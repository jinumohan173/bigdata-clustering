import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


def Generate():

    password_provided = "password1234" # This is input in the form of a string
    password = password_provided.encode() # Convert to type bytes
    salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
    file = open('key.key', 'wb')
    file.write(key)  # The key is type bytes still
    file.close()
    print("key genrating")


def Encrypt():

    input_file = 'cluster.txt'
    output_file = 'cluster.encrypted'

    with open(input_file, 'rb') as f:
        data = f.read()
    file = open('key.key', 'rb')
    key2 = file.read()  # The key will be type bytes
    file.close()
    fernet = Fernet(key2)
    encrypted = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)

    print("encrypting")


def Decrypt():
    file = open('key.key', 'rb')
    key = file.read()  # The key will be type bytes
    file.close()

    input_file1 = 'cluster.encrypted'
    output_file1 = 'cluster.txt'

    with open(input_file1, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

    with open(output_file1, 'wb') as f:
        f.write(encrypted)
    print("decrytping")

#Generate()
#Encrypt()
#Decrypt()