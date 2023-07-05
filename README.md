# 601-Group-Project
Class project to exercise the skills and knowledge gained in the Foundations of Software Engineering class.

## Starting SQLite database
To create the database with create_db.py you must first ensure you have sqlite installed. See instructions [here](https://www.sqlitetutorial.net/download-install-sqlite/) based off your operating system.

Run the script using 'python3 create_db.py'. You then will have a file created called 'trivial_pursuit.db'. Start sqlite with this file and you will have a database that you can write to called 'trivial_pursuit.db'.

Database Structure is as follows

## Table (Users)
| `Name`      | `Data Type`             |
| ----------- | --------------------- |
| user_id   | INTEGER PRIMARY KEY AUTOINCREMENT|
| username   | TEXT NOT NULL|
| password   | TEXT NOT NULL|
| email   | TEXT NOT NULL|
| created_at   |  TIMESTAMP DEFAULT CURRENT_TIMESTAMP|
| position   | TEXT NOT NULL|

## Table (Questions)
| `Name`      | `Data Type`             |
| ----------- | --------------------- |
| question_id   | INTEGER PRIMARY KEY AUTOINCREMENT|
| category   | TEXT NOT NULL|
| question_text  | TEXT NOT NULL|
| correct_answer    | TEXT NOT NULL|
| incorrect_answers   |  TIMESTAMP DEFAULT CURRENT_TIMESTAMP| NOTE: Is this a timestamp? What is the rationale behind storing incorrect_answers?
| difficulty   | TEXT NOT NULL|

