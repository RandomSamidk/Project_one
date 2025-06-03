from fastapi import APIRouter, HTTPException, Depends
from ..models.employee import create_employee,UserCreate,UserLogin,get_password_from_username,verify_password
from ..utils.response_wrapper import api_response
import requests


router = APIRouter()

#CREATE NEW EMPLOYEE
@router.post("/employee/")
def create_new_employee(user: UserCreate):
    emp_id = create_employee(user.username,user.password)

    if emp_id:
        return api_response({"emp_id":emp_id},"Employee created successfully",201)
    else:
        raise HTTPException(status_code=400, detail="Employee creation failed")
    

#LOGIN AND AUTHENTICATION
@router.post("/login/")
def login(user: UserLogin ):
    user_row = get_password_from_username(user.username)
    if user_row is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    if not verify_password(user.password,user_row["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return api_response({"emp_id": user_row["emp_id"],"username": user_row["username"]},"Login successful",True)
        