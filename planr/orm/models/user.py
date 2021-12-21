from tortoise import validators
from tortoise.models import Model
from tortoise import fields
from tortoise.validators import Validator
from planr.orm.validators import EmailValidator


class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True, validators=[EmailValidator()])
    username = fields.CharField(max_length=50, unique=True)
    name = fields.CharField(max_length=50)
    password = fields.TextField()
    is_admin = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True)

    class Meta:
        table = "users"
        table_description = "All planr users"
