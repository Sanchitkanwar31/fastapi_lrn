
from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session,joinedload
from app import oauth2, schemas_pydant as schemas
from app import model
from ..database import get_db
from ..model import PostDB 

router = APIRouter(
    tags=["Post API"]
)

@router.post("/posts", response_model=schemas.PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db),get_current_user: int = Depends(oauth2.get_current_user)):
    print(get_current_user.email)  # This will print the email of the current user
    new_post = PostDB(owner_id=get_current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post



# @router.post("/posts",status_code=status.HTTP_201_CREATED)
# def create_post_with_body(post: model.PostDB, db :Session = Depends(get_db)):

#     # print(post.title) in this post:was from class Post created to define the list of dictionary
#     # post_dict = post.dict()
#     # post_dict['id'] = randrange(0, 100)
#     # my_data.append(post_dict)      return {"data": f"Post {post_dict['title']} created with content: {post_dict['content']} saved in array"}
    
#     # USING SQL COMMANDS ON POSTGRESQL DIRECTLY
#     # cursor.execute(""" INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
#     # new_post=cursor.fetchone()
#     # conn.commit()

@router.get("/all_post")
def get_all_post(db: Session = Depends(get_db),get_current_user: int = Depends(oauth2.get_current_user)):
    
    print("Current User is:",get_current_user.id)
    db_post_all = db.query(model.PostDB).options(joinedload(model.PostDB.owner)).all()

    return {"all":db_post_all}



@router.get("/posts/{id}")
def get_post_by_id(id: int,db: Session = Depends(get_db),get_current_user: int = Depends(oauth2.get_current_user)):
    # print(f"fetching post by id: {id}")
    # p = find_post(int(id))
    # return p
    
    #SQL COMMANDS ON POSTGRESQL DIRECTLY
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""",(str(id)))
    # #we need to change the id to str
    # id_post=cursor.fetchone()
    # return {"data":id_post}
    # return {"error": "Post not found"}, 404

    # db_post = db.query(model.PostDB).filter(model.PostDB.owner_id == get_current_user.id).all() #this will give all post of CURRENT USER
    # The FILTER will show POST og login user only.But  ABOVE db_post will show all....but def get_post_by_id(id: int)THIS id is also remove from this
    
    # SQLALCHEMY USE TO FETCH POST BY ID--👇
    db_post = db.query(model.PostDB).filter(model.PostDB.id == id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")   
    # This ensures that the user can only access their own posts
    if db_post.owner_id !=get_current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this post")
    return {"data": db_post}

@router.delete("/posts/{id}")
def delete_post(id: int,db: Session = Depends(get_db),get_current_user: int = Depends(oauth2.get_current_user)):
    print(f"deleting post by id: {id}")
    # p = find_post(int(id))
    #my_data.remove(p)
    
    #SQL COMMANDS ON POSTGRESQL DIRECTLY
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id)))
    # p = cursor.fetchone()
    # conn.commit()
    # if not p:
    #     raise HTTPException(status_code=404, detail="Post not found")
    # return {"message": f"Post with id {id} deleted successfully that is {p}"}

    check_post=db.query(model.PostDB).filter(model.PostDB.id == id)
    if not check_post.first():
        raise HTTPException(status_code=404, detail="Post not found")
    if check_post.first().owner_id != get_current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this post")
    
    check_post.delete(synchronize_session=False)
    db.commit() 
    return {"data":check_post.first(), "message": f"Post with id {id} deleted successfully"}



@router.put("/posts/{id}",status_code= status.HTTP_201_CREATED)
def update_post(id: int, updated_post: schemas.PostCreate,db: Session = Depends(get_db),get_current_user: int = Depends(oauth2.get_current_user)):
    print("updating post by id:", {id})
    
    # for index, post in enumerate(my_data):
    #     if post['id'] == id:
    #         post_data = updated_post.dict()
    #         post_data['id'] = id  # Keep the same ID
    #         my_data[index] = post_data
    #         return {"message": f"Post with id {id} updated successfully", "data": post_data}
   
    #SQL COMMANDS ON POSTGRESQL DIRECTLY to update
    # cursor.execute("""UPDATE posts SET title=%s , content=%s WHERE id=%s RETURNING *""",(updated_post.title,updated_post.content,str(id)))
    # latest_post=cursor.fetchone()
    # conn.commit()
    # if not latest_post:
    #     raise HTTPException(status_code=404, detail="Post not found")
    # return {"data":latest_post}
    
    #SQLALCHEMY USE
    check_post = db.query(model.PostDB).filter(model.PostDB.id == id)
    up_post = check_post.first()
    # db_post = model.PostDB(**updated_post.dict(), id=id)
    if not check_post.first():
        raise HTTPException(status_code=404, detail="Post not found")   
    check_post.update(updated_post.dict(), synchronize_session=False)
    db.commit() 
    return {"data": update_post, "message": f"Post with id {id} updated successfully"}