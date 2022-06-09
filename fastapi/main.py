from fastapi import FastAPI
from db.database import engine
from db.base import Base
from routes import users, products
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()   

origins = [
    "*",
    "http://localhost:8000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def create_tables():
    Base.metadata.create_all(bind=engine)

def define_route():
    app.include_router(users.router)
    app.include_router(products.router)



def start_application():
    create_tables()
    define_route()
  


start_application()      
    