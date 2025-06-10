from fastapi import APIRouter, HTTPException
from ..models.employee import create_employee,UserCreate,UserLogin,UserToken,get_password_from_username,verify_password
from ..utils.response_wrapper import api_response
from ..utils.jwt_handler import create_access_token,decode_access_token

a = 1
router = APIRouter()

#CREATE NEW EMPLOYEE
@router.post("/employee")
def create_new_employee(user: UserCreate):
    emp_id = create_employee(user.username,user.password)

    if emp_id:
        return api_response({"emp_id":emp_id},"Employee created successfully",True)
    else:
        raise HTTPException(status_code=400, detail="Employee creation failed")
    

#LOGIN AND AUTHENTICATION
@router.post("/employee_login")
def login(user: UserLogin):
    user_row = get_password_from_username(user.username)
    if user_row is None or not verify_password(user.password, user_row["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token({"emp_id": user_row["emp_id"], "username": user_row["username"]})
    return api_response({"access_token": token}, "Login successful and access token generated", True)
      

#DECODE ACCESS TOKEN ROUTE
@router.post("/employee_decode")
def decode_token(token: UserToken):
    data = decode_access_token(token.token)
    return api_response({"emp_id": data["emp_id"], "username": data["username"]}, "Access token validated", True)
