from tortoise.validators import Validator
import re

email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

class EmailValidator(Validator):
    def __call__(self, value: str):
        if not re.match(email_regex, value):
            return "Invalid email address"