
from typing import Optional, List
from fastapi import Path, Query, Depends, HTTPException
import fastapi
from pydantic_schemas.user import User, UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from .utils.users import create_user, get_user, get_user_by_email, get_users 
from db.db_setup import get_db


router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def index(skip: int = 0, limit:int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip, limit)
    return users



# In the post request we can define path parameters like that: app.post("/users")
@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/users/{id}", response_model=User)
async def show(
    id: int = Path(..., description="The ID of the user"),  # ... means it's required. Called epllepsis (Something like that)
    q: str = Query(None, max_length=5),    # None means optional parameter
    db: Session = Depends(get_db)
):      
    user = get_user(db, id)
    if user is None:
        raise HTTPException(404, "Invalid user id")
    return user