from fastapi import FastAPI

from db.db_setup import engine
from db.models import user
from api import users

# bind all the models to the engine
user.Base.metadata.create_all(bind=engine) 

app = FastAPI(
    title="Backend Task Forsit",
    description="Sample e-commerce application",
    version="0.0.1",
    contact={
        "name": "Talha",
        "email": "talhashabbir9@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(users.router)