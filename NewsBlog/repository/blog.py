from sqlalchemy import null
from sqlalchemy.orm.session import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
import models
import schemas

templates = Jinja2Templates(directory="html-directory")


def showAllBlog(request: Request, db: Session):
    blogs = db.query(models.Blog).all()
    if not blogs:
        Dict = null
    else:
        Dict = {"request": request, "blogs": blogs[0].title}
        # "blog2_title": blogs[1].title, "blog2_body": blogs[1].description}
    return templates.TemplateResponse("homepage.html", Dict)


def showOneBlog(blogID, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blogID).first()
    return blog


def createBlogPage(request: Request):
    return templates.TemplateResponse("create_blog.html", {"request": request})


def createBlog(title: str, description: str, db: Session):
    new_blog = models.Blog(title=title, description=description)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def deleteBlog(blogID: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blogID)
    blog.delete(synchronize_session=False)
    db.commit()
    return f"{blogID} No blog is deleted"


def updateBlog(blogID: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blogID)
    blog.update({models.Blog.title: request.title})
    db.commit()
    return f"{blogID} No. blog is updated"
