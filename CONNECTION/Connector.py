import mysql.connector


class DBConnection:

    db = ""

    # Open database connection

    def __init__(self):
        self.db = mysql.connector.connect(user="root", password="kithsiri", host="localhost", database="nlp_compare")


    # Return DB Connection

    def getConnection(self):
        return self.db

