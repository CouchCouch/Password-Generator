import random
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from getpass import getpass

alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
symbols = "!@#$%-_"

def check_salt():
    """Checks if salt.txt.encrypted exists, if it does it returns the salt, if not it creates it and returns the salt."""
    if os.path.exists('salt.txt.encrypted'):
        with open('salt.txt.encrypted', 'rb') as f:
            for line in f:
                if line != "":
                    return line
                else:
                    salt = os.urandom(16)
                    with open('salt.txt.encrypted', 'ab') as f:
                        f.write(salt)
                    return salt
    else:
        salt = os.urandom(16)
        with open('salt.txt.encrypted', 'ab') as f:
            f.write(salt)
        return salt

def generate(length: int):
    """Generates a password based on the length given."""
    password = ""
    for i in range(int(length)):
        r = random.randint(0,length)
        if r%5 == 1:
            password += random.choice(symbols)
        elif r%4 == 1:
            password += random.choice(numbers)
        elif r%2 == 1:
            password += random.choice(alphabet).upper()
        else:
            password += random.choice(alphabet)
    return password

def encrypt(password:str, lock:str):
    """Encrypts the password to save with the encryption password given. Returns True if successful."""
    dLock = lock.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=check_salt(),
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(dLock))
    name = input("What is the password for?\n")
    name += (f": {password}")
    encoded = name.encode()

    f = Fernet(key)
    encrypted = f.encrypt(encoded)

    with open('passwords.txt.encrypted', 'ab') as f:
        f.write(encrypted + b'\n')
    return True

def decrypt(password:str):
    """Decrypts the passwords.txt.encrypted file with the password. Returns a list of the passwords"""
    dLock = password.encode()

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=check_salt(),
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(dLock))

    decrypted_passwords = []
    with open('passwords.txt.encrypted', 'rb') as f:
        for line in f:
            fernet = Fernet(key)
            decrypted = fernet.decrypt(line)
            decrypted_passwords.append(decrypted.decode())
        return decrypted_passwords

def main():
    choice = input("Generate Password or decrypt?\n")
    if choice.lower() == "generate" or choice.lower() == "g":
        length = input("Length of password?\n")
        while(length.isnumeric() == False):
            print("Please enter a number.")
            length = input("Length of password?\n")
        password = generate(int(length))
        print(f"Your password is:\n{password}")
        enc = input("Would you like to encrypt your password?(y/n)\n")
        if enc.lower() == "yes" or enc.lower() == "y":
            if encrypt(password,getpass("Enter your password to encrypt the file.\n")):
                print("Your password has been encrypted and saved to passwords.txt.encrypted")
    elif choice.lower() == "decrypt" or choice.lower() == "d":
        try:
            passwords = (decrypt(getpass("Enter your password to decrypt the file.\n")))
            for p in passwords:
                print(p)
        except:
            print("Incorrect password.")
    elif choice.lower() == "save" or choice.lower() == "s":
        password = getpass("What is the password?\n")
        print(encrypt(password,getpass("Enter your password to encrypt the file.\n")))

if __name__ == '__main__':
    main()