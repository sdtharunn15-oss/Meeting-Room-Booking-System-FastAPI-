from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

SECRET_KEY = "meetingroomsecret"
ALGORITHM = "HS256"


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )


def admin_required(user=Depends(get_current_user)):
    if user.get("role") != "Admin":
        raise HTTPException(
            status_code=403,
            detail="Admins only"
        )
    return user