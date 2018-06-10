""""
File: interface.py
Authors:
        Name                        Student ID        Major                                     Role
        Kilichbek Haydarov          16012676        Computer Science & Engineering              Project Manager
        Ulugbek Yusupov             Unknown         Computer Science & Engineering              Senior Developer
        Farrukh Yokubjanov          Unknown         Computer Science & Engineering              Junior Developer
        Bakhriddin                  Unknown         Business Administration                     Intern
        Gulchiroy                   Unknown         Computer Science & Engineering              Intern

Description: A program to help restaurant employees to manage and keep
            track of tables and orders from that tables, and calculate total
            prices. This program also provides the bar chart of daily income
            in a particular week

Version: 1.0.0

"""

import tkinter as tk
import tkinter.messagebox as tm
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import sqlite3 as lite
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


LARGE_FONT = ("Verdana", 12)
logged_in = False

class Root(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self,default="logo_icon.ico")
        tk.Tk.wm_title(self,"Restaurant Management System")

        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo,PageThree,LoginPage,Today,):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        if logged_in:
            self.show_frame(StartPage)
        else:
            self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Start Page",font=LARGE_FONT)
        label.pack(pady = 10,padx = 10)


        button1 = ttk.Button(self,text="Visit Page 1",
                            command=lambda:controller.show_frame(PageOne))
        button1.pack()
        button2 = ttk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button4 = ttk.Button(self, text="Visit Page 3",
                             command=lambda: controller.show_frame(PageThree))
        button4.pack()


        button3 = ttk.Button(self, text="Today",
                             command=lambda: controller.show_frame(Today))
        button3.pack()
        #TODO Fix the bug with displaying Matplotlib graph on main page
"""
        # Connection to Database and querying data from connected db
        con = lite.connect('incomes.db')
        cursor = con.execute("SELECT days,income from db_table")

        # Splitting each column
        a = cursor.fetchall()
        b = dict(a)
        plt.show()
        days = tuple(b.keys())
        y_pos = np.arange(len(days))
        incomes = list(b.values())

        # Attaching Data to window by using bar charts
        f = Figure(figsize=(5, 5), dpi=100)
        b = f.add_subplot(111)
        width = .5
        k = b.bar(days, incomes, width, align='center', alpha=1)
        plt.ylabel('INCOME')
        plt.title('WEEKLY INCOME')

        # Setting color of each bar column
        k[0].set_color('r')
        k[1].set_color('b')
        k[2].set_color('g')
        k[3].set_color('m')
        k[4].set_color('c')
        k[5].set_color('k')
        k[6].set_color('y')

        # Initializing canvas for our bar chart
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        #canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

"""
class Today(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Today Graph", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        button1 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Income Graph",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack()
        # Connection to Database and querying data from connected db
        con = lite.connect('incomes.db')
        cursor = con.execute("SELECT hours,hourly_income from today")

        # Splitting each column
        t = cursor.fetchall()
        b = dict(t)
        plt.show()
        hours = tuple(b.keys())
        y_pos = np.arange(len(hours))
        hourly_incomes = list(b.values())

        # Attaching Data to window by using line
        f = Figure(figsize=(5, 5), dpi=100)
        b = f.add_subplot(111)
        width = .5
        k = b.plot(hours, hourly_incomes)
        plt.ylabel('HOURS')
        plt.title('TODAY')

        # Initializing canvas for our bar chart
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page one", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Page Two",
                           command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page two", font=LARGE_FONT)
        self.grid()

        for r in range(6):
            self.master.rowconfigure(r, weight=1)

        Frame1 = tk.Frame(self, bg="red")
        Frame1.grid(row=0, column=0, rowspan=3, columnspan=2, sticky="WENS")
        Frame2 = tk.Frame(self)
        Frame2.grid(row=3, column=0, rowspan=3, columnspan=2, sticky="WENS")
        Frame3 = tk.Frame(self, bg="green")
        Frame3.grid(row=0, column=2, rowspan=6, columnspan=3, sticky="WENS")

        notebook = ttk.Notebook(Frame1)
        f1 = ttk.Frame(notebook)
        f2 = ttk.Frame(notebook)
        f3 = ttk.Frame(notebook)
        f4 = ttk.Frame(notebook)
        f5 = ttk.Frame(notebook)
        f6 = ttk.Frame(notebook)
        notebook.add(f1,text = 'Starter')
        notebook.add(f2,text = 'Main Menu')
        notebook.add(f3, text='Salad')
        notebook.add(f4, text='Pizza')
        notebook.add(f5, text='Desert')
        notebook.add(f6, text='Drink')
        notebook.grid(row=0, column=0, rowspan=3, columnspan=2, sticky="WENS")

        treeview = ttk.Treeview(f1)

        treeview.pack()
        treeview.config(columns = ('name','price'))
        treeview.heading('#0',text = '#')
        treeview.heading('name',text = 'Name')
        treeview.heading('price', text='Price')

        treeview.insert('', 'end', text="1", values=("French Fries","$3"))



        # set frame resize priorities
        f1.rowconfigure(0, weight=1)
        f1.columnconfigure(0, weight=1)

        self.listbox = tk.Listbox(Frame2)
        self.listbox.insert(1, "Table 1")
        self.listbox.insert(2, "Table 2")
        self.listbox.insert(3, "Table 3")
        self.listbox.insert(4, "Table 4")
        self.listbox.insert(5, "Table 5")
        self.listbox.insert(6, "Table 6")
        self.listbox.grid(row=1, column=0, rowspan=4, columnspan=2, sticky="WENS")
        self.listbox.focus()

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))

        button2 = ttk.Button(self, text="Page One",
                           command=lambda: controller.show_frame(PageOne))
        button1.grid(row=6, column=0, rowspan=1, columnspan=1, sticky="WENS")
        self.listbox.bind('<Double-1>', lambda event,frame = Frame2: self._addToMenu(event,frame))

    def _addToMenu(self,event,frame):

        labels = ["Table Number","Food Name"]
       # for i in range(4):

        label_username = tk.Label(frame, text=str(self.listbox.selection_get()))
        label_password = tk.Label(frame, text="Password")
        label_usernae = tk.Label(frame, text="Username")
        label_passwrd = tk.Label(frame, text="Password")

        label_username.grid(row=1,column = 2, sticky="E")
        label_password.grid(row=2,column = 2, sticky="E")

        entry_table = tk.Entry(frame)
        entry_food = tk.Entry(frame)
        entry_amount = tk.Entry(frame)
        entry_username = tk.Entry(frame)

        entry_table.grid(row=1, column=3)
        entry_food.grid(row=2, column=3)
        entry_amount.grid(row=3, column=3)
        entry_username.grid(row=4, column=3)

        dummy_buttons = []
        for i in range(4):
            button = ttk.Button(frame, text="Button")
            button.grid(row=i + 1, column=4, sticky="WENS")
            dummy_buttons.append(ttk.Button)
"""
        def _removeFromMenu():

        def _makeOrder():

        def _clear():

"""
class PageThree(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Three", font=LARGE_FONT)
        self.grid()

        for r in range(6):
            self.master.rowconfigure(r, weight=1)

        Frame1 = tk.Frame(self, bg="red")
        Frame1.grid(row=0, column=0, rowspan=3, columnspan=2, sticky="WENS")
        Frame2 = tk.Frame(self, bg="green")
        Frame2.grid(row=0, column=2, rowspan=6, columnspan=3, sticky="WENS")

        self.listbox = tk.Listbox(Frame1)
        self.listbox.insert(1, "Table 1")
        self.listbox.insert(2, "Table 2")
        self.listbox.insert(3, "Table 3")
        self.listbox.insert(4, "Table 4")
        self.listbox.insert(5, "Table 5")
        self.listbox.insert(6, "Table 6")
        self.listbox.grid(row=1, column=0, rowspan=4, columnspan=3, sticky="WENS")
        self.listbox.focus()
        self.listbox.bind('<Double-1>', lambda event, frame=Frame1: self.menuPopUpWindow(event, frame))
        self.listbox.bind('<<ListboxSelect>>', lambda event,frame=Frame2:self.onselect(event,frame))

        menu_button = ttk.Button(Frame1,text="Close Table",command = lambda: self.closeTable())
        menu_button.grid(row=5,column = 0,columnspan = 3,sticky="WENS")

    def closeTable(self):
        table = self.selection_get() #TODO Adding total price and date to database
        open("Files/"+table+".txt", 'w').close()
        self.treeview.delete(*self.treeview.get_children())

    def onselect(self,event,frame):
        self.treeview = ttk.Treeview(frame)
        self.treeview.grid(row=0, column=2, rowspan=6, columnspan=3, sticky="WENS")
        self.treeview.config(columns=('name', 'price','amount','total'))
        self.treeview.heading('#0', text='#')
        self.treeview.heading('name', text='Name')
        self.treeview.heading('price', text='Price')
        self.treeview.heading('amount', text='Amount')
        self.treeview.heading('total', text='Total')
        self.treeview.delete(*self.treeview.get_children())
        table = self.listbox.selection_get()
        total_price = 0.0
        file = open("Files/" + table + ".txt", "r")
        for line in file:
            food,price,amount,total = line.split("\t")
            self.treeview.insert('','end',text="1",values=(food,price,amount,total))
            total_price += float(total[1:])
        self.treeview.insert('','end',text="------",values=("-------","------","------",total_price))

        file.close()

    def menuPopUpWindow(self,event,frame):
        win = tk.Toplevel()
        win.wm_title("Menu")
        win.geometry("500x500+30+30")
        tabel_no = str(self.listbox.selection_get())
        l = tk.Label(win,text=tabel_no)
        l.grid(row=4,column=0)



        notebook = ttk.Notebook(win)
        f1 = ttk.Frame(notebook)
        f2 = ttk.Frame(notebook)
        f3 = ttk.Frame(notebook)
        f4 = ttk.Frame(notebook)
        f5 = ttk.Frame(notebook)
        f6 = ttk.Frame(notebook)
        notebook.add(f1, text='Starter')
        notebook.add(f2, text='Main Menu')
        notebook.add(f3, text='Salad')
        notebook.add(f4, text='Pizza')
        notebook.add(f5, text='Desert')
        notebook.add(f6, text='Drink')
        notebook.grid(row=0, column=0, rowspan=3, columnspan=2, sticky="WENS")

        self.treeview = ttk.Treeview(f1)

        self.treeview.pack()
        self.treeview.config(columns=('name', 'price'))
        self.treeview.heading('#0', text='#')
        self.treeview.heading('name', text='Name')
        self.treeview.heading('price', text='Price')

        self.treeview.insert('', 'end', text="1", values=("French Fries", "$3"))
        self.treeview.bind('<Double-1>',lambda x: self.amountPopUpWindow(event,table=tabel_no))

        # set frame resize priorities
        f1.rowconfigure(0, weight=1)
        f1.columnconfigure(0, weight=1)

        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.grid(row=5, column=0)

    def amountPopUpWindow(self,event,table):
        win = tk.Toplevel()
        win.wm_title("Amount")
        win.geometry("200x200+30+30")
        item = self.treeview.selection()[0]
        values = self.treeview.item(item)['values']
        food,price = values[0],float(values[-1][1:])
        l = tk.Label(win, text=food)
        l.grid(row=0, column=0)

        l1 = tk.Label(win, text=price)
        l1.grid(row=1, column=0)

        file = open("Files/"+table+".txt","a")
        file.write(food + "\t$"+str(price)+"\t"+str(4)+"\t$"+str(price*4)+"\n")

        file.close()


        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.grid(row=2, column=0)




class LoginPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.label_username = tk.Label(self,text="Username")
        self.label_password = tk.Label(self,text = "Password")
        self.label_username.grid(row=0, sticky="E")
        self.label_password.grid(row=1, sticky="E")


        self.entry_username = tk.Entry(self)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)


        self.checkbox = tk.Checkbutton(self,text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = tk.Button(self,text="Login",
                           command=lambda:self._login_btn_clicked(controller))
        self.logbtn.grid(columnspan=2)

    def _login_btn_clicked(self,controller):
        global logged_in
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "john" and password == "password":
            tm.showinfo("Login info", "Welcome John")
            logged_in = True
            controller.show_frame(StartPage)
        else:
            tm.showerror("Login error", "Incorrect username")
            logged_in = False



app = Root()
#app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(),
                                 # app.winfo_screenheight()))
app.mainloop()
