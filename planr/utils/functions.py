import string, random
import hashlib
import os

# function that generates a password
def generate_password(length=8, chars=string.ascii_letters + string.digits):
    return "".join(random.choice(chars) for _ in range(length))

# function that generates a hash
def generate_hash(password) -> tuple:
    salt: bytes = os.urandom(32)
    return salt, hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1).hex()