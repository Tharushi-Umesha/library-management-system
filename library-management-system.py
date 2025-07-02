import mysql.connector
from mysql.connector import Error
import datetime
from getpass import getpass
import os

# Try to import config, fall back to default if not available
try:
    from database_config import DB_CONFIG,ADMIN_CONFIG,APP_CONFIG
except ImportError:
    print("Database Config File not found!!")
    print("Please create database_config.py with your database settings.")
    exit(1)

#print("✅ Configuration loaded successfully!")

class LibraryManagementSystem:

    def __init__ (self):
        self.db_config = DB_CONFIG
        self.admin_username = ADMIN_CONFIG['username']
        self.admin_password = ADMIN_CONFIG['password']
        self.loan_period = APP_CONFIG['loan_period_days']
    
    def get_connection (self):
        """Create and return database connection"""
        try:
            connection = mysql.connector.connect(**self.db_config)
            if connection.is_connected():
                return connection
            
        except Error as e:
            print(f"❌ Error connecting to MySQL: {e}")
            return None
        
    def test_connection (self):
        """test database connection and show status"""
        print ("Testing database connection ....")
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT DATABASE()")
                db_name = cursor.fetchone()[0] # type: ignore
                cursor.execute("SELECT VERSION()")
                version = cursor.fetchone()[0] # type: ignore
                print(f"connected to the database:{db_name}")
                print(f"mysql version: {version}")

                 # Check if tables exist
                
                cursor.execute("show tables")
                tables = cursor.fetchall()
                if tables:
                    print(f"found {len(tables)} tables: {[table[0] for table in tables]}") # type: ignore
                else:
                    print("no tables found..")
                
                cursor.close()
                connection.close()
                return True
            
            except Error as e:
                print(f"database connection failed : {e}")
                connection.close()
                return False
            
        return False
        
    def admin_login (self):
        """Admin Login Funciton"""
        print("\n" + "="*40)
        print ("  ADMIN LOGIN  ")
        print("="*40)

        username= input("ENTER YOUR USERNAME::")
        password= input("ENTER YOUR PASSWORD::")

        if username == self.admin_username and password == self.admin_password:
            print("Login Successful...")
            return True
        
        else:
            print("Invalid Credentials ...")
            return False
        
    def add_members (self):
        """Add new member"""
        print ("\n"+"="*40)
        print("ADD A NEW MEMBER")
        print("="*40)

        name = input("ENTER NEW MEMBER NAME:").strip()

        if not name:
            print("Name Cannot be empty..")
            return
        
        phone =  input("ENTER YOUR PHONE NUMBER:").strip()
        email = input("ENTER YOUR EMAIL:").strip()

        connection = self.get_connection()

        if not connection:
            return
        
        cursor = connection.cursor()

        try:
            #check the memeber already in
            cursor.execute("SELECT member_name FROM members WHERE email =%s or phone =%s",(email,phone))
            if cursor.fetchone():
                print("MEEMBER ALREADY EXISTS..")
                return
            
            query = """INSERT INTO members (member_name,phone,email) VALUES (%s, %s, %s) """
            cursor.execute(query, (name,phone,email))
            print(f"member {name} added successfully")
            print(f"email: {email}")
            print(f"phone: {phone}")

        except Error as e:
            print(f"Failed to add member: {e}")

        finally:
            cursor.close()
            connection.close()

    
    def add_books(self):
        """Add New Books"""
        print("\n"+"="*40)
        print("ADD NEW BOOK")
        print("="*40)

        book_name= input("Enter new book Name: ").strip()

        if not book_name:
            print("Book name cannot be empty")
            return
        
        title = input("Enter Title of the book:  ").strip()
        theme = input("Enter theme of the book:  ").strip()
        author = input("Enter name of the author of the book:  ").strip()

        connection = self.get_connection()

        if not connection:
            return
        
        cursor = connection.cursor()

        try:
            query = """INSERT INTO books(book_name, title, theme, author) VALUES(%s, %s, %s, %s)"""
            print(f"Book: {book_name} added Successfully.")
            print (f"Author: {author}")
            print(f"theme: {theme}")
            print(f"title: {title}")

        except Error as e:
            print(f"Failed to add book: {e}")
        

        finally:
            cursor.close()
            connection.close()

    def admin_menu(self):
        while True:
            print("\n"+"="*60)
            print("Library Management system")
            print("="*60)
            print("1.ADD NEW MEMEBER")
            print("2.ADD A NEW BOOK")
            print("3.LOGOUT")
            print("="*60)

            choice = input("Enter your choice 1-10: ").strip()

            if choice == '1':
                self.add_members()
            elif choice == '2':
                self.add_books()
            elif choice == '3':
                print("Login Out")
                break
            else:
                print("Invalid choice.! Please enter a number from 1-10.")
            
            input("\n Press enter to continue")
    
    def run(self):
        """Main Applicaton Entry Point"""

        os.system('cls' if os.name == 'nt' else 'clear')

        print("="*60)
        print("Library Management System")
        print("="*60)

        #test database connection first

        if not self.test_connection():
            print("\n cannot proceed without connection")
            input("press enter to exist..")
            return
        
        print("System is ready..")

        while True:
            if self.admin_login():
                self.admin_menu()
            
            else:
                retry = input("\n Do you want to try Again? (y/n):  ")
                if retry.lower() != 'y':
                    break

        print("Thankyou for using Library Management System..")
        print("Remember to Backup your Database Regularly..")

    
def main():
    """Main FUnction To run the application"""
    try:
        library=LibraryManagementSystem()
        library.run()

    except KeyboardInterrupt:
        print("\n\n System Interuppt..GoodBye")
    
    except Exception as e:
        print(f"\n unexpected error : {e}")
        print("Please contact System Admin")


if __name__ == "__main__":
    main()

    

