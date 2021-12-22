from planr.orm import init
from planr.orm.models import User
from planr.utils.functions import generate_hash
import os
from PyInquirer import prompt
import asyncio
import re
import logging
import tortoise
from dotenv import load_dotenv
load_dotenv()

email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

clear = lambda: os.system("clear")
logging.basicConfig(
    level=logging.INFO,
    filename="planr.log",
    filemode="a",
    encoding="utf-8",
    format="%(asctime)s -  [%(name)s] %(levelname)s: %(message)s",
)
logger = logging.getLogger("planr.manage")


class Database:
    @staticmethod
    async def init() -> None:
        try:
            await init()
            demo_user = await User.filter(email="demo@demo.demo").first()
            if demo_user:
                raise tortoise.exceptions.IntegrityError
            password = generate_hash("demo")
            demo = User(
                email="demo@demo.demo",
                username="demo",
                name="Demo",
                password=password,
                is_admin=True,
            )
            await demo.save()
            print("✔️ | Done")
        except tortoise.exceptions.IntegrityError:
            print("✔️ | Done")
        # asyncio.run(Tortoise.close_connections())

    @staticmethod
    async def user() -> None:
        await init()
        clear()
        print("Creating user \n")
        questions = [
            {
                "type": "input",
                "name": "name",
                "message": "Full Name: ",
                "filter": lambda val: str(val),
            },
            {
                "type": "input",
                "name": "username",
                "message": "Username: ",
                "filter": lambda val: str(val),
            },
            {
                "type": "input",
                "name": "email",
                "message": "Email: ",
                "validate": lambda val: re.match(email_regex, val) is not None,
            },
            {
                "type": "password",
                "name": "password",
                "message": "Password: ",
                "filter": lambda val: str(val),
            },
            {
                "type": "confirm",
                "name": "admin",
                "message": "Is this user an admin?",
                "default": False,
            },
        ]
        answers = prompt(questions)
        password = generate_hash(answers["password"])
        user = User(
            name=answers["name"],
            username=answers["username"],
            email=answers["email"],
            password=password,
            is_admin=answers["admin"],
        )
        await user.save()

    class Proxy:
        @staticmethod
        def user() -> None:
            asyncio.run(Database.user())

        @staticmethod
        def init() -> None:
            asyncio.run(Database.init())
