from fastapi import FastAPI
from app.controllers.employee import router as employee_router

app = FastAPI()

app.include_router(employee_router,prefix="/api",tags=["Employee"])

@app.get("/")
def root():
    return {"output":"WELOCOME TO HOME PAGE"}


