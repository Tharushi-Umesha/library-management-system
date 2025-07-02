# Database Configuration File

# MySQL Database Configuration
DB_CONFIG ={
    'host':'localhost',
    'database':'library_management_system',
    'port':3306,
    'user':'root',
    'password':'enTER123456~',
    'charset':'utf8mb4',
    'autocommit':True,
     'collation': 'utf8mb4_unicode_ci'
}

# Admin Login Credentials
ADMIN_CONFIG ={
    'username':'admin',
    'password':'password123'
}

APP_CONFIG={
    'loan_period_days': 14,
    'max_books_per_member':5,
    'fine_per_day':1.0
}