
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint
#  Pydantic Input Model (for request body)
class PostCreate(BaseModel):
	title: str
	content: str
	published: bool = True

class Userout(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config():
        from_attributes = True

#  Pydantic Output Model (for response_model=...)
class PostResponse(PostCreate):
    id: int
    owner_id: int
    owner: Userout

    class Config:
        from_attributes = True
  
#---------------uUSER PYDANTIC model---
     
class Usercreate(BaseModel):
    email: EmailStr
    password: str
    
# class Userout(BaseModel):
#     id: int
#     email: EmailStr
#     created_at: datetime
    
#     class Config():
#         from_attributes = True
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[int]=  None
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)  # type: ignore # 1 or 0, where 1 means upvote and 0 means downvote

   