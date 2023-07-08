# 601-Group-Project
Class project to exercise the skills and knowledge gained in the Foundations of Software Engineering class.

## Starting SQLite database
To create the database with create_db.py you must first ensure you have sqlite installed. See instructions [here](https://www.sqlitetutorial.net/download-install-sqlite/) based off your operating system.

Run the script using 'python3 create_db.py'. You then will have a file created called 'trivial_pursuit.db'. Start sqlite with this file and you will have a database that you can write to called 'trivial_pursuit.db'.

The database Structure is as follows

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
| incorrect_answers   |  TIMESTAMP DEFAULT CURRENT_TIMESTAMP|
| difficulty   | TEXT NOT NULL|

## GUI Designing
For GUI design the tool used to generate and modify the .ui files is QT Designer, which can be installed [here](https://build-system.fman.io/qt-designer-download)

To learn more about QT Designer please visit: https://realpython.com/qt-designer-python/

Once the .ui file is created a Python file can be generated using the following command: <code>pyuic5 -x yourform.ui -o file.py</code>
