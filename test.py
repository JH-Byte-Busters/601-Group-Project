import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def add_question_to_database(category, question_text, correct_answer):
    # Establish a connection to the database (replace 'your_database.db' with the actual database file name)
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("trivial_pursuit.db")

    if not db.open():
        print("Error: Unable to open database.")
        return

    # Prepare the SQL query to insert the question into the table
    query = QSqlQuery()
    query.prepare("INSERT INTO Questions (category, question_text, correct_answer) "
                  "VALUES (?, ?, ?)")

    # Bind the values to the placeholders in the query
    query.addBindValue(category)
    query.addBindValue(question_text)
    query.addBindValue(correct_answer)

    # Execute the query
    if not query.exec_():
        print("Error:", query.lastError().text())
    else:
        print("Question added successfully.")

    # Close the database connection
    db.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Sample data for multiple questions
    questions_data = [
        ("Science", "What is the capital of France?", "Paris"),
        ("Geography", "What is the longest river in the world?", "Nile"),
    ]

    # Loop through the questions data and add each question to the database
    for question_data in questions_data:
        add_question_to_database(*question_data)

    sys.exit(app.exec_())