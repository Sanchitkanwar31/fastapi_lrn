# from app.database import Base
# from pydantic import BaseModel
# from sqlalchemy import Column,Integer,String,Boolean

# class PostDB(Base):
#     __tablename__ = "posting"
#     id= Column(Integer,primary_key=True,nullable=False)
#     title=Column(String,nullable=False)
#     content=Column(String,nullable=False)
#     published=Column(Boolean,default=False)
    
# class PostCreate(BaseModel):
#     title: str
#     content: str
#     published: bool = True


from app.database import Base
from pydantic import BaseModel,EmailStr
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean,text
from sqlalchemy.orm import relationship

# SQLAlchemy DB Model
class PostDB(Base):
    __tablename__ = "posting"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")

#----SQLAlchemy User Model----
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    phone_no=Column(String,nullable=True)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

#----SQLAlchemy VOTE Model----
class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posting.id", ondelete="CASCADE"), primary_key=True)