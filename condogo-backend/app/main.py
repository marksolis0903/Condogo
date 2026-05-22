from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CondoGo API")

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "CondoGo API is running"}