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

# library-management-system

```
library-management-system/
│
├── models/                  # Data models representation.
│   ├── book.py              # Defines the Book model.
│   └── user.py              # Defines the User model.
│
├── storage/                 # Data storage abstraction layer.
│   ├── storage_interface.py # Storage operation definitions.
│   ├── json_storage.py      # JSON-based storage implementation.
│   └── csv_storage.py       # Optional CSV-based storage implementation.
│
├── services/                # Business logic for library operations.
│   ├── base_service.py      # Base class for common service functionalities.
│   ├── book_service.py      # Book-related business operations.
│   └── user_service.py      # User-related business operations.
│
├── commands/                # Command pattern implementation for CLI interactions.
│   ├── add_book_command.py  # Command to add a new book.
│   ├── add_user_command.py  # Command to add a new user.
│   ├── command_interface.py # Common interface for all commands.
│   ├── delete_book_command.py  # Command to delete a book.
│   ├── delete_user_command.py  # Command to delete a user.
│   ├── list_books_command.py   # Command to list all books.
│   ├── list_users_command.py   # Command to list all users.
│   ├── update_book_command.py  # Command to update book details.
│   └── update_user_command.py  # Command to update user details.
│
├── utils/                   # Utility functions and helpers.
│   ├── logger.py            # Simple logging utility for system operations.
│   └── validators.py        # Input validation functions.
│
└── main.py                  # Application entry point; initializes CLI.
```
