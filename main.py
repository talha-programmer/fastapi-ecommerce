from fastapi import FastAPI

from db.db_setup import engine, Base
from db.models import product
from api import products

# bind all the models to the engine
Base.metadata.create_all(bind=engine) 


app = FastAPI(
    title="Backend Task FORSIT",
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

app.include_router(products.router)