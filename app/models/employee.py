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
        cursor=database.get_cursor()
        query = "INSERT INTO employee (username, password) VALUES (%s,%s)"
        cursor.execute(query,(username,hashed_password))
        cursor.connection.commit()
        return cursor.lastrowid
    except Exception as e:
        print("Error found : ",e)
        return None
    finally:
        if cursor:
            cursor.close()