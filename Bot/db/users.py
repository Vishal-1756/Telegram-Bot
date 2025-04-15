from Bot.db import SESSION, BASE
from sqlalchemy import Column, Integer, UnicodeText, DateTime
from datetime import datetime

class Users(BASE):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(UnicodeText)
    first_name = Column(UnicodeText)
    last_name = Column(UnicodeText)
    join_date = Column(DateTime, default=datetime.utcnow)
    last_seen = Column(DateTime, default=datetime.utcnow)
    
    def __init__(self, user_id, username, first_name=None, last_name=None):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.join_date = datetime.utcnow()
        self.last_seen = datetime.utcnow()

    def __repr__(self):
        return f"<User {self.user_id}>"
    
Users.__table__.create(checkfirst=True)

def add_user(user_id, username, first_name=None, last_name=None):
    try:
        user = SESSION.query(Users).get(user_id)
        if not user:
            user = Users(user_id, username, first_name, last_name)
            SESSION.add(user)
            SESSION.commit()
            return True
        else:
            # Update existing user
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.last_seen = datetime.utcnow()
            SESSION.commit()
            return False
    finally:
        SESSION.close()
    

def id_to_username(user_id):
    try:
        user = SESSION.query(Users).get(user_id)
        if user:
            return user.username
    finally:
        SESSION.close()

def get_user(user_id):
    return SESSION.query(Users).get(user_id)

def get_all_users():
    return SESSION.query(Users).all()

def update_last_seen(user_id):
    try:
        user = SESSION.query(Users).get(user_id)
        if user:
            user.last_seen = datetime.utcnow()
            SESSION.commit()
            return True
    finally:
        SESSION.close()
    return False