from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
import database
import schemas
from repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)
get_db = database.get_db


# Show All User
@router.get('/')
async def showAllUser(db: Session = Depends(get_db)):
    return user.showAllUser(db)


# Get a User
@router.get('/{userID}')
async def showOneUser(userID, db: Session = Depends(get_db)):
    return user.showOneUser(userID, db)


# Create a User
@router.post('/')
async def createUser(request: schemas.User, db: Session = Depends(get_db)):
    return user.createUser(request, db)


# Delete a User
@router.delete('/user-delete')
async def deleteUser(userID: int, db: Session = Depends(get_db)):
    return user.deleteUser(userID, db)


# Update a User
@router.put('/')
async def updateUser(request: schemas.User, db: Session = Depends(get_db)):
    return user.updateUser(request, db)
