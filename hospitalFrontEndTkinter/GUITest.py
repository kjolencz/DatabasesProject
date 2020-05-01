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
def appointment_crud(toplev):
    #Method and button to add equipment to db
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

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `appointment` WHERE a_id = "
        sql_command = sql_command + id
        print(sql_command)
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
        print(cursor.execute(sql_command))
        conn.commit()

    label_apptId = Label(toplev, text="Appointment ID Number: ").grid(row=0, column=0, sticky="w")
    label_apptStartTime = Label(toplev, text="Appointment Start Time: ").grid(row=1, column=0, sticky="w")
    label_apptEndTime = Label(toplev, text="Appointment End Time: ").grid(row=2, column=0, sticky="w")

    box_id = Entry(toplev)
    box_id.grid(row=0, column=1)
    box_start = Entry(toplev)
    box_start.grid(row=1, column=1)
    box_end = Entry(toplev)
    box_end.grid(row=2, column=1)
    btn_add = Button(toplev, text="Add Appointment To Database", command=add_to_db)
    btn_add.grid(row=3, column=0, sticky = "w")
    btn_clear_fields = Button(toplev, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=3, column=1)
    btn_delete = Button(toplev, text="Delete From DB (Only Enter Appointment ID#", command=delete)
    btn_delete.grid(row=3, column=2)
    btn_update = Button(toplev, text="Update Appointment(Enter Appointment ID# And New Times", command=update)
    btn_update.grid(row=4, column=0)

    btn_search_by_id = Button(toplev, text="Search", command=search)
    btn_search_by_id.grid(row = 5, column = 0, sticky = "w")

    label_search = Label(toplev, text="TEST")
    label_search.grid(row=5, column=1, sticky="w")

    box_search = Entry(toplev)
    box_search.grid(row=5,column=2)

#METHOD -----------------------Open Second Window---------------------------------------------
def open():
    top = Toplevel()
    top.title(clicked.get())
    top.geometry("800x400")
    if clicked.get() == "Appointment":
        appointment_crud(top)
    #CLOSES WINDOW WHEN "Close Window Clicked"
    tnClose = Button(top, text="Close Window", command=top.destroy)

#Button To Open Second Window With CRUD Options--------------------------------------------------
buttonConfirmTable = Button(root, text="Open CRUD", command=open).pack()

#Keeps Windows Running
mainloop()
#Closes Connection To DB
conn.close()