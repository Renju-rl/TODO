from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from database import engine, Base
from router import auth_router, todo_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Full-Stack Auth Todo App")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth_router.router)
app.include_router(todo_router.router)

@app.get("/")
def root():
    return RedirectResponse(url="/todos")