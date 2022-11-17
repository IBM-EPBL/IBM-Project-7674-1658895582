from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
       self.root = root
       self.root.geometry("1272x650+0+0")
       self.root.title("Customer_DataBase")
       #=========varabile========
       self.var_atten_Name = StringVar()
       self.var_atten_NO = StringVar()
       self.var_atten_Phone= StringVar()
       self.var_atten_Email = StringVar()
       self.var_atten_Address = StringVar()
       self.var_atten_date = StringVar()
       self.var_atten_Transport = StringVar()
       


       # first image
       img = Image.open("image/6.jpg")
       img = img.resize((1600, 800), Image.ANTIALIAS)
       self.photoimg = ImageTk.PhotoImage(img)

       bg_image = Label(self.root, image=self.photoimg)
       bg_image.place(x=0, y=0, width=1600, height=700)
       title_lb1 = Label(bg_image, text="Emerging Methods For Early Detection Of Forest Fires",
                         font=("time new roman", 25, "bold"), bg="green", fg="red")
       title_lb1.place(x=0, y=0, width=1600, height=75)

       main_frame = Frame(bg_image, bd=2, bg="white")
       main_frame.place(x=0, y=75, width=1600, height=700)

       # left label frame
       Left_frame = LabelFrame(main_frame, bd=2, bg="WHITE", relief=RIDGE,
                               font=("time new roman", 12, "bold"))
       Left_frame.place(x=20, y=10, width=590, height=535)

       img2_Left = Image.open("E:\\vasanth\\mini project\\SA3.png")
       img2_Left = img2_Left.resize((517, 97), Image.ANTIALIAS)
       self.photoimg2_Left = ImageTk.PhotoImage(img2_Left)
       b1 = Label(Left_frame, image=self.photoimg2_Left, cursor="hand2")
       b1.place(x=30, y=10, width=520, height=100)


      #logo
       #s a.engineeing College
       img1=Image.open("image/SA.png")
       img1 = img1.resize((100, 100), Image.ANTIALIAS)
       self.photoimg1 = ImageTk.PhotoImage(img1)
       b1 = Label(title_lb1, image=self.photoimg1)
       b1.place(x=30, y=0, width=100, height=70)

       #IBM
       img7=Image.open("image/IBM.png")
       img7 = img7.resize((100, 100), Image.ANTIALIAS)
       self.photoimg7 = ImageTk.PhotoImage(img7)
       b1 = Label(title_lb1, image=self.photoimg7)
       b1.place(x=150, y=0, width=100, height=70)

       #labeland entry
       # Class student information
       Customer_DataBase_frame = LabelFrame(Left_frame, bd=2, bg="white",
                                             relief=RIDGE, text="Customer_details",
                                             font=("time new roman", 12, "bold"))
       Customer_DataBase_frame.place(x=0, y=163, width=585.5, height=368)
       # Customer_Name
       Name_Label = Label(Customer_DataBase_frame, text="NAME:", font=("time new roman", 12, "bold"),
                                 bg="WHITE", width=0)
       Name_Label.grid(row=0, column=2,  pady=8)
       Name_Entry = ttk.Entry(Customer_DataBase_frame, textvariable=self.var_atten_NO,width=14, font=("time new roman", 12, "bold"))
       Name_Entry.grid(row=0, column=3,  pady=8)

       # Customer_NO
       No_Label = Label(Customer_DataBase_frame, text="N0:", font=("time new roman", 12, "bold"),
                                 bg="WHITE", width=0)
       No_Label.grid(row=0, column=0,  pady=8)
       No_Entry = ttk.Entry(Customer_DataBase_frame, textvariable=self.var_atten_Name,width=14, font=("time new roman", 12, "bold"))
       No_Entry.grid(row=0, column=1,  pady=8)
       

       # Phone Number
       Phone_Label = Label(Customer_DataBase_frame, text="Phone No:", font=("time new roman", 12, "bold"),
                                 bg="WHITE", width=0)
       Phone_Label.grid(row=1, column=0,  pady=8)
       Phone_Entry = ttk.Entry(Customer_DataBase_frame, textvariable=self.var_atten_Phone,width=14, font=("time new roman", 12, "bold"))
       Phone_Entry.grid(row=1, column=1,  pady=8)

       # Email
       Email_Label = Label(Customer_DataBase_frame, text="Email:", font=("time new roman", 12, "bold"),
                                 bg="WHITE", width=0)
       Email_Label.grid(row=1, column=2,  pady=8)
       Email_Entry = ttk.Entry(Customer_DataBase_frame,textvariable=self.var_atten_Email, width=14, font=("time new roman", 12, "bold"))
       Email_Entry.grid(row=1, column=3,  pady=8)

       # Address
       Address_Label = Label(Customer_DataBase_frame, text="Address:", font=("time new roman", 12, "bold"),
                                 bg="WHITE", width=0)
       Address_Label.grid(row=2, column=0,  pady=8)
       Address_Entry = ttk.Entry(Customer_DataBase_frame, textvariable=self.var_atten_Address,width=14, font=("time new roman", 12, "bold"))
       Address_Entry.grid(row=2, column=1,  pady=8)



       # date
       date_Label = Label(Customer_DataBase_frame, text="Date:", font=("time new roman", 12, "bold"),
                                 bg="WHITE", width=0)
       date_Label.grid(row=2, column=2, pady=8)
       date_entry = ttk.Entry(Customer_DataBase_frame, textvariable=self.var_atten_date,width=14, font=("time new roman", 12, "bold"))
       date_entry.grid(row=2, column=3, pady=8)
       #Transport
       Transport_Label = Label(Customer_DataBase_frame, text="Transport Status", font=("time new roman", 11, "bold"),
                                 bg="WHITE", width=0)
       Transport_Label.grid(row=3, column=0)

       self.Transport_status = ttk.Combobox(Customer_DataBase_frame,
                                   font=("time new roman", 13, "bold"), textvariable=self.var_atten_Transport,
                                   state="read only", width=12)
       self.Transport_status["values"] = ("Status", "Car", "Bike","Truck","Ambulance",)
       self.Transport_status.current(0)
       self.Transport_status.grid(row=3, column=1, pady=8)

       # button frame
       btn_Frame = Frame(Customer_DataBase_frame, bd=2, relief=RIDGE, bg="white")
       btn_Frame.place(x=0, y=220, width=715, height=100)

       save_btn = Button(btn_Frame, text="Save",command=self.add_data,width=15, font=("time new roman", 12, "bold"),
                         bg="blue", fg="white")
       save_btn.grid(row=0, column=0)

       update_btn = Button(btn_Frame, text="Update",command=self.update_data ,width=13,
                           font=("time new roman", 12, "bold"), bg="blue", fg="white")
       update_btn.grid(row=0, column=1)

       delete_btn = Button(btn_Frame, text="Delete", command=self.delete_data, width=13,
                           font=("time new roman", 12, "bold"), bg="blue",
                           fg="white")
       delete_btn.grid(row=0, column=2)

       reset_btn = Button(btn_Frame, text="Reset", command=self.reset_data, width=13,
                          font=("time new roman", 12, "bold"), bg="blue", fg="white")
       reset_btn.grid(row=0, column=3)







      # right label frame
       Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Customer Details",
                                font=("time new roman", 12, "bold"))
       Right_frame.place(x=620, y=10, width=620, height=535)

       img3_Right = Image.open("E:\\vasanth\\mini project\\SA3.png")
       img3_Right = img3_Right.resize((517, 97), Image.ANTIALIAS)
       self.photoimg3_Right = ImageTk.PhotoImage(img3_Right)
       b1 = Label(Right_frame, image=self.photoimg3_Right, cursor="hand2")
       b1.place(x=0, y=0, width=590, height=100)

       # ========serach System========

       Serach_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Serach System",
                                 font=("time new roman", 12, "bold"))
       Serach_frame.place(x=5, y=100, width=590, height=100)


       ShowAll_btn = Button(Serach_frame, text="Show All", width=13,
                            font=("time new roman", 10, "bold"), bg="blue",
                            fg="white")
       ShowAll_btn.grid(row=1, column=1, padx=2)
       # table frame
       table_frame = Frame(Right_frame, bd=2, bg="green", relief=RIDGE)
       table_frame.place(x=5, y=205, width=590, height=300)

       scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
       scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

       self.Customer_table = ttk.Treeview(table_frame, columns=("No","Name","Phone", "Email", "Address", "Transport", "date"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_y.pack(side=RIGHT, fill=Y)

       scroll_x.config(command=self.Customer_table.xview)
       scroll_y.config(command=self.Customer_table.yview)

       self.Customer_table.heading("No", text="Customer N0")
       self.Customer_table.heading("Name", text="Customer Name")
       self.Customer_table.heading("Phone", text="Phone Number")
       self.Customer_table.heading("Email", text="Email ID")
       self.Customer_table.heading("Address", text="Address")
       self.Customer_table.heading("date", text="Date")
       self.Customer_table.heading("Transport", text="Transport")
       self.Customer_table["show"] = "headings"

       self.Customer_table.column("No", width=100)
       self.Customer_table.column("Name", width=100)
       self.Customer_table.column("Phone", width=100)
       self.Customer_table.column("Email", width=100)
       self.Customer_table.column("Address", width=100)
       self.Customer_table.column("date", width=100)
       self.Customer_table.column("Transport", width=100)
       self.Customer_table.pack(fill=BOTH, expand=1)
       self.Customer_table.bind("<ButtonRelease>", self.get_cursor)
       self.fetch_data()

       # ======FUNCTION DECRATION=====
    def add_data(self):
        if (self.var_atten_Name.get() == "" or self.var_atten_Email.get() == "" or self.var_atten_Phone.get() == ""):
              messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                                  database="customer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into Customer values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_atten_Name.get(),
                    self.var_atten_NO.get(),
                    self.var_atten_Phone.get(),
                    self.var_atten_Email.get(),
                    self.var_atten_Address.get(),
                    self.var_atten_date.get(),
                    self.var_atten_Transport.get()
                   ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

                   # _____fetch data___

    def fetch_data(self):
           conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                          database="customer")
           my_cursor = conn.cursor()
           my_cursor.execute("Select *  From Customer")
           data = my_cursor.fetchall()
           if len(data) != 0:
               self.Customer_table.delete(*self.Customer_table.get_children())
               for i in data:
                   self.Customer_table.insert("", END, values=i)
               conn.commit()
           conn.close()
           # =======get cursor======

    def get_cursor(self, event=""):
           cursor_focus = self.Customer_table.focus()
           content = self.Customer_table.item(cursor_focus)
           data = content["values"]

           self.var_atten_Name.set(data[0]),
           self.var_atten_NO.set(data[1]),
           self.var_atten_Phone.set(data[2]),
           self.var_atten_Email.set(data[3]),
           self.var_atten_Address.set(data[4]),
           self.var_atten_date.set(data[5]),
           self.var_atten_Transport.set(data[6])

       # updata function
    def update_data(self):
           if (self.var_atten_Name.get() == "" or self.var_atten_Phone.get() == "" or self.var_atten_Email.get() == ""):
               messagebox.showerror("Error", "All Fields are required", parent=self.root)
           else:
               try:
                   update = messagebox.askyesno("Update", "Are You want to update this Customer details",
                                                parent=self.root)
                   if update > 0:
                       conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                                      database="customer")
                       my_cursor = conn.cursor()
                       my_cursor.execute(
                           "update Customer set  Name=%s, No=%s,Phone=%s, Email=%s,"
                           " Address=%s,  date=%s, Transport=%s", (
                               self.var_atten_Name.get(),
                               self.var_atten_NO.get(),
                               self.var_atten_Phone.get(),
                               self.var_atten_Email.get(),
                               self.var_atten_Address.get(),
                               self.var_atten_date.get(),
                               self.var_atten_Transport.get()

                           ))
                   else:
                       if not update:
                           return
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Success", "Customer details successfully update completed", parent=self.root)
               except Exception as es:
                   messagebox.showerror("Error", f"Do To:{str(es)}", parent=self.root)
           # delete function

    def delete_data(self):
           if self.var_atten_Email.get == "":
               messagebox.showerror("Error", "Customer id must be required", parent=self.root)
           else:
               try:
                   delete = messagebox.askyesno("Customer delete page", "Do You want to delete this Customer",
                                                parent=self.root)
                   if delete > 0:
                       conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                                      database="customer")
                       my_cursor = conn.cursor()
                       sql = "delete from Customer where Email=%s"
                       val = (self.var_atten_Email.get(),)
                       my_cursor.execute(sql, val)
                   else:
                       if not delete:
                           return
                   conn.commit()
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Delete", "successfully deleted Customer details", parent=self.root)
               except Exception as es:
                   messagebox.showerror("Error", f"Do To:{str(es)}", parent=self.root)
           # reset functiom

    def reset_data(self):


           self.var_atten_Name.set("")
           self.var_atten_NO.set("")
           self.var_atten_Phone.set("")
           self.var_atten_Email.set("")
           self.var_atten_Address.set("")
           self.var_atten_date.set("")
           self.var_atten_Transport.set("")

       # Take Photos Samples or generate data
    def generate_dataset(self):
           if (self.var_atten_Name.get() == "" or self.var_atten_Phone.get() == "" or self.var_atten_Email.get() == ""):
               messagebox.showerror("Error", "All Fields are required", parent=self.root)
           else:
               try:
                   conn = mysql.connector.connect(host="localhost", user="root", passwd="Vasanthvishva2308",
                                                  database="customer")
                   my_cursor = conn.cursor()
                   my_cursor.execute("Select * from Customer")
                   myresult = my_cursor.fetchall()
                   id = 0
                   for x in myresult:
                       id += 1
                   my_cursor.execute( "update Customer set  Name=%s, No=%s,Phone=%s, Email=%s,"
                           " Address=%s,  date=%s,Transport=%s", (
                       self.var_atten_Name.get(),
                       self.var_atten_NO.get(),
                       self.var_atten_Phone.get(),
                       self.var_atten_Email.get(),
                       self.var_atten_Address.get(),
                       self.var_atten_date.get(), 
                       self.var_atten_Transport.get() == id + 1

                                     ))
                   conn.commit()
                   self.fetch_data()
                   self.reset_data()
                   conn.close()
                   messagebox.showinfo("Result", "Generating data sets compeled!!!!")
               except Exception as es:
                   messagebox.showerror("Error", f"Do To:{str(es)}", parent=self.root)
   

                   

    




if __name__ == '__main__':
    root = tk.Tk()
    obj = Attendance(root)
    root.mainloop()