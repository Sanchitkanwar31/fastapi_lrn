
from fastapi import APIRouter, FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app import schemas_pydant as schemas, model, utils
from ..database import get_db

router=APIRouter(
    tags=["User"]
)

@router.post("/users", status_code=status.HTTP_201_CREATED,response_model=schemas.Userout)
def create_user(user: schemas.Usercreate,db:Session =Depends(get_db)):
    # Hash the password
    hash_pswd = utils.hash_password(user.password)
    user.password = hash_pswd
    new_user=model.User(**user.dict())
    db.add(new_user)
    db.commit() 
    db.refresh(new_user)
    return new_user

@router.get("/users/{id}", response_model=schemas.Userout)
def get_user(id: int, db: Session = Depends(get_db)):
    print("finding User id:",id)
    user_db=db.query(model.User).filter(model.User.id == id).first()
    if not user_db:
        raise HTTPException(status_code=404,detail="user not found")
    
    return user_db
    

   