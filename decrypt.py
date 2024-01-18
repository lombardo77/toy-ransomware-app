#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
from art import *


with open("key.txt", "rb") as k:
	key = k.read()

files = []

for f in os.listdir():
	if f == "key.txt" or "encrypt.py" in f or "decrypt.py" in f or f == "README.txt" or f =="reset.sh":
		pass
	else:
		files.append(f)	

for f in files:
	with open(f, "rb") as thefile:
		contents = thefile.read()
	decrypted_contents = Fernet(key).decrypt(contents)
	with open(f, "wb") as thefile:
		thefile.write(decrypted_contents)
os.remove("README.txt")

fon = "cybermedium"
tprint("Your files", font = fon)
tprint("have been", font = fon)
tprint("decrypted", font = fon)
