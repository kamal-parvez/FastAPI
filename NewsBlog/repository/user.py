from sqlalchemy.orm.session import Session

import models
import schemas


def showAllUser(db: Session):
    allUsers = db.query(models.User).all()
    return allUsers


def showOneUser(userID, db: Session):
    myUser = db.query(models.User).filter(models.User.id == userID).first()
    return myUser


def createUser(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return "New user is Created"


def deleteUser(userID: int, db: Session):
    old_user = db.query(models.User).filter(models.User.id == userID)
    old_user.delete(synchronize_session=False)
    db.commit()
    return f"{userID} No user is deleted"


def updateUser(request: schemas.User, db: Session):
    old_user = db.query(models.User).filter(models.User.name == request.name)
    old_user.update({models.User.email: request.email})
    db.commit()
    return "User is updated"
