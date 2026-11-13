# import bcrypt
# from fastapi import Request
# from sqlalchemy.orm import Session
# from model import User

# def hash_password(password:str) -> str:
#     pwd_bytes = password.encode('utf-8')
#     if len(pwd_bytes)> 72:
#         pwd_bytes = pwd_bytes[:72]
#     salt = bcrypt.gensalt()
#     return bcrypt.hashpw(pwd_bytes,salt).decode('utf-8')

# def varify_password(plain_password:str, hash_password:str)-> bool:
#     pwd_bytes = plain_password.encode('utf-8')
#     if len(pwd_bytes)> 72:
#         pwd_bytes = pwd_bytes[:72]
#     return bcrypt.checkpw(pwd_bytes,hash_password.encode('utf-8'))


# def get_current_user(request:Request,db:Session):
#     user_id = request.cookies.get('user_id')
#     if not user_id:
#         return None
#     try:
#         return db.query(User).filter(User.id == int(user_id)).first()
#     except ValueError:
#         return None




import bcrypt
from fastapi import Request
from sqlalchemy.orm import Session
from model import User

def hash_password(password: str) -> str:
    """Directly hash password using bcrypt, safely truncating at 72 bytes."""
    pwd_bytes = password.encode('utf-8')
    if len(pwd_bytes) > 72:
        pwd_bytes = pwd_bytes[:72]
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password securely."""
    pwd_bytes = plain_password.encode('utf-8')
    if len(pwd_bytes) > 72:
        pwd_bytes = pwd_bytes[:72]
    return bcrypt.checkpw(pwd_bytes, hashed_password.encode('utf-8'))

def get_current_user(request: Request, db: Session):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return None
    try:
        return db.query(User).filter(User.id == int(user_id)).first()
    except ValueError:
        return None