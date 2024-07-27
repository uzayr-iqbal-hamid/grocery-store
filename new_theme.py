#GUI
from ast import Delete
#importing tkinter is the main step
from tkinter import *
from turtle import back, bgcolor, clear
#importing mysql connector
import mysql.connector as c


#Creating the canvas
root = Tk()
root.geometry("1600x900")
root.title("My Store Manager")
#root.iconbitmap(r'grocery store.ico')
root.configure(bg = "white")
groceryStore = Label(root, text = "GROCERY STORE",fg = "black",bg = "white", font = "Gabriola 45 bold")
groceryStore.place(x= 625,y =87)

entry1=Entry()
entry1.place(x=800,y=300,height=25)
enter_ID=Label(root,text="Enter Grocery Store Name:",fg="White",bg="#1877F2",font="Times")
enter_ID.place(x=600,y=300)
   
entry2=Entry(root, show="*")
entry2.place(x=800,y=350,height=25)
enter_ID=Label(root,text="Enter your Database Password:",fg="White",bg="#1877F2",font="Times")
enter_ID.place(x=600,y=350)
   
def access():
    E1=entry1.get()
    E2=entry2.get()
    conn=c.connect(host="localhost",user="root",passwd=E2)
    if conn.is_connected:
        f0= Frame()
        f0.place(x=0,y=0,width=1600,height= 900)
        f0.configure(bg = "white")
        #back button (the same thing repeated for all the buttons and frames)
        def back():
            f0.destroy()
        b1 = Button(f0,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
        b1.place(x=0,y=0)
        conn=c.connect(host="localhost",user="root",passwd=E2)
        mycsr=conn.cursor()
        l_dbases=[]
        mycsr.execute("SHOW DATABASES")
        for x in mycsr:
           l_dbases.append(x[0])
        if 'grocery_store' in l_dbases:
            conn=c.connect(host="localhost",user="root",passwd=E2,database="grocery_store")
            mycsr=conn.cursor
        else:
            mycsr.execute("CREATE DATABASE grocery_store")
        mycsr=conn.cursor()

        l_tables=[]
        mycsr.execute("SHOW TABLES")
        for x in mycsr:
            l_tables.append(x[0])

        #inventory    
        if 'inv_cook' not in l_tables:
            mycsr.execute("Create table inv_cook (item_code varchar(10) primary key , item_name varchar(250) not null, cost_price int not null, selling_price int not null, quantity int not null, expiry_date varchar(11) not null)")
           
        if 'inv_house' not in l_tables:
            mycsr.execute("Create table inv_house (item_code varchar(10) primary key , item_name varchar(250) not null, cost_price int not null, selling_price int not null, quantity int not null, expiry_date varchar(11) not null)")

        if 'inv_snacks' not in l_tables:
            mycsr.execute("Create table inv_snacks (item_code varchar(10) primary key , item_name varchar(250) not null, cost_price int not null, selling_price int not null, quantity int not null, expiry_date varchar(11) not null)")
           
        if 'inv_beauty' not in l_tables:
            mycsr.execute("Create table inv_beauty (item_code varchar(10) primary key , item_name varchar(250) not null, cost_price int not null, selling_price int not null, quantity int not null, expiry_date varchar(11) not null)")

        if 'inv_drinks' not in l_tables:
            mycsr.execute("Create table inv_drinks (item_code varchar(10) primary key , item_name varchar(250) not null, cost_price int not null, selling_price int not null, quantity int not null, expiry_date varchar(11) not null)")

        if 'inv_stationery' not in l_tables:
            mycsr.execute("Create table inv_stationery (item_code varchar(10) primary key , item_name varchar(250) not null, cost_price int not null, selling_price int not null, quantity int not null, expiry_date varchar(11) not null)")
           
        #customer
        if 'cust_details' not in l_tables:
            mycsr.execute("Create table cust_details (cust_code char(4) primary key , cust_name varchar(250) not null, contact_no char(10) not null, ledger_id varchar(10) not null)")

        #ledger
        if 'led_details' not in l_tables:
            mycsr.execute("Create table led_details (Led_id char(4) primary key , cust_name varchar(250) not null, amt_to_pay int not null, date_edited char(11) not null)")
        #billing
        if 'bill' not in l_tables:
            mycsr.execute("Create table bill (item_code char(4) primary key , Quantity int not null, total_price int not null)")
        #Store Management Button
        def store(x,y,text,bcolor,fcolor,new):

            def on_enter(e):
                mybutton['background']=bcolor
                mybutton['foreground']=fcolor

            def on_leave(e):
                mybutton['background']=fcolor
                mybutton['foreground']=bcolor
            head=Label(f0, text =E1,fg = "black",bg = "white", font = "Gabriola 45 bold").pack()

            mybutton=Button(f0,width=42,height=4,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=new,)
           
            mybutton.bind("<Enter>",on_enter)
            mybutton.bind("<Leave>",on_leave)

            mybutton.place(x=x,y=y)
        #Command for store management button
        def new():
            first_frame = Frame()
            first_frame.place(x=0,y=0,width=1600,height= 900)
            first_frame.configure(bg = "white")
            #back button (the same thing repeated for all the buttons and frames)
            def back():
                first_frame.destroy()
            b1 = Button(first_frame,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
            b1.place(x=0,y=0)
            Menu = Label(first_frame, text = "MENU",fg = "black",bg = "white", font = "Gabriola 45 bold").pack()

            #Inventory Button (Inside the store button)
            def inventory(x,y,text,bcolor,fcolor,inv):

                def on_enter(e):
                    mybutton['background']=bcolor
                    mybutton['foreground']=fcolor

                def on_leave(e):
                    mybutton['background']=fcolor
                    mybutton['foreground']=bcolor

                mybutton=Button(first_frame,width=42,height=4,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=inv,)
           
                mybutton.bind("<Enter>",on_enter)
                mybutton.bind("<Leave>",on_leave)

                mybutton.place(x=x,y=y)
            #Command for Inventory button
            def inv():
                f1 = Frame()
                f1.place(x=0,y=0,width=1600,height= 900)
                f1.configure(bg = "white")
                label = Label(f1, text = "Categories",bg="white",fg="black",font="Impact 40")
                label.place(x=675,y=45)
                #back button
                def back():
                    f1.destroy()
                b1 = Button(f1,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                b1.place(x=0,y=0)

                #Cooking Essentials Button (Inside the inventory button)
                def Cook(x,y,text,bcolor,fcolor,cook):

                    def on_enter(e):
                        mybutton['background']=bcolor
                        mybutton['foreground']=fcolor

                    def on_leave(e):
                        mybutton['background']=fcolor
                        mybutton['foreground']=bcolor

                    mybutton=Button(f1,width=42,height=6,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=cook,)
           
                    mybutton.bind("<Enter>",on_enter)
                    mybutton.bind("<Leave>",on_leave)

                    mybutton.place(x=x,y=y)
                #Command for cooking essentials button
                def cook():
                    f2 = Frame()
                    f2.place(x=0,y=0,width=1600,height= 900)
                    f2.configure(bg = "white")
                 
                    #back button
                    def back():
                        f2.destroy()
                    b1 = Button(f2,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                    b1.place(x=0,y=0)
               
                    def add_items(x,y,text,bcolor,fcolor,add):

                        def on_enter(e):
                            mybutton['background']=bcolor
                            mybutton['foreground']=fcolor

                        def on_leave(e):
                            mybutton['background']=fcolor
                            mybutton['foreground']=bcolor

                        mybutton=Button(f2,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                        border=0,
                                        activeforeground=fcolor,
                                        activebackground=bcolor,
                                        command=add,)
                        mybutton.bind("<Enter>",on_enter)
                        mybutton.bind("<Leave>",on_leave)

                        mybutton.place(x=x,y=y)
                   
                    def add():
                        f3 = Frame()
                        f3.place(x=0,y=0,width=1600,height= 900)
                        f3.configure(bg = "white")

                       
                        entry1=Entry()
                        entry1.place(x=800,y=300,height=25)
                        enter_ID=Label(f3,text="Item Code:",fg="White",bg="#1877F2",font="Times")
                        enter_ID.place(x=600,y=300)

                        entry2=Entry()
                        entry2.place(x=800,y=350,height=25)
                        enter_name=Label(f3,text="Item Name:",fg="white",bg="#1877F2",font="Times")
                        enter_name.place(x=600,y=350)

                        entry3=Entry()
                        entry3.place(x=800,y=400,height=25)
                        enter_contact=Label(f3,text="Cost Price:",fg="white",bg="#1877F2",font="Times")
                        enter_contact.place(x=600,y=400)

                        entry4=Entry()
                        entry4.place(x=800,y=450,height=25)
                        enter_ledgerID=Label(f3,text="Selling Price:",fg="white",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=450)
                       
                        entry5=Entry()
                        entry5.place(x=830,y=500,height=25)
                        enter_ledgerID=Label(f3,text="Quantity:",fg="White",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=500)
                       
                        entry6=Entry()
                        entry6.place(x=830,y=550,height=25)
                        enter_ledgerID=Label(f3,text="Date of Expiry(DD-MM-YYYY)",fg="White",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=550)

                           

                        def sub():
                            E1=entry1.get()
                            E2=entry2.get()
                            E3=entry3.get()
                            E4=entry4.get()
                            E5=entry5.get()
                            E6=entry6.get()
                            sql = "INSERT INTO inv_cook VALUES (%s, %s, %s, %s, %s, %s)"
                            values=(E1,E2,int(E3),int(E4),int(E5),E6)
                            mycsr.execute(sql, values)
                            conn.commit()
                            entry1.delete(0, END)
                            entry2.delete(0, END)
                            entry3.delete(0, END)
                            entry4.delete(0, END)
                            entry5.delete(0, END)
                            entry6.delete(0, END)
                               

                       
                        t = Button(f3,text="Submit",fg="black",bg="white",font="arahoni 10 bold",command=sub,)
                        t.place(x=750,y=600)    
                       
                        def back():
                            entry1.destroy()
                            entry2.destroy()
                            entry3.destroy()
                            entry4.destroy()
                            entry5.destroy()
                            entry6.destroy()
                            f3.destroy()
                        b1 = Button(f3,width = 21,height = 2,text = "<--",
                            border = 0,
                            fg='cyan',
                            bg='black',
                            activeforeground='black',
                            activebackground='cyan',
                            command = back)
                        b1.place(x=0,y=0)

                    add_items(650,250,"ADD ITEMS",'cyan',"black",add)
                   
                    def view_items(x,y,text,bcolor,fcolor,view):

                        def on_enter(e):
                            mybutton['background']=bcolor
                            mybutton['foreground']=fcolor

                        def on_leave(e):
                            mybutton['background']=fcolor
                            mybutton['foreground']=bcolor

                        mybutton=Button(f2,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                        border=0,
                                        activeforeground=fcolor,
                                        activebackground=bcolor,
                                        command=view,)
                        mybutton.bind("<Enter>",on_enter)
                        mybutton.bind("<Leave>",on_leave)

                        mybutton.place(x=x,y=y)
                   
                    def view():
                        f3 = Frame()
                        f3.place(x=0,y=0,width=1600,height= 900)
                        f3.configure(bg = "white")
                        scroll_bar=Scrollbar(f3)
                        scroll_bar.pack( side = RIGHT, fill = Y )
                        Head=Label(f3,text="Cooking Items Available",fg="white",bg="#1877F2",font="Times 30")
                        Head.pack()
                        mycsr.execute("select * from inv_cook")
                        myres=mycsr.fetchall()
                        x=500
                        y=210
                        note=Label(f3,text="DATA IN THE FORM:",fg="white",bg="#1877F2",font="Times 20").place(x=500,y=115)
                        h=('Item Code | Item Name | Cost Price | Selling Price | Quantity | Expiry Date')
                        hl=Label(f3,text=h,fg="white",bg="#1877F2",font="Times 20").place(x=500,y=150)
                        for rec in myres:
                            Out=Label(f3,text=rec,fg="white",bg="#1877F2",font="Times 20")
                            Out.place(x=x,y=y)
                            y+=40
                           
                        def back():
                            f3.destroy()
                        b1 = Button(f3,width = 21,height = 2,text = "<--",
                            border = 0,
                            fg='cyan',
                            bg='black',
                            activeforeground='black',
                            activebackground='cyan',
                            command = back)
                        b1.place(x=0,y=0)
                       
                    view_items(650,350,"VIEW ITEMS",'cyan',"black",view)
                   
                   
                   
                Cook(200,150,"COOKING ESSENTIALS",'cyan',"black",cook)
                     

                #Household Supplies Button (Inside the inventory button)
                def House(x,y,text,bcolor,fcolor,house):

                    def on_enter(e):
                        mybutton['background']=bcolor
                        mybutton['foreground']=fcolor

                    def on_leave(e):
                        mybutton['background']=fcolor
                        mybutton['foreground']=bcolor

                    mybutton=Button(f1,width=42,height=6,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=house,)
           
                    mybutton.bind("<Enter>",on_enter)
                    mybutton.bind("<Leave>",on_leave)

                    mybutton.place(x=x,y=y)
                #Command for household supplies button
                def house():
                    f2 = Frame()
                    f2.place(x=0,y=0,width=1600,height= 900)
                    f2.configure(bg = "white")
                    #back button
                    def back():
                        f2.destroy()
                    b1 = Button(f2,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                    b1.place(x=0,y=0)
                   
                    def add_items(x,y,text,bcolor,fcolor,add):

                        def on_enter(e):
                            mybutton['background']=bcolor
                            mybutton['foreground']=fcolor

                        def on_leave(e):
                            mybutton['background']=fcolor
                            mybutton['foreground']=bcolor

                        mybutton=Button(f2,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                        border=0,
                                        activeforeground=fcolor,
                                        activebackground=bcolor,
                                        command=add,)
                        mybutton.bind("<Enter>",on_enter)
                        mybutton.bind("<Leave>",on_leave)

                        mybutton.place(x=x,y=y)
                   
                    def add():
                        f3 = Frame()
                        f3.place(x=0,y=0,width=1600,height= 900)
                        f3.configure(bg = "white")

                       
                        entry1=Entry()
                        entry1.place(x=800,y=300,height=25)
                        enter_ID=Label(f3,text="Item Code:",fg="White",bg="#1877F2",font="Times")
                        enter_ID.place(x=600,y=300)

                        entry2=Entry()
                        entry2.place(x=800,y=350,height=25)
                        enter_name=Label(f3,text="Item Name:",fg="white",bg="#1877F2",font="Times")
                        enter_name.place(x=600,y=350)

                        entry3=Entry()
                        entry3.place(x=800,y=400,height=25)
                        enter_contact=Label(f3,text="Cost Price",fg="white",bg="#1877F2",font="Times")
                        enter_contact.place(x=600,y=400)

                        entry4=Entry()
                        entry4.place(x=800,y=450,height=25)
                        enter_ledgerID=Label(f3,text="Selling Price",fg="white",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=450)
                       
                        entry5=Entry()
                        entry5.place(x=830,y=500,height=25)
                        enter_ledgerID=Label(f3,text="Quantity:",fg="White",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=500)
                       
                        entry6=Entry()
                        entry6.place(x=830,y=550,height=25)
                        enter_ledgerID=Label(f3,text="Date of Expiry(DD-MM-YYYY)",fg="White",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=550)

                           

                        def sub():
                            E1=entry1.get()
                            E2=entry2.get()
                            E3=entry3.get()
                            E4=entry4.get()
                            E5=entry5.get()
                            E6=entry6.get()
                            sql = "INSERT INTO inv_house VALUES (%s, %s, %s, %s, %s, %s)"
                            values=(E1,E2,int(E3),int(E4),int(E5),E6)
                            mycsr.execute(sql, values)
                            conn.commit()
                            entry1.delete(0, END)
                            entry2.delete(0, END)
                            entry3.delete(0, END)
                            entry4.delete(0, END)
                            entry5.delete(0, END)
                            entry6.delete(0, END)
                               

                       
                        t = Button(f3,text="Submit",fg="black",bg="white",font="arahoni 10 bold",command=sub,)
                        t.place(x=750,y=600)    
                       
                        def back():
                            entry1.destroy()
                            entry2.destroy()
                            entry3.destroy()
                            entry4.destroy()
                            entry5.destroy()
                            entry6.destroy()
                            f3.destroy()
                        b1 = Button(f3,width = 21,height = 2,text = "<--",
                            border = 0,
                            fg='cyan',
                            bg='black',
                            activeforeground='black',
                            activebackground='cyan',
                            command = back)
                        b1.place(x=0,y=0)

                    add_items(650,250,"ADD ITEMS",'cyan',"black",add)
                   
                    def view_items(x,y,text,bcolor,fcolor,view):

                        def on_enter(e):
                            mybutton['background']=bcolor
                            mybutton['foreground']=fcolor

                        def on_leave(e):
                            mybutton['background']=fcolor
                            mybutton['foreground']=bcolor

                        mybutton=Button(f2,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                        border=0,
                                        activeforeground=fcolor,
                                        activebackground=bcolor,
                                        command=view,)
                        mybutton.bind("<Enter>",on_enter)
                        mybutton.bind("<Leave>",on_leave)

                        mybutton.place(x=x,y=y)
                   
                    def view():
                        f3 = Frame()
                        f3.place(x=0,y=0,width=1600,height= 900)
                        f3.configure(bg = "white")
                        scroll_bar=Scrollbar(f3)
                        scroll_bar.pack( side = RIGHT, fill = Y )
                        Head=Label(f3,text="Household Items Available",fg="white",bg="#1877F2",font="Times 30")
                        Head.pack()
                        mycsr.execute("select * from inv_house")
                        myres=mycsr.fetchall()
                        x=500
                        y=210
                        note=Label(f3,text="DATA IN THE FORM:",fg="white",bg="#1877F2",font="Times 20").place(x=500,y=115)
                        h=('Item Code | Item Name | Cost Price | Selling Price | Quantity | Expiry Date')
                        hl=Label(f3,text=h,fg="white",bg="#1877F2",font="Times 20").place(x=500,y=150)
                        for rec in myres:
                            Out=Label(f3,text=rec,fg="white",bg="#1877F2",font="Times 20")
                            Out.place(x=x,y=y)
                            y+=40
                           
                        def back():
                            f3.destroy()
                        b1 = Button(f3,width = 21,height = 2,text = "<--",
                            border = 0,
                            fg='cyan',
                            bg='black',
                            activeforeground='black',
                            activebackground='cyan',
                            command = back)
                        b1.place(x=0,y=0)
                       
                    view_items(650,350,"VIEW ITEMS",'cyan',"black",view)

                House(650,150,"HOUSEHOLD SUPPLIES",'cyan',"black",house)

                #Snacks Button (Insider the inventory button)
                def Snacks(x,y,text,bcolor,fcolor,snack):

                        def on_enter(e):
                            mybutton['background']=bcolor
                            mybutton['foreground']=fcolor

                        def on_leave(e):
                            mybutton['background']=fcolor
                            mybutton['foreground']=bcolor

                        mybutton=Button(f1,width=42,height=6,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=snack,)
           
                        mybutton.bind("<Enter>",on_enter)
                        mybutton.bind("<Leave>",on_leave)

                        mybutton.place(x=x,y=y)
                #Command for snacks button
                def snack():
                    f2 = Frame()
                    f2.place(x=0,y=0,width=1600,height= 900)
                    f2.configure(bg = "white")
                    def back():
                        f2.destroy()
                    b1 = Button(f2,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                    b1.place(x=0,y=0)
                   
                    def add_items(x,y,text,bcolor,fcolor,add):

                        def on_enter(e):
                            mybutton['background']=bcolor
                            mybutton['foreground']=fcolor

                        def on_leave(e):
                            mybutton['background']=fcolor
                            mybutton['foreground']=bcolor

                        mybutton=Button(f2,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                        border=0,
                                        activeforeground=fcolor,
                                        activebackground=bcolor,
                                        command=add,)
                        mybutton.bind("<Enter>",on_enter)
                        mybutton.bind("<Leave>",on_leave)

                        mybutton.place(x=x,y=y)
                   
                    def add():
                        f3 = Frame()
                        f3.place(x=0,y=0,width=1600,height= 900)
                        f3.configure(bg = "white")

                       
                        entry1=Entry()
                        entry1.place(x=800,y=300,height=25)
                        enter_ID=Label(f3,text="Item Code:",fg="White",bg="#1877F2",font="Times")
                        enter_ID.place(x=600,y=300)

                        entry2=Entry()
                        entry2.place(x=800,y=350,height=25)
                        enter_name=Label(f3,text="Item Name:",fg="white",bg="#1877F2",font="Times")
                        enter_name.place(x=600,y=350)

                        entry3=Entry()
                        entry3.place(x=800,y=400,height=25)
                        enter_contact=Label(f3,text="Cost Price",fg="white",bg="#1877F2",font="Times")
                        enter_contact.place(x=600,y=400)

                        entry4=Entry()
                        entry4.place(x=800,y=450,height=25)
                        enter_ledgerID=Label(f3,text="Selling Price",fg="white",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=450)
                       
                        entry5=Entry()
                        entry5.place(x=830,y=500,height=25)
                        enter_ledgerID=Label(f3,text="Quantity:",fg="White",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=500)
                       
                        entry6=Entry()
                        entry6.place(x=830,y=550,height=25)
                        enter_ledgerID=Label(f3,text="Date of Expiry(DD-MM-YYYY)",fg="White",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=550)
                           

                        def sub():
                            E1=entry1.get()
                            E2=entry2.get()
                            E3=entry3.get()
                            E4=entry4.get()
                            E5=entry5.get()
                            E6=entry6.get()
                            sql = "INSERT INTO inv_snacks VALUES (%s, %s, %s, %s, %s, %s)"
                            values=(E1,E2,int(E3),int(E4),int(E5),E6)
                            mycsr.execute(sql, values)
                            conn.commit()
                            entry1.delete(0, END)
                            entry2.delete(0, END)
                            entry3.delete(0, END)
                            entry4.delete(0, END)
                            entry5.delete(0, END)
                            entry6.delete(0, END)
                               

                       
                        t = Button(f3,text="Submit",fg="black",bg="white",font="arahoni 10 bold",command=sub,)
                        t.place(x=750,y=600)    
                       
                        def back():
                            entry1.destroy()
                            entry2.destroy()
                            entry3.destroy()
                            entry4.destroy()
                            entry5.destroy()
                            entry6.destroy()
                            f3.destroy()
                        b1 = Button(f3,width = 21,height = 2,text = "<--",
                            border = 0,
                            fg='cyan',
                            bg='black',
                            activeforeground='black',
                            activebackground='cyan',
                            command = back)
                        b1.place(x=0,y=0)

                    add_items(650,250,"ADD ITEMS",'cyan',"black",add)
                   
                    def view_items(x,y,text,bcolor,fcolor,view):

                        def on_enter(e):
                            mybutton['background']=bcolor
                            mybutton['foreground']=fcolor

                        def on_leave(e):
                            mybutton['background']=fcolor
                            mybutton['foreground']=bcolor

                        mybutton=Button(f2,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                        border=0,
                                        activeforeground=fcolor,
                                        activebackground=bcolor,
                                        command=view,)
                        mybutton.bind("<Enter>",on_enter)
                        mybutton.bind("<Leave>",on_leave)

                        mybutton.place(x=x,y=y)
                   
                    def view():
                        f3 = Frame()
                        f3.place(x=0,y=0,width=1600,height= 900)
                        f3.configure(bg = "white")
                        scroll_bar=Scrollbar(f3)
                        scroll_bar.pack( side = RIGHT, fill = Y )
                        Head=Label(f3,text="Snacks Items Available",fg="white",bg="#1877F2",font="Times 30")
                        Head.pack()
                        mycsr.execute("select * from inv_snacks")
                        myres=mycsr.fetchall()
                        x=500
                        y=210
                        note=Label(f3,text="DATA IN THE FORM:",fg="white",bg="#1877F2",font="Times 20").place(x=500,y=115)
                        h=('Item Code | Item Name | Cost Price | Selling Price | Quantity | Expiry Date')
                        hl=Label(f3,text=h,fg="white",bg="#1877F2",font="Times 20").place(x=500,y=150)
                        for rec in myres:
                            Out=Label(f3,text=rec,fg="white",bg="#1877F2",font="Times 20")
                            Out.place(x=x,y=y)
                            y+=40
                           
                        def back():
                            f3.destroy()
                        b1 = Button(f3,width = 21,height = 2,text = "<--",
                            border = 0,
                            fg='cyan',
                            bg='black',
                            activeforeground='black',
                            activebackground='cyan',
                            command = back)
                        b1.place(x=0,y=0)
                       
                    view_items(650,350,"VIEW ITEMS",'cyan',"black",view)

                Snacks(1100,150,"SNACKS",'cyan',"black",snack)

                #Beauty and Personal Button (Insider the inventory button)
                def Beauty(x,y,text,bcolor,fcolor,beauty):

                    def on_enter(e):
                        mybutton['background']=bcolor
                        mybutton['foreground']=fcolor

                    def on_leave(e):
                        mybutton['background']=fcolor
                        mybutton['foreground']=bcolor

                    mybutton=Button(f1,width=42,height=6,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=beauty,)
           
                    mybutton.bind("<Enter>",on_enter)
                    mybutton.bind("<Leave>",on_leave)

                    mybutton.place(x=x,y=y)
                #Command for beauty and personal button    
                def beauty():
                    f2 = Frame()
                    f2.place(x=0,y=0,width=1600,height= 900)
                    f2.configure(bg = "white")
                    def back():
                        f2.destroy()
                    b1 = Button(f2,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                    b1.place(x=0,y=0)
                   
                    def add_items(x,y,text,bcolor,fcolor,add):

                        def on_enter(e):
                            mybutton['background']=bcolor
                            mybutton['foreground']=fcolor

                        def on_leave(e):
                            mybutton['background']=fcolor
                            mybutton['foreground']=bcolor

                        mybutton=Button(f2,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                        border=0,
                                        activeforeground=fcolor,
                                        activebackground=bcolor,
                                        command=add,)
                        mybutton.bind("<Enter>",on_enter)
                        mybutton.bind("<Leave>",on_leave)

                        mybutton.place(x=x,y=y)
                   
                    def add():
                        f3 = Frame()
                        f3.place(x=0,y=0,width=1600,height= 900)
                        f3.configure(bg = "white")

                       
                        entry1=Entry()
                        entry1.place(x=800,y=300,height=25)
                        enter_ID=Label(f3,text="Item Code:",fg="White",bg="#1877F2",font="Times")
                        enter_ID.place(x=600,y=300)

                        entry2=Entry()
                        entry2.place(x=800,y=350,height=25)
                        enter_name=Label(f3,text="Item Name:",fg="white",bg="#1877F2",font="Times")
                        enter_name.place(x=600,y=350)

                        entry3=Entry()
                        entry3.place(x=800,y=400,height=25)
                        enter_contact=Label(f3,text="Cost Price",fg="white",bg="#1877F2",font="Times")
                        enter_contact.place(x=600,y=400)

                        entry4=Entry()
                        entry4.place(x=800,y=450,height=25)
                        enter_ledgerID=Label(f3,text="Selling Price",fg="white",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=450)
                       
                        entry5=Entry()
                        entry5.place(x=830,y=500,height=25)
                        enter_ledgerID=Label(f3,text="Quantity:",fg="White",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=500)
                       
                        entry6=Entry()
                        entry6.place(x=830,y=550,height=25)
                        enter_ledgerID=Label(f3,text="Date of Expiry(DD-MM-YYYY)",fg="White",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=550)

                           

                        def sub():
                            E1=entry1.get()
                            E2=entry2.get()
                            E3=entry3.get()
                            E4=entry4.get()
                            E5=entry5.get()
                            E6=entry6.get()
                            sql = "INSERT INTO inv_beauty VALUES (%s, %s, %s, %s, %s, %s)"
                            values=(E1,E2,int(E3),int(E4),int(E5),E6)
                            mycsr.execute(sql, values)
                            conn.commit()
                            entry1.delete(0, END)
                            entry2.delete(0, END)
                            entry3.delete(0, END)
                            entry4.delete(0, END)
                            entry5.delete(0, END)
                            entry6.delete(0, END)
                               

                       
                        t = Button(f3,text="Submit",fg="black",bg="white",font="arahoni 10 bold",command=sub,)
                        t.place(x=750,y=600)    
                       
                        def back():
                            entry1.destroy()
                            entry2.destroy()
                            entry3.destroy()
                            entry4.destroy()
                            entry5.destroy()
                            entry6.destroy()
                            f3.destroy()
                        b1 = Button(f3,width = 21,height = 2,text = "<--",
                            border = 0,
                            fg='cyan',
                            bg='black',
                            activeforeground='black',
                            activebackground='cyan',
                            command = back)
                        b1.place(x=0,y=0)

                    add_items(650,250,"ADD ITEMS",'cyan',"black",add)
                   
                    def view_items(x,y,text,bcolor,fcolor,view):

                        def on_enter(e):
                            mybutton['background']=bcolor
                            mybutton['foreground']=fcolor

                        def on_leave(e):
                            mybutton['background']=fcolor
                            mybutton['foreground']=bcolor

                        mybutton=Button(f2,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                        border=0,
                                        activeforeground=fcolor,
                                        activebackground=bcolor,
                                        command=view,)
                        mybutton.bind("<Enter>",on_enter)
                        mybutton.bind("<Leave>",on_leave)

                        mybutton.place(x=x,y=y)
                   
                    def view():
                        f3 = Frame()
                        f3.place(x=0,y=0,width=1600,height= 900)
                        f3.configure(bg = "white")
                        scroll_bar=Scrollbar(f3)
                        scroll_bar.pack( side = RIGHT, fill = Y )
                        Head=Label(f3,text="Beauty Items Available",fg="white",bg="#1877F2",font="Times 30")
                        Head.pack()
                        mycsr.execute("select * from inv_beauty")
                        myres=mycsr.fetchall()
                        x=500
                        y=210
                        note=Label(f3,text="DATA IN THE FORM:",fg="white",bg="#1877F2",font="Times 20").place(x=500,y=115)
                        h=('Item Code | Item Name | Cost Price | Selling Price | Quantity | Expiry Date')
                        hl=Label(f3,text=h,fg="white",bg="#1877F2",font="Times 20").place(x=500,y=150)
                        for rec in myres:
                            Out=Label(f3,text=rec,fg="white",bg="#1877F2",font="Times 20")
                            Out.place(x=x,y=y)
                            y+=40
                           
                        def back():
                            f3.destroy()
                        b1 = Button(f3,width = 21,height = 2,text = "<--",
                            border = 0,
                            fg='cyan',
                            bg='black',
                            activeforeground='black',
                            activebackground='cyan',
                            command = back)
                        b1.place(x=0,y=0)
                       
                    view_items(650,350,"VIEW ITEMS",'cyan',"black",view)

                Beauty(200,400,"BEAUTY AND PERSONAL",'cyan',"black",beauty)

                #Drinks Button (Inside the inventory button)
                def Drinks(x,y,text,bcolor,fcolor,drink):

                    def on_enter(e):
                        mybutton['background']=bcolor
                        mybutton['foreground']=fcolor

                    def on_leave(e):
                        mybutton['background']=fcolor
                        mybutton['foreground']=bcolor

                    mybutton=Button(f1,width=42,height=6,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=drink,)
           
                    mybutton.bind("<Enter>",on_enter)
                    mybutton.bind("<Leave>",on_leave)

                    mybutton.place(x=x,y=y)
                #Command for drinks button
                def drink():
                    f2 = Frame()
                    f2.place(x=0,y=0,width=1600,height= 900)
                    f2.configure(bg = "white")
                    def back():
                        f2.destroy()
                    b1 = Button(f2,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                    b1.place(x=0,y=0)
                   
                    def add_items(x,y,text,bcolor,fcolor,add):

                        def on_enter(e):
                            mybutton['background']=bcolor
                            mybutton['foreground']=fcolor

                        def on_leave(e):
                            mybutton['background']=fcolor
                            mybutton['foreground']=bcolor

                        mybutton=Button(f2,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                        border=0,
                                        activeforeground=fcolor,
                                        activebackground=bcolor,
                                        command=add,)
                        mybutton.bind("<Enter>",on_enter)
                        mybutton.bind("<Leave>",on_leave)

                        mybutton.place(x=x,y=y)
                   
                    def add():
                        f3 = Frame()
                        f3.place(x=0,y=0,width=1600,height= 900)
                        f3.configure(bg = "white")

                       
                        entry1=Entry()
                        entry1.place(x=800,y=300,height=25)
                        enter_ID=Label(f3,text="Item Code:",fg="White",bg="#1877F2",font="Times")
                        enter_ID.place(x=600,y=300)

                        entry2=Entry()
                        entry2.place(x=800,y=350,height=25)
                        enter_name=Label(f3,text="Item Name:",fg="white",bg="#1877F2",font="Times")
                        enter_name.place(x=600,y=350)

                        entry3=Entry()
                        entry3.place(x=800,y=400,height=25)
                        enter_contact=Label(f3,text="Cost Price",fg="white",bg="#1877F2",font="Times")
                        enter_contact.place(x=600,y=400)

                        entry4=Entry()
                        entry4.place(x=800,y=450,height=25)
                        enter_ledgerID=Label(f3,text="Selling Price",fg="white",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=450)
                       
                        entry5=Entry()
                        entry5.place(x=830,y=500,height=25)
                        enter_ledgerID=Label(f3,text="Quantity:",fg="White",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=500)
                       
                        entry6=Entry()
                        entry6.place(x=830,y=550,height=25)
                        enter_ledgerID=Label(f3,text="Date of Expiry(DD-MM-YYYY)",fg="White",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=550)
                           

                        def sub():
                            E1=entry1.get()
                            E2=entry2.get()
                            E3=entry3.get()
                            E4=entry4.get()
                            E5=entry5.get()
                            E6=entry6.get()
                            sql = "INSERT INTO inv_drinks VALUES (%s, %s, %s, %s, %s, %s)"
                            values=(E1,E2,int(E3),int(E4),int(E5),E6)
                            mycsr.execute(sql, values)
                            conn.commit()
                            entry1.delete(0, END)
                            entry2.delete(0, END)
                            entry3.delete(0, END)
                            entry4.delete(0, END)
                            entry5.delete(0, END)
                            entry6.delete(0, END)
                               

                       
                        t = Button(f3,text="Submit",fg="black",bg="white",font="arahoni 10 bold",command=sub,)
                        t.place(x=750,y=600)    
                       
                        def back():
                            entry1.destroy()
                            entry2.destroy()
                            entry3.destroy()
                            entry4.destroy()
                            entry5.destroy()
                            entry6.destroy()
                            f3.destroy()
                        b1 = Button(f3,width = 21,height = 2,text = "<--",
                            border = 0,
                            fg='cyan',
                            bg='black',
                            activeforeground='black',
                            activebackground='cyan',
                            command = back)
                        b1.place(x=0,y=0)

                    add_items(650,250,"ADD ITEMS",'cyan',"black",add)
                   
                    def view_items(x,y,text,bcolor,fcolor,view):

                        def on_enter(e):
                            mybutton['background']=bcolor
                            mybutton['foreground']=fcolor

                        def on_leave(e):
                            mybutton['background']=fcolor
                            mybutton['foreground']=bcolor

                        mybutton=Button(f2,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                        border=0,
                                        activeforeground=fcolor,
                                        activebackground=bcolor,
                                        command=view,)
                        mybutton.bind("<Enter>",on_enter)
                        mybutton.bind("<Leave>",on_leave)

                        mybutton.place(x=x,y=y)
                   
                    def view():
                        f3 = Frame()
                        f3.place(x=0,y=0,width=1600,height= 900)
                        f3.configure(bg = "white")
                        scroll_bar=Scrollbar(f3)
                        scroll_bar.pack( side = RIGHT, fill = Y )
                        Head=Label(f3,text="Drinking Items Available",fg="white",bg="#1877F2",font="Times 30")
                        Head.pack()
                        mycsr.execute("select * from inv_drinks")
                        myres=mycsr.fetchall()
                        x=500
                        y=210
                        note=Label(f3,text="DATA IN THE FORM:",fg="white",bg="#1877F2",font="Times 20").place(x=500,y=115)
                        h=('Item Code | Item Name | Cost Price | Selling Price | Quantity | Expiry Date')
                        hl=Label(f3,text=h,fg="white",bg="#1877F2",font="Times 20").place(x=500,y=150)
                        for rec in myres:
                            Out=Label(f3,text=rec,fg="white",bg="#1877F2",font="Times 20")
                            Out.place(x=x,y=y)
                            y+=40
                           
                        def back():
                            f3.destroy()
                        b1 = Button(f3,width = 21,height = 2,text = "<--",
                            border = 0,
                            fg='cyan',
                            bg='black',
                            activeforeground='black',
                            activebackground='cyan',
                            command = back)
                        b1.place(x=0,y=0)
                       
                    view_items(650,350,"VIEW ITEMS",'cyan',"black",view)

                Drinks(650,400,"DRINKS",'cyan',"black",drink)

                #Stationery Button (Inside the inventory button)
                def Stationery(x,y,text,bcolor,fcolor,stationery):

                    def on_enter(e):
                        mybutton['background']=bcolor
                        mybutton['foreground']=fcolor

                    def on_leave(e):
                        mybutton['background']=fcolor
                        mybutton['foreground']=bcolor

                    mybutton=Button(f1,width=42,height=6,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=stationery,)
           
                    mybutton.bind("<Enter>",on_enter)
                    mybutton.bind("<Leave>",on_leave)

                    mybutton.place(x=x,y=y)
                #Command for stationery button
                def stationery():
                    f2 = Frame()
                    f2.place(x=0,y=0,width=1600,height= 900)
                    f2.configure(bg = "white")
                    def back():
                        f2.destroy()
                    b1 = Button(f2,width = 21,height = 2,text = "<--",
                                border = 0,
                                fg='cyan',
                                bg='black',
                                activeforeground='black',
                                activebackground='cyan',
                                command = back)
                    b1.place(x=0,y=0)
                   
                    def add_items(x,y,text,bcolor,fcolor,add):

                        def on_enter(e):
                            mybutton['background']=bcolor
                            mybutton['foreground']=fcolor

                        def on_leave(e):
                            mybutton['background']=fcolor
                            mybutton['foreground']=bcolor

                        mybutton=Button(f2,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                        border=0,
                                        activeforeground=fcolor,
                                        activebackground=bcolor,
                                        command=add,)
                        mybutton.bind("<Enter>",on_enter)
                        mybutton.bind("<Leave>",on_leave)

                        mybutton.place(x=x,y=y)
                   
                    def add():
                        f3 = Frame()
                        f3.place(x=0,y=0,width=1600,height= 900)
                        f3.configure(bg = "white")

                       
                        entry1=Entry()
                        entry1.place(x=800,y=300,height=25)
                        enter_ID=Label(f3,text="Item Code:",fg="White",bg="#1877F2",font="Times")
                        enter_ID.place(x=600,y=300)

                        entry2=Entry()
                        entry2.place(x=800,y=350,height=25)
                        enter_name=Label(f3,text="Item Name:",fg="white",bg="#1877F2",font="Times")
                        enter_name.place(x=600,y=350)

                        entry3=Entry()
                        entry3.place(x=800,y=400,height=25)
                        enter_contact=Label(f3,text="Cost Price",fg="white",bg="#1877F2",font="Times")
                        enter_contact.place(x=600,y=400)

                        entry4=Entry()
                        entry4.place(x=800,y=450,height=25)
                        enter_ledgerID=Label(f3,text="Selling Price",fg="white",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=450)
                       
                        entry5=Entry()
                        entry5.place(x=830,y=500,height=25)
                        enter_ledgerID=Label(f3,text="Quantity:",fg="White",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=500)
                       
                        entry6=Entry()
                        entry6.place(x=830,y=550,height=25)
                        enter_ledgerID=Label(f3,text="Date of Expiry(DD-MM-YYYY)",fg="White",bg="#1877F2",font="Times")
                        enter_ledgerID.place(x=600,y=550)
                           

                        def sub():
                            E1=entry1.get()
                            E2=entry2.get()
                            E3=entry3.get()
                            E4=entry4.get()
                            E5=entry5.get()
                            E6=entry6.get()
                            sql = "INSERT INTO inv_stationery VALUES (%s, %s, %s, %s, %s, %s)"
                            values=(E1,E2,int(E3),int(E4),int(E5),E6)
                            mycsr.execute(sql, values)
                            conn.commit()
                            entry1.delete(0, END)
                            entry2.delete(0, END)
                            entry3.delete(0, END)
                            entry4.delete(0, END)
                            entry5.delete(0, END)
                            entry6.delete(0, END)
                               

                       
                        t = Button(f3,text="Submit",fg="black",bg="white",font="arahoni 10 bold",command=sub,)
                        t.place(x=750,y=600)    
                       
                        def back():
                            entry1.destroy()
                            entry2.destroy()
                            entry3.destroy()
                            entry4.destroy()
                            entry5.destroy()
                            entry6.destroy()
                            f3.destroy()
                        b1 = Button(f3,width = 21,height = 2,text = "<--",
                            border = 0,
                            fg='cyan',
                            bg='black',
                            activeforeground='black',
                            activebackground='cyan',
                            command = back)
                        b1.place(x=0,y=0)

                    add_items(650,250,"ADD ITEMS",'cyan',"black",add)
                   
                    def view_items(x,y,text,bcolor,fcolor,view):

                        def on_enter(e):
                            mybutton['background']=bcolor
                            mybutton['foreground']=fcolor

                        def on_leave(e):
                            mybutton['background']=fcolor
                            mybutton['foreground']=bcolor

                        mybutton=Button(f2,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                        border=0,
                                        activeforeground=fcolor,
                                        activebackground=bcolor,
                                        command=view,)
                        mybutton.bind("<Enter>",on_enter)
                        mybutton.bind("<Leave>",on_leave)

                        mybutton.place(x=x,y=y)
                   
                    def view():
                        f3 = Frame()
                        f3.place(x=0,y=0,width=1600,height= 900)
                        f3.configure(bg = "white")
                        scroll_bar=Scrollbar(f3)
                        scroll_bar.pack( side = RIGHT, fill = Y )
                        Head=Label(f3,text="Stationery Items Available",fg="white",bg="#1877F2",font="Times 30")
                        Head.pack()
                        mycsr.execute("select * from inv_stationery")
                        myres=mycsr.fetchall()
                        x=500
                        y=210
                        note=Label(f3,text="DATA IN THE FORM:",fg="white",bg="#1877F2",font="Times 20").place(x=500,y=115)
                        h=('Item Code | Item Name | Cost Price | Selling Price | Quantity | Expiry Date')
                        hl=Label(f3,text=h,fg="white",bg="#1877F2",font="Times 20").place(x=500,y=150)
                        for rec in myres:
                            Out=Label(f3,text=rec,fg="white",bg="#1877F2",font="Times 20")
                            Out.place(x=x,y=y)
                            y+=40
                           
                        def back():
                            f3.destroy()
                        b1 = Button(f3,width = 21,height = 2,text = "<--",
                            border = 0,
                            fg='cyan',
                            bg='black',
                            activeforeground='black',
                            activebackground='cyan',
                            command = back)
                        b1.place(x=0,y=0)
                       
                    view_items(650,350,"VIEW ITEMS",'cyan',"black",view)

                Stationery(1100,400,"STATIONERY",'cyan',"black",stationery)

            inventory(650,150,"INVENTORY",'cyan',"black",inv)

            #Customer Details Button (Inside store button)
            def customer_details(x,y,text,bcolor,fcolor,details):

                def on_enter(e):
                    mybutton['background']=bcolor
                    mybutton['foreground']=fcolor

                def on_leave(e):
                    mybutton['background']=fcolor
                    mybutton['foreground']=bcolor

                mybutton=Button(first_frame,width=42,height=4,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=details,)
           
                mybutton.bind("<Enter>",on_enter)
                mybutton.bind("<Leave>",on_leave)

                mybutton.place(x=x,y=y)

            def details():
                f1 = Frame()
                f1.place(x=0,y=0,width=1600,height= 900)
                f1.configure(bg = "white")
                def back():
                    f1.destroy()
                b1 = Button(f1,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                b1.place(x=0,y=0)

                def add_customer(x,y,text,bcolor,fcolor,add):

                    def on_enter(e):
                        mybutton['background']=bcolor
                        mybutton['foreground']=fcolor

                    def on_leave(e):
                        mybutton['background']=fcolor
                        mybutton['foreground']=bcolor

                    mybutton=Button(f1,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                    border=0,
                                    activeforeground=fcolor,
                                    activebackground=bcolor,
                                    command=add,)
                    mybutton.bind("<Enter>",on_enter)
                    mybutton.bind("<Leave>",on_leave)

                    mybutton.place(x=x,y=y)
               
                def add():
                    f2 = Frame()
                    f2.place(x=0,y=0,width=1600,height= 900)
                    f2.configure(bg = "white")

                   
                    entry1=Entry()
                    entry1.place(x=750,y=300,height=25)
                    enter_ID=Label(f2,text="Customer ID: ",fg="white",bg="green",font="Times")
                    enter_ID.place(x=600,y=300)

                    entry2=Entry()
                    entry2.place(x=750,y=350,height=25)
                    enter_name=Label(f2,text="Customer name: ",fg="white",bg="green",font="Times")
                    enter_name.place(x=600,y=350)

                    entry3=Entry()
                    entry3.place(x=750,y=400,height=25)
                    enter_contact=Label(f2,text="Contact no.: ",fg="white",bg="green",font="Times")
                    enter_contact.place(x=600,y=400)

                    entry4=Entry()
                    entry4.place(x=750,y=450,height=25)
                    enter_ledgerID=Label(f2,text="Ledger ID: ",fg="white",bg="green",font="Times")
                    enter_ledgerID.place(x=600,y=450)

                       

                    def sub():
                            E1=entry1.get()
                            E2=entry2.get()
                            E3=entry3.get()
                            E4=entry4.get()
                            sql = "INSERT INTO cust_details VALUES (%s, %s, %s, %s)"
                            values=(E1,E2,E3,E4)
                            mycsr.execute(sql, values)
                            conn.commit()
                            entry1.delete(0, END)
                            entry2.delete(0, END)
                            entry3.delete(0, END)
                            entry4.delete(0, END)
                           

                   
                    t = Button(f2,text="Submit",fg="black",bg="white",font="arahoni 10 bold",command=sub,)
                    t.place(x=750,y=500)    
                   
                    def back():
                        entry1.destroy()
                        entry2.destroy()
                        entry3.destroy()
                        entry4.destroy()
                        f2.destroy()
                    b1 = Button(f2,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                    b1.place(x=0,y=0)

                add_customer(650,250,"ADD CUSTOMER",'cyan',"black",add)

                def view_customer(x,y,text,bcolor,fcolor,view):

                    def on_enter(e):
                        mybutton['background']=bcolor
                        mybutton['foreground']=fcolor

                    def on_leave(e):
                        mybutton['background']=fcolor
                        mybutton['foreground']=bcolor

                    mybutton=Button(f1,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                    border=0,
                                    activeforeground=fcolor,
                                    activebackground=bcolor,
                                    command=view,)
                    mybutton.bind("<Enter>",on_enter)
                    mybutton.bind("<Leave>",on_leave)

                    mybutton.place(x=x,y=y)
               
                def view():
                    f2 = Frame()
                    f2.place(x=0,y=0,width=1600,height= 900)
                    f2.configure(bg = "white")
                    scroll_bar=Scrollbar(f2)
                    scroll_bar.pack( side = RIGHT, fill = Y )
                    Head=Label(f2,text="My Customers",fg="white",bg="#1877F2",font="Times 30")
                    Head.pack()
                    mycsr.execute("select * from cust_details")
                    myres=mycsr.fetchall()
                    x=500
                    y=210
                    note=Label(f2,text="DATA IN THE FORM:",fg="white",bg="#1877F2",font="Times 20").place(x=500,y=115)
                    h=('Customer ID | Customer Name | Contact No. | Ledger ID')
                    hl=Label(f2,text=h,fg="white",bg="#1877F2",font="Times 20").place(x=500,y=150)
                    for rec in myres:
                        Out=Label(f2,text=rec,fg="white",bg="#1877F2",font="Times 20")
                        Out.place(x=x,y=y)
                        y+=40
                       
                    def back():
                        f2.destroy()
                    b1 = Button(f2,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                    b1.place(x=0,y=0)
                   
                view_customer(650,350,"VIEW CUSTOMER DETIALS",'cyan',"black",view)
               
            customer_details(650,250,"CUSTOMER DETAILS",'cyan',"black",details)

            #Ledger Button (Insider store button)
            def ledger(x,y,text,bcolor,fcolor,led):

                def on_enter(e):
                    mybutton['background']=bcolor
                    mybutton['foreground']=fcolor

                def on_leave(e):
                    mybutton['background']=fcolor
                    mybutton['foreground']=bcolor

                mybutton=Button(first_frame,width=42,height=4,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=led,)
           
                mybutton.bind("<Enter>",on_enter)
                mybutton.bind("<Leave>",on_leave)

                mybutton.place(x=x,y=y)

            #Command for ledger button
            def led():
                f1 = Frame()
                f1.place(x=0,y=0,width=1600,height= 900)
                f1.configure(bg = "white")
                def back():
                    f1.destroy()
                b1 = Button(f1,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                b1.place(x=0,y=0)
                # add ledger button (Inside Ledger button)
                def add_ledger(x,y,text,bcolor,fcolor,ledger):

                    def on_enter(e):
                        mybutton['background']=bcolor
                        mybutton['foreground']=fcolor

                    def on_leave(e):
                        mybutton['background']=fcolor
                        mybutton['foreground']=bcolor

                    mybutton=Button(f1,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                    border=0,
                                    activeforeground=fcolor,
                                    activebackground=bcolor,
                                    command=ledger,)
                    mybutton.bind("<Enter>",on_enter)
                    mybutton.bind("<Leave>",on_leave)

                    mybutton.place(x=x,y=y)
                   
                #Command for add ledger button
                def ledger():
                    f2 = Frame()
                    f2.place(x=0,y=0,width=1600,height= 900)
                    f2.configure(bg = "white")

                    #Entries
                    entry1=Entry()
                    entry1.place(x=750,y=300,height=25)
                    enter_ID=Label(f2,text="Ledger ID: ",fg="white",bg="#aa1231",font="Times")
                    enter_ID.place(x=600,y=300)

                    entry2=Entry()
                    entry2.place(x=750,y=350,height=25)
                    enter_name=Label(f2,text="Customer name: ",fg="white",bg="#aa1231",font="Times")
                    enter_name.place(x=600,y=350)

                    entry3=Entry()
                    entry3.place(x=750,y=400,height=25)
                    enter_contact=Label(f2,text="Amount to be paid: ",fg="white",bg="#aa1231",font="Times")
                    enter_contact.place(x=600,y=400)

                    entry4=Entry()
                    entry4.place(x=750,y=450,height=25)
                    enter_ledgerID=Label(f2,text="Date edited: ",fg="white",bg="#aa1231",font="Times")
                    enter_ledgerID.place(x=600,y=450)

                       
                    #Command for submit button
                    def sub():
                            E1=entry1.get()
                            E2=entry2.get()
                            E3=entry3.get()
                            E4=entry4.get()
                            sql = "INSERT INTO led_details VALUES (%s, %s, %s, %s)"
                            values=(E1,E2,int(E3),E4)
                            mycsr.execute(sql, values)
                            conn.commit()
                            entry1.delete(0, END)
                            entry2.delete(0, END)
                            entry3.delete(0, END)
                            entry4.delete(0, END)
                           
                    t = Button(f2,text="Submit",fg="black",bg="white",font="arahoni 10 bold",command=sub,)
                    t.place(x=750,y=500)    
                    #Command for back button
                    def back():
                        entry1.destroy()
                        entry2.destroy()
                        entry3.destroy()
                        entry4.destroy()
                        f2.destroy()
                    b1 = Button(f2,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                    b1.place(x=0,y=0)

                add_ledger(650,250,"CREATE LEDGER",'cyan',"black",ledger)
                #view ledger button(Insider ledger button)
                def view_ledger(x,y,text,bcolor,fcolor,l_view):

                    def on_enter(e):
                        mybutton['background']=bcolor
                        mybutton['foreground']=fcolor

                    def on_leave(e):
                        mybutton['background']=fcolor
                        mybutton['foreground']=bcolor

                    mybutton=Button(f1,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                    border=0,
                                    activeforeground=fcolor,
                                    activebackground=bcolor,
                                    command=l_view,)
                    mybutton.bind("<Enter>",on_enter)
                    mybutton.bind("<Leave>",on_leave)

                    mybutton.place(x=x,y=y)
                #Command for ledger button
                def l_view():
                    f2 = Frame()
                    f2.place(x=0,y=0,width=1600,height= 900)
                    f2.configure(bg = "white")
                    scroll_bar=Scrollbar(f2)
                    scroll_bar.pack( side = RIGHT, fill = Y )
                    Head=Label(f2,text="Ledger Records",fg="white",bg="#1877F2",font="Times 30")
                    Head.pack()
                    mycsr.execute("select * from led_details")
                    myres=mycsr.fetchall()
                    x=500
                    y=210
                    note=Label(f2,text="DATA IN THE FORM:",fg="white",bg="#1877F2",font="Times 20").place(x=500,y=115)
                    h=('Ledger ID | Customer Name | Amount To Pay | Date Edited')
                    hl=Label(f2,text=h,fg="white",bg="#1877F2",font="Times 20").place(x=500,y=150)
                    for rec in myres:
                        Out=Label(f2,text=rec,fg="white",bg="#1877F2",font="Times 20")
                        Out.place(x=x,y=y)
                        y+=40
                    def back():
                        f2.destroy()
                    b1 = Button(f2,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                    b1.place(x=0,y=0)
                   
                view_ledger(650,350,"VIEW LEDGER RECORD",'cyan',"black",l_view)
                #edit ledger button(Inside ledger button)
                def edit_ledger(x,y,text,bcolor,fcolor,l_edit):

                    def on_enter(e):
                        mybutton['background']=bcolor
                        mybutton['foreground']=fcolor

                    def on_leave(e):
                        mybutton['background']=fcolor
                        mybutton['foreground']=bcolor

                    mybutton=Button(f1,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                    border=0,
                                    activeforeground=fcolor,
                                    activebackground=bcolor,
                                    command=l_edit,)
                    mybutton.bind("<Enter>",on_enter)
                    mybutton.bind("<Leave>",on_leave)

                    mybutton.place(x=x,y=y)
                #Command for edit ledger button
                #Command for edit ledger button
                def l_edit():
                    f2 = Frame()
                    f2.place(x=0,y=0,width=1600,height= 900)
                    f2.configure(bg = "white")

                   
                    entry1=Entry()
                    entry1.place(x=770,y=300,height=25)
                    enter_ID=Label(f2,text="Ledger ID: ",fg="white",bg="#aa1231",font="Times")
                    enter_ID.place(x=600,y=300)

                    entry2=Entry()
                    entry2.place(x=770,y=350,height=25)
                    enter_name=Label(f2,text="Amount to be added: ",fg="white",bg="#aa1231",font="Times")
                    enter_name.place(x=600,y=350)

                    entry3=Entry()
                    entry3.place(x=770,y=400,height=25)
                    enter_ledgerID=Label(f2,text="Amount to be deducted: ",fg="white",bg="#aa1231",font="Times")
                    enter_ledgerID.place(x=600,y=400)
                   
                    entry4=Entry()
                    entry4.place(x=770,y=450,height=25)
                    enter_ledgerID=Label(f2,text="Date edited: ",fg="white",bg="#aa1231",font="Times")
                    enter_ledgerID.place(x=600,y=450)

                       

                    def sub():
                            E1=entry1.get()
                            E2=entry2.get()
                            E3=entry3.get()
                            E4=entry4.get()
                            id_led=(E1,)
                            sql=("select amt_to_pay, date_edited from led_details where Led_id=%s")
                            val=id_led
                            mycsr.execute(sql, val)
                            myres=mycsr.fetchone()
                            lres=list(myres)
                            a=int(lres[0])+int(E2)
                            b=int(a)-int(E3)
                            lres[0]=b
                            lres[1]=E4
                            sql1=('update led_details set amt_to_pay=%s, date_edited=%s where Led_id=%s')
                            values=(lres[0],lres[1],E1)
                            mycsr.execute(sql1, values)
                            entry1.delete(0, END)
                            entry2.delete(0, END)
                            entry3.delete(0, END)
                            entry4.delete(0, END)
                       
                           

                   
                    t = Button(f2,text="Submit",fg="black",bg="white",font="arahoni 10 bold",command=sub,)
                    t.place(x=750,y=500)    
                   
                    def back():
                        entry1.destroy()
                        entry2.destroy()
                        entry3.destroy()
                        entry4.destroy()
                        f2.destroy()
                    b1 = Button(f2,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                    b1.place(x=0,y=0)

                edit_ledger(650,450,"EDIT LEDGER",'cyan',"black",l_edit)

            ledger(650,350,"LEDGER",'cyan',"black",led)
           
            #Create Bills Button (Inside store button)
            def billing(x,y,text,bcolor,fcolor,details):
               

               
                def on_enter(e):
                    mybutton['background']=bcolor
                    mybutton['foreground']=fcolor

                def on_leave(e):
                    mybutton['background']=fcolor
                    mybutton['foreground']=bcolor

                mybutton=Button(first_frame,width=42,height=4,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=details,)

                mybutton.bind("<Enter>",on_enter)
                mybutton.bind("<Leave>",on_leave)

                mybutton.place(x=x,y=y)

            def details():
                f1 = Frame()
                f1.place(x=0,y=0,width=1600,height= 900)
                f1.configure(bg = "white")
                def back():
                    f1.destroy()
                b1 = Button(f1,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                b1.place(x=0,y=0)

                def create_bill(x,y,text,bcolor,fcolor,add):

                    def on_enter(e):
                        mybutton['background']=bcolor
                        mybutton['foreground']=fcolor

                    def on_leave(e):
                        mybutton['background']=fcolor
                        mybutton['foreground']=bcolor

                    mybutton=Button(f1,width=42,height=4,text=text,fg=bcolor,bg=fcolor,
                                    border=0,
                                    activeforeground=fcolor,
                                    activebackground=bcolor,
                                    command=add,)
                    mybutton.bind("<Enter>",on_enter)
                    mybutton.bind("<Leave>",on_leave)

                    mybutton.place(x=x,y=y)
               
                def add():
                    f2 = Frame()
                    f2.place(x=0,y=0,width=1600,height= 900)
                    f2.configure(bg = "white")

                   
                    entry1=Entry()
                    entry1.place(x=750,y=300,height=25)
                    enter_ID=Label(f2,text="Item Code:",fg="white",bg="green",font="Times")
                    enter_ID.place(x=665,y=300)
                   
                    entry2=Entry()
                    entry2.place(x=750,y=350,height=25)
                    enter_name=Label(f2,text="Category(cook/house/snack/beauty/drink/stat):",fg="white",bg="green",font="Times")
                    enter_name.place(x=450,y=350)
                   
                    entry3=Entry()
                    entry3.place(x=750,y=400,height=25)
                    enter_name=Label(f2,text="Quantity",fg="white",bg="green",font="Times")
                    enter_name.place(x=680,y=400)
                   
                   

                    def add_to_bill():
                            E1=entry1.get()
                            E2=entry2.get()
                            E3=entry3.get()
                            if E2 == "cook":
                                sql=("select selling_price from inv_cook where item_code=%s")
                                val=(E1,)
                                mycsr.execute(sql, val)
                                res=list(mycsr.fetchone())
                                sql1 = "INSERT INTO bill VALUES (%s, %s, %s)"
                                values=(E1,E3,(int(res[0])*int(E3)))
                                mycsr.execute(sql1, values)
                                sql2="select quantity from inv_cook where item_code=%s"
                                val=(E1,)
                                mycsr.execute(sql2, val)
                                res1=list(mycsr.fetchone())
                                sql3="UPDATE inv_cook SET quantity=%s WHERE item_code=%s"
                                val=((int(res1[0])-int(E3)),E1)
                                mycsr.execute(sql3, val)
                                conn.commit()
                               
                            elif E2 == "house":
                                sql=("select selling_price from inv_house where item_code=%s")
                                val=(E1,)
                                mycsr.execute(sql, val)
                                res=list(mycsr.fetchone())
                                sql1 = "INSERT INTO bill VALUES (%s, %s, %s)"
                                values=(E1,E3,(int(res[0])*int(E3)))
                                mycsr.execute(sql1, values)
                                sql2="select quantity from inv_house where item_code=%s"
                                val=(E1,)
                                mycsr.execute(sql2, val)
                                res1=list(mycsr.fetchone())
                                sql3="UPDATE inv_house SET quantity=%s WHERE item_code=%s"
                                val=((int(res1[0])-int(E3)),E1)
                                mycsr.execute(sql3, val)
                                conn.commit()
                            elif E2 == "snack":
                                sql=("select selling_price from inv_snacks where item_code=%s")
                                val=(E1,)
                                mycsr.execute(sql, val)
                                res=list(mycsr.fetchone())
                                sql1 = "INSERT INTO bill VALUES (%s, %s, %s)"
                                values=(E1,E3,(int(res[0])*int(E3)))
                                mycsr.execute(sql1, values)
                                sql2="select quantity from inv_snacks where item_code=%s"
                                val=(E1,)
                                mycsr.execute(sql2, val)
                                res1=list(mycsr.fetchone())
                                sql3="UPDATE inv_snacks SET quantity=%s WHERE item_code=%s"
                                val=((int(res1[0])-int(E3)),E1)
                                mycsr.execute(sql3, val)
                                conn.commit()
                            elif E2 == "beauty":
                                sql=("select selling_price from inv_beauty where item_code=%s")
                                val=(E1,)
                                mycsr.execute(sql, val)
                                res=list(mycsr.fetchone())
                                sql1 = "INSERT INTO bill VALUES (%s, %s, %s)"
                                values=(E1,E3,(int(res[0])*int(E3)))
                                mycsr.execute(sql1, values)
                                sql2="select quantity from inv_beauty where item_code=%s"
                                val=(E1,)
                                mycsr.execute(sql2, val)
                                res1=list(mycsr.fetchone())
                                sql3="UPDATE inv_beauty SET quantity=%s WHERE item_code=%s"
                                val=((int(res1[0])-int(E3)),E1)
                                mycsr.execute(sql3, val)
                                conn.commit()
                            elif E2 == "drink":
                                sql=("select selling_price from inv_drinks where item_code=%s")
                                val=(E1,)
                                mycsr.execute(sql, val)
                                res=list(mycsr.fetchone())
                                sql1 = "INSERT INTO bill VALUES (%s, %s, %s)"
                                values=(E1,E3,(int(res[0])*int(E3)))
                                mycsr.execute(sql1, values)
                                sql2="select quantity from inv_drinks where item_code=%s"
                                val=(E1,)
                                mycsr.execute(sql2, val)
                                res1=list(mycsr.fetchone())
                                sql3="UPDATE inv_drinks SET quantity=%s WHERE item_code=%s"
                                val=((int(res1[0])-int(E3)),E1)
                                mycsr.execute(sql3, val)
                                conn.commit()
                            elif E2 == "stat":
                                sql=("select selling_price from inv_stationery where item_code=%s")
                                val=(E1,)
                                mycsr.execute(sql, val)
                                res=list(mycsr.fetchone())
                                sql1 = "INSERT INTO bill VALUES (%s, %s, %s)"
                                values=(E1,E3,(int(res[0])*int(E3)))
                                mycsr.execute(sql1, values)
                                sql2="select quantity from inv_stationery where item_code=%s"
                                val=(E1,)
                                mycsr.execute(sql2, val)
                                res1=list(mycsr.fetchone())
                                sql3="UPDATE inv_stationery SET quantity=%s WHERE item_code=%s"
                                val=((int(res1[0])-int(E3)),E1)
                                mycsr.execute(sql3, val)
                                conn.commit()
                           
                            entry1.delete(0, END)
                            entry2.delete(0, END)
                            entry3.delete(0, END)
                   
                    def calculate():
                            f_cost=0
                            mycsr.execute("select total_price from bill")
                            myres=list(mycsr.fetchall())
                            for x in myres:
                                for i in x:
                                    f_cost+=int(i)
                            a="THE CUSTOMER HAS TO PAY YOU",f_cost
                           
                            f3 = Frame()
                            f3.place(x=0,y=0,width=1600,height= 900)
                            f3.configure(bg = "white")
                           
                            ptop=Label(f3, text=a,fg='white',bg="#1877F2",font="Times 25").place(x=500,y=350)
                            def back():
                                sql="DELETE FROM bill"
                                mycsr.execute(sql)
                                f3.destroy()
                               
                            b1 = Button(f3,width = 21,height = 2,text = "<--",
                                border = 0,
                                fg='cyan',
                                bg='black',
                                activeforeground='black',
                                activebackground='cyan',
                                command = back)
                            b1.place(x=0,y=0)
                           
                           
                           
                               
                           

                   
                    t = Button(f2,text="add item",fg="black",bg="white",font="arahoni 10 bold",command=add_to_bill,)
                    t.place(x=750,y=450)
                   
                    u = Button(f2,text="Calculate",fg="black",bg="white",font="arahoni 10 bold",command=calculate,)
                    u.place(x=750,y=500)
                   
                    def back():
                        entry1.destroy()
                        entry2.destroy()
                        entry3.destroy()
                        f2.destroy()
                       
                    b1 = Button(f2,width = 21,height = 2,text = "<--",
                        border = 0,
                        fg='cyan',
                        bg='black',
                        activeforeground='black',
                        activebackground='cyan',
                        command = back)
                    b1.place(x=0,y=0)
                       
               
                create_bill(650,250,"MAKE A BILL",'cyan',"black",add)
            billing(650, 450, "CREATE BILLS", 'cyan',"black", details)

        store(650,300,"STORE MANAGEMENT",'cyan',"black",new)
       

       

    else:
        exit()
    entry1.delete(0, END)
    entry2.delete(0, END)
           

t = Button(root,text="Submit",fg="black",bg="white",font="arahoni 10 bold",command=access,)
t.place(x=800,y=400)


#The Exit button
def Exit(x,y,text,bcolor,fcolor,exit):

    def on_enter(e):
        mybutton['background']=bcolor
        mybutton['foreground']=fcolor

    def on_leave(e):
        mybutton['background']=fcolor
        mybutton['foreground']=bcolorq

    mybutton=Button(root,width=42,height=4,text=text,
                    fg=bcolor,
                    bg=fcolor,
                    border=0,
                    activeforeground=fcolor,
                    activebackground=bcolor,
                    command=exit,)
   
    mybutton.bind("<Enter>",on_enter)
    mybutton.bind("<Leave>",on_leave)

    mybutton.place(x=x,y=y)
#Command for exit button
def exit():
    root.destroy()

Exit(650,600,"EXIT","cyan",'black',exit)

root.mainloop()
