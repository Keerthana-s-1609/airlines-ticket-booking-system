from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry


USER = "root"
PASSWORD = "root"
DATABASE = "airlines"

mydb = mysql.connector.connect(  host="localhost",   user=USER,   password= PASSWORD, database = DATABASE)

def signin ():
    newwindow3 = Toplevel()
    my_w.geometry('1550x800')
    my_w.title("sign in")
    
    
    bg = PhotoImage(file = r"C:\Users\shipm\Downloads\WhatsApp Image 2023-11-15 at 11.08.44 PM.png") 
    canvas2 = Canvas( newwindow3, width = 400, height = 400) 
  
    canvas2.pack(fill = "both", expand = True)
    canvas2.create_image( 0, 0, image = bg,  anchor = "nw")

    usernameLabel = Label(canvas2, text="User Name",width=50,anchor = "c")
    usernameLabel.place(relx = 0.2,rely = 0.1)
    
    username = StringVar()
    usernameEntry = Entry(newwindow3, textvariable=username)
    canvas2.create_window(450,150,window = usernameEntry)
 
    passwordLabel = Label(newwindow3,text="Password",width=50,anchor = "c")
    passwordLabel.place(relx=0.2, rely = 0.25)  
    password = StringVar()
    passwordEntry = Entry(newwindow3, textvariable=password)
    canvas2.create_window(450,250,window = passwordEntry)

    mc = mydb.cursor()
    q='select * from signin where username = %s and password = %s'
    
    mc.execute(q,(usernameEntry.get(),password.get()))
    print(mc.fetchone())
               
    loginButton = Button(newwindow3, text="Sign in",command = entrypage )
    canvas2.create_window(450,350,window = loginButton)
    
    newwindow3.mainloop()

def signup():
    newwindow5 = Toplevel()
    newwindow5.geometry('1550x800')
    newwindow5.title("sign up")
    
    
    bg = PhotoImage(file = r"C:\Users\shipm\Downloads\WhatsApp Image 2023-11-15 at 11.08.44 PM.png") 
    canvas4 = Canvas( newwindow5, width = 400, height = 400) 
  
    canvas4.pack(fill = "both", expand = True)
    canvas4.create_image( 0, 0, image = bg,  anchor = "nw")

    nameLabel = Label(canvas4, text="Name",width=50,anchor = "c")
    nameLabel.place(relx = 0.2,rely = 0.1)
    name = StringVar()
    nameEntry = Entry(newwindow5, textvariable=name)
    canvas4.create_window(450,150,window = nameEntry)
    
    usernameLabel = Label(canvas4,text="Username",width=50,anchor = "c")
    usernameLabel.place(relx=0.2, rely = 0.25)  
    username = StringVar()
    usernameEntry = Entry(newwindow5, textvariable=username)
    canvas4.create_window(450,250,window = usernameEntry)

    passwordLabel = Label(canvas4,text="Password",width=50,anchor = "c")
    passwordLabel.place(relx=0.2, rely = 0.37)  
    password = StringVar()
    passwordEntry = Entry(newwindow5, textvariable=password)
    canvas4.create_window(450,350,window = passwordEntry)

    emailLabel = Label(canvas4, text="Email",width=50,anchor = "c")
    emailLabel.place(relx = 0.2,rely = 0.49)
    email = StringVar()
    emailEntry = Entry(newwindow5, textvariable=email)
    canvas4.create_window(450,450,window = emailEntry)

    pwdconfirmLabel = Label(canvas4, text="Password Reconfirmation",width=50,anchor = "c")
    pwdconfirmLabel.place(relx = 0.2,rely = 0.61)
    pwdconfirm = StringVar()
    pwdconfirmEntry = Entry(newwindow5, textvariable=pwdconfirm)
    canvas4.create_window(450,550,window = pwdconfirmEntry)

    b6=Button(canvas4,text="sign up",width=50,command=entrypage)

    b6_canvas = canvas4.create_window( 450, 650,  
                                       anchor = "c", 
                                       window = b6)
    mc=mydb.cursor()
        
    newwindow5.mainloop()

def entrypage():
    newwindow4 = Toplevel()
    my_w.geometry('1500x1500')
    my_w.title("book or cancel")
    newwindow4.state('zoomed')
    
    bg = PhotoImage(file = r"C:\Users\shipm\Downloads\WhatsApp Image 2023-11-15 at 11.08.44 PM.png") 
    canvas3 = Canvas( newwindow4, width = 400, height = 400) 
  
    canvas3.pack(fill = "both", expand = True)
    canvas3.create_image( 0, 0, image = bg,  anchor = "nw")

    b1=Button(canvas3,text="BOOK A TICKET",width=50,command=openbook)
    b2=Button(canvas3,text="CANCEL A TICKET",width=50,command=cancelbook)

    b1_canvas = canvas3.create_window( 200, 50,  
                                       anchor = "c", 
                                       window = b1) 
  
    b2_canvas = canvas3.create_window( 600, 50, 
                                       anchor = "c", 
                                       window = b2) 
    newwindow4.mainloop()
    
def cancelbook():
    newwindow1 = Toplevel()
    my_w.geometry('1500x1500')
    my_w.title("cancel new window")

    frame1 = Frame(newwindow1)
    
    
    can_label1 = Label(frame1, text ="Enter your booking reference id ")
    can_label1.grid(row = 0, column=0)
    
    can_entry1 = Entry(frame1)
    can_entry1.grid(row =0, column=1)

    frame1.grid(row = 0 , column=0)

    def search():
        mycursor = mydb.cursor(prepared=True)
        sql_query = "SELECT  b.booking_id , f.flight_id, f.airline_name , b.date_of_journey , f.departure , f.arrival, b.amount FROM FLIGHTDETAILS  f, BOOKINGS b where f.flight_id  = b.flight_id and b.booking_id = %s"
        data_tuple = (int(can_entry1.get()),)
        mycursor.execute(sql_query, data_tuple)

        #clear the tree first with all the data first
        for item in tree.get_children():
          tree.delete(item)
        for x in mycursor:
            #print(x)  
            tree.insert('', 'end', text="1", values = x)


        sql_q1 = "SELECT customer_name , gender, mobile_no from customer_details where booking_id= %s"
        mycursor.execute(sql_q1, data_tuple)
        #clear the tree first with all the data first
        for item in tree1.get_children():
          tree1.delete(item)
          
        for x in mycursor:
            tree1.insert('', 'end', text="1", values = x)

    can_button1 = Button(newwindow1, text = "Search booking", command = search)
    can_button1.grid(row =1, column=0)

    
    

    # Add a Treeview widget

    style = ttk.Style()
    style.theme_use('clam')
    
    tree = ttk.Treeview(newwindow1, column=("Booking ID", "Flight ID", "Flight Name", "Date of Journey", "Departure","Arrival", "Amount"), show='headings', height=1)
    tree.column ("# 1", anchor='center')
    tree.heading("# 1", text="Booking ID")
    tree.column ("# 2", anchor='center')
    tree.heading("# 2", text="Flight ID")
    tree.column ("# 3", anchor='center')
    tree.heading("# 3", text="Flight Name")
    tree.column ("# 4", anchor='center')
    tree.heading("# 4", text="Date of Journey")
    tree.column ("# 5", anchor='center')
    tree.heading("# 5", text="Departure")
    tree.column ("# 6", anchor='center')
    tree.heading("# 6", text="Arrival")
    tree.column ("# 7", anchor='center')
    tree.heading("# 7", text="Amount")
    
    tree.grid(row =2, column=0)

    tree1 = ttk.Treeview(newwindow1, column=("Passenger name", "Gender", "Mobile"), show='headings', height=4)
    tree1.column ("# 1", anchor='center')
    tree1.heading("# 1", text="Passenger Name")
    tree1.column ("# 2", anchor='center')
    tree1.heading("# 2", text="Gender")
    tree1.column ("# 3", anchor='center')
    tree1.heading("# 3", text="Mobile")

    tree1.grid(row = 3,column = 0)


    def cancelBooking():
        ans = messagebox.askyesno('Yes|No', 'Are you sure you want to proceed with the cancellation?')
        print(ans)
        if ( ans ) :
            mycursor = mydb.cursor(prepared=True)
            sql_query = "UPDATE bookings set status = 'CANCELLED' where booking_id = %s"
            data_tuple = (int(can_entry1.get()),)
            mycursor.execute(sql_query, data_tuple)
            mydb.commit()
            messagebox.showinfo("showinfo", "The booking has been successfully cancelled")
        
    can_button2 = Button(newwindow1, text = "Cancel booking", command = cancelBooking)
    can_button2.grid(row =4, column=0)

   
    newwindow1.mainloop()
    
    
def openbook():
    newwindow1 = Toplevel()
    my_w.geometry('1500x1500')
    my_w.title("booking new window")
    label1 = Label(newwindow1, text ="Booking Page")
    label1.pack()

    frame1 = Frame(newwindow1)

    label2 = Label(frame1, text= "Boarding Place")
    label2.grid(row = 0,column =0)
    
    n = StringVar()
    boarding = ttk.Combobox(frame1, width = 27, textvariable = n)

    mycursor = mydb.cursor()
    sql_query = "select distinct departure from flightdetails"
    mycursor.execute(sql_query)
    result =  mycursor.fetchall()
    
    boarding['values'] = result
    boarding.grid(row = 0,column= 1)

    label3 = Label(frame1, text= "Destination Place")
    label3.grid(row = 1,column =0)
    n1 = StringVar()
    destination = ttk.Combobox(frame1, width = 27, textvariable = n1)
    destination.grid(row = 1,column = 1)

    def getSelectedItem(eventObject):
        print(boarding.get())
        mycursor1= mydb.cursor(prepared=True)
        sql_query = "select distinct arrival from flightdetails where departure = %s"
        #print(boarding.get())
        data_tuple = (boarding.get(), )
        mycursor.execute(sql_query, data_tuple)
        result =  mycursor.fetchall()
        #print(result)
        destination['values'] = result
        
        
   
    boarding.bind("<<ComboboxSelected>>", getSelectedItem)
    
    label4 = Label(frame1, text= "Pick your Travel Date")
    label4.grid(row = 2,column =0)
    cal = DateEntry(frame1, date_pattern="dd-mm-yyyy")
    cal.grid(row=2, column=1)


    frame2 = Frame(newwindow1)

    #vertical_scroll = Scrollbar(frame2)
    #vertical_scroll.pack(side=RIGHT, fill=Y)

    
    column1 =  ("Airline name", "Flight Id", "Departure Time", "Arrival Time", "Duration", "Cost per ticket", "Tickets Available")
    tree1 = ttk.Treeview(frame2, column=column1, show='headings', height=4) #yscrollcommand =vertical_scroll.set)
    tree1.column ("# 1", anchor='center')
    tree1.heading("# 1", text="Airline name")
    tree1.column ("# 2", anchor='center')
    tree1.heading("# 2", text="Flight Id")
    tree1.column ("# 3", anchor='center')
    tree1.heading("# 3", text="Departure Time")
    tree1.column ("# 4", anchor='center')
    tree1.heading("# 4", text="Arrival Time ")
    tree1.column ("# 5", anchor='center')
    tree1.heading("# 5", text="Duration ")
    tree1.column ("# 6", anchor='center')
    tree1.heading("# 6", text="Cost per ticket ")
    tree1.column ("# 7", anchor='center')
    tree1.heading("# 7", text="Tickets Available") 

    
    def searchFlights():
        b = boarding.get()
        d = destination.get()
        date = cal.get()
        mycursor1= mydb.cursor(prepared=True)
        sql_query = "SELECT airline_name, flight_id, departure_time, arrival_time, duration, cost_per_seat, no_of_seats from flightdetails WHERE departure = %s AND arrival = %s "
        data_tuple = (b , d )
        mycursor.execute(sql_query, data_tuple)
        #clear the tree first with all the data first
        for item in tree1.get_children():
          tree1.delete(item)
        for x in mycursor:
            tree1.insert('', 'end', text="1", values = x)

    searchflightsButton = Button(frame1, text = "Search flights ", command=searchFlights)
    searchflightsButton.grid(row=3, columnspan=2, sticky='ew')
    frame1.pack()

    tree1.pack()
    frame2.pack()

    def selectFlight():
        for selected_item in tree1.selection():
            item = tree1.item(selected_item)
            record = item['values']
            # show a message
            print(record)
            s1 = "You selected  :\n\n"
            s1 += "Flight name: " + record[0] + "\n"
            s1 += "Flight Id: " + record[1] + "\n"
            s1 += "Boarding :" + boarding.get() + "\n"
            s1 += "Boarding Time : " + record[2] + "\n"
            s1 += "Destination: " + destination.get() + "\n"
        
            s1 += "Arrival Time in destination  :" + record[3] + "\n"
            s1 += "Your Travel Date: " + cal.get() + "\n"
            s1 += "Fare per ticket :" + str(record[5]) + "\n"
            print(s1)
            selectFlightLabel.configure(text = s1)
            
    selectFlightButton = Button(newwindow1, text = "Select flights ", command = selectFlight)
    selectFlightButton.pack()

    selectFlightLabel = Label(newwindow1,text = " ", font=("Arial", 12 ))
    selectFlightLabel.pack()
    
    newwindow1.mainloop()


    
# initial page    
my_w = Tk()
my_w.geometry('1550x800')
my_w.title("Airways registration")

my_font=("times",8,"bold")

bg = PhotoImage(file = r"C:\Users\shipm\Downloads\WhatsApp Image 2023-11-15 at 11.08.44 PM.png") 
canvas1 = Canvas( my_w, width = 400, height = 400) 
  
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,  anchor = "nw")

#write sign in and sign up functions
b3=Button(my_w,text="SIGN IN",width=50,command=signin)
b4=Button(my_w,text="SIGN UP",width=50,command=signup)


b3_canvas = canvas1.create_window( 400, 300,  
                                       anchor = "c", 
                                       window = b3)
b4_canvas = canvas1.create_window( 400, 400,  
                                       anchor = "c", 
                                       window = b4) 
my_w.mainloop()
