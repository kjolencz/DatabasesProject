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
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for Bill
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
    #------------------------------------------Bill Buttons/Boxes/Labels
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
        id = box_id.get()
        ill = box_ill.get()
        allergy = box_allergies.get()
        firstn = box_firstname.get()
        middlei = box_middlei.get()
        if(len(middlei) != 1):
            middlei = " "
        lastn = box_lastname.get()

        values = id + ",\"" + ill + "\",\"" + allergy + "\",\"" + firstn + "\",\"" + middlei + "\",\"" + lastn + "\""
        sql_command = "INSERT INTO `medical record`(`mr_id`, `mr_pastIllnesses`, `mr_allergies`, `mr_fn`, `mr_mi`, `mr_ln`) VALUES ("
        sql_command = sql_command + values
        sql_command = sql_command + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for medical record
    def clear_fields():
        box_lastname.delete(0,END)
        box_middlei.delete(0,END)
        box_firstname.delete(0,END)
        box_allergies.delete(0,END)
        box_ill.delete(0,END)
        box_search.delete(0,END)
        box_id.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `Medical Record` WHERE mr_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        pastIllness = ""
        pastIllness = box_ill.get()
        allergies = ""
        allergies = box_allergies.get()
        firstn= ""
        firstn = box_firstname.get()
        mi = ""
        mi = box_middlei.get()
        lastn = ""
        lastn = box_lastname.get()
        id = 0
        id = box_id.get()
        sql_command = "UPDATE `medical record` SET `mr_pastIllnesses`=\"" + pastIllness + "\",`mr_allergies`=\"" + allergies + "\", `mr_fn`=\"" + firstn + "\""  + ",`mr_mi`=\"" + mi + "\", `mr_ln`=\"" + lastn +"\" WHERE mr_id = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `mr_pastIllnesses`, `mr_allergies`, `mr_fn`, `mr_mi`, `mr_ln` FROM `medical record` WHERE mr_id = " + id
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=8, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Medical record Buttons/Boxes/Labels
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
    btn_delete = Button(level, text="Delete From DB (Only Enter Medical Record ID#", command=delete)
    btn_delete.grid(row=7, column=3)
    btn_update = Button(level, text="Update Medical Record", command=update)
    btn_update.grid(row=7, column=0, sticky = "w")

    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=8, column=0, sticky="w")

    searchResults = "Result"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=8, column=3, sticky="w")

    box_search = Entry(level)
    box_search.grid(row=8, column=2)
#---------------------------------------CRUD Methods for Equipment Window----------------------------------------------
def eq_crud(level):
    #Method and button to add equipment to db
    def add_to_db():
        id = box_id.get()
        desc = box_desc.get()
        name = box_name.get()
        values = id + ",\"" + desc + "\",\"" + name + "\""
        sql_command = "INSERT INTO `equipment`(`eq_id`, `eq_desc`, `eq_name`) VALUES ("
        sql_command = sql_command + values
        sql_command = sql_command + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for medical record
    def clear_fields():
        box_name.delete(0,END)
        box_desc.delete(0,END)
        box_id.delete(0,END)
        box_search.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `equipment` WHERE eq_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        description = ""
        description = box_desc.get()
        name = ""
        name = box_name.get()
        id = 0
        id = box_id.get()
        sql_command = "UPDATE `equipment` SET `eq_desc`=\"" + description + "\",`eq_name`=\""+ name + "\" WHERE eq_id = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `eq_desc`, `eq_name` FROM `equipment` WHERE eq_id = " + id
        print(sql_command)
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=8, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Equipment Buttons/Boxes/Labels
    label_eqid= Label(level, text="Equipment ID Number: ").grid(row=0, column=0, sticky="w")
    label_eqdesc = Label(level, text="Equipment Description: ").grid(row=1, column=0, sticky="w")
    label_eqname = Label(level, text="Equipment Name: ").grid(row=2, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_desc= Entry(level)
    box_desc.grid(row=1, column=1)
    box_name = Entry(level)
    box_name.grid(row=2, column=1)

    btn_add = Button(level, text="Add Equipment To Database", command=add_to_db)
    btn_add.grid(row=7, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=7, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Equipment ID#", command=delete)
    btn_delete.grid(row=7, column=3)
    btn_update = Button(level, text="Update Equipment", command=update)
    btn_update.grid(row=7, column=0, sticky = "w")

    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=8, column=0, sticky="w")

    searchResults = "Result"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=8, column=3, sticky="w")

    box_search = Entry(level)
    box_search.grid(row=8, column=2)
#---------------------------------------CRUD Methods for Patient Window----------------------------------------------
def patient_crud(level):
    #Method and button to add patient to db

    def add_to_db():
        id = box_id.get()
        fn = box_fn.get()
        ln = box_ln.get()
        mi=box_mi.get()
        gender = box_gender.get()
        phoneNum = box_phonenum.get()
        ssn = box_ssn.get()
        admissiondate = box_admissiondate.get()
        releasedate = box_releasedate.get()
        insurancename = box_insurancename.get()
        insurancenum = box_insurancenum.get()
        buildingnum = box_buildingnum.get()
        roomnum = box_roomnum.get()
        medicalrecordid = box_mrid.get()
        billid = box_billid.get()
        appointmentid = box_apptid.get()


        values = id + ",\"" + fn + "\",\"" + ln + "\""+ ",\"" + mi + "\",\"" + gender + "\""+ ",\"" + phoneNum + "\",\"" + ssn + "\""+ ",\"" + admissiondate + "\",\"" + releasedate + "\",\""+ insurancename + "\",\"" + insurancenum + "\""+ ",\"" + buildingnum + "\",\"" + roomnum + "\", \""+ medicalrecordid + "\",\"" + billid + "\""+ ",\"" + appointmentid + "\""""
        sql_command = "INSERT INTO `patient`(`p_id`, `p_firstName`, `p_lastName`, `p_middleIn`, `p_gender`, `p_phoneNum`, `p_ssn`, `p_admissionDate`, `p_releaseDate`, `p_insuranceName`, `p_insuranceNum`, `p_buildingNum`, `p_roomNum`, `p_medicalRecordId`, `p_billId`, `p_appointmentId`) VALUES ("
        sql_command = sql_command + values
        sql_command = sql_command + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for patient
    def clear_fields():
        box_id.delete(0,END)
        box_fn.delete(0,END)
        box_ln.delete(0,END)
        box_mi.delete(0,END)
        box_gender.delete(0,END)
        box_phonenum.delete(0,END)
        box_ssn.delete(0,END)
        box_admissiondate.delete(0,END)
        box_releasedate.delete(0,END)
        box_insurancename.delete(0,END)
        box_insurancenum.delete(0,END)
        box_buildingnum.delete(0,END)
        box_roomnum.delete(0,END)
        box_mrid.delete(0,END)
        box_billid.delete(0,END)
        box_apptid.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `patient` WHERE p_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        id = box_id.get()
        fn = box_fn.get()
        ln = box_ln.get()
        mi = box_mi.get()
        gender = box_gender.get()
        phoneNum = box_phonenum.get()
        ssn = box_ssn.get()
        admissiondate = box_admissiondate.get()
        releasedate = box_releasedate.get()
        insurancename = box_insurancename.get()
        insurancenum = box_insurancenum.get()
        buildingnum = box_buildingnum.get()
        roomnum = box_roomnum.get()
        medicalrecordid = box_mrid.get()
        billid = box_billid.get()
        appointmentid = box_apptid.get()
        sql_command = "UPDATE `patient` SET `p_firstName`=\"" + fn + "\",`p_lastName`=\""+ ln + "\",`p_middleIn`=\""+ mi + "\",`p_gender`=\"" + gender + "\",`p_phoneNum`=\""+ phoneNum + "\",`p_ssn`="+ ssn + ",`p_admissionDate`=\""+ admissiondate + "\",`p_releaseDate`=\""+ releasedate + "\",`p_insuranceName`=\""+ insurancename + "\",`p_insuranceNum`=\"" + insurancenum + "\",`p_buildingNum`=" + buildingnum + ",`p_roomNum`="+ roomnum + ",`p_medicalRecordId`="+ medicalrecordid + ",`p_billId`="+ billid + ",`p_appointmentId`="+ appointmentid + " WHERE p_id = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `p_firstName`, `p_lastName`, `p_middleIn`, `p_gender`,`p_phoneNum`,`p_ssn`,`p_admissionDate`,`p_releaseDate`,`p_insuranceName`,`p_insuranceNum`,`p_buildingNum`,`p_roomNum`,`p_medicalRecordId`,`p_billId`,`p_appointmentId`  FROM `patient` WHERE p_id = " + id
        print(sql_command)
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=8, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Patient Buttons/Boxes/Labels
    label_id= Label(level, text="Patient ID Number: ").grid(row=0, column=0, sticky="w")
    label_fn = Label(level, text="Patient First Name: ").grid(row=1, column=0, sticky="w")
    label_ln = Label(level, text="Patient Last Name: ").grid(row=2, column=0, sticky="w")
    label_mi = Label(level, text="Patient Middle Initial: ").grid(row=3, column=0, sticky="w")
    label_gender= Label(level, text="Patient Gender: ").grid(row=4, column=0, sticky="w")
    label_phonenum = Label(level, text="Patient Phone Number: ").grid(row=5, column=0, sticky="w")
    label_patientssn = Label(level, text="Patient Social Security Number(No Hyphens): ").grid(row=6, column=0, sticky="w")
    label_admissiondate= Label(level, text="Patient Admission Date (yyyy-dd-mm): ").grid(row=7, column=0, sticky="w")
    label_releasedate = Label(level, text="Patient Release Date (yyyy-dd-mm): ").grid(row=8, column=0, sticky="w")
    label_insurancename = Label(level, text="Patient Insurance Name: ").grid(row=9, column=0, sticky="w")
    label_insurancenum= Label(level, text="Patient Insurance Number: ").grid(row=10, column=0, sticky="w")
    label_buildingnum = Label(level, text="Patient Building Number: ").grid(row=11, column=0, sticky="w")
    label_roomnum = Label(level, text="Patient Room Number: ").grid(row=12, column=0, sticky="w")
    label_medicalrecordid = Label(level, text="Patient Medical Record ID: ").grid(row=13, column=0, sticky="w")
    label_billid = Label(level, text="Patient Bill ID: ").grid(row=14, column=0, sticky="w")
    label_appointmentid = Label(level, text="Patient Appointment ID: ").grid(row=15, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_fn = Entry(level)
    box_fn.grid(row=1,column=1)
    box_ln = Entry(level)
    box_ln.grid(row=2,column=1)
    box_mi = Entry(level)
    box_mi.grid(row=3, column=1)
    box_gender = Entry(level)
    box_gender.grid(row=4, column=1)
    box_phonenum = Entry(level)
    box_phonenum.grid(row=5, column=1)
    box_ssn = Entry(level)
    box_ssn.grid(row=6, column=1)
    box_admissiondate = Entry(level)
    box_admissiondate.grid(row=7, column=1)
    box_releasedate = Entry(level)
    box_releasedate.grid(row=8, column=1)
    box_insurancename= Entry(level)
    box_insurancename.grid(row=9, column=1)
    box_insurancenum = Entry(level)
    box_insurancenum.grid(row=10, column=1)
    box_buildingnum = Entry(level)
    box_buildingnum.grid(row=11, column=1)
    box_roomnum = Entry(level)
    box_roomnum.grid(row=12, column=1)
    box_mrid = Entry(level)
    box_mrid.grid(row=13, column=1)
    box_billid = Entry(level)
    box_billid.grid(row=14, column=1)
    box_apptid = Entry(level)
    box_apptid.grid(row=15, column=1)

    btn_add = Button(level, text="Add Patient To Database", command=add_to_db)
    btn_add.grid(row=16, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=16, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Patient ID#", command=delete)
    btn_delete.grid(row=16, column=3)
    btn_update = Button(level, text="Update Patient Information (Please Fill In All Information)", command=update)
    btn_update.grid(row=16, column=0, sticky = "w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=17, column=0, sticky="w")
    searchResults = "Result"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=17, column=1, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=17, column=2)
#---------------------------------------CRUD Methods for Doctor Window----------------------------------------------
def doctor_crud(level):
    #Method and button to add doctor to db

    def add_to_db():
        id = box_id.get()
        fn = box_fn.get()
        ln = box_ln.get()
        mi=box_mi.get()
        gender = box_gender.get()
        salary = box_salary.get()
        phoneNum = box_phonenum.get()
        ssn = box_ssn.get()
        startdate = box_startdate.get()
        enddate = box_enddate.get()

        values = id + ",\"" + fn + "\",\"" + ln + "\""+ ",\"" + mi + "\",\"" + gender + "\",\"" + salary + "\",\"" + phoneNum + "\",\"" + ssn + "\""+ ",\"" + startdate + "\",\"" + enddate + "\""
        sql_command = "INSERT INTO `doctor`(`doc_id`, `doc_firstName`, `doc_lastName`, `doc_middleIn`, `doc_gender`, `doc_salary`,`doc_phoneNum`, `doc_ssn`, `doc_startDate`, `doc_endDate`) VALUES ("
        sql_command = sql_command + values
        sql_command = sql_command + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for doctor
    def clear_fields():
        box_id.delete(0,END)
        box_fn.delete(0,END)
        box_ln.delete(0,END)
        box_mi.delete(0,END)
        box_gender.delete(0,END)
        box_phonenum.delete(0,END)
        box_ssn.delete(0,END)
        box_startdate.delete(0,END)
        box_enddate.delete(0,END)
        box_salary.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `doctor` WHERE doc_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        id = box_id.get()
        fn = box_fn.get()
        ln = box_ln.get()
        mi = box_mi.get()
        gender = box_gender.get()
        salary = box_salary.get()
        phoneNum = box_phonenum.get()
        ssn = box_ssn.get()
        startdate = box_startdate.get()
        enddate = box_enddate.get()
        sql_command = "UPDATE `doctor` SET `doc_firstName`=\"" + fn + "\",`doc_lastName`=\""+ ln + "\",`doc_middleIn`=\""+ mi + "\",`doc_gender`=\"" + gender + "\",`doc_salary`=\"" + salary + "\",`doc_phoneNum`=\""+ phoneNum + "\",`doc_ssn`="+ ssn + ",`doc_startDate`=\""+ startdate + "\",`doc_endDate`=\""+ enddate + "\" WHERE doc_id = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `doc_firstName`, `doc_lastName`, `doc_middleIn`, `doc_gender`,`doc_salary`,`doc_phoneNum`,`doc_ssn`,`doc_startDate`,`doc_endDate`  FROM `doctor` WHERE doc_id = " + id
        print(sql_command)
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=11, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Doctor Buttons/Boxes/Labels
    label_id= Label(level, text="Doctor ID Number: ").grid(row=0, column=0, sticky="w")
    label_fn = Label(level, text="Doctor First Name: ").grid(row=1, column=0, sticky="w")
    label_ln = Label(level, text="Doctor Last Name: ").grid(row=2, column=0, sticky="w")
    label_mi = Label(level, text="Doctor Middle Initial: ").grid(row=3, column=0, sticky="w")
    label_gender= Label(level, text="Doctor Gender: ").grid(row=4, column=0, sticky="w")
    label_salary = Label(level, text="Doctor Salary: ").grid(row=5, column=0, sticky="w")
    label_phonenum = Label(level, text="Doctor Phone Number: ").grid(row=6, column=0, sticky="w")
    label_patientssn = Label(level, text="Doctor Social Security Number(No Hyphens): ").grid(row=7, column=0, sticky="w")
    label_startdate= Label(level, text="Doctor Start Date (yyyy-dd-mm): ").grid(row=8, column=0, sticky="w")
    label_enddate = Label(level, text="Doctor End Date (yyyy-dd-mm): ").grid(row=9, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_fn = Entry(level)
    box_fn.grid(row=1,column=1)
    box_ln = Entry(level)
    box_ln.grid(row=2,column=1)
    box_mi = Entry(level)
    box_mi.grid(row=3, column=1)
    box_gender = Entry(level)
    box_gender.grid(row=4, column=1)
    box_salary = Entry(level)
    box_salary.grid(row=5, column=1)
    box_phonenum = Entry(level)
    box_phonenum.grid(row=6, column=1)
    box_ssn = Entry(level)
    box_ssn.grid(row=7, column=1)
    box_startdate = Entry(level)
    box_startdate.grid(row=8, column=1)
    box_enddate = Entry(level)
    box_enddate.grid(row=9, column=1)

    btn_add = Button(level, text="Add Doctor To Database", command=add_to_db)
    btn_add.grid(row=10, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=10, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Doctor ID#", command=delete)
    btn_delete.grid(row=10, column=3)
    btn_update = Button(level, text="Update Doctor Information (Please Fill In All Information)", command=update)
    btn_update.grid(row=10, column=0, sticky = "w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=11, column=0, sticky="w")
    searchResults = "Result"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=11, column=1, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=11, column=2)
#---------------------------------------CRUD Methods for Nurse Window----------------------------------------------
def nurse_crud(level):
    #Method and button to add Nurse to db

    def add_to_db():
        id = box_id.get()
        fn = box_fn.get()
        ln = box_ln.get()
        mi=box_mi.get()
        gender = box_gender.get()
        salary = box_salary.get()
        phoneNum = box_phonenum.get()
        ssn = box_ssn.get()
        startdate = box_startdate.get()
        enddate = box_enddate.get()

        values = id + ",\"" + fn + "\",\"" + ln + "\""+ ",\"" + mi + "\",\"" + gender + "\",\"" + salary + "\",\"" + phoneNum + "\",\"" + ssn + "\""+ ",\"" + startdate + "\",\"" + enddate + "\""
        sql_command = "INSERT INTO `nurse`(`n_id`, `n_firstName`, `n_lastName`, `n_middleIn`, `n_gender`, `n_salary`,`n_phoneNum`, `n_ssn`, `n_startDate`, `n_endDate`) VALUES ("
        sql_command = sql_command + values
        sql_command = sql_command + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for nurse
    def clear_fields():
        box_id.delete(0,END)
        box_fn.delete(0,END)
        box_ln.delete(0,END)
        box_mi.delete(0,END)
        box_gender.delete(0,END)
        box_phonenum.delete(0,END)
        box_ssn.delete(0,END)
        box_startdate.delete(0,END)
        box_enddate.delete(0,END)
        box_salary.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `nurse` WHERE n_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        id = box_id.get()
        fn = box_fn.get()
        ln = box_ln.get()
        mi = box_mi.get()
        gender = box_gender.get()
        salary = box_salary.get()
        phoneNum = box_phonenum.get()
        ssn = box_ssn.get()
        startdate = box_startdate.get()
        enddate = box_enddate.get()
        sql_command = "UPDATE `nurse` SET `n_firstName`=\"" + fn + "\",`n_lastName`=\""+ ln + "\",`n_middleIn`=\""+ mi + "\",`n_gender`=\"" + gender + "\",`n_salary`=\"" + salary + "\",`n_phoneNum`=\""+ phoneNum + "\",`n_ssn`="+ ssn + ",`n_startDate`=\""+ startdate + "\",`n_endDate`=\""+ enddate + "\" WHERE n_id = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `n_firstName`, `n_lastName`, `n_middleIn`, `n_gender`,`n_salary`,`n_phoneNum`,`n_ssn`,`n_startDate`,`n_endDate`  FROM `nurse` WHERE n_id = " + id
        print(sql_command)
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=11, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Nurse Buttons/Boxes/Labels
    label_id= Label(level, text="Nurse ID Number: ").grid(row=0, column=0, sticky="w")
    label_fn = Label(level, text="Nurse First Name: ").grid(row=1, column=0, sticky="w")
    label_ln = Label(level, text="Nurse Last Name: ").grid(row=2, column=0, sticky="w")
    label_mi = Label(level, text="Nurse Middle Initial: ").grid(row=3, column=0, sticky="w")
    label_gender= Label(level, text="Nurse Gender: ").grid(row=4, column=0, sticky="w")
    label_salary = Label(level, text="Nurse Salary: ").grid(row=5, column=0, sticky="w")
    label_phonenum = Label(level, text="Nurse Phone Number: ").grid(row=6, column=0, sticky="w")
    label_patientssn = Label(level, text="Nurse Social Security Number(No Hyphens): ").grid(row=7, column=0, sticky="w")
    label_startdate= Label(level, text="Nurse Start Date (yyyy-dd-mm): ").grid(row=8, column=0, sticky="w")
    label_enddate = Label(level, text="Nurse End Date (yyyy-dd-mm): ").grid(row=9, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_fn = Entry(level)
    box_fn.grid(row=1,column=1)
    box_ln = Entry(level)
    box_ln.grid(row=2,column=1)
    box_mi = Entry(level)
    box_mi.grid(row=3, column=1)
    box_gender = Entry(level)
    box_gender.grid(row=4, column=1)
    box_salary = Entry(level)
    box_salary.grid(row=5, column=1)
    box_phonenum = Entry(level)
    box_phonenum.grid(row=6, column=1)
    box_ssn = Entry(level)
    box_ssn.grid(row=7, column=1)
    box_startdate = Entry(level)
    box_startdate.grid(row=8, column=1)
    box_enddate = Entry(level)
    box_enddate.grid(row=9, column=1)

    btn_add = Button(level, text="Add Nurse To Database", command=add_to_db)
    btn_add.grid(row=10, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=10, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Nurse ID#", command=delete)
    btn_delete.grid(row=10, column=3)
    btn_update = Button(level, text="Update Nurse Information (Please Fill In All Information)", command=update)
    btn_update.grid(row=10, column=0, sticky = "w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=11, column=0, sticky="w")
    searchResults = "Result"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=11, column=1, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=11, column=2)
#---------------------------------------CRUD Methods for Secretary Window----------------------------------------------
def secretary_crud(level):
    #Method and button to add secretary to db

    def add_to_db():
        id = box_id.get()
        fn = box_fn.get()
        ln = box_ln.get()
        mi=box_mi.get()
        gender = box_gender.get()
        salary = box_salary.get()
        phoneNum = box_phonenum.get()
        ssn = box_ssn.get()
        startdate = box_startdate.get()
        enddate = box_enddate.get()

        values = id + ",\"" + fn + "\",\"" + ln + "\""+ ",\"" + mi + "\",\"" + gender + "\",\"" + salary + "\",\"" + phoneNum + "\",\"" + ssn + "\""+ ",\"" + startdate + "\",\"" + enddate + "\""
        sql_command = "INSERT INTO `secretary`(`s_id`, `s_firstName`, `s_lastName`, `s_middleIn`, `s_gender`, `s_salary`,`s_phoneNumber`, `s_ssn`, `s_startDate`, `s_endDate`) VALUES ("
        sql_command = sql_command + values
        sql_command = sql_command + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for secretary
    def clear_fields():
        box_id.delete(0,END)
        box_fn.delete(0,END)
        box_ln.delete(0,END)
        box_mi.delete(0,END)
        box_gender.delete(0,END)
        box_phonenum.delete(0,END)
        box_ssn.delete(0,END)
        box_startdate.delete(0,END)
        box_enddate.delete(0,END)
        box_salary.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `secretary` WHERE s_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        id = box_id.get()
        fn = box_fn.get()
        ln = box_ln.get()
        mi = box_mi.get()
        gender = box_gender.get()
        salary = box_salary.get()
        phoneNum = box_phonenum.get()
        ssn = box_ssn.get()
        startdate = box_startdate.get()
        enddate = box_enddate.get()
        sql_command = "UPDATE `secretary` SET `s_firstName`=\"" + fn + "\",`s_lastName`=\""+ ln + "\",`s_middleIn`=\""+ mi + "\",`s_gender`=\"" + gender + "\",`s_salary`=\"" + salary + "\",`s_phoneNumber`=\""+ phoneNum + "\",`s_ssn`="+ ssn + ",`s_startDate`=\""+ startdate + "\",`s_endDate`=\""+ enddate + "\" WHERE s_id = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `s_firstName`, `s_lastName`, `s_middleIn`, `s_gender`,`s_salary`,`s_phoneNumber`,`s_ssn`,`s_startDate`,`s_endDate`  FROM `secretary` WHERE s_id = " + id
        print(sql_command)
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=11, column=3, sticky="w")
        conn.commit()
    #------------------------------------------secretary Buttons/Boxes/Labels
    label_id= Label(level, text="Secretary ID Number: ").grid(row=0, column=0, sticky="w")
    label_fn = Label(level, text="Secretary First Name: ").grid(row=1, column=0, sticky="w")
    label_ln = Label(level, text="Secretary Last Name: ").grid(row=2, column=0, sticky="w")
    label_mi = Label(level, text="Secretary Middle Initial: ").grid(row=3, column=0, sticky="w")
    label_gender= Label(level, text="Secretary Gender: ").grid(row=4, column=0, sticky="w")
    label_salary = Label(level, text="Secretary Salary: ").grid(row=5, column=0, sticky="w")
    label_phonenum = Label(level, text="Secretary Phone Number: ").grid(row=6, column=0, sticky="w")
    label_patientssn = Label(level, text="Secretary Social Security Number(No Hyphens): ").grid(row=7, column=0, sticky="w")
    label_startdate= Label(level, text="Secretary Start Date (yyyy-dd-mm): ").grid(row=8, column=0, sticky="w")
    label_enddate = Label(level, text="Secretary End Date (yyyy-dd-mm): ").grid(row=9, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_fn = Entry(level)
    box_fn.grid(row=1,column=1)
    box_ln = Entry(level)
    box_ln.grid(row=2,column=1)
    box_mi = Entry(level)
    box_mi.grid(row=3, column=1)
    box_gender = Entry(level)
    box_gender.grid(row=4, column=1)
    box_salary = Entry(level)
    box_salary.grid(row=5, column=1)
    box_phonenum = Entry(level)
    box_phonenum.grid(row=6, column=1)
    box_ssn = Entry(level)
    box_ssn.grid(row=7, column=1)
    box_startdate = Entry(level)
    box_startdate.grid(row=8, column=1)
    box_enddate = Entry(level)
    box_enddate.grid(row=9, column=1)

    btn_add = Button(level, text="Add Secretary To Database", command=add_to_db)
    btn_add.grid(row=10, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=10, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Secretary ID#", command=delete)
    btn_delete.grid(row=10, column=3)
    btn_update = Button(level, text="Update Secretary Information (Please Fill In All Information)", command=update)
    btn_update.grid(row=10, column=0, sticky = "w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=11, column=0, sticky="w")
    searchResults = "Result"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=11, column=1, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=11, column=2)
#---------------------------------------CRUD Methods for Custodian Window----------------------------------------------
def custodian_crud(level):
    #Method and button to add Custodian to db

    def add_to_db():
        id = box_id.get()
        fn = box_fn.get()
        ln = box_ln.get()
        mi=box_mi.get()
        gender = box_gender.get()
        salary = box_salary.get()
        phoneNum = box_phonenum.get()
        ssn = box_ssn.get()
        startdate = box_startdate.get()
        enddate = box_enddate.get()

        values = id + ",\"" + fn + "\",\"" + ln + "\""+ ",\"" + mi + "\",\"" + gender + "\",\"" + salary + "\",\"" + phoneNum + "\",\"" + ssn + "\""+ ",\"" + startdate + "\",\"" + enddate + "\""
        sql_command = "INSERT INTO `custodian`(`c_id`, `c_firstName`, `c_lastName`, `c_middleIn`, `c_gender`, `c_salary`,`c_phoneNum`, `c_ssn`, `c_startDate`, `c_endDate`) VALUES ("
        sql_command = sql_command + values
        sql_command = sql_command + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for Custodian
    def clear_fields():
        box_id.delete(0,END)
        box_fn.delete(0,END)
        box_ln.delete(0,END)
        box_mi.delete(0,END)
        box_gender.delete(0,END)
        box_phonenum.delete(0,END)
        box_ssn.delete(0,END)
        box_startdate.delete(0,END)
        box_enddate.delete(0,END)
        box_salary.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `custodian` WHERE c_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        id = box_id.get()
        fn = box_fn.get()
        ln = box_ln.get()
        mi = box_mi.get()
        gender = box_gender.get()
        salary = box_salary.get()
        phoneNum = box_phonenum.get()
        ssn = box_ssn.get()
        startdate = box_startdate.get()
        enddate = box_enddate.get()
        sql_command = "UPDATE `custodian` SET `c_firstName`=\"" + fn + "\",`c_lastName`=\""+ ln + "\",`c_middleIn`=\""+ mi + "\",`c_gender`=\"" + gender + "\",`c_salary`=\"" + salary + "\",`c_phoneNum`=\""+ phoneNum + "\",`c_ssn`="+ ssn + ",`c_startDate`=\""+ startdate + "\",`c_endDate`=\""+ enddate + "\" WHERE c_id = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `c_firstName`, `c_lastName`, `c_middleIn`, `c_gender`,`c_salary`,`c_phoneNum`,`c_ssn`,`c_startDate`,`c_endDate`  FROM `custodian` WHERE c_id = " + id
        print(sql_command)
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=11, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Custodian Buttons/Boxes/Labels
    label_id= Label(level, text="Custodian ID Number: ").grid(row=0, column=0, sticky="w")
    label_fn = Label(level, text="Custodian First Name: ").grid(row=1, column=0, sticky="w")
    label_ln = Label(level, text="Custodian Last Name: ").grid(row=2, column=0, sticky="w")
    label_mi = Label(level, text="Custodian Middle Initial: ").grid(row=3, column=0, sticky="w")
    label_gender= Label(level, text="Custodian Gender: ").grid(row=4, column=0, sticky="w")
    label_salary = Label(level, text="Custodian Salary: ").grid(row=5, column=0, sticky="w")
    label_phonenum = Label(level, text="Custodian Phone Number: ").grid(row=6, column=0, sticky="w")
    label_patientssn = Label(level, text="Custodian Social Security Number(No Hyphens): ").grid(row=7, column=0, sticky="w")
    label_startdate= Label(level, text="Custodian Start Date (yyyy-dd-mm): ").grid(row=8, column=0, sticky="w")
    label_enddate = Label(level, text="Custodian End Date (yyyy-dd-mm): ").grid(row=9, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_fn = Entry(level)
    box_fn.grid(row=1,column=1)
    box_ln = Entry(level)
    box_ln.grid(row=2,column=1)
    box_mi = Entry(level)
    box_mi.grid(row=3, column=1)
    box_gender = Entry(level)
    box_gender.grid(row=4, column=1)
    box_salary = Entry(level)
    box_salary.grid(row=5, column=1)
    box_phonenum = Entry(level)
    box_phonenum.grid(row=6, column=1)
    box_ssn = Entry(level)
    box_ssn.grid(row=7, column=1)
    box_startdate = Entry(level)
    box_startdate.grid(row=8, column=1)
    box_enddate = Entry(level)
    box_enddate.grid(row=9, column=1)

    btn_add = Button(level, text="Add Custodian To Database", command=add_to_db)
    btn_add.grid(row=10, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=10, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Custodian ID#", command=delete)
    btn_delete.grid(row=10, column=3)
    btn_update = Button(level, text="Update Custodian Information (Please Fill In All Information)", command=update)
    btn_update.grid(row=10, column=0, sticky = "w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=11, column=0, sticky="w")
    searchResults = "Result"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=11, column=1, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=11, column=2)
#---------------------------------------CRUD Methods for Room Window----------------------------------------------
def room_crud(level):
    #Method and button to add Room to db

    def add_to_db():
        id = box_id.get()
        roomnum = box_roomnum.get()
        roomcapacity = box_roomcapacity.get()
        roomtype =box_roomtype.get()
        isVacant= box_vacant.get()
        vacant = "0"
        if isVacant == 'Y':
            vacant = "1"
        values = id + ",\"" + roomnum + "\",\"" + roomtype + "\""+ ",\"" + roomcapacity + "\",\"" + vacant + "\""""
        sql_command = "INSERT INTO `room`(`currentPatient_id`, `room_number`, `room_type`, `room_capacity`, `room_vacant`) VALUES ("
        sql_command = sql_command + values
        sql_command = sql_command + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for Room
    def clear_fields():
        box_id.delete(0,END)
        box_roomnum.delete(0,END)
        box_search.delete(0,END)
        box_roomcapacity.delete(0,END)
        box_roomtype.delete(0,END)
        box_vacant.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `room` WHERE currentPatient_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        id = box_id.get()
        roomnum = box_roomnum.get()
        roomcapacity = box_roomcapacity.get()
        roomtype = box_roomtype.get()
        isVacant = box_vacant.get()
        vacant = "0"
        sql_command = "UPDATE `room` SET `room_number`=\"" + roomnum + "\",`room_type`=\""+ roomtype + "\",`room_capacity`=\""+ roomcapacity + "\",`room_vacant`=\"" + vacant + "\" WHERE currentPatient_id = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `room_number`, `room_type`, `room_capacity`, `room_vacant`  FROM `room` WHERE currentPatient_id = " + id
        print(sql_command)
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=11, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Room Buttons/Boxes/Labels
    label_id= Label(level, text="Occupying Patient ID Number(Type 0 if Room Empty): ").grid(row=0, column=0, sticky="w")
    label_roomnum = Label(level, text="Room Number: ").grid(row=1, column=0, sticky="w")
    label_roomtype = Label(level, text="Room Type: ").grid(row=2, column=0, sticky="w")
    label_roomcapacity = Label(level, text="Room Capacity: ").grid(row=3, column=0, sticky="w")
    label_vacant= Label(level, text="Is the room vacant(Y/N): ").grid(row=4, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_roomnum = Entry(level)
    box_roomnum.grid(row=1,column=1)
    box_roomtype= Entry(level)
    box_roomtype.grid(row=2,column=1)
    box_roomcapacity = Entry(level)
    box_roomcapacity.grid(row=3, column=1)
    box_vacant = Entry(level)
    box_vacant.grid(row=4, column=1)

    btn_add = Button(level, text="Add Room To Database", command=add_to_db)
    btn_add.grid(row=5, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=5, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Room Number", command=delete)
    btn_delete.grid(row=5, column=3)
    btn_update = Button(level, text="Update Room Information (Please Fill In All Information)", command=update)
    btn_update.grid(row=5, column=0, sticky = "w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=6, column=0, sticky="w")
    searchResults = "Result"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=6, column=1, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=6, column=2)
#---------------------------------------CRUD Methods for Building Window----------------------------------------------
def building_crud(level):
    #Method and button to add Building to db

    def add_to_db():
        id = box_id.get()
        buildingname = box_buildingname.get()
        buildingcapacity = box_buildingcapacity.get()
        numberofrooms =box_numberofrooms.get()
        values = id + ",\"" + buildingname + "\",\"" + buildingcapacity + "\""+ ",\"" + numberofrooms + "\""""
        sql_command = "INSERT INTO `building`(`b_id`, `b_name`, `b_capacity`, `b_numRooms`) VALUES ("
        sql_command = sql_command + values
        sql_command = sql_command + ")"
        print(sql_command)
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for Building
    def clear_fields():
        box_id.delete(0,END)
        box_buildingcapacity.delete(0,END)
        box_numberofrooms.delete(0,END)
        box_search.delete(0,END)
        box_buildingname.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `building` WHERE b_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        #`b_id`, `b_name`, `b_capacity`, `b_numRooms`
        id = box_id.get()
        buildingname = box_buildingname.get()
        buildingcapacity = box_buildingcapacity.get()
        numberofrooms = box_numberofrooms.get()
        sql_command = "UPDATE `building` SET `b_name`=\"" + buildingname + "\",`b_capacity`=\""+ buildingcapacity + "\",`b_numRooms`=\""+ numberofrooms + "\" WHERE b_id = " + id
        print(sql_command)
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `b_name`, `b_capacity`, `b_numRooms` FROM `building` WHERE b_id = " + id
        print(sql_command)
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=5, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Building Buttons/Boxes/Labels
    label_id= Label(level, text="Building ID Number: ").grid(row=0, column=0, sticky="w")
    label_buildingname= Label(level, text="Building Name: ").grid(row=1, column=0, sticky="w")
    label_buildingcapacity = Label(level, text="Building Capacity: ").grid(row=2, column=0, sticky="w")
    label_numberofrooms = Label(level, text="Number of Rooms in Building: ").grid(row=3, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_buildingname = Entry(level)
    box_buildingname.grid(row=1,column=1)
    box_buildingcapacity= Entry(level)
    box_buildingcapacity.grid(row=2,column=1)
    box_numberofrooms = Entry(level)
    box_numberofrooms.grid(row=3, column=1)

    btn_add = Button(level, text="Add Building To Database", command=add_to_db)
    btn_add.grid(row=4, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=4, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Building ID#", command=delete)
    btn_delete.grid(row=4, column=3)
    btn_update = Button(level, text="Update Building Information (Please Fill In All Information)", command=update)
    btn_update.grid(row=4, column=0, sticky = "w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=5, column=0, sticky="w")
    searchResults = "Result"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=5, column=1, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=5, column=2)
#---------------------------------------CRUD Methods for Department Window----------------------------------------------
def dept_crud(level):
    #Method and button to add Department to db

    def add_to_db():
        id = box_id.get()
        deptname = box_deptname.get()
        deptnumemployees = box_deptnumeployees.get()
        deptmanagername =box_deptheadmanager.get()
        values = id + ",\"" + deptname + "\"," + deptnumemployees + ""+ ",\"" + deptmanagername + "\""""
        sql_command = "INSERT INTO `department`(`d_id`, `d_name`, `d_numEmployees`, `d_managerFullName`) VALUES ("
        sql_command = sql_command + values
        sql_command = sql_command + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for Department
    def clear_fields():
        box_id.delete(0,END)
        box_deptheadmanager.delete(0,END)
        box_deptnumeployees.delete(0,END)
        box_deptname.delete(0,END)
        box_search.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `department` WHERE d_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        #`d_id`, `d_name`, `d_numEmployees`, `d_managerFullName`
        id = box_id.get()
        deptname = box_deptname.get()
        deptnumemployees = box_deptnumeployees.get()
        deptmanagername = box_deptheadmanager.get()
        sql_command = "UPDATE `department` SET `d_name`=\"" + deptname + "\",`d_numEmployees`="+ deptnumemployees + ",`d_managerFullName`=\""+ deptmanagername + "\" WHERE d_id = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `d_name`, `d_numEmployees`, `d_managerFullName` FROM `department` WHERE d_id = " + id
        print(sql_command)
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=5, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Department Buttons/Boxes/Labels
    label_id= Label(level, text="DepartmentID Number: ").grid(row=0, column=0, sticky="w")
    label_deptname= Label(level, text="Department Name: ").grid(row=1, column=0, sticky="w")
    label_deptnumeployees = Label(level, text="Department Number of Employees: ").grid(row=2, column=0, sticky="w")
    label_deptheadmanager = Label(level, text="Department Head Manager Full Name: ").grid(row=3, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_deptname = Entry(level)
    box_deptname.grid(row=1,column=1)
    box_deptnumeployees= Entry(level)
    box_deptnumeployees.grid(row=2,column=1)
    box_deptheadmanager = Entry(level)
    box_deptheadmanager.grid(row=3, column=1)

    btn_add = Button(level, text="Add Department To Database", command=add_to_db)
    btn_add.grid(row=4, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=4, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Department ID#", command=delete)
    btn_delete.grid(row=4, column=3)
    btn_update = Button(level, text="Update Department Information (Please Fill In All Information)", command=update)
    btn_update.grid(row=4, column=0, sticky = "w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=5, column=0, sticky="w")
    searchResults = "Result"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=5, column=1, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=5, column=2)
#METHOD -----------------------Open Second Window Method---------------------------------------------
def open():
    level= Toplevel()
    level.title(clicked.get())
    level.geometry("1000x500")
    #If structure for window selection from dropdown
    if clicked.get() == "Appointment":
        appointment_crud(level)
    if clicked.get() == "Bill":
        bill_crud(level)
    if clicked.get() == "Medical Record":
        mr_crud(level)
    if clicked.get() == "Equipment":
        eq_crud(level)
    if clicked.get() == "Patient":
        patient_crud(level)
    if clicked.get() == "Doctor":
        doctor_crud(level)
    if clicked.get() == "Nurse":
        nurse_crud(level)
    if clicked.get() == "Secretary":
        secretary_crud(level)
    if clicked.get() == "Custodian":
        custodian_crud(level)
    if clicked.get() == "Room":
        room_crud(level)
    if clicked.get() == "Building":
        building_crud(level)
    if clicked.get() == "Department":
        dept_crud(level)
    #CLOSES WINDOW WHEN "Close Window Clicked"
    #tnClose = Button(top, text="Close Window", command=top.destroy)

#Button To Open Second Window With CRUD Options--------------------------------------------------
buttonConfirmTable = Button(root, text="Open CRUD", command=open).pack()

#Keeps Windows Running
mainloop()
#Closes Connection To DB
conn.close()