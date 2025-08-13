from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas_pydant as schemas , model, utils, oauth2
from .database import get_db

from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
     tags=["auth"]
)

@router.post("/login")
def login(userinfo: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    
    # user_db = db.query(model.User).filter(model.User.email == userinfo.email).first()
    user_db = db.query(model.User).filter(model.User.email == userinfo.username).first()
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not utils.verify(userinfo.password, user_db.password):
        raise HTTPException(status_code=403, detail="Invalid credentials")
#create token
    access_token = oauth2.create_access_token(data={"user_id": user_db.id})
    return {"message": "Login successful user_id token type=bearer" ,"access_token": access_token}
    