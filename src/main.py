from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
root= Tk()
root.title("Getz")
#root.iconbitmap(r'C:\projectGetz\mainicon.ico')

root.geometry("300x200")

def justPrint():
    print("Printing a New Message")

def recentevents():
    top = Toplevel(root)
    cal = Calendar(top, selectmode='none')
    
    #Changable
    date = cal.datetime.today() + cal.timedelta(days=2)
    cal.calevent_create(date, 'Hello World', 'message')
    cal.calevent_create(date, 'Reminder 2', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')
    cal.tag_config('reminder', background='red', foreground='yellow')
    
    cal.pack(fill="both", expand=True)
    ttk.Label(top, text="Hover over the events.").pack()

def opencallender():
    def print_sel():
        print(cal.selection_get())
    top = Toplevel(root)
    cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',cursor="hand2")
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

def dateentry():
    def print_sel():
        print(cal.get_date())
    top = Toplevel(root)
    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
    cal = DateEntry(top, width=12, background='darkblue',foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)
    ttk.Button(top, text="ok", command=print_sel).pack()

def addevents():
    
    def calender():
        def print_sel():
            print(cal.selection_get())
        top = Toplevel(root)
        cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',cursor="hand2")
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=print_sel).pack()

    def dateentry():
        def print_sel():
            print(cal.get_date())
        top = Toplevel(root)
        ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
        cal = DateEntry(top, width=12, background='darkblue',foreground='white', borderwidth=2)
        cal.pack(padx=10, pady=10)
        ttk.Button(top, text="ok", command=print_sel).pack()

    ttk.Button(root, text='Calendar', command=calender).pack(padx=10, pady=10)
    ttk.Button(root, text='DateEntry', command=dateentry).pack(padx=10, pady=10)



main_menu= Menu(root)
root.config(menu= main_menu)

#File Menu

fileMenu= Menu(main_menu,tearoff=0)
main_menu.add_cascade(label= "File", menu= fileMenu)

fileMenu.add_command(label="New", command=justPrint)
fileMenu.add_command(label="Open", command=justPrint)

save_menu= Menu(fileMenu, tearoff=0)
save_menu.add_command(label="save as new", command= justPrint)
save_menu.add_command(label="save Later", command= justPrint)
fileMenu.add_cascade(label="save", menu=save_menu)

fileMenu.add_separator()

#supportMenu(File)
support_menu= Menu(fileMenu, tearoff=0)
support_menu.add_command(label="Facebook", command= justPrint)
support_menu.add_command(label="GitHub", command= justPrint)
fileMenu.add_cascade(label="Support", menu=support_menu)


#Edit Menu
editMenu= Menu(main_menu,tearoff=0)
main_menu.add_cascade(label= "Edit", menu= editMenu)

editMenu.add_command(label="Saved Task", command=justPrint)
editMenu.add_command(label="Recent Task", command=justPrint)
editMenu.add_command(label="Current Task", command=justPrint)
editMenu.add_command(label="Completed", command=justPrint)



#Profile
profileMenu= Menu(main_menu, tearoff=0)
main_menu.add_cascade(label= "Profile", menu= profileMenu)
profileMenu.add_command(label="Edit Your Profile", command=justPrint)
profileMenu.add_separator()
profileMenu.add_command(label="Add New Account", command=justPrint)
profileMenu.add_command(label="Delete Current Account", command=justPrint)
profileMenu.add_command(label="Progress", command=justPrint)


#Callender
callenderMenu= Menu(main_menu,tearoff=0)
main_menu.add_cascade(label= "Callender", menu= callenderMenu)
callenderMenu.add_command(label="Open Callender", command=opencallender)
callenderMenu.add_separator()
callenderMenu.add_command(label="Add Events", command=addevents)
callenderMenu.add_command(label="Recent Events", command=recentevents)


#Help
helpMenu= Menu(main_menu,tearoff=0)
main_menu.add_cascade(label= "Help", menu= helpMenu)

helpMenu.add_command(label="About Getz", command=justPrint)
helpMenu.add_command(label="Getz Help", command=justPrint)

helpMenu.add_separator()

#social
visit_menu= Menu(helpMenu,tearoff=0)
visit_menu.add_command(label="Facebook", command= justPrint)
visit_menu.add_command(label="GitHub", command= justPrint)
helpMenu.add_cascade(label="Visit Our Page", menu= visit_menu)

root.mainloop()
