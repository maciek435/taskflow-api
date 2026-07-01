from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserResponse, TokenResponse, UserLogin
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from passlib.context import CryptContext
from sqlalchemy import select
from app.core.security import verify_password, hash_password, create_access_token



router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(
        name = user.name,
        email = user.email,
        hashed_password = hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login", response_model=TokenResponse)
def login_user(data: UserLogin, db: Session = Depends(get_db)):

    email = data.email
    password = data.password

    result = db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=401, detail="Nieprawidłowe dane")
    
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Nieprawidłowe dane")
    
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}







