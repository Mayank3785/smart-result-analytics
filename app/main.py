from fastapi import FastAPI
from app.routes import students, results, analytics, auth

app = FastAPI(title="Smart Result Analytics Backend")

app.include_router(auth.router)
app.include_router(students.router)
app.include_router(results.router)
app.include_router(analytics.router)

@app.get("/")
def home():
    return {"message": "Smart Result Analytics Backend Running"}
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)
from app.routes import students, results, analytics, auth
app.include_router(analytics.router)
app.include_router(auth.router)
app.include_router(students.router)
app.include_router(results.router)
app.include_router(analytics.router)
