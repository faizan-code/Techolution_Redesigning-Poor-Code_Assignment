# Library Management System

## Overview
The Library Management System is a Python-based application designed to simplify the management of a library's operations, including handling books and users, facilitating book checkouts and returns, and maintaining the availability status of books. It leverages Object-Oriented Programming (OOP) principles to ensure the system is scalable, maintainable, and extensible.

## Features
- **Book Management**: Add, update, delete, and list books; search by title, author, or ISBN.
- **User Management**: Add, update, delete, and list users; search by name or user ID.
- **Transaction Handling**: Support for checking books in and out.
- **Logging**: Basic logging of system operations for auditing and troubleshooting.
- **Extensibility**: Designed with future expansion in mind, such as adding new item types or features like due dates and late fees.

## Getting Started

### Prerequisites
- Python 3.8 or higher

### Installation
```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
```

# Running the Application
## `python main.py`


```
# library-management-system/
│
├── models/                  # Contains classes that represent data models.
│   ├── book.py              # Book class with properties like title and author.
│   └── user.py              # User class with properties like name and user ID.
│
├── storage/                 # Abstracts storage mechanism (JSON, CSV).
│   ├── storage_interface.py # Interface for storage operations.
│   ├── json_storage.py      # Implements storage_interface with JSON.
│   └── csv_storage.py       # Optional CSV storage implementation.
│
├── services/                # Business logic layer for entity management.
│   ├── base_service.py      # Base class for shared service functionalities.
│   ├── book_service.py      # Service class for book management operations.
│   └── user_service.py      # Service class for user management operations.
│
├── commands/                # Implements the Command pattern for CLI interactions.
│   ├── add_book_command.py
│   ├── add_user_command.py
│   ├── command_interface.py # Defines the command interface.
│   ├── delete_book_command.py
│   ├── delete_user_command.py
│   ├── list_books_command.py
│   ├── list_users_command.py
│   ├── update_book_command.py
│   └── update_user_command.py
│
├── utils/                   # Utilities and helpers like logging and validation.
│   ├── logger.py            # Logging utility for tracking system operations.
│   └── validators.py        # Input validation utility.
│
└── main.py                  # Entry point for the application, initializes the CLI.
```
