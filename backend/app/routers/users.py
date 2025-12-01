# backend/app/routers/users.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db
from ..deps import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=schemas.UserOut)
def read_me(current_user: models.User = Depends(get_current_user)):
    return current_user
