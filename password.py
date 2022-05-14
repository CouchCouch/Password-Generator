import random
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
symbols = "!@#$%-_"
password = ""

def generate(length):
    for i in range(int(length)):
        if i%5 == 1:
            password += random.choice(symbols)
        elif i%4 == 1:
            password += random.choice(numbers)
        elif i%2 == 1:
            password += random.choice(alphabet).upper()
        else:
            password += random.choice(alphabet)
    print(f"Your password is:\n{password}")

def encrypt(password,lock):
    dLock = lock.encode()
    salt = b'\xf2\x10DQ\x80\xe4\x1d`<\xdaJ\xf9\x98h\x1c\xc0Kw\x91\xe3=\xe8\x82y\xb8\xc4\xb4\x16>\xc1?\xd8'

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(dLock))
    name = input("What website is the password for?\n")
    name += (f": {password}")
    encoded = name.encode()

    f = Fernet(key)
    global encrypted
    encrypted = f.encrypt(encoded)

    with open('passwords.txt.encrypted', 'ab') as f:
        f.write(encrypted + b'\n')
    print("Your password has been encrypted and saved to passwords.txt.encrypted")

def decrypt(key):
    with open('passwords.txt.encrypted', 'rb') as f:
        for line in f:
            fernet = Fernet(key)
            decrypted = fernet.decrypt(line)
            print(decrypted.decode())

choice = input("Generate Password(g) or decrypt(d)?\n")

if choice.lower() == "generate" or "g":
    length = input("Length of password?\n")
    generate()
    enc = input("Would you like to encrypt your password?/n")
    if enc.lower() == "yes":
        encrypt(password,input("Enter your password to encrypt the file.\n"))
elif choice.lower() == "decrypt" or "d":
    decrypt(input("Enter your password to decrypt the file.\n"))
else:
    print("please chose a valid option")
