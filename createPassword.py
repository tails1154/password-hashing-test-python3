print("Loading Modules")
import hashlib
print("Loaded Modules!")
print("Welcome to tails1154 Password hashing test!")
passwordHashed=hashlib.sha256(input("Enter a password:").encode()).hexdigest()
f = open("password.txt", "w")
f.write(str(passwordHashed))
