from fastapi import APIRouter, HTTPException, Depends
from ..models.employee import create_employee,UserCreate
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
        