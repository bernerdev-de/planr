import string, random
import bcrypt
import os
import dotenv
dotenv.load_dotenv()
# function that generates a password
def generate_password(length=8, chars=string.ascii_letters + string.digits):
    return "".join(random.choice(chars) for _ in range(length))


# function that generates a hash
def generate_hash(password) -> bytes:
    return bcrypt.hashpw(
        password.encode("utf-8") + os.getenv("pepper").encode("utf-8"), bcrypt.gensalt()
    ).decode("utf-8")

# function that checks the password against the hash
def check_hash(password: str, hash_pwd: str) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8") + os.getenv("pepper").encode("utf-8"), hash_pwd.encode("utf-8")
    )