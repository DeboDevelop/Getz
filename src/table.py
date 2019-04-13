import datetime
import sqlite3

def create():
    c.execute("""CREATE TABLE memo (
                ID Integer PRIMARY KEY AUTOINCREMENT,
                Description text,
                Remind integer,
                Dt integer
                )""")
    
conn = sqlite3.connect("projects.db")

c = conn.cursor()

def insert_data(Description, Remind, Dt=None):
    with conn:
        c.execute("INSERT INTO memo(Description, Remind, Dt) VALUES (:Description, :Remind, :Dt)", {'Description': Description, 'Remind':Remind, 'Dt': Dt})

def display_data():
    c.execute("SELECT * FROM memo")
    data=c.fetchall()
    for d in data:
        print(d[1], end=" ")
        print(d[3])

def delete_data(ID):
    with conn:
        c.execute("DELETE from memo WHERE ID = :ID", {'ID': ID}) 

def delete_all():
    with conn:
        c.execute("DELETE from memo") 

def sort_ascending():
    sort_data=[]
    c.execute("SELECT * FROM memo")
    data=c.fetchall()
    for d in data:
        sort_data.append(d[1])
    sort_data.sort()
    for d in sort_data:
        print(d)

def sort_descending():
    sort_data=[]
    c.execute("SELECT * FROM memo")
    data=c.fetchall()
    for d in data:
        sort_data.append(d[1])
    sort_data.sort()
    sort_data.reverse()
    for d in sort_data:
        print(d)

def menu():
    # create()
    # while True:
    #     Description=str(input("Enter the description: "))
    #     Remind = int(input("Do you want to Remind. Press 0 for No and Press 1 for Yes: "))
    #     if(Remind==1):
    #         date=int(input("Enter the date: "))
    #         month=int(input("Enter the month: "))
    #         year=int(input("Enter the year: "))
    #         hour=int(input("Enter the hour: "))
    #         minute=int(input("Enter the min: "))
    #         Dt = datetime.datetime(year, month, date, hour, minute, 0)
    #         insert_data(Description, Remind, Dt)
    #     elif(Remind==0):
    #         insert_data(Description, Remind)
    #     choice=int(input("Do you want to insert more. Press 0 for No and Press 1 for Yes: "))
    #     if(choice==0):
    #         break

    # del_id=int(input("Enter the id to delete: "))
    # delete_data(del_id)

    display_data()
    sort_ascending()
    sort_descending()
    delete_all()
    display_data()
    conn.close()

menu()

