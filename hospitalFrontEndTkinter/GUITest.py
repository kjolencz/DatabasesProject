from tkinter import *
from PIL import ImageTk, Image
import pymysql

root = Tk()
root.title('Hospital Project')
root.geometry("600x400")

conn = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    db="hospital"
)
cursor = conn.cursor()


clicked = StringVar()
clicked.set("Appointment")
dropdownMenu = OptionMenu(root, clicked, "Appointment", "Bill", "Medical Record", "Equipment", "Patient", "Doctor",
                          "Nurse", "Secretary", "Custodian", "Room", "Building", "Department")
dropdownMenu.pack()

#---------------------------------------CRUD Methods for Appointment Window----------------------------------------------
def appointment_crud(level):
    #Method and button to add appointment to db
    def add_to_db():
        values = ""
        values = values+box_id.get()
        values = values + ",\""
        values = values+box_start.get()
        values = values + "\",\""
        values = values+box_end.get() + "\""
        sql_command = "INSERT INTO `appointment`(`a_id`, `a_startTime`, `a_endTime`) VALUES ("
        sql_command = sql_command+values
        sql_command = sql_command+")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()


    #Method and Button to Clear Fields for Appointment
    def clear_fields():
        box_id.delete(0,END)
        box_start.delete(0,END)
        box_end.delete(0,END)
        box_search.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `appointment` WHERE a_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        startTime = "00:00"
        startTime = box_start.get()
        endTime = "00:00"
        endTime = box_end.get()
        id = 00
        id = box_id.get()
        sql_command = "UPDATE `appointment` SET `a_startTime`=\"" + startTime + "\"" + ",`a_endTime`=\"" + endTime + "\"" +  "WHERE a_id = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()


    def search():
        #SELECT `a_startTime`, `a_endTime` FROM `appointment` WHERE a_id = 1
        id = box_search.get()
        sql_command = "SELECT `a_startTime`, `a_endTime` FROM `appointment` WHERE a_id = " + id
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=5, column=1, sticky="w")
        conn.commit()
    #------------------------------------------Appointment Buttons/Boxes/Labels
    label_apptId = Label(level, text="Appointment ID Number: ").grid(row=0, column=0, sticky="w")
    label_apptStartTime = Label(level, text="Appointment Start Time: ").grid(row=1, column=0, sticky="w")
    label_apptEndTime = Label(level, text="Appointment End Time: ").grid(row=2, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_start = Entry(level)
    box_start.grid(row=1, column=1)
    box_end = Entry(level)
    box_end.grid(row=2, column=1)
    btn_add = Button(level, text="Add Appointment To Database", command=add_to_db)
    btn_add.grid(row=3, column=0, sticky = "w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=3, column=1)
    btn_delete = Button(level, text="Delete From DB (Only Enter Appointment ID#", command=delete)
    btn_delete.grid(row=3, column=2)
    btn_update = Button(level, text="Update Appointment(Enter Appointment ID# And New Times", command=update)
    btn_update.grid(row=4, column=0)

    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row = 5, column = 0, sticky = "w")

    searchResults = "Result"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=5, column=1, sticky="w")

    box_search = Entry(level)
    box_search.grid(row=5,column=2)
#---------------------------------------CRUD Methods for Bill Window----------------------------------------------
def bill_crud(level):
    #Method and button to add bill to db
    def add_to_db():
        billPaid = "0"
        if(box_isPaid.get() =="Y"):
            billPaid = "1"
        values = ""
        values = values + box_id.get()
        values = values + ",\""
        values = values + box_amount.get()
        values = values + "\","
        values = values + billPaid + ",\""
        values = values + box_billIsuee.get() + "\""
        sql_command = "INSERT INTO `bill`(`bill_id`, `bill_amount`, `bill_isPaid`, `bill_isuee`) VALUES ("
        sql_command = sql_command + values
        sql_command = sql_command + ")"
        print(sql_command)
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for Appointment
    def clear_fields():
        box_id.delete(0, END)
        box_isPaid.delete(0, END)
        box_billIsuee.delete(0, END)
        box_amount.delete(0, END)
        box_search.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `bill` WHERE bill_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        billAmount = "-1"
        billAmount = box_amount.get()
        billIsPaid = "0"
        billPaidString = box_isPaid.get()
        if(billPaidString == "Y"):
            billIsPaid = "1"
        billIsuee = ""
        billIsuee = box_billIsuee.get()
        id = 0
        id = box_id.get()
        sql_command = "UPDATE `bill` SET `bill_amount`=" + billAmount + ",`bill_isPaid`=" + billIsPaid + ", `bill_isuee`=\"" + billIsuee +"\" WHERE bill_id = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()


    def search():
        id = box_search.get()
        sql_command = "SELECT `bill_amount`, `bill_isPaid`, `bill_isuee` FROM `bill` WHERE bill_id = " + id
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=6, column=4, sticky="w")
        conn.commit()
    #------------------------------------------Appointment Buttons/Boxes/Labels
    label_billId = Label(level, text="Bill ID Number: ").grid(row=0, column=0, sticky="w")
    label_billAmount = Label(level, text="Bill Amount: ").grid(row=1, column=0, sticky="w")
    label_billIsPaid = Label(level, text="Is the bill already Paid (Y/N)").grid(row=2, column=0, sticky="w")
    label_billIssuee = Label(level, text="Bill Issuee").grid(row=3, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_amount = Entry(level)
    box_amount.grid(row=1, column=1)
    box_isPaid = Entry(level)
    box_isPaid.grid(row=2, column=1)
    box_billIsuee = Entry(level)
    box_billIsuee.grid(row=3, column=1)
    btn_add = Button(level, text="Add Bill To Database", command=add_to_db)
    btn_add.grid(row=4, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=4, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Bill ID#", command=delete)
    btn_delete.grid(row=4, column=3)
    btn_update = Button(level, text="Update Bill", command=update)
    btn_update.grid(row=4, column=0, sticky = "w")

    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=6, column=0, sticky="w")

    searchResults = "Result"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=6, column=1, sticky="w")

    box_search = Entry(level)
    box_search.grid(row=6, column=2)
#---------------------------------------CRUD Methods for Medical_Record Window----------------------------------------------
def mr_crud(level):
    #Method and button to add medical record to db
    def add_to_db():
        return

    #Method and Button to Clear Fields for Appointment
    def clear_fields():
        return

    #Method and Button to Delete ID From DB
    def delete():
        return

    def update():
        return


    def search():
        return
    #------------------------------------------Appointment Buttons/Boxes/Labels
    label_mrid= Label(level, text="Medical Record ID Number: ").grid(row=0, column=0, sticky="w")
    label_mrill = Label(level, text="Past Illnesses: ").grid(row=1, column=0, sticky="w")
    label_mrallergies = Label(level, text="Allergies: ").grid(row=2, column=0, sticky="w")
    label_mrfirstname = Label(level, text="First Name").grid(row=3, column=0, sticky="w")
    label_mrmiddlei= Label(level, text="Middle Initial").grid(row=4, column=0, sticky="w")
    label_mrlastname = Label(level, text="Last Name").grid(row=5, column=0, sticky="w")


    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_ill= Entry(level)
    box_ill.grid(row=1, column=1)
    box_allergies = Entry(level)
    box_allergies.grid(row=2, column=1)
    box_firstname = Entry(level)
    box_firstname.grid(row=3, column=1)
    box_middlei = Entry(level)
    box_middlei.grid(row=4, column=1)
    box_lastname = Entry(level)
    box_lastname.grid(row=5, column=1)
    btn_add = Button(level, text="Add Medical Record To Database", command=add_to_db)
    btn_add.grid(row=7, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=7, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Bill ID#", command=delete)
    btn_delete.grid(row=7, column=3)
    btn_update = Button(level, text="Update Bill", command=update)
    btn_update.grid(row=7, column=0, sticky = "w")

    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=8, column=0, sticky="w")

    searchResults = "Result"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=8, column=1, sticky="w")

    box_search = Entry(level)
    box_search.grid(row=8, column=2)
#METHOD -----------------------Open Second Window---------------------------------------------
def open():
    level= Toplevel()
    level.title(clicked.get())
    level.geometry("800x400")
    if clicked.get() == "Appointment":
        appointment_crud(level)
    if clicked.get() == "Bill":
        bill_crud(level)
    if clicked.get() == "Medical Record":
        mr_crud(level)
    #CLOSES WINDOW WHEN "Close Window Clicked"
    #tnClose = Button(top, text="Close Window", command=top.destroy)

#Button To Open Second Window With CRUD Options--------------------------------------------------
buttonConfirmTable = Button(root, text="Open CRUD", command=open).pack()

#Keeps Windows Running
mainloop()
#Closes Connection To DB
conn.close()