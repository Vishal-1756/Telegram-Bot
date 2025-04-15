# Telegram-Bot

A modular Telegram Bot boilerplate with database integration. This project provides a structured foundation for building Telegram bots with a clean architecture that's easy to extend.

## Features

- Modular structure for easy addition of commands and features
- SQLAlchemy database integration with comprehensive user tracking
- Asynchronous programming with uvloop for improved performance (automatically installed on non-Windows platforms)
- Comprehensive logging system
- User tracking functionality with join date and last seen tracking
- Environment-based configuration with dotenv
- Utility functions for common operations
- Rate limiting and error handling
- Inline keyboard support

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`:
  - Pyrogram (Telegram client library)
  - SQLAlchemy (ORM for database operations)
  - psycopg2-binary (PostgreSQL adapter)
  - tgcrypto (Fast cryptography library for Telegram)
  - python-dotenv (Environment variable management)
  - uvloop (Automatically installed on non-Windows platforms for improved performance)

## Setup

1. Clone the repository
   ```
   git clone https://github.com/yourusername/Telegram-Bot.git
   cd Telegram-Bot
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

3. Configure the bot
   - Copy the sample environment file and edit it with your credentials:
     ```
     cp .env.sample .env
     ```
   - Open `.env` and configure:
     - `BOT_TOKEN`: Your bot token from @BotFather
     - `API_ID`: Your Telegram API ID
     - `API_HASH`: Your Telegram API Hash
     - `DB_URI`: Database connection URI (default: SQLite)

4. Run the bot
   ```
   python -m Bot
   ```

## Project Structure

```
Telegram-Bot/
├── Bot/                    # Main bot package
│   ├── core/               # Core functionality
│   │   ├── decorators/     # Decorator functions
│   │   └── utils/          # Utility functions
│   ├── db/                 # Database models and operations
│   │   ├── __init__.py     # Database connection setup
│   │   └── users.py        # User model and operations
│   ├── modules/            # Bot command modules
│   │   ├── __init__.py     # Module loader
│   │   └── start.py        # Start and help commands
│   ├── config.py           # Configuration settings
│   ├── __init__.py         # Bot initialization
│   └── __main__.py         # Entry point
├── .env.sample             # Sample environment variables
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

## Environment Configuration

The bot uses environment variables for configuration, which can be set in the `.env` file. This allows for easier deployment across different environments while keeping sensitive information secure.

Available environment variables:
- `BOT_TOKEN`: Telegram bot token from BotFather
- `API_ID`: Telegram API ID
- `API_HASH`: Telegram API Hash
- `DB_URI`: Database connection string

## Database

The bot uses SQLAlchemy ORM for database operations. By default, it's configured to use SQLite, but you can change the `DB_URI` in `config.py` to use other database engines like PostgreSQL or MySQL.

The database module provides:
- A base model system in `db/__init__.py`
- User tracking functionality in `db/users.py` with:
  - User ID and username tracking
  - First and last name storage
  - Join date and last seen tracking

For more detailed information about the database structure and operations, see the [Database Documentation](Bot/db/README.md).

## Modules

The bot has a modular design that makes it easy to add new commands and features:

1. Create a new Python file in the `Bot/modules/` directory
2. Define your command handlers using the Pyrogram decorator system
3. The module will be automatically loaded at startup

### Available Commands

- `/start` - Start the bot and get a welcome message
- `/help` - Show available commands
- `/info` - Show information about yourself
- `/stats` - Show bot statistics

For more information about creating and customizing modules, see the [Modules Documentation](Bot/modules/README.md).

## Core Functionality

### Decorators

The bot includes several decorators in the `Bot/core/decorators` directory:

- `rate_limit.py` - Rate limit a function to a certain number of calls per time window
- `tracking.py` - Track user activity
- `error_handler.py` - Handle errors in functions

### Utilities

The bot includes utility functions in the `Bot/core/utils` directory:

- `parser.py` - Parse command arguments from a message text
- `formatting.py` - Format user mentions and time intervals

## Extending

To add new features:

1. **New commands**: Add new modules in the `Bot/modules/` directory
2. **Database models**: Create new models in the `Bot/db/` directory
3. **Configuration**: Add new configuration options in `Bot/config.py`
4. **Utility functions**: Add new utility functions in the appropriate directory

## Logging

The bot includes a comprehensive logging system configured in `Bot/__init__.py`. Logs are saved to `log.txt` and also output to the console.

## License

This project is licensed under the terms included in the LICENSE file.