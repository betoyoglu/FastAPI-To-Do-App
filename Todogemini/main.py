from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse

from .models import Base
from .database import engine
from .routers.auth import router as auth_router
from .routers.todo import router as todo_router
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

script_dir = os.path.dirname(__file__)
st_abs_file_path = os.path.join(script_dir, "static/")

app.mount("/static", StaticFiles(directory=st_abs_file_path), name="static")

@app.get("/")
def read_root(request:Request):
    return RedirectResponse(url="/todo/todo-page", status_code=302) #html

app.include_router(auth_router)
app.include_router(todo_router)

Base.metadata.create_all(bind=engine) #veritabanını oluşturucak

