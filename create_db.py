#!/usr/bin/python3

import sqlite3
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Create a function to create the database and table
def create_database():
    # Create the SQLite database
    database = QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName("trivial_pursuit.db")

    if not database.open():
        print("Could not open the database!")
        return False

    # Create the "Users" table
    query = QSqlQuery()
    query.exec("CREATE TABLE IF NOT EXISTS Users ("
            "user_id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "username TEXT NOT NULL,"
            "password TEXT NOT NULL,"
            "email TEXT NOT NULL,"
            "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
           " position TEXT NOT NULL)")

    # Create the "Questions" table
    query.exec("CREATE TABLE IF NOT EXISTS Questions ("
               "question_id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "category TEXT NOT NULL,"
               "question_text TEXT NOT NULL,"
               "correct_answer TEXT NOT NULL,"
               "incorrect_answers TEXT NOT NULL,"
               "difficulty TEXT NOT NULL)")


    return True

# Create the QApplication instance
app = QApplication([])

# Call the create_database function to create the database and table
if create_database():
    print("Database and table created successfully!")

# Close the database connection
QSqlDatabase.database().close()
QSqlDatabase.removeDatabase("QSQLITE")