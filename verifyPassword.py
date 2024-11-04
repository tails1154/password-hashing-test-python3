print("Importing Modules")
import hashlib
print("Loaded Modules!")
print("Welcome to verifyPassword.py!")
print("This will NOT work if you have not ran createPassword.py and let it create password.txt!")
print("\n\n\n\n\n\n\n\n")
print("Loading password.txt...")
f = open("password.txt", "r")
print("Storing password.txt in RAM...")
print("and no, your password is not in plain text")
password=f.read()
text=input("Enter your password:")
print("Creating sha256 hash for your input....")
hash=hashlib.sha256(text.encode()).hexdigest()
print("Checking password hash...")
if password == hash:
	print("Password check passed!")
else:
	print("Password check failed!")
