from tortoise import Tortoise

async def init() -> None:
    await Tortoise.init(
        db_url="postgres://postgres:planrdb@localhost:5432/planr",
        modules={
            "models": ["planr.orm.models"],
        },
    )
    await Tortoise.generate_schemas()