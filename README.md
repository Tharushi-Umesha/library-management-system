# Library Management System

A Python-based Library Management System using MySQL database for efficient management of books, members, and borrowing operations.

## Author
**Tharushi Umesha Mahipala**  
📧 Email: umemahee@gmail.com

## Features

- **Member Management**: Add new library members with contact information
- **Book Management**: Add new books with detailed information (title, author, theme)
- **Book Borrowing**: Track book loans with automatic return date calculation
- **Availability Tracking**: Real-time book availability status
- **Admin Authentication**: Secure admin login system
- **Database Integration**: MySQL database for persistent data storage

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.6 or higher
- MySQL Server
- Required Python packages (see Installation section)

## Installation

1. **Clone or download the project files**
   ```bash
   # Ensure you have these files:
   # - library-management-system.py
   # - database_config.py
   ```

2. **Install required Python packages**
   ```bash
   pip install mysql-connector-python
   ```

3. **Set up MySQL Database**
   - Install MySQL Server on your system
   - Create a database named `library_management_system`
   - Create the required tables using the SQL schema below

4. **Configure Database Connection**
   - Update `database_config.py` with your MySQL credentials
   - Default configuration uses:
     - Host: localhost
     - Port: 3306
     - Database: library_management_system
     - User: root
     - Password: enTER123456~

## Database Schema

Create the following tables in your MySQL database:

```sql
-- Create Members Table
CREATE TABLE members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Books Table
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_name VARCHAR(200) NOT NULL,
    title VARCHAR(200),
    theme VARCHAR(100),
    author VARCHAR(100),
    available BOOLEAN DEFAULT TRUE,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Borrowed Books Table
CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    book_id INT,
    member_name VARCHAR(100),
    book_name VARCHAR(200),
    borrow_date DATE,
    return_date DATE,
    notes TEXT,
    returned BOOLEAN DEFAULT FALSE,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);
```

## Configuration

### Database Configuration (`database_config.py`)

```python
# MySQL Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'database': 'library_management_system',
    'port': 3306,
    'user': 'your_username',
    'password': 'your_password',
    'charset': 'utf8mb4',
    'autocommit': True,
    'collation': 'utf8mb4_unicode_ci'
}

# Admin Login Credentials
ADMIN_CONFIG = {
    'username': 'admin',
    'password': 'password123'
}

# Application Settings
APP_CONFIG = {
    'loan_period_days': 14,
    'max_books_per_member': 5,
    'fine_per_day': 1.0
}
```

## Usage

1. **Run the Application**
   ```bash
   python library-management-system.py
   ```

2. **Admin Login**
   - Default credentials:
     - Username: `admin`
     - Password: `password123`

3. **Main Menu Options**
   - **1. Add New Member**: Register new library members
   - **2. Add New Book**: Add books to the library catalog
   - **3. Borrow Book**: Process book borrowing transactions
   - **4. Show Available Books**: Display all available books
   - **5. Logout**: Exit the admin session

## System Features

### Member Management
- Add new members with name, phone, and email
- Duplicate member detection based on email or phone
- Member validation during book borrowing

### Book Management
- Add books with comprehensive details
- Track book availability status
- Organized display by theme and author

### Borrowing System
- Automatic calculation of return dates (14-day loan period)
- Real-time availability checking
- Optional notes for borrowing records
- Automatic book status updates

### Security
- Admin authentication system
- Input validation and sanitization
- Error handling for database operations

## Application Structure

```
Library Management System/
├── library-management-system.py    # Main application file
├── database_config.py              # Database and app configuration
└── README.md                       # This documentation file
```

## Error Handling

The system includes comprehensive error handling for:
- Database connection failures
- Invalid user inputs
- Missing configuration files
- SQL execution errors
- Network connectivity issues

## Development Notes

- Uses MySQL Connector for Python for database operations
- Implements prepared statements to prevent SQL injection
- Follows object-oriented programming principles
- Includes connection pooling and proper resource cleanup

## Future Enhancements

Potential improvements for future versions:
- Book return functionality
- Member search and management
- Overdue book tracking and fines
- Report generation
- Web-based interface
- Barcode scanning integration

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Verify MySQL server is running
   - Check database credentials in `database_config.py`
   - Ensure database exists

2. **Import Error for database_config**
   - Ensure `database_config.py` is in the same directory
   - Check file permissions

3. **Table doesn't exist error**
   - Run the database schema creation SQL commands
   - Verify table names match the code

## License

This project is open source and available for educational and personal use.

## Contact

For questions, suggestions, or support:
**Tharushi Umesha Mahipala**  
📧 umemahee@gmail.com

---

*Last updated: July 2025*
