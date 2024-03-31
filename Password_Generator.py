import string
import random

def generate_password(passlength):
    s=list(string.ascii_letters+string.digits+string.punctuation)
    random.shuffle(s)
    password = "".join(s[:passlength])
    return password

passlength = int(input("Enter the length of the password: "))
print(f"The generated password is \"{generate_password(passlength)}\"")