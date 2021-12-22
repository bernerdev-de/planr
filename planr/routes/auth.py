import datetime
from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from fastapi_jwt import JwtAccessBearer, JwtAuthorizationCredentials, JwtRefreshBearer
import pydantic
from planr.orm.models import User
from planr.utils.functions import check_hash

router = APIRouter()

access_security = JwtAccessBearer(
    secret_key="secret_key",
    auto_error=False,
    access_expires_delta=datetime.timedelta(days=1),
)

refresh_security = JwtRefreshBearer(
    secret_key="secret_key",
    auto_error=True,  # automatically raise HTTPException: HTTP_401_UNAUTHORIZED
)


class LoginData(pydantic.BaseModel):
    username: str = None
    email: str = None
    password: str


@router.post("/login")
async def login(login: LoginData) -> dict:
    if not login.username and not login.email:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY, "username or email is required"
        )
    user = (
        await User.filter(email=login.email).first()
        or await User.filter(username=login.username).first()
    )
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "wrong username")
    password_matches: bool = check_hash(login.password, user.password)
    if not password_matches:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "wrong password")
    payload = {"username": user.username, "id": user.id}
    return {
        "access_token": access_security.create_access_token(payload),
        "refresh_token": refresh_security.create_refresh_token(payload),
        "expires_in": int(access_security.access_expires_delta.total_seconds()),
    }


@router.get("/me")
async def me(credentials: JwtAuthorizationCredentials = Depends(access_security)):
    return credentials.subject


@router.post("/refresh")
async def refresh(credentials: JwtAuthorizationCredentials = Depends(refresh_security)):
    return {
        "access_token": access_security.create_access_token(credentials.subject),
        "expires_in": int(access_security.access_expires_delta.total_seconds()),
    }
