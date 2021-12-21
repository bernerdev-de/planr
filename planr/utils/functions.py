import string, random

# function that generates a password
def generate_password(length=8, chars=string.ascii_letters + string.digits):
    return "".join(random.choice(chars) for _ in range(length))
