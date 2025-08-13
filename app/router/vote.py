from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import database, model, oauth2
from app import schemas_pydant as schemas

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote_post(vote: schemas.Vote, db: Session = Depends(database.get_db),get_current_user: int = Depends(oauth2.get_current_user)):
    v_query=db.query(model.Vote).filter(
            model.Vote.post_id == vote.post_id,
            model.Vote.user_id == get_current_user.id
        )
    vote_query=v_query.first()
    if(vote.dir == 1):
        if vote_query:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="You have already voted on this post")
        new_vote = model.Vote(post_id=vote.post_id, user_id=get_current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Vote added successfully"}
        
    else:
        if not vote_query:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote not found")
        v_query.delete(synchronize_session=False)
        
        db.commit()
        return {"message": "Vote removed successfully"} 