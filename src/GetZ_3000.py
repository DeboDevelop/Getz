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

# note that there are many other schedulers available
from apscheduler.schedulers.background import BackgroundScheduler


sched = BackgroundScheduler()

def remind():
    conn = sqlite3.connect("projects.db")
    c = conn.cursor()
    c.execute("SELECT * FROM memo")
    data=c.fetchall()
    for task in data:
        c=0
        # print(task[3])
        if task[3]!= None:
            # print(type(Dt[3]))
            # print(Dt[3])
            current_date=str(datetime.datetime.now().replace(second=0,microsecond=0))
            # print(type(current_date))
            #print(current_date)
            if(task[3]==current_date and c==0):
                #Put the Pop-Up Here
                print("Yes")
                c+=1
                length=len(task[1])

                reminder = Toplevel(root)
                reminder.maxsize(length*6+100,140)
                reminder.minsize(length*6+100,140)
                reminder.title("Your Task")
        
                ttk.Label(reminder, text=task[1]).pack(padx=10, pady=10)
                Ok = Button(reminder, text="  Ok  ", command=reminder.destroy).pack(pady=40)
                
                
                

# seconds can be replaced with minutes, hours, or days
sched.add_job(remind, 'interval', seconds=59)
sched.start()

# sched.shutdown()

root = Tk()

root.configure(bg="gray25")
root.geometry('500x300')
root.title("To-Do Zone")


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
    c.execute("SELECT * FROM memo WHERE Description = :Description", {'Description': Description})
    data=c.fetchall()
    print(len(data))
    print(len(data)==0)
    if (len(data)==0):
        c.execute("INSERT INTO memo(Description, Remind, Dt) VALUES (:Description, :Remind, :Dt)", {'Description': Description, 'Remind':Remind, 'Dt': Dt})
        conn.commit()
        

def display_data():
    c.execute("SELECT * FROM memo")
    data=c.fetchall()
    # print(data)
    return data

def fetch_data(Description):
    c.execute("SELECT * FROM memo WHERE Description = :Description", {'Description': Description})
    data=c.fetchall()
    return data

def update_data(ID, Description):
    with conn:
        c.execute("""UPDATE memo SET Description = :Description
                    WHERE ID = :ID""",
                  {'ID': ID, 'Description': Description})

def update_dt(Description, Dt):
    with conn:
        c.execute("""UPDATE memo SET Dt = :Dt
                    WHERE Description = :Description""",
                  {'Description': Description, 'Dt': Dt})         


def delete_data(Description):
    with conn:
        c.execute("DELETE from memo WHERE Description = :Description", {'Description': Description})

def delete_all_data():
    with conn:
        c.execute("DELETE from memo") 

def sort_ascending():
    c.execute("SELECT * FROM memo")
    data=c.fetchall()
    for i in range(0,len(data)):
        data[i]=list(data[i])
        data[i][0]=0

    data.sort()
    return data

def sort_descending():
    c.execute("SELECT * FROM memo")
    data=c.fetchall()
    for i in range(0,len(data)):
        data[i]=list(data[i])
        data[i][0]=0
    data.sort()
    data.reverse()
    return data

def number_of_data():
    c.execute("SELECT * FROM memo")
    data=c.fetchall()
    return len(data)

# def menu():
#     #create()
#     while True:
#         Description=str(input("Enter the description: "))
#         Remind = int(input("Do you want to Remind. Press 0 for No and Press 1 for Yes: "))
#         if(Remind==1):
#             date=int(input("Enter the date: "))
#             month=int(input("Enter the month: "))
#             year=int(input("Enter the year: "))
#             hour=int(input("Enter the hour: "))
#             minute=int(input("Enter the min: "))
#             Dt = datetime.datetime(year, month, date, hour, minute, 0)
#             insert_data(Description, Remind, Dt)
#         elif(Remind==0):
#             insert_data(Description, Remind)
#         wish=int(input("Do you want to Update. Press 0 for No and Press 1 for Yes: "))
#         if(wish==1):
#             k=int(input("Press 0 for Update Description and Press 1 for Update Date&Time and Press 2 for Update Both: "))
#             if(k==0):
#                 ID=int(input("Enter the ID to Update: "))
#                 Description=str(input("Enter the description: "))
#                 update_data(ID, Description)
#             elif(k==1):
#                 ID=int(input("Enter the ID to Update: "))
#                 date=int(input("Enter the date: "))
#                 month=int(input("Enter the month: "))
#                 year=int(input("Enter the year: "))
#                 hour=int(input("Enter the hour: "))
#                 minute=int(input("Enter the min: "))
#                 Dt = datetime.datetime(year, month, date, hour, minute, 0)
#                 update_dt(ID, Dt)
#             elif(k==2):
#                 ID=int(input("Enter the ID to Update: "))
#                 Description=str(input("Enter the description: "))
#                 date=int(input("Enter the date: "))
#                 month=int(input("Enter the month: "))
#                 year=int(input("Enter the year: "))
#                 hour=int(input("Enter the hour: "))
#                 minute=int(input("Enter the min: "))
#                 Dt = datetime.datetime(year, month, date, hour, minute, 0)
#                 update_data(ID, Description)
#                 update_dt(ID, Dt)
#         choice=int(input("Do you want to Insert more. Press 0 for No and Press 1 for Yes: "))
#         if(choice==0):
#             break

#     del_id=int(input("Enter the id to delete: "))
#     delete_data(del_id)

#     display_data()
#     sort_ascending()
#     sort_descending()
    # conn.close()

tasks=[]
store=[]
'''tasks[] stores description of the events as list'''

'''This func. updates LISTBOX of the prog.'''
def update_listbox():
    clear_listbox()
    global tasks
    tasks=display_data()
    for task in tasks:
        # print(task[1])
        if (task[3]!=None):
            full_task = f"{task[3]}     ||     {task[1]}"
        else:
            full_task = f"                ---                  ||     {task[1]}"
        lb_tasks.insert("end",full_task)
        # print(task[1])
        # print(task[3])
    pos=0
    ln_tks = len(tasks)
    while pos is not ln_tks:
        color_sel(pos)
        pos+=1 
    '''the above loop inserts tasks from tasks[] to the LISTBOX'''
    '''instead of loop, it should read description WITH OR WITHOUT date and time'''
    '''Then insert description WITH OR WITHOUT date and time containing date and time to the list box from table'''

         
def clear_listbox():
    lb_tasks.delete(0,"end")

'''This func. Adds task'''

def color_sel(pos):
    if(pos%2 == 0):
        lb_tasks.itemconfig(pos, {'bg':'lightgrey'})
        lb_tasks.itemconfig(pos, {'fg':'black'})
    else:
        lb_tasks.itemconfig(pos, {'bg':'grey'})
        lb_tasks.itemconfig(pos, {'fg':'white'})
        
def add_task():
    '''This func. updates date'''
    def dateentry():
        
        def app_sel():
            a=(cal.get_date())
            year=a.strftime("%Y")
            month=a.strftime("%m")
            date=a.strftime("%d")
            #Dt = datetime.datetime(year, month, date, hour, minute, 0)
            Dt = datetime.datetime(int(year), int(month), int(date), 0, 0, 0)
            store.append( Dt)
            insert_data(task, 1, Dt)
            #####
            update_listbox()
            ######
            pos=0
            ln_tks = len(tasks)
            while pos is not ln_tks:
                color_sel(pos)
                pos+=1
            '''cal.get_date() gets the selected date in format YYYY-MM-DD'''
            '''command=print() func. should be changed to func. table_append_date()'''
            top.destroy()

        top = Toplevel(root)
        top.maxsize(200,140)
        top.minsize(200,140)
        top.title("Date-Entry")
        
        ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
        cal = DateEntry(top, font="Arial 14", selectmode='day', locale='en_US',cursor="hand2")
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=app_sel).pack()
        ttk.Button(top, text="EXIT", command=top.destroy).pack()


    '''This func. updates time(Note- Still incomplete, to be done by AYAN, So no touching)'''
    def addtime():
            
        top2 = Toplevel(root)
        top2.maxsize(280,200)
        top2.minsize(280,200)
        top2.title("Time")
        
        ttk.Label(top2, text='CHOOSE TIME').pack(padx=1, pady=10)
        
        tkvar1 = StringVar(top2)
        tkvar2 = StringVar(top2)
        #tkvar3 = StringVar(top2)
        tkvar4 = StringVar(top2)
        
        hour = []
        for i in range(1,10):
            a = f"0{i}"
            hour.append(a)
        for i in range(10,13):
            hour.append(i)
        set1 = "01"
        tkvar1.set(set1)
        
        minute = []
        
        for i in range(0,10):
            a = f"0{i}"
            minute.append(a)
        for i in range(10,60):
            minute.append(i)
        set2 = "00"
        tkvar2.set(set2)
        '''
        second = []
        for i in range(0,9):
            a = f"0{i}"
            second.append(a)
        for i in range(10,60):
            second.append(i)
        set3 = "00"
        tkvar3.set(set3)
        '''
        
        mode = ['AM', 'PM']
        tkvar4.set('AM')
         
        popupMenu1 = OptionMenu(top2, tkvar1, *hour)
        popupMenu1.place(x=16, y=40)
        
        popupMenu2 = OptionMenu(top2, tkvar2, *minute)
        popupMenu2.place(x=107, y=40)
        
        #popupMenu3 = OptionMenu(top2, tkvar3, *second)
        #popupMenu3.place(x=136, y=40)
        
        popupMenu4 = OptionMenu(top2, tkvar4, *mode)
        popupMenu4.place(x=197, y=40)

        ttk.Label(top2, text='  HOUR                    MIN                     AM/PM    ').pack(padx=16, pady=35)
        
        def change_dropdown(*args):
            print(f"{tkvar1.get()} : {tkvar2.get()}   {tkvar4.get()}")
            hour=int(tkvar1.get())
            minute=int(tkvar2.get())
            #second=int(tkvar3.get())
            day_night=tkvar4.get()
            if day_night=="PM" and hour!=12:
                hour+=12
            if hour==24:
                hour=0
            data=fetch_data(task)
            # print(data)
            # print(data[0][3])
            date_fetched=data[0][3]
            year=int(date_fetched[0:4])
            month=int(date_fetched[5:7])
            date=int(date_fetched[8:10])
            Dt = datetime.datetime(year, month, date, hour, minute)
            update_dt(task, Dt)
            update_listbox()
            # print(" ")
            # data=fetch_data(task)
            # print(data)
            # print(date_fetched[0:4])
            # print(date_fetched[5:7])
            # print(date_fetched[8:10])
            top2.destroy()

            
         
        #tkvar1.trace('w', change_dropdown)
        #tkvar2.trace('w', change_dropdown)
        #tkvar3.trace('w', change_dropdown)
        #tkvar4.trace('w', change_dropdown)
        Ok = Button(top2, text="     Ok     ", command=change_dropdown).place(x=107, y=131)
        Exit = Button(top2, text="    EXIT    ", command=top2.destroy).place(x=107, y=165)
        
    
    task = text_input.get()
    '''task takes description'''
    if(task!=""):
        value = tmg.askquestion("Added task","Do you want to add timer?")
        '''Above line asks the user to add reminder or not'''
        '''if yes= description_append with date and time'''
        '''if no= description_append WITHOUT date and time'''
        
        if(value == 'yes'):
            '''add a func. to append_description WITH date and time from task'''
            newwin = Toplevel(root)
            newwin.title("Timer-Set")
            newwin.maxsize(200,140)
            newwin.minsize(200,140)
            
            ttk.Button(newwin, text='Date Entry', command=dateentry).place(x=65, y=17)
            '''Calls dateentry()'''
            ttk.Button(newwin, text='Time', command=addtime).place(x=65, y=59)
            '''Calls addtime()'''
            ttk.Button(newwin, text='EXIT', command=newwin.destroy).place(x=65, y=100)
    
            
            
            
        else:
            msg = "Ok! Fine!"
            tmg.showinfo("As your wish",msg)
            '''add a func. to append_description WITHOUT date and time from task'''
            insert_data(task, 0)
            update_listbox()
        update_listbox()
        pos=0
        ln_tks = len(tasks)
        while pos is not ln_tks:
            color_sel(pos)
            pos+=1  
        text_input.delete(0,"end")

        display["text"]="Display"
    else:
        display["text"]="Please! enter a task"
        
'''This func. Adds task by pressing enter'''
def add_task_with_enter(event):
    add_task()

        
def delete_all():
    
    global tasks
    num_of_tasks=len(tasks)
    if(num_of_tasks == 0):
        display["text"]="Please! Enter a task!"
    else:
        value = tmg.askquestion("Delete All","Do you want to delete all tasks?")
        if(value=='yes'):
            delete_all_data()
            tasks = []
            update_listbox()
            display["text"]="Display"
            
            '''call func. to delete all the events in the table'''
            update_listbox()

def delete():
    global tasks
    num_of_tasks=len(tasks)
    if(num_of_tasks == 0):
        display["text"]="Please! Enter a task!"
    else:
        value = tmg.askquestion("Delete ","Do you want to delete this task?")
        if(value=='yes'):
            task = lb_tasks.get("active")
            index=task.find("||")
            print(index)
            task=task[index+7:]
            print(task)
            '''task stores the selected event to be deleted'''
            delete_data(task)
            tasks=[]
            '''First check if the event to be deleted is present in table or not'''
            '''instead of remove(task),call del. func. to del. event from table'''
            update_listbox()
            pos=0
            ln_tks = len(tasks)
            while pos is not ln_tks:
                color_sel(pos)
                pos+=1
                
def delete_key(event):
    delete()
    
def sort_asc():
    global tasks
    num_of_tasks=len(tasks)
    if(num_of_tasks == 0):
        display["text"]="Please! Enter a task!"
    else:
        
        tasks=sort_ascending()
        clear_listbox()
        '''instead of tasks[].sort, call a func. to sort the events acc. to date and time in table'''
        for task in tasks:
            if (task[3]!=None):
                full_task = f"{task[3]} || {task[1]}"
            else:
                full_task = f"--- || {task[1]}"
            lb_tasks.insert("end",full_task)
            
        pos=0
        ln_tks = len(tasks)
        while pos is not ln_tks:
            color_sel(pos)
            pos+=1  
        text_input.delete(0,"end")
        
def sort_desc():
    global tasks
    num_of_tasks=len(tasks)
    if(num_of_tasks == 0):
        display["text"]="Please! Enter a task!"
    else:
        tasks=sort_descending()
        clear_listbox()
        '''instead of tasks[].sort and .reverse(), call a func. to sort in desc. order the events acc. to date and time in table'''
        for task in tasks:
            if (task[3]!=None):
                full_task = f"{task[3]} || {task[1]}"
            else:
                full_task = f"--- || {task[1]}"
            lb_tasks.insert("end",full_task)
             
        pos=0
        ln_tks = len(tasks)
        while pos is not ln_tks:
            color_sel(pos)
            pos+=1  
        text_input.delete(0,"end")

# def choose_random():
#     task = random.choice(tasks)
#     display["text"] = task
     
def number_of_tasks():
    num_of_tasks=number_of_data()
    '''instead of len(tasks), call a func. to return the no. of events in table'''
    msg = "Number of tasks: %s" % num_of_tasks
    display["text"]=msg

def upload():
    statusvar.set("Loading... Wait Please...")
    sbar.update()
    import time
    time.sleep(5)
    root.maxsize(700,500)
    root.minsize(700, 500)
    statusvar.set("Ready Now")

lbl_title = Label(root, text="GetZ")
lbl_title.config(bg='black', fg='yellow')  
lbl_title.config(font=('bebas neue', 25))           
lbl_title.config(height=2)
lbl_title.pack(fill=X)

statusvar = StringVar()
sbar =Label(root, textvariable=statusvar, bg='khaki',relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)
#upload()




#listbox

scrollbar = Scrollbar(root)  
scrollbar.pack(side = RIGHT, fill = Y)

lb_tasks = Listbox(root, width=82, height=14, bg='white',yscrollcommand = scrollbar.set)
lb_tasks.place(x = 160, y = 180)
scrollbar.config( command = lb_tasks.yview )
lb_tasks.bind("<Delete>",delete_key)


#other buttons

display = Label(root, text='Display', bg='khaki', width=79, fg='black' , font=("comicsanss", 10, "bold"))
display.place(x = 22, y = 100)


text_input = Entry(root, width=85, bg="white", fg="black")
text_input.pack()
text_input.place(x = 22, y = 140)
text_input.bind("<Return>",add_task_with_enter)


btn_add_task = Button(root, text='Add task', command=add_task, width=13)
btn_add_task.place(x = 555, y = 138)

btn_delete = Button(root, text='Delete', command=delete, width=13)
btn_delete.place(x = 22, y = 178)

btn_delete_all = Button(root, text='Delete all', command=delete_all, width=13)
btn_delete_all.place(x = 22, y = 230)

btn_sort_asc = Button(root, text='Sort_asc',command=sort_asc, width=13)
btn_sort_asc.place(x = 22, y = 281)

btn_sort_desc = Button(root, text='Sort_desc', command=sort_desc, width=13)
btn_sort_desc.place(x = 22, y = 331)

btn_number_of_tasks = Button(root, text='Number of tasks', command= number_of_tasks, width=13)
btn_number_of_tasks.place(x = 22, y = 381)

button1= Button(root, text="EXIT",height=1 , width=12, command= root.destroy)
button1.pack(side=BOTTOM, pady=21)

update_listbox()
pos=0
ln_tks = len(tasks)
while pos is not ln_tks:
    color_sel(pos)
    pos+=1
    
root.mainloop()
