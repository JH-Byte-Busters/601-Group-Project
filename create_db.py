#!/usr/bin/python3

import sqlite3
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Create a function to create the database and table
def create_database():
    # Create the SQLite database
    database = QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName("trivial_pursuit2.db")

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
               "category TEXT CHECK(category IN ('Category1', 'Category2', 'Category3', 'Category4')) NOT NULL,"
               "question_text TEXT NOT NULL,"
               "correct_answer TEXT NOT NULL,"
               "incorrect_answers TEXT,"
               "difficulty TEXT)")

    query.exec("CREATE TABLE IF NOT EXISTS Categories ("
                "category_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "category_name TEXT NOT NULL UNIQUE)")

    return True, database

# Create the QApplication instance
app = QApplication([])

# Call the create_database function to create the database and table
if create_database():
    print("Database and table created successfully!")

# Create a function to create the database and table
def close_database(database):
    print("Database and table closed successfully!")
    # Close the database connection
    database.database().close()
    database.removeDatabase("QSQLITE")
    database.removeDatabase(database.database().connectionName())
