import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "kriptonite.py" or file == "thekey.key" or file == "dekryptonite.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key", "rb") as key_file:
    key = key_file.read()

password = "krypton"

user_input = input("Enter the password to decrypt the files: ")

if user_input == password:
    for file in files:
        with open(file, "rb") as file_object:
            file_data = file_object.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(file_data)

        with open(file, "wb") as file_object:
            file_object.write(decrypted_data)
    print("Files decrypted.")
else:
    print("Incorrect password.")