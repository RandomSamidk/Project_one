#models
from pydantic import BaseModel
from ..database import database
import bcrypt

class UserCreate(BaseModel):
    username : str 
    password : str

def create_employee(username: str, password: str):
    password_bytes = password.encode('utf-8') # converting password to array of bytes
    salt = bcrypt.gensalt()# generating the salt
    hashed_password = bcrypt.hashpw(password_bytes, salt).decode('utf-8')
    #insering new employee into the database
    try: 
        conn = database.get_connection()
        cursor=conn.cursor()
        query = "INSERT INTO employee (username, password) VALUES (%s,%s)"
        cursor.execute(query,(username,hashed_password))
        conn.commit()
        return cursor.lastrowid
    except Exception as e:
        print("Error found : ",e)
        return None
    finally:
        if cursor:
            cursor.close()

class UserLogin(BaseModel):
    username: str
    password: str


#login and authentication
def get_password_from_username(username: str):
    conn=None
    cursor=None
    try:
        conn=database.get_connection()
        cursor=conn.cursor(dictionary=True)
        query="SELECT * FROM EMPLOYEE WHERE username=%s"
        cursor.execute(query,(username,))
        return cursor.fetchone()
    except Exception as e:
        print("Error found: ",e)
        return None
    finally:
        if cursor:
            cursor.close()

def verify_password(password: str, hashed_password: str) ->bool:
    password_bytes = password.encode('utf-8') # converting password to array of bytes
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes,hashed_password_bytes)