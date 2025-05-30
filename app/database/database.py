# db/database.py
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

DATABASE_URL = "mysql+pymysql://root:user123@localhost:3306/Hifx"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_db_connection():
    """
    Verify that the database connection is working properly.
    Returns True if connection is successful, False otherwise.
    """
    try:
        # Create a connection to test
        conn = engine.connect()
        # Execute a simple query
        conn.execute(text("SELECT 1"))
        conn.close()
        print("\033[92m[SUCCESS]\033[0m Database connection verified successfully!")
        return True
    except Exception as e:
        print(f"\033[91m[ERROR]\033[0m Database connection failed: {str(e)}")
        return False

# Automatically verify connection when this module is imported
try:
    verify_db_connection()
except Exception as e:
    print(f"\033[93m[WARNING]\033[0m Failed to verify database connection: {str(e)}")
    print("Application will continue, but database operations may fail.")
