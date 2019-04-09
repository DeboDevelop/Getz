import datetime
import sqlite3

def create():
    c.execute("""CREATE TABLE memo (
        ID Integer PRIMARY KEY AUTOINCREMENT,
        Description text,
        Dt integer
        )""")
conn = sqlite3.connect("project.db")

c = conn.cursor()

def insert_data(description, Dt):
    with conn:
        c.execute("INSERT INTO memo(Description, Dt) VALUES (:Description, :Dt)", {'Description': description, 'Dt': Dt})

def display_data():
    c.execute("SELECT * FROM memo")
    print(c.fetchall())

def delete_data(ID):
    with conn:
        c.execute("DELETE from memo WHERE ID = :ID", {'ID': ID}) 

def menu():
    #create()
    while True:
        description=str(input("Enter the description: "))
        date=int(input("Enter the date: "))
        month=int(input("Enter the month: "))
        year=int(input("Enter the year: "))
        hour=int(input("Enter the hour: "))
        minute=int(input("Enter the min: "))
        Dt = datetime.datetime(year, month, date, hour, minute, 0)
        insert_data(description, Dt)
        choice=int(input("Do you want to insert more. Please 0 for No and anything else for Yes: "))
        if(choice==0):
            break

    del_id=int(input("Enter the id to delete: "))
    delete_data(del_id)

    display_data()
    conn.close()

menu()
