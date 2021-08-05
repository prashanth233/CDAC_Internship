import sqlite3

def createTable():
    connection = sqlite3.connect("new_login.db")
    connection.execute("CREATE TABLE USERS (USERNAME TEXT NOT NULL, EMAIL TEXT NOT NULL, PASSWORD TEXT NOT NULL)")
    connection.execute("INSERT INTO USERS VALUES(?,?,?)",('admin1827','admin@gmail.com','admin123'))
    connection.commit()
    result = connection.execute("SELECT * FROM USERS")

    for data in result:
        print("Username : ", data[0])
        print("Email Address : ", data[1])
        print("Password : ", data[2])
    connection.close()

createTable()

