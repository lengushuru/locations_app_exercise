import mysql.connector  as mysqlConnector

dataBase = mysqlConnector.connect(
    host="localhost",
    user = "root",
    passwd = "Lenguchally@12",
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE locations")

print("Database Created Successfully")
