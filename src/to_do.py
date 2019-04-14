#import table
from tkinter import *
import tkinter.messagebox as tmg
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import random
#from PIL import Image, ImageTk
import time

import datetime
import sqlite3

root = Tk()

root.configure(bg="gray25")
root.geometry('700x500')
root.title("To-Do App")


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
    return data
    # for d in data:
    #     print(d[1], end=" ")
    #     print(d[3])

def update_data(ID, Description):
    with conn:
        c.execute("""UPDATE memo SET Description = :Description
                    WHERE ID = :ID""",
                  {'ID': ID, 'Description': Description})

def update_dt(ID, Dt):
    with conn:
        c.execute("""UPDATE memo SET Dt = :Dt
                    WHERE ID = :ID""",
                  {'ID': ID, 'Dt': Dt})         


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
    #create()
    while True:
        Description=str(input("Enter the description: "))
        Remind = int(input("Do you want to Remind. Press 0 for No and Press 1 for Yes: "))
        if(Remind==1):
            date=int(input("Enter the date: "))
            month=int(input("Enter the month: "))
            year=int(input("Enter the year: "))
            hour=int(input("Enter the hour: "))
            minute=int(input("Enter the min: "))
            Dt = datetime.datetime(year, month, date, hour, minute, 0)
            insert_data(Description, Remind, Dt)
        elif(Remind==0):
            insert_data(Description, Remind)
        wish=int(input("Do you want to Update. Press 0 for No and Press 1 for Yes: "))
        if(wish==1):
            k=int(input("Press 0 for Update Description and Press 1 for Update Date&Time and Press 2 for Update Both: "))
            if(k==0):
                ID=int(input("Enter the ID to Update: "))
                Description=str(input("Enter the description: "))
                update_data(ID, Description)
            elif(k==1):
                ID=int(input("Enter the ID to Update: "))
                date=int(input("Enter the date: "))
                month=int(input("Enter the month: "))
                year=int(input("Enter the year: "))
                hour=int(input("Enter the hour: "))
                minute=int(input("Enter the min: "))
                Dt = datetime.datetime(year, month, date, hour, minute, 0)
                update_dt(ID, Dt)
            elif(k==2):
                ID=int(input("Enter the ID to Update: "))
                Description=str(input("Enter the description: "))
                date=int(input("Enter the date: "))
                month=int(input("Enter the month: "))
                year=int(input("Enter the year: "))
                hour=int(input("Enter the hour: "))
                minute=int(input("Enter the min: "))
                Dt = datetime.datetime(year, month, date, hour, minute, 0)
                update_data(ID, Description)
                update_dt(ID, Dt)
        choice=int(input("Do you want to Insert more. Press 0 for No and Press 1 for Yes: "))
        if(choice==0):
            break

    del_id=int(input("Enter the id to delete: "))
    delete_data(del_id)

    display_data()
    sort_ascending()
    sort_descending()
    conn.close()

menu()


# tasks=[]
'''tasks[] stores description of the events as list'''

'''This func. updates LISTBOX of the prog.'''
def update_listbox():
    clear_listbox()
    tasks=display_data()
    for task in tasks:
         lb_tasks.insert("end",task[1])
    '''the above loop inserts tasks from tasks[] to the LISTBOX'''
    '''instead of loop, it should read description WITH OR WITHOUT date and time'''
    '''Then insert description WITH OR WITHOUT date and time containing date and time to the list box from table'''

         
def clear_listbox():
    lb_tasks.delete(0,"end")

    
'''This func. Adds task'''
def add_task():
    
    '''This func. updates date'''
    def dateentry():
        def app_sel():
            print(cal.get_date())
            '''cal.get_date() gets the selected date in format YYYY-MM-DD'''
            '''command=print() func. should be changed to func. table_append_date()'''
        top = Toplevel(root)
        ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
        cal = DateEntry(top, font="Arial 14", selectmode='day', locale='en_US',cursor="hand2")
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=app_sel).pack()
        


    '''This func. updates time(Note- Still incomplete, to be done by AYAN, So no touching)'''
    def addtime():
        def print_sel():
            print(cal.get_date())
        bt = Toplevel(root)
        ttk.Label(bt, text='Choose time').pack(padx=10, pady=10)

        
        
    task = text_input.get(1.0,END).strip()
    '''task takes description'''
    
    if(task!=""):
        value = tmg.askquestion("Added task","Do you want to add timer?")
        '''Above line asks the user to add reminder or not'''
        '''if yes= description_append with date and time'''
        '''if no= description_append WITHOUT date and time'''
        if(value == 'yes'):
            '''add a func. to append_description WITH date and time from task'''
            newwin = Toplevel(root)
            
            ttk.Button(newwin, text='Date Entry', command=dateentry).pack(padx=10, pady=10)
            '''Calls dateentry()'''
            
            ttk.Button(newwin, text='Time', command=addtime).pack(padx=10, pady=10)
            '''Calls addtime()'''
            
        else:
            msg = "Ok! Fine!"
            tmg.showinfo("As your wish",msg)
            '''add a func. to append_description WITHOUT date and time from task'''
            
        tasks.append(task)
        update_listbox()
        text_input.delete(1.0,END)

        display["text"]="Display"
    else:
        display["text"]="Please! enter a task"
        
'''This func. Adds task by pressing enter'''
def add_task_with_enter(event):
    
    '''This func. updates date'''
    def dateentry():
        def app_sel():
            print(cal.get_date())
            '''cal.get_date() gets the selected date in format YYYY-MM-DD'''
            '''command=print() func. should be changed to func. table_append_date()'''
        top = Toplevel(root)
        ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
        cal = DateEntry(top, font="Arial 14", selectmode='day', locale='en_US',cursor="hand2")
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=app_sel).pack()

    '''This func. updates time(Note- Still incomplete, to be done by AYAN, So no touching)'''
    def addtime():
        def print_sel():
            print(cal.get_date())
        bt = Toplevel(root)
        ttk.Label(bt, text='Choose time').pack(padx=10, pady=10)
        
    
    task = text_input.get(1.0,END).strip()
    '''task takes description'''
    if(task!=""):
        value = tmg.askquestion("Added task","Do you want to add timer?")
        '''Above line asks the user to add reminder or not'''
        '''if yes= description_append with date and time'''
        '''if no= description_append WITHOUT date and time'''
        
        if(value == 'yes'):
            '''add a func. to append_description WITH date and time from task'''
            newwin = Toplevel(root)
            
            ttk.Button(newwin, text='Date Entry', command=dateentry).pack(padx=10, pady=10)
            '''Calls dateentry()'''
            ttk.Button(newwin, text='Time', command=addtime).pack(padx=10, pady=10)
            '''Calls addtime()'''
            
        else:
            msg = "Ok! Fine!"
            tmg.showinfo("As your wish",msg)
            '''add a func. to append_description WITHOUT date and time from task'''
            
        tasks.append(task)
        update_listbox()
        text_input.delete(1.0,END)

        display["text"]="Display"
    else:
        display["text"]="Please! enter a task"

        
def delete_all():
    global tasks
    tasks = []
    '''call func. to delete all the events in the table'''
    update_listbox()

def delete():
    task = lb_tasks.get("active")
    '''task stores the selected event to be deleted'''
    if task in tasks:
        tasks.remove(task)
        '''First check if the event to be deleted is present in table or not'''
        '''instead of remove(task),call del. func. to del. event from table'''
    update_listbox()
    
def sort_asc():
    tasks.sort()
    '''instead of tasks[].sort, call a func. to sort the events acc. to date and time in table'''
    update_listbox()

def sort_desc():
    tasks.sort()
    tasks.reverse()
    '''instead of tasks[].sort and .reverse(), call a func. to sort in desc. order the events acc. to date and time in table'''
    update_listbox()

def choose_random():
    task = random.choice(tasks)
    display["text"] = task
     
def number_of_tasks():
    num_of_tasks=len(tasks)
    '''instead of len(tasks), call a func. to return the no. of events in table'''
    msg = "Number of tasks: %s" % num_of_tasks
    display["text"]=msg

def upload():
    statusvar.set("Wait Please...")
    sbar.update()
    import time
    time.sleep(5)
    statusvar.set("Ready Now")

lbl_title = Label(root, text="To-Do List")
lbl_title.config(bg='black', fg='yellow')  
lbl_title.config(font=('bebas neue', 25))           
lbl_title.config(height=2)
lbl_title.pack(fill=X)

statusvar = StringVar()
sbar =Label(root, textvariable=statusvar, bg='khaki',relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)
upload()




#listbox

scrollbar = Scrollbar(root)  
scrollbar.pack(side = RIGHT, fill = Y)

lb_tasks = Listbox(root, width=82, height=14, bg='white',yscrollcommand = scrollbar.set)
lb_tasks.place(x = 150, y = 180)
scrollbar.config( command = lb_tasks.yview )



#other buttons

display = Label(root, text='Display', bg='khaki', width=80, fg='black' , font=("comicsanss", 10, "bold"))
display.place(x = 10, y = 100)


text_input = Text(root, height=1,width=65, bg="white", fg="black")
text_input.pack()
text_input.place(x = 10, y = 140)
text_input.bind("<Return>",add_task_with_enter)


btn_add_task = Button(root, text='Add task', command=add_task, width=10)
btn_add_task.place(x = 570, y = 140)

btn_delete = Button(root, text='Delete', command=delete, width=13)
btn_delete.place(x = 10, y = 180)

btn_delete_all = Button(root, text='Delete all', command=delete_all, width=13)
btn_delete_all.place(x = 10, y = 220)

btn_sort_asc = Button(root, text='Sort_asc',command=sort_asc, width=13)
btn_sort_asc.place(x = 10, y = 260)

btn_sort_desc = Button(root, text='Sort_desc', command=sort_desc, width=13)
btn_sort_desc.place(x = 10, y = 300)

btn_number_of_tasks = Button(root, text='Number of tasks', command= number_of_tasks, width=13)
btn_number_of_tasks.place(x = 10, y = 340)

button1= Button(root, text="EXIT",height=1 , width=12, command= root.destroy)
button1.pack(side=BOTTOM)

root.mainloop()
