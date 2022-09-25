from fastapi import APIRouter, Depends, Request, Form
from sqlalchemy.orm.session import Session
import database
import models
import schemas
from repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)
get_db = database.get_db


# Show ALl Blog
@router.get('/show-all')
async def showAllBlog(request: Request, db: Session = Depends(get_db)):
    return blog.showAllBlog(request, db)


# Show Create Blog Page
@router.get('/create-blog')
async def createBlogPage(request: Request, db: Session = Depends(get_db)):
    return blog.createBlogPage(request)


# Create a blog
@router.post('/blog-created')
async def createBlog(title: str = Form(...), description: str = Form(...), db: Session = Depends(get_db)):
    print("title: " + title + "  Description: " + description)
    return blog.createBlog(title, description, db)


# Get a Specific Blog
@router.get('/{blog_ID}')
async def showOneBlog(blogID, db: Session = Depends(get_db)):
    return blog.showOneBlog(blogID, db)


# Delete a blog
@router.delete('/')
async def deleteBlog(blogID: int, db: Session = Depends(get_db)):
    return blog.deleteBlog(blogID, db)


# Update a blog
@router.put('/{blog-id}')
async def updateBlog(blogID: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.updateBlog(blogID, request, db)
