from fastapi import FastAPI, Request, File, UploadFile, Form
import models
from database import engine
from routers import blog, user
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)

# templates = Jinja2Templates(directory="html-directory")
# @app.get('/', response_class=HTMLResponse)
# async def read_items(request: Request):
#     name = "kamal";
#     return templates.TemplateResponse("test.html", {"request": request, "name": name})  # generate_html_response()
#
# @app.post('/submitform')
# async def handle_form(assignment: str = Form(...), assignment_file: UploadFile = Form(...)):
#     print(assignment)
#     print(assignment_file.filename)
#     content_assignment = await assignment_file.read()
#     print(content_assignment)
#     return {"kamal is coding now"}



