from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose  import JWTError, jwt
from app import model, schemas_pydant as schemas
from app import database
from sqlalchemy.orm import Session

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY="your_secret_key"
ALGORITHM="HS256"   
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
            
        payload= jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id_pay: str =payload.get("user_id")
        
        if id_pay is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id_pay)
        return token_data
    except JWTError:
        raise credentials_exception
    
def get_current_user(token: str= Depends(oauth2_schema),db: Session= Depends(database.get_db)):
    try:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        token= verify_access_token(token, credentials_exception)
        user_protect= db.query(model.User).filter(model.User.id == token.id).first()
        return user_protect #now in post it will be returning current_user
    except HTTPException as e:
        raise e


# from datetime import datetime, timedelta
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt
# from app import model, schemas_pydant as schemas, database
# from sqlalchemy.orm import Session
# from .config import settings

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

# def create_access_token(data: dict):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
#     return encoded_jwt

# def verify_access_token(token: str, credentials_exception):
#     try:
#         payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
#         id_pay: str = payload.get("user_id")
#         if id_pay is None:
#             raise credentials_exception
#         return schemas.TokenData(id=id_pay)
#     except JWTError:
#         raise credentials_exception

# def get_current_user(
#     token: str = Depends(oauth2_schema),
#     db: Session = Depends(database.get_db)
# ):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     token_data = verify_access_token(token, credentials_exception)
#     return db.query(model.User).filter(model.User.id == token_data.id).first()
