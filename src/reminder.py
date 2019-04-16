import datetime
import sqlite3
import notify2

def remind():
    conn = sqlite3.connect("projects.db")
    c = conn.cursor()
    c.execute("SELECT * FROM memo")
    data=c.fetchall()
    notify2.init('Reminder')
    while True:
        for task in data:
            if task[3]!= None:
                # print(type(Dt[3]))
                # print(Dt[3])
                current_date=str(datetime.datetime.now().replace(microsecond=0))
                # print(type(current_date))
                # print(current_date)
                if(task[3]==current_date):
                    #Put the Pop-Up Here
                    print("Yes")
                    n = notify2.Notification('Reminder', task[1])
                    n.show()

remind()