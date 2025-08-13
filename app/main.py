#THIS IS LEARNIG ------------------------Practice part comment out----------------
# 
# from fastapi import FastAPI, Body, HTTPException,Depends
# from fastapi import status
# from pydantic import BaseModel
# from typing import Optional
# from random import randrange
# from app import utils
# from app.database import get_db

# import time
# import psycopg2 #this is install outside my environment
# from psycopg2.extras import RealDictCursor

# from .database import engine,SessionLocal

# # from . import schemas_pydant as schemas
#  from . import model
# from app.model import PostDB  # SQLAlchemy model ✅ for 

# model.Base.metadata.create_all(bind=engine)

# from sqlalchemy.orm import Session

# from passlib.context import CryptContext



# import sys
# import time
# # print("RUNNING FROM:", sys.executable)

# # Define Post structure

# class Post(BaseModel):

#     title: str

#     content: str

#     published: bool = True

#     # rating: Optional[int] = None


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #hashing algo used is Bcrypt


# # app = FastAPI()
# while (True):
#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='Zuzz@8021',cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("Connected Postgres Database")
#         break
#     except Exception as e:
#         print(f"Database connection failed: {e}")
#         conn = None
#         cursor = None
#         time.sleep(2)

# # Sample in-memory database
# # my_data = [
# #     {"title": "Post 1", "content": "Content of post 1", "id": 1},
# #     {"title": "Post 2", "content": "Content of post 2", "id": 2}
# # ]

# # def find_post(id: int):
# #     for p in my_data:
# #         if p['id'] == id:
# #             return p

# #     return None

# from .router import post, user
# app = FastAPI()
# app.include_router(post.router)
# app.include_router(user.router)
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/sqlaclmy")
# def test_post(db :Session = Depends(get_db)):
#     p=db.query(model.PostDB).all()
#     print(p)
#     return {"data":p}


# @app.post("/getposts")
# def get_post():
#     cursor.execute("""SELECT * FROM posts""")
#     posts=cursor.fetchall()
#     print(posts)
#     return {"data SQL": posts}



# # # @app.post("/createpost")
# # # def create_post(new_post: Post):
# # #     print(new_post.title)
# # #     print(new_post.rating)
# # #     return {"message": "Post created successfully!", "content": new_post.content}


# # @app.post("/posts", response_model=schemas.PostResponse, status_code=status.HTTP_201_CREATED)
# # def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
# #     new_post = PostDB(**post.dict())
# #     db.add(new_post)
# #     db.commit()
# #     db.refresh(new_post)
# #     return new_post



# # # @app.post("/posts",status_code=status.HTTP_201_CREATED)
# # # def create_post_with_body(post: model.PostDB, db :Session = Depends(get_db)):

# # #     # print(post.title) in this post:was from class Post created to define the list of dictionary
# # #     # post_dict = post.dict()
# # #     # post_dict['id'] = randrange(0, 100)
# # #     # my_data.append(post_dict)      return {"data": f"Post {post_dict['title']} created with content: {post_dict['content']} saved in array"}
    
# # #     # USING SQL COMMANDS ON POSTGRESQL DIRECTLY
# # #     # cursor.execute(""" INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
# # #     # new_post=cursor.fetchone()
# # #     # conn.commit()
    
# # #  

# # @app.get("/posts/{id}")
# # def get_post_by_id(id: int,db: Session = Depends(get_db)):
# #     # print(f"fetching post by id: {id}")
# #     # p = find_post(int(id))
# #     # return p
    
# #     #SQL COMMANDS ON POSTGRESQL DIRECTLY
# #     # cursor.execute("""SELECT * FROM posts WHERE id = %s""",(str(id)))
# #     # #we need to change the id to str
# #     # id_post=cursor.fetchone()
# #     # return {"data":id_post}
# #     # return {"error": "Post not found"}, 404

# #     db_post = db.query(model.PostDB).filter(model.PostDB.id == id).first()
# #     if not db_post:
# #         raise HTTPException(status_code=404, detail="Post not found")   
# #     return {"data": db_post}

# # @app.delete("/posts/{id}")
# # def delete_post(id: int,db: Session = Depends(get_db)):
# #     print(f"deleting post by id: {id}")
# #     # p = find_post(int(id))
# #     #my_data.remove(p)
    
# #     #SQL COMMANDS ON POSTGRESQL DIRECTLY
# #     # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id)))
# #     # p = cursor.fetchone()
# #     # conn.commit()
# #     # if not p:
# #     #     raise HTTPException(status_code=404, detail="Post not found")
# #     # return {"message": f"Post with id {id} deleted successfully that is {p}"}
# #     check_post=db.query(model.PostDB).filter(model.PostDB.id == id)
# #     if not check_post.first():
# #         raise HTTPException(status_code=404, detail="Post not found")
# #     check_post.delete(synchronize_session=False)
# #     db.commit() 
# #     return {"data":check_post.first(), "message": f"Post with id {id} deleted successfully"}



# # @app.put("/posts/{id}",status_code= status.HTTP_201_CREATED)
# # def update_post(id: int, updated_post: schemas.PostCreate,db: Session = Depends(get_db)):
# #     print("updating post by id:", {id})
    
# #     # for index, post in enumerate(my_data):
# #     #     if post['id'] == id:
# #     #         post_data = updated_post.dict()
# #     #         post_data['id'] = id  # Keep the same ID
# #     #         my_data[index] = post_data
# #     #         return {"message": f"Post with id {id} updated successfully", "data": post_data}
   
# #     #SQL COMMANDS ON POSTGRESQL DIRECTLY to update
# #     # cursor.execute("""UPDATE posts SET title=%s , content=%s WHERE id=%s RETURNING *""",(updated_post.title,updated_post.content,str(id)))
# #     # latest_post=cursor.fetchone()
# #     # conn.commit()
# #     # if not latest_post:
# #     #     raise HTTPException(status_code=404, detail="Post not found")
# #     # return {"data":latest_post}
    
# #     #SQLALCHEMY USE
# #     check_post = db.query(model.PostDB).filter(model.PostDB.id == id)
# #     up_post= check_post.first()
# #     # db_post = model.PostDB(**updated_post.dict(), id=id)
# #     if not check_post.first():
# #         raise HTTPException(status_code=404, detail="Post not found")   
# #     check_post.update(updated_post.dict(), synchronize_session=False)
# #     db.commit() 
# #     return {"data": update_post, "message": f"Post with id {id} updated successfully"}
    

# # #---------------------USERS REGISTER------------------

# # @app.post("/users", status_code=status.HTTP_201_CREATED,response_model=schemas.Userout)
# # def create_user(user: schemas.Usercreate,db:Session =Depends(get_db)):
# #     # Hash the password
# #     hash_pswd = utils.hash(user.password)
# #     user.password = hash_pswd
# #     new_user=model.User(**user.dict())
# #     db.add(new_user)
# #     db.commit() 
# #     db.refresh(new_user)
# #     return new_user

# # @app.get("/users/{id}", response_model=schemas.Userout)
# # def get_user(id: int, db: Session = Depends(get_db)):
# #     print("finding User id:",id)
# #     user_db=db.query(model.User).filter(model.User.id == id).first()
# #     if not user_db:
# #         raise HTTPException(status_code=404,detail="user not found")
    
# #     return user_db
    

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router import vote
from .router import post, user
from app import model, oauth2
from app.database import engine
from app import auth

from app.config import settings  # <-- Add this import

# Global cursor and connection
conn = None
cursor = None

#This is to make a creation with Postgressql
# while True:
#     try:
#         conn = psycopg2.connect(
#             host='localhost',
#             database='fastapi',
#             user='postgres',
#             password='Zuzz@8021',
#             cursor_factory=RealDictCursor
#         )
#         # conn = psycopg2.connect(
#         #     host=settings.database_hostname,
#         #     database=settings.database_name,
#         #     user=settings.database_username,
#         #     password=settings.database_password,
#         #     cursor_factory=RealDictCursor
#         # )
#         cursor = conn.cursor()
#         print("✅ Connected to PostgreSQL using psycopg2")
#         break
#     except Exception as e:
#         print(f"❌ Database connection failed: {e}")
#         time.sleep(2)


# model.Base.metadata.create_all(bind=engine)
# print("✅ Tables created!")

print("✅ Using database:", settings.database_name)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, adjust as needed    
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, adjust as needed
    allow_headers=["*"],  # Allows all headers, adjust as needed
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Welcome!"}

@app.get("/raw-posts")
def get_raw_posts():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    return {"raw_data": posts}


from app.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session  # <-- Add this import
from sqlalchemy import func  # <-- Import func for SQL functions
from typing import Optional

@app.get("/sqlaclmy")
def test_post(search: Optional[str]= "",limit: Optional[int] = 2,skip: int = 1,db: Session = Depends(get_db),get_current_user: int = Depends(oauth2.get_current_user)):
    print(limit)
    
    ''' # this will find search ofcurrent user's post
    posts = (db.query(model.PostDBa).filter(model.PostDB.title.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )

    return posts '''

    
    # result = db.query(model.PostDB,func.count(model.Vote.post_id)).join(model.Vote, model.PostDB.id == model.Vote.post_id,isouter=True).group_by(model.PostDB.id).all()
     # Join with votes and count them
    result = db.query(model.PostDB, func.count(model.Vote.post_id).label("votes")).join(
        model.Vote, model.PostDB.id == model.Vote.post_id, isouter=True
    ).group_by(model.PostDB.id).order_by(model.PostDB.id.asc()).all()

    # Sort by ID ascending: .order_by(model.PostDB.id.asc())

    # Manual serialization to avoid JSON errors
    response = []
    # for post, votes in p: FOR INTIATING SEARCH
    for post, votes in result:
        response.append({
            "post": {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "published": post.published,
                "owner_id": post.owner_id
            },
            "votes": votes
        })

    return {"data": response}  