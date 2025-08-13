from tkinter import *   # for GUI
from  mydb import Database
from  tkinter import messagebox

class NLPApp:
    def __init__(self):
        # create  db object
        self.dbo=Database()   # self means  we can  use  multiple times variable

        # GUI of login
        self.root = Tk()
        self.root.title("NLPApp")
        self.root.iconbitmap("resources/favicon.ico")
        self.root.geometry("350x600")
        self.root.configure(bg="#34495E")
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()

        heading =Label(self.root,text="NLPApp",bg="#34495E",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=("verdana","24","bold"))

        label1=Label(self.root,text="Enter Email ")
        label1.pack(pady=(10,10))  # enter email paid

        self.email_input =Entry(self.root,width=50)    # we will  use  multiple times
        self.email_input.pack(pady=(5,10),ipady=4) # email checkbox length

        label2=Label(self.root, text="Enter Password")
        label2.pack(pady=(10,10))

        self.password_input=Entry(self.root,width=50,show="*")  # show * means  encrypted password
        self.password_input.pack(pady=(5,10),ipady=4)

        login_btn=Button(self.root,text="login",width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text="Not a member?")
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text="Register Now", command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#34495E", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", "24", "bold"))

        label0 = Label(self.root, text="Enter Name")
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)  # we will  use  multiple times
        self.name_input.pack(pady=(5, 10), ipady=4)


        label1 = Label(self.root, text="Enter Email")
        label1.pack(pady=(10, 10))  # enter email paid

        self.email_input = Entry(self.root, width=50)  # we will  use  multiple times
        self.email_input.pack(pady=(5, 10), ipady=4)  # email checkbox length

        label2 = Label(self.root, text="Enter Password")
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show="*")  # show * means  encrypted password
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text="Register", width=30, height=2,command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text="Already  a member?")
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text="Login Now", command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def  clear(self):            # it is very  important
        # clear the existing gui
        for i  in self.root.pack_slaves():
           i.destroy()    # for clear  screen after click on register  now  button

    def perform_registration(self):
        # fetch  data from gui
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()

        response =self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo("Success","Registration successful. You can  login  now")
        else:
            messagebox.showerror("Email already exists")  # for showing message   on gui

    def perform_login(self):
        email = self.email_input.get().strip()
        password = self.password_input.get().strip()
        response =self.dbo.search(email,password)

        if response:
            messagebox.showinfo("Success","Login successful")
        else:
            messagebox.showerror("error","Incorrect email/password")





nlp = NLPApp()


