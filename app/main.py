from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

from app.routes import authUser, auth

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

# static
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# LOGIN SEM JINJA
@app.get("/login", response_class=HTMLResponse)
def login():
    file_path = BASE_DIR / "templates" / "login.html"
    return file_path.read_text(encoding="utf-8")


# LOGIN SEM JINJA
@app.get("/", response_class=HTMLResponse)
def login():
    file_path = BASE_DIR / "templates" / "index.html"
    return file_path.read_text(encoding="utf-8")



# routers
app.include_router(auth.router)
app.include_router(authUser.router)