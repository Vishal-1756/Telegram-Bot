# Database Module

This directory contains the database models and operations for the Telegram bot. The bot uses SQLAlchemy to interact with the database.

## Structure

The database module consists of:

- `__init__.py` - Sets up the database connection and defines the base model
- `users.py` - Implements the User model and user-related operations

## Database Connection

The database connection is established in `__init__.py`. The connection string is read from the environment variables and defaults to an SQLite database if not specified.

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from Bot.config import DB_URI

# Create engine
engine = create_engine(DB_URI)

# Create session
SESSION = scoped_session(sessionmaker(bind=engine))

# Create base model
BASE = declarative_base()
```

## User Model

The User model (`users.py`) stores information about bot users:

```python
class Users(BASE):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(UnicodeText)
    first_name = Column(UnicodeText)
    last_name = Column(UnicodeText)
    join_date = Column(DateTime, default=datetime.utcnow)
    last_seen = Column(DateTime, default=datetime.utcnow)
```

### Fields

- `user_id` - Telegram user ID (primary key)
- `username` - Telegram username
- `first_name` - User's first name
- `last_name` - User's last name
- `join_date` - When the user first interacted with the bot
- `last_seen` - When the user last interacted with the bot

## User Operations

The `users.py` file provides several functions for user operations:

- `add_user(user_id, username, first_name, last_name)` - Add a new user or update existing user
- `get_user(user_id)` - Get a user by their ID
- `get_all_users()` - Get all users
- `update_last_seen(user_id)` - Update a user's last seen time
- `id_to_username(user_id)` - Get a username for a given user ID

## Example Usage

### Adding or Updating a User

```python
from Bot.db.users import add_user

# Add a new user or update existing user
add_user(
    user_id=123456789,
    username="john_doe",
    first_name="John",
    last_name="Doe"
)
```

### Getting User Information

```python
from Bot.db.users import get_user

# Get user information
user = get_user(123456789)
if user:
    print(f"Username: {user.username}")
    print(f"First name: {user.first_name}")
    print(f"Last seen: {user.last_seen}")
```

### Updating Last Seen

```python
from Bot.db.users import update_last_seen

# Update user's last seen time
update_last_seen(123456789)
```

### Getting All Users

```python
from Bot.db.users import get_all_users

# Get all users
users = get_all_users()
print(f"Total users: {len(users)}")
```

## Creating New Models

To create a new database model:

1. Create a new Python file in the `Bot/db/` directory (e.g., `messages.py`)
2. Import the necessary components:
   ```python
   from Bot.db import SESSION, BASE
   from sqlalchemy import Column, Integer, UnicodeText, DateTime, ForeignKey
   from sqlalchemy.orm import relationship
   from datetime import datetime
   ```
3. Define your model class:
   ```python
   class Messages(BASE):
       __tablename__ = "messages"
       
       id = Column(Integer, primary_key=True)
       user_id = Column(Integer, ForeignKey('users.user_id'))
       text = Column(UnicodeText)
       timestamp = Column(DateTime, default=datetime.utcnow)
       
       user = relationship("Users", backref="messages")
   ```
4. Create the table and implement operations:
   ```python
   # Create table
   Messages.__table__.create(checkfirst=True)
   
   # Add a message
   def add_message(user_id, text):
       message = Messages(user_id=user_id, text=text)
       SESSION.add(message)
       SESSION.commit()
       return message
   ```

## Best Practices

1. Always use a session safely with try/finally blocks:
   ```python
   try:
       # Perform database operations
       SESSION.commit()
   finally:
       SESSION.close()
   ```

2. Use appropriate column types for your data

3. Create indexes for frequently queried columns

4. Use relationships between models where appropriate

5. Keep database operations separate from bot logic

6. Close sessions after use to prevent resource leaks 