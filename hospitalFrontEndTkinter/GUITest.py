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
    db="test"
)
cursor = conn.cursor()

clicked = StringVar()
clicked.set("Appointment")
dropdownMenu = OptionMenu(root, clicked, "Appointment", "Bill", "Medical Record", "Equipment", "Patient", "Doctor",
                          "Nurse", "Secretary", "Custodian", "Room", "Building", "Department", "Perscription", "Distributor", "Employee")
dropdownMenu.pack()

#---------------------------------------CRUD Methods for Appointment Window----------------------------------------------
def appointment_crud(level):
    #Method and button to add appointment to db
    def add_to_db():
        #INSERT INTO `appointment`(`a_patientId`, `a_id`, `a_roomNum`, `a_startTime`, `a_date`, `a_doctor`) VALUES ([value-1],[value-2],[value-3],[value-4],[value-5],[value-6])
        docid = box_apptdocid.get()
        apptid = box_apptid.get()
        roomnum = box_roomnum.get()
        start = box_start.get()
        date = box_date.get()
        pid = box_apptpatientid.get()

        values = pid + "," + apptid + "," + roomnum + ",\"" + start + "\", \"" + date + "\"," + docid

        sql_command = "INSERT INTO `appointment`(`a_patientId`, `a_id`, `a_roomNum`, `a_startTime`, `a_date`, `a_doctor`) VALUES ("
        sql_command = sql_command+values + ")"
        print(sql_command)
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()


    #Method and Button to Clear Fields for Appointment
    def clear_fields():
        box_apptid.delete(0,END)
        box_start.delete(0,END)
        box_date.delete(0,END)
        box_search.delete(0,END)
        box_roomnum.delete(0, END)
        box_apptdocid.delete(0, END)
        box_apptpatientid.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_apptid.get()
        sql_command = "DELETE FROM `appointment` WHERE a_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        #UPDATE `appointment` SET `a_patientId`=[value-1],`a_id`=[value-2],`a_roomNum`=[value-3],`a_startTime`=[value-4],`a_date`=[value-5],`a_doctor`=[value-6] WHERE a_id =
        docid = box_apptdocid.get()
        apptid = box_apptid.get()
        roomnum = box_roomnum.get()
        start = box_start.get()
        date = box_date.get()
        pid = box_apptpatientid.get()

        sql_command = "UPDATE `appointment` SET `a_patientId`=" + apptid + ",`a_roomNum`=" + roomnum + ",`a_startTime`= \"" + start + "\",`a_date`= " + date + ",`a_doctor`=" + docid + " WHERE a_id =" + apptid
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()


    def search():
        id = box_search.get()
        sql_command = "SELECT `a_patientId`, `a_roomNum`, `a_startTime`, `a_date`, `a_doctor` FROM `appointment` WHERE a_id = " + id
        cursor.execute(sql_command)
        searchResults = cursor.fetchall()
        label_search = Label(level, text=searchResults)
        label_search.grid(row=7, column=3)
        conn.commit()
    #------------------------------------------Appointment Buttons/Boxes/Labels
    label_apptId = Label(level, text="Appointment ID Number: ").grid(row=0, column=0, sticky="w")
    label_apptStartTime = Label(level, text="Appointment Start Time: ").grid(row=1, column=0, sticky="w")
    label_apptdate = Label(level, text="Appointment Date (yyyy-mm-dd): ").grid(row=2, column=0, sticky="w")
    label_roomnum = Label(level, text="Appointment Room Number: ").grid(row=3, column=0, sticky="w")
    label_apptdocid = Label(level, text="Appointment Doctor ID Number: ").grid(row=4, column=0, sticky="w")
    label_apptpatientid = Label(level, text="Appointment Patient ID Number: ").grid(row=5, column=0, sticky="w")

    box_apptid = Entry(level)
    box_apptid.grid(row=0, column=1)
    box_start = Entry(level)
    box_start.grid(row=1, column=1)
    box_date = Entry(level)
    box_date.grid(row=2,column=1)
    box_roomnum = Entry(level)
    box_roomnum.grid(row=3, column=1)
    box_apptdocid = Entry(level)
    box_apptdocid.grid(row=4, column=1)
    box_apptpatientid = Entry(level)
    box_apptpatientid.grid(row=5, column=1)

    btn_add = Button(level, text="Add Appointment To Database", command=add_to_db)
    btn_add.grid(row=6, column=0)
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=6, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Appointment ID#)", command=delete)
    btn_delete.grid(row=6, column=3)
    btn_update = Button(level, text="Update Appointment(Enter all new and old info)", command=update)
    btn_update.grid(row=6, column=1)

    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row = 7, column = 0, sticky="w")

    searchResults = "{Patient Id# Room # Start_Time DateDoctor ID#}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=7, column=2, sticky="w")

    box_search = Entry(level)
    box_search.grid(row=7,column=1, sticky="w")
#---------------------------------------CRUD Methods for Bill Window----------------------------------------------
def bill_crud(level):
    #Method and button to add bill to db
    def add_to_db():
        billid = box_id.get()
        billamount = box_amount.get()
        patientid = box_patientid.get()
        issue = box_billIsuee.get()
        sql_command = "INSERT INTO `bill`(`bill_id`, `bill_amount`, `bill_patientId`, `bill_issue`) VALUES ("
        sql_command = sql_command + billid + "," + billamount + "," + patientid + "," + issue + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for Bill
    def clear_fields():
        box_id.delete(0, END)
        box_patientid.delete(0, END)
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
        billid = box_id.get()
        billamount = box_amount.get()
        patientid = box_patientid.get()
        issue = box_billIsuee.get()
        sql_command = "UPDATE `bill` SET `bill_amount`=" + billamount + ",`bill_patientId`=" + patientid + ",`bill_issue`=\"" + issue + "\" WHERE bill_id = " + billid
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()


    def search():
        id = box_search.get()
        sql_command = "SELECT `bill_amount`, `bill_patientId`, `bill_issue` FROM `bill` WHERE bill_id = " + id
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=6, column=3)
        conn.commit()
    #------------------------------------------Bill Buttons/Boxes/Labels
    label_billId = Label(level, text="Bill ID Number: ").grid(row=0, column=0, sticky="w")
    label_billAmount = Label(level, text="Bill Amount: ").grid(row=1, column=0, sticky="w")
    label_patientid = Label(level, text="Enter Patient ID").grid(row=2, column=0, sticky="w")
    label_billIssue = Label(level, text="Bill Issuee").grid(row=3, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_amount = Entry(level)
    box_amount.grid(row=1, column=1)
    box_patientid = Entry(level)
    box_patientid.grid(row=2, column=1)
    box_billIsuee = Entry(level)
    box_billIsuee.grid(row=3, column=1)
    btn_add = Button(level, text="Add Bill To Database", command=add_to_db)
    btn_add.grid(row=4, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=4, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Bill ID#) ", command=delete)
    btn_delete.grid(row=4, column=3)
    btn_update = Button(level, text="Update Bill", command=update)
    btn_update.grid(row=4, column=0, sticky = "w")

    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=6, column=0, sticky="w")

    searchResults = "{BillAmount$ PatientID# BillIssue}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=6, column=2, sticky="w")

    box_search = Entry(level)
    box_search.grid(row=6, column=1)
#---------------------------------------CRUD Methods for Medical_Record Window----------------------------------------------
def mr_crud(level):
    #Method and button to add medical record to db

    label_mrid = Label(level, text="Medical Record ID Number: ").grid(row=0, column=0, sticky="w")
    label_mrill = Label(level, text="Past Illnesses: ").grid(row=1, column=0, sticky="w")
    label_mrallergies = Label(level, text="Allergies: ").grid(row=2, column=0, sticky="w")
    label_mrbloodtype = Label(level, text="Blood Type").grid(row=3, column=0, sticky="w")
    label_mrpastappointment = Label(level, text="Past Appointment ID#").grid(row=4, column=0, sticky="w")
    label_mrpatientid = Label(level, text="Patient ID #").grid(row=5, column=0, sticky="w")

    def add_to_db():
        mrid = box_mrid.get()
        mrill = box_ill.get()
        mrallergies = box_allergies.get()
        mrbloodtype = box_bloodtype.get()
        mrpastapptnum = box_pastapptnumber.get()
        mrpatientid = box_mrpatientid.get()

        sql_command = "INSERT INTO `medicalrecord`(`mr_id`, `mr_patientId`, `mr_pastAppointment`, `mr_bloodType`, `mr_alLergies`, `mr_pastIllnesses`) VALUES ("
        sql_command = sql_command + mrid + ",\"" + mrill + "\",\"" + mrallergies + "\", \""  + mrbloodtype + "\", " + mrpastapptnum + ","  + mrpatientid + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for medical record
    def clear_fields():
        box_mrpatientid.delete(0,END)
        box_pastapptnumber.delete(0,END)
        box_bloodtype.delete(0,END)
        box_allergies.delete(0,END)
        box_ill.delete(0,END)
        box_search.delete(0,END)
        box_mrid.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = box_mrid.get()
        sql_command = "DELETE FROM `medicalrecord` WHERE mr_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        mrid = box_mrid.get()
        mrill = box_ill.get()
        mrallergies = box_allergies.get()
        mrbloodtype = box_bloodtype.get()
        mrpastapptnum = box_pastapptnumber.get()
        mrpatientid = box_mrpatientid.get()
        sql_command = "UPDATE `medicalrecord` SET `mr_patientId`=" + mrpatientid + ",`mr_pastAppointment`=" + mrpastapptnum + ",`mr_bloodType`=\"" + mrbloodtype + "\",`mr_alLergies`=\"" + mrallergies + "\",`mr_pastIllnesses`=\"" + mrill + " \" WHERE mr_id = " + mrid
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `mr_patientId`, `mr_pastAppointment`, `mr_bloodType`, `mr_alLergies`, `mr_pastIllnesses` FROM `medicalrecord` WHERE mr_id = " + id

        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=8, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Medical record Buttons/Boxes/Labels
    label_mrid= Label(level, text="Medical Record ID Number: ").grid(row=0, column=0, sticky="w")
    label_mrill = Label(level, text="Past Illnesses: ").grid(row=1, column=0, sticky="w")
    label_mrallergies = Label(level, text="Allergies: ").grid(row=2, column=0, sticky="w")
    label_mrbloodtype = Label(level, text="Blood Type").grid(row=3, column=0, sticky="w")
    label_mrpastappointment = Label(level, text="Past Appointment ID#").grid(row=4, column=0, sticky="w")
    label_mrpatientid = Label(level, text = "Patient ID #")    .grid(row=5, column=0, sticky="w")

    box_mrid = Entry(level)
    box_mrid.grid(row=0, column=1)
    box_ill= Entry(level)
    box_ill.grid(row=1, column=1)
    box_allergies = Entry(level)
    box_allergies.grid(row=2, column=1)
    box_bloodtype = Entry(level)
    box_bloodtype.grid(row=3,column=1)
    box_pastapptnumber = Entry(level)
    box_pastapptnumber.grid(row=4, column=1)
    box_mrpatientid = Entry(level)
    box_mrpatientid.grid(row=5,column=1)

    btn_add = Button(level, text="Add Medical Record To Database", command=add_to_db)
    btn_add.grid(row=7, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=7, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Medical Record ID#) ", command=delete)
    btn_delete.grid(row=7, column=3)
    btn_update = Button(level, text="Update Medical Record", command=update)
    btn_update.grid(row=7, column=0, sticky = "w")

    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=8, column=0, sticky="w")

    searchResults = "{PatientID# PastAppointmentID# BloodType Allegies {Past Illnesses}}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=8, column=2, sticky="w")

    box_search = Entry(level)
    box_search.grid(row=8, column=1)
#---------------------------------------CRUD Methods for Equipment Window----------------------------------------------
def eq_crud(level):
    #Method and button to add equipment to db
    def add_to_db():
        id = box_id.get()
        desc = box_desc.get()
        name = box_name.get()
        roomnum = box_roomnum.get()
        values = id + ",\"" + desc + "\",\"" + name + "\"," + roomnum
        sql_command = "INSERT INTO `equipment`(`eq_id`, `eq_desc`, `eq_name`, `eq_room`) VALUES ("
        sql_command = sql_command + values + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for equipment
    def clear_fields():
        box_name.delete(0,END)
        box_desc.delete(0,END)
        box_id.delete(0,END)
        box_search.delete(0,END)
        box_roomnum.delete(0,END)

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
        id = box_id.get()
        desc = box_desc.get()
        name = box_name.get()
        roomnum = box_roomnum.get()
        sql_command = "UPDATE `equipment` SET `eq_desc`=\"" + desc + "\",`eq_name`=\""+ name + "\", `eq_room`=" + roomnum + " WHERE eq_id = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `eq_desc`, `eq_name` FROM `equipment` WHERE eq_id = " + id
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=5, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Equipment Buttons/Boxes/Labels
    label_eqid= Label(level, text="Equipment ID Number: ").grid(row=0, column=0, sticky="w")
    label_eqdesc = Label(level, text="Equipment Description: ").grid(row=1, column=0, sticky="w")
    label_eqname = Label(level, text="Equipment Name: ").grid(row=2, column=0, sticky="w")
    label_eqroomnum = Label(level, text="Equipment Room Number").grid(row=3, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_desc= Entry(level)
    box_desc.grid(row=1, column=1)
    box_name = Entry(level)
    box_name.grid(row=2, column=1)
    box_roomnum = Entry(level)
    box_roomnum.grid(row=3,column=1)

    btn_add = Button(level, text="Add Equipment To Database", command=add_to_db)
    btn_add.grid(row=4, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=4, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Equipment ID#) ", command=delete)
    btn_delete.grid(row=4, column=3)
    btn_update = Button(level, text="Update Equipment", command=update)
    btn_update.grid(row=4, column=0, sticky = "w")

    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=5, column=0, sticky="w")

    searchResults = "{Description Name}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=5, column=2, sticky="w")

    box_search = Entry(level)
    box_search.grid(row=5, column=1)
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
        insurancenum = box_insurancenum.get()


        values = fn + "\",\"" + ln + "\""+ ",\"" + mi + "\",\"" + gender + "\"," + ssn + "," + insurancenum + "," + id + ",\"" + phoneNum +  "\""
        sql_command = "INSERT INTO `patient`(`p_firstName`, `p_lastName`, `p_middleIn`, `p_gender`, `p_ssn`, `p_insuranceNum`, `p_id`, `p_phoneNum`) VALUES (\""
        sql_command = sql_command + values + ")"
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
        box_insurancenum.delete(0,END)


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
        insurancenum = box_insurancenum.get()
        sql_command = "UPDATE `patient` SET `p_firstName`=\"" + fn + "\",`p_middleIn`=\"" + mi + "\",`p_lastName`=\"" + ln + "\",`p_gender`=\"" + gender +"\",`p_ssn`=" + ssn + ",`p_insuranceNum`=" + insurancenum + ", `p_phoneNum`=\"" + phoneNum + "\" WHERE `p_id` = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `p_firstName`, `p_middleIn`, `p_lastName`, `p_gender`, `p_ssn`, `p_insuranceNum`, `p_phoneNum` FROM `patient` WHERE `p_id` = " + id
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=9, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Patient Buttons/Boxes/Labels
    label_id= Label(level, text="Patient ID Number: ").grid(row=0, column=0, sticky="w")
    label_fn = Label(level, text="Patient First Name: ").grid(row=1, column=0, sticky="w")
    label_ln = Label(level, text="Patient Last Name: ").grid(row=2, column=0, sticky="w")
    label_mi = Label(level, text="Patient Middle Initial: ").grid(row=3, column=0, sticky="w")
    label_gender= Label(level, text="Patient Gender: ").grid(row=4, column=0, sticky="w")
    label_phonenum = Label(level, text="Patient Phone Number: ").grid(row=5, column=0, sticky="w")
    label_patientssn = Label(level, text="Patient Social Security Number(No Hyphens): ").grid(row=6, column=0, sticky="w")
    label_insurancenum= Label(level, text="Patient Insurance Number: ").grid(row=7, column=0, sticky="w")

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
    box_insurancenum = Entry(level)
    box_insurancenum.grid(row=7, column=1)

    btn_add = Button(level, text="Add Patient To Database", command=add_to_db)
    btn_add.grid(row=8, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=8, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Patient ID#) ", command=delete)
    btn_delete.grid(row=8, column=3)
    btn_update = Button(level, text="Update Patient Information (Please Fill In All Information)", command=update)
    btn_update.grid(row=8, column=0, sticky = "w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=9, column=0, sticky="w")
    searchResults = "{FirstName MiddleIn LastName Gender SSN InsuranceID# PhoneNumber}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=9, column=2, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=9, column=1)
#---------------------------------------CRUD Methods for Doctor Window----------------------------------------------
def doctor_crud(level):
    #Method and button to add doctor to db

    def add_to_db():
        id = box_id.get()
        title = box_title.get()
        salary = box_salary.get()
        ssn = box_ssn.get()
        deptnumber = box_deptidnumber.get()

        values = "\"" + title + "\"," + ssn + "," + id + "," + salary + "," + deptnumber
        sql_command = "INSERT INTO `doctor`(`doc_title`, `doc_ssn`, `doc_id`, `doc_salary`, `doc_departmentId`) VALUES ("
        sql_command = sql_command  + values + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for doctor
    def clear_fields():
        box_id.delete(0,END)
        box_title.delete(0,END)
        box_ssn.delete(0,END)
        box_salary.delete(0,END)
        box_deptidnumber.delete(0,END)

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
        title = box_title.get()
        salary = box_salary.get()
        ssn = box_ssn.get()
        deptnumber = box_deptidnumber.get()

        sql_command = "UPDATE `doctor` SET `doc_title`=\"" + title + "\",`doc_ssn`=" + ssn + ",`doc_salary`=" + salary + ",`doc_departmentId`=" + deptnumber + " WHERE `doc_id` = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `doc_title`, `doc_ssn`, `doc_salary`, `doc_departmentId` FROM `doctor` WHERE `doc_id` = "+ id
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=6, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Doctor Buttons/Boxes/Labels
    label_id= Label(level, text="Doctor ID Number: ").grid(row=0, column=0, sticky="w")
    label_title = Label(level, text="Doctor Title: ").grid(row=1, column=0, sticky="w")
    label_salary = Label(level, text="Doctor Salary: ").grid(row=2, column=0, sticky="w")
    label_docssn = Label(level, text="Doctor Social Security Number(No Hyphens): ").grid(row=3, column=0, sticky="w")
    label_deptidnumber= Label(level, text="Doctor Department ID#: ").grid(row=4, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_title = Entry(level)
    box_title.grid(row=1,column=1)
    box_salary = Entry(level)
    box_salary.grid(row=2, column=1)
    box_ssn = Entry(level)
    box_ssn.grid(row=3, column=1)
    box_deptidnumber = Entry(level)
    box_deptidnumber.grid(row =4,column=1)

    btn_add = Button(level, text="Add Doctor To Database", command=add_to_db)
    btn_add.grid(row=5, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=5, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Doctor ID#) ", command=delete)
    btn_delete.grid(row=5, column=3)
    btn_update = Button(level, text="Update Doctor Information (Please Fill In All Information)", command=update)
    btn_update.grid(row=5, column=0, sticky = "w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=6, column=0, sticky="w")
    searchResults = "{DoctorTitle DoctorSSN DoctorSalary DoctorDepartmentID#}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=6, column=2, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=6, column=1)
#---------------------------------------CRUD Methods for Nurse Window----------------------------------------------
def nurse_crud(level):
    #Method and button to add Nurse to db

    def add_to_db():
        id = box_id.get()
        salary = box_salary.get()
        title = box_title.get()
        ssn = box_ssn.get()
        deptidnum = box_deptidnum.get()
        worksroom = box_worksroom.get()

        values = id + "," + ssn + ",\"" + title + "\"," + worksroom + "," + salary + "," + deptidnum
        sql_command = "INSERT INTO `nurse`(`nurse_id`, `nurse_ssn`, `nurse_title`, `nurse_worksRoom`, `nurse_salary`, `nurse_departmentId`) VALUES ("
        sql_command = sql_command + values + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for nurse
    def clear_fields():
        box_id.delete(0,END)
        box_title.delete(0,END)
        box_ssn.delete(0,END)
        box_salary.delete(0,END)
        box_deptidnum.delete(0,END)
        box_worksroom.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `nurse` WHERE nurse_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        id = box_id.get()
        salary = box_salary.get()
        title = box_title.get()
        ssn = box_ssn.get()
        deptidnum = box_deptidnum.get()
        worksroom = box_worksroom.get()
        sql_command = "UPDATE `nurse` SET `nurse_ssn`=" + ssn + ",`nurse_title`=\"" +title + "\",`nurse_worksRoom`=" + worksroom + ",`nurse_salary`=" + salary +",`nurse_departmentId`=" + deptidnum + " WHERE `nurse_id` = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `nurse_ssn`, `nurse_title`, `nurse_worksRoom`, `nurse_salary`, `nurse_departmentId` FROM `nurse` WHERE `nurse_id` = " + id
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=7, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Nurse Buttons/Boxes/Labels
    label_id= Label(level, text="Nurse ID Number: ").grid(row=0, column=0, sticky="w")
    label_title = Label(level, text="Nurse Title: ").grid(row=1, column=0, sticky="w")
    label_salary = Label(level, text="Nurse Salary: ").grid(row=2, column=0, sticky="w")
    label_ssn = Label(level, text="Nurse SSN").grid(row=3,column=0,sticky="w")
    label_worksroom = Label(level, text="Work Room ID#: ").grid(row=4, column=0, sticky="w")
    label_deptidnum = Label(level, text="Department ID#: ").grid(row=5, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_title = Entry(level)
    box_title.grid(row=1,column=1)
    box_salary = Entry(level)
    box_salary.grid(row=2, column=1)
    box_ssn = Entry(level)
    box_ssn.grid(row=3, column=1)
    box_worksroom = Entry(level)
    box_worksroom.grid(row=4, column=1)
    box_deptidnum = Entry(level)
    box_deptidnum.grid(row=5, column=1)

    btn_add = Button(level, text="Add Nurse To Database", command=add_to_db)
    btn_add.grid(row=6, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=6, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Nurse ID#) ", command=delete)
    btn_delete.grid(row=6, column=3)
    btn_update = Button(level, text="Update Nurse Information (Please Fill In All Information)", command=update)
    btn_update.grid(row=6, column=0, sticky = "w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=7, column=0, sticky="w")
    searchResults = "{SSN Title WorksRoomID# Salary DeptID#}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=7, column=2, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=7, column=1)
#---------------------------------------CRUD Methods for Secretary Window----------------------------------------------
def secretary_crud(level):
    #Method and button to add secretary to db

    def add_to_db():
        id = box_id.get()
        salary = box_salary.get()
        title = box_title.get()
        ssn = box_ssn.get()
        deptidnum = box_deptidnum.get()
        worksroom = box_worksroom.get()

        values = "\"" + title + "\"," + ssn + "," + id + "," + worksroom + "," + salary + "," + deptidnum
        sql_command = "INSERT INTO `secretary`(`s_title` , `s_ssn`, `s_id`, `s_worksRoom`, `s_salary`, `s_departmentId`) VALUES ("
        sql_command = sql_command + values + ")"
        print(sql_command)
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for secretary
    def clear_fields():
        box_id.delete(0, END)
        box_title.delete(0, END)
        box_ssn.delete(0, END)
        box_salary.delete(0, END)
        box_deptidnum.delete(0, END)
        box_worksroom.delete(0, END)

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
        salary = box_salary.get()
        title = box_title.get()
        ssn = box_ssn.get()
        deptidnum = box_deptidnum.get()
        worksroom = box_worksroom.get()
        sql_command = "UPDATE `secretary` SET `s_title`=\"" + title + "\",`s_ssn`=" + ssn + ",`s_worksRoom`=" + worksroom + ",`s_salary`=" + salary + ",`s_departmentId`=" + deptidnum + " WHERE `s_id` = " + id
        print(sql_command)
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `s_title`, `s_ssn`, `s_worksRoom`, `s_salary`, `s_departmentId` FROM `secretary` WHERE `s_id`=" + id
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=7, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Secretary Buttons/Boxes/Labels
    label_id = Label(level, text="Secretary ID Number: ").grid(row=0, column=0, sticky="w")
    label_title = Label(level, text="Secretary Title: ").grid(row=1, column=0, sticky="w")
    label_salary = Label(level, text="Secretary Salary: ").grid(row=2, column=0, sticky="w")
    label_ssn = Label(level, text="Secretary SSN").grid(row=3, column=0, sticky="w")
    label_worksroom = Label(level, text="Work Room ID#: ").grid(row=4, column=0, sticky="w")
    label_deptidnum = Label(level, text="Department ID#: ").grid(row=5, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_title = Entry(level)
    box_title.grid(row=1, column=1)
    box_salary = Entry(level)
    box_salary.grid(row=2, column=1)
    box_ssn = Entry(level)
    box_ssn.grid(row=3, column=1)
    box_worksroom = Entry(level)
    box_worksroom.grid(row=4, column=1)
    box_deptidnum = Entry(level)
    box_deptidnum.grid(row=5, column=1)

    btn_add = Button(level, text="Add Secretary To Database", command=add_to_db)
    btn_add.grid(row=6, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=6, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Secretary ID#) ", command=delete)
    btn_delete.grid(row=6, column=3)
    btn_update = Button(level, text="Update Secretary Information (Please Fill In All Information)", command=update)
    btn_update.grid(row=6, column=0, sticky="w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=7, column=0, sticky="w")
    searchResults = "{Title SSN WorksRoomID# Salary DeptID#}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=7, column=2, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=7, column=1)
#---------------------------------------CRUD Methods for Custodian Window----------------------------------------------
def custodian_crud(level):
    #Method and button to add Custodian to db

    def add_to_db():
        id = box_id.get()
        salary = box_salary.get()
        title = box_title.get()
        ssn = box_ssn.get()
        deptidnum = box_deptidnum.get()

        values = "\"" + title + "\"," + ssn + "," + id + "," + salary + "," + deptidnum
        sql_command = "INSERT INTO `custodian`(`c_title` , `c_ssn`, `c_id`, `c_salary`, `c_departmentId`) VALUES ("
        sql_command = sql_command + values + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    # Method and Button to Clear Fields for secretary
    def clear_fields():
        box_id.delete(0, END)
        box_title.delete(0, END)
        box_ssn.delete(0, END)
        box_salary.delete(0, END)
        box_deptidnum.delete(0, END)

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
        salary = box_salary.get()
        title = box_title.get()
        ssn = box_ssn.get()
        deptidnum = box_deptidnum.get()
        sql_command = "UPDATE `custodian` SET `c_title`=\"" + title + "\",`c_ssn`=" + ssn + ",`c_salary`=" + salary + ",`c_departmentId`=" + deptidnum + " WHERE `c_id` = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `c_title`, `c_ssn`, `c_salary`, `c_departmentId` FROM `custodian` WHERE `c_id`=" + id
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=6, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Custodian Buttons/Boxes/Labels
    label_id = Label(level, text="Custodian ID Number: ").grid(row=0, column=0, sticky="w")
    label_title = Label(level, text="Custodian Title: ").grid(row=1, column=0, sticky="w")
    label_salary = Label(level, text="Custodian Salary: ").grid(row=2, column=0, sticky="w")
    label_ssn = Label(level, text="Custodian SSN").grid(row=3, column=0, sticky="w")
    label_deptidnum = Label(level, text="Department ID#: ").grid(row=4, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_title = Entry(level)
    box_title.grid(row=1, column=1)
    box_salary = Entry(level)
    box_salary.grid(row=2, column=1)
    box_ssn = Entry(level)
    box_ssn.grid(row=3, column=1)
    box_deptidnum = Entry(level)
    box_deptidnum.grid(row=4, column=1)

    btn_add = Button(level, text="Add Custodian To Database", command=add_to_db)
    btn_add.grid(row=5, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=5, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Custodian ID#) ", command=delete)
    btn_delete.grid(row=5, column=3)
    btn_update = Button(level, text="Update Custodian Information (Please Fill In All Information)", command=update)
    btn_update.grid(row=5, column=0, sticky="w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=6, column=0, sticky="w")
    searchResults = "{Title SSN WorksRoomID# Salary DeptID#}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=6, column=2, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=6, column=1)
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
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=6, column=3, sticky="w")
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
    btn_search_by_id = Button(level, text="Search by Occupying Patient ID#", command=search)
    btn_search_by_id.grid(row=6, column=0, sticky="w")
    searchResults = "{RoomNumber RoomType Capacity IsVacant}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=6, column=2, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=6, column=1)
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
    searchResults = "{BuildingName Capacity NumberOfRooms}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=5, column=2, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=5, column=1)
#---------------------------------------CRUD Methods for Department Window----------------------------------------------
def dept_crud(level):
    #Method and button to add Department to db

    def add_to_db():
        id = box_id.get()
        deptname = box_deptname.get()
        deptbuildingid = box_buildingid.get()
        managerid = box_managerid.get()
        values = "\"" + deptname + "\", " +  id + "," + deptbuildingid + "," + managerid
        sql_command = "INSERT INTO `department`(`d_name`, `d_id`, `d_buildingId`, `d_managerId`) VALUES ("
        sql_command = sql_command + values + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for Department
    def clear_fields():
        box_id.delete(0,END)
        box_buildingid.delete(0,END)
        box_managerid.delete(0,END)
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
        id = box_id.get()
        deptname = box_deptname.get()
        deptbuildingid = box_buildingid.get()
        managerid = box_managerid.get()
        sql_command = "UPDATE `department` SET `d_name`=\"" + deptname + "\",`d_buildingId`=" + deptbuildingid + ",`d_managerId`=" + managerid +" WHERE `d_id`=" + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `d_name`, `d_buildingId`, `d_managerId` FROM `department` WHERE `d_id`=" + id
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=5, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Department Buttons/Boxes/Labels
    label_id= Label(level, text="DepartmentID Number: ").grid(row=0, column=0, sticky="w")
    label_deptname= Label(level, text="Department Name: ").grid(row=1, column=0, sticky="w")
    label_buildingid = Label(level, text="Department Building ID#: ").grid(row=2, column=0, sticky="w")
    label_managerid = Label(level, text="Department Manager ID#: ").grid(row=3, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_deptname = Entry(level)
    box_deptname.grid(row=1,column=1)
    box_buildingid= Entry(level)
    box_buildingid.grid(row=2,column=1)
    box_managerid  = Entry(level)
    box_managerid .grid(row=3, column=1)

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
    searchResults = "{Name BuildingID ManagerID}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=5, column=2, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=5, column=1)
#---------------------------------------CRUD Methods for Perscription Window----------------------------------------------
def perscription_crud(level):
    #Method and button to add Perscription to db

    def add_to_db():
        id = box_id.get()
        medicinename = box_medicinename.get()
        distributorid = box_distributorid.get()
        forpatient = box_forpatient.get()
        persribedby = box_prescribedby.get()

        values = id + ",\"" + medicinename + "\"," + distributorid + "," + forpatient + "," + persribedby + ")"
        sql_command = "INSERT INTO `perscription`(`persc_id`, `persc_medicineName`, `persc_distributorId`, `persc_forPatient`, `persc_perscribedBy`) VALUES ("
        sql_command = sql_command + values
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for Perscription
    def clear_fields():
        box_id.delete(0,END)
        box_prescribedby.delete(0,END)
        box_forpatient.delete(0,END)
        box_distributorid.delete(0,END)
        box_search.delete(0,END)
        box_prescribedby.delete(0,END)
        box_medicinename.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `perscription` WHERE persc_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        id = box_id.get()
        medicinename = box_medicinename.get()
        distributorid = box_distributorid.get()
        forpatient = box_forpatient.get()
        persribedby = box_prescribedby.get()
        sql_command = "UPDATE `perscription` SET `persc_medicineName`=\"" + medicinename + "\",`persc_distributorId`=" + distributorid + ",`persc_forPatient`=" + forpatient + ",`persc_perscribedBy`=" + persribedby + " WHERE `persc_id`=" + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `persc_medicineName`, `persc_distributorId`, `persc_forPatient`, `persc_perscribedBy` FROM `perscription` WHERE `persc_id` =" + id
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=6, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Perscription Buttons/Boxes/Labels
    label_id= Label(level, text="Perscription ID Number: ").grid(row=0, column=0, sticky="w")
    label_medicinename =  Label(level, text="Medication Name: ").grid(row=1, column=0, sticky="w")
    label_distributorid = Label(level, text="Distributor ID#: ").grid(row=2, column=0, sticky="w")
    label_forpatient= Label(level, text="For Patient (ID#): ").grid(row=3, column=0, sticky="w")
    label_prescribedby= Label(level, text="Prescribed By (Doc ID#): ").grid(row=4, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_medicinename = Entry(level)
    box_medicinename.grid(row=1,column=1)
    box_distributorid = Entry(level)
    box_distributorid.grid(row=2, column=1)
    box_forpatient= Entry(level)
    box_forpatient.grid(row=3,column=1)
    box_prescribedby  = Entry(level)
    box_prescribedby.grid(row=4, column=1)

    btn_add = Button(level, text="Add Perscription To Database", command=add_to_db)
    btn_add.grid(row=5, column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=5, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Perscription ID#", command=delete)
    btn_delete.grid(row=5, column=3)
    btn_update = Button(level, text="Update Perscription Information", command=update)
    btn_update.grid(row=5, column=0, sticky = "w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=6, column=0, sticky="w")
    searchResults = "{MedicineName DistributorID# PatientID# DoctorID#}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=6, column=2, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=6, column=1)
#---------------------------------------CRUD Methods for Distributor Window----------------------------------------------
def distributor_crud(level):
    #Method and button to add Distributor to db

    def add_to_db():
        id = box_id.get()
        distdept = box_distdept.get()
        distname = box_distname.get()
        distproduct = box_distproduct.get()

        values = "\"" + distname + "\",\"" + distproduct + "\"," + id + "," + distdept
        sql_command = "INSERT INTO `distributor`(`dist_name`, `dist_product`, `dist_id`, `dist_department`) VALUES ("
        sql_command = sql_command + values + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for Distributor
    def clear_fields():
        box_id.delete(0,END)
        box_search.delete(0,END)
        box_distdept.delete(0,END)
        box_distname.delete(0,END)
        box_distproduct.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `distributor` WHERE dist_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        id = box_id.get()
        distdept = box_distdept.get()
        distname = box_distname.get()
        distproduct = box_distproduct.get()

        sql_command = "UPDATE `distributor` SET `dist_name`=\"" + distname + "\",`dist_product`=\"" + distproduct + "\",`dist_department`=" + distdept + " WHERE `dist_id` = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `dist_name`, `dist_product`, `dist_department` FROM `distributor` WHERE `dist_id` = " + id
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=5, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Distributor Buttons/Boxes/Labels
    label_id= Label(level, text="Distributor ID#: ").grid(row=0, column=0, sticky="w")
    label_distname =  Label(level, text="Distributor  Name: ").grid(row=1, column=0, sticky="w")
    label_distproduct = Label(level, text="Distributor Product: ").grid(row=2, column=0, sticky="w")
    label_distdept= Label(level, text="Distributor Department ID#: ").grid(row=3, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_distname = Entry(level)
    box_distname.grid(row=1,column=1)
    box_distproduct = Entry(level)
    box_distproduct.grid(row=2, column=1)
    box_distdept= Entry(level)
    box_distdept.grid(row=3,column=1)

    btn_add = Button(level, text="Add Distributor To Database", command=add_to_db)
    btn_add.grid(row=4,column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=4, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Distributor ID#", command=delete)
    btn_delete.grid(row=4, column=3)
    btn_update = Button(level, text="Update Distributor Information", command=update)
    btn_update.grid(row=4, column=0, sticky = "w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=5, column=0, sticky="w")
    searchResults = "{Name Product Department}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=5, column=2, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=5, column=1)

#---------------------------------------CRUD Methods for Employee Window----------------------------------------------
def employee_crud(level):
    #Method and button to add Employee to db

    def add_to_db():
        id = box_id.get()
        ssn = box_ssn.get()
        firstname = box_firstname.get()
        middlein = box_middlein.get()
        lastname = box_lastname.get()
        gender = box_gender.get()
        datehired = box_datehired.get()
        phonenumber = box_phonenumber.get()

        values = id + "," + ssn + ",\"" + firstname + "\",\"" + middlein + "\",\"" + lastname + "\",\"" + datehired + "\",\"" + gender + "\",\"" + phonenumber + "\""
        sql_command = "INSERT INTO `employee`(`employee_id`, `employee_ssn`, `employee_firstName`, `employee_middleIn`, `employee_lastName`, `employee_hired`, `employee_gender`, `employee_phone`) VALUES ("
        sql_command = sql_command + values + ")"
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    #Method and Button to Clear Fields for Employee
    def clear_fields():
        box_id.delete(0,END)
        box_search.delete(0,END)
        box_ssn.delete(0,END)
        box_firstname.delete(0,END)
        box_middlein.delete(0,END)
        box_lastname.delete(0,END)
        box_gender.delete(0,END)
        box_datehired.delete(0,END)
        box_phonenumber.delete(0,END)

    #Method and Button to Delete ID From DB
    def delete():
        id = ""
        id = id + box_id.get()
        sql_command = "DELETE FROM `employee` WHERE employee_id = "
        sql_command = sql_command + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()

    def update():
        id = box_id.get()
        ssn = box_ssn.get()
        firstname = box_firstname.get()
        middlein = box_middlein.get()
        lastname = box_lastname.get()
        gender = box_gender.get()
        datehired = box_datehired.get()
        phonenumber = box_phonenumber.get()

        sql_command = "UPDATE `employee` SET `employee_ssn`=" + ssn + ",`employee_firstName`=\"" + firstname + "\",`employee_middleIn`=\"" + middlein + "\",`employee_lastName`=\""+lastname + "\",`employee_hired`=\"" + datehired + "\",`employee_gender`=\"" + gender + "\",`employee_phone`=\"" + phonenumber + "\" WHERE `employee_id` = " + id
        cursor.execute(sql_command)
        conn.commit()
        clear_fields()
    def search():
        id = box_search.get()
        sql_command = "SELECT `employee_ssn`, `employee_firstName`, `employee_middleIn`, `employee_lastName`, `employee_hired`, `employee_gender`, `employee_phone` FROM `employee` WHERE `employee_id` = " + id
        cursor.execute(sql_command)
        searchResults = (cursor.fetchall())
        label_search = Label(level, text=searchResults)
        label_search.grid(row=9, column=3, sticky="w")
        conn.commit()
    #------------------------------------------Employee Buttons/Boxes/Labels
    label_id= Label(level, text="Employee ID#: ").grid(row=0, column=0, sticky="w")
    label_ssn =  Label(level, text="Employee SSN: ").grid(row=1, column=0, sticky="w")
    label_firstname = Label(level, text="Employee First Name: ").grid(row=2, column=0, sticky="w")
    label_middlein = Label(level, text="Employee Middle Initial: ").grid(row=3, column=0, sticky="w")
    label_lastname= Label(level, text="Employee Last Name: ").grid(row=4, column=0, sticky="w")
    label_datehired = Label(level, text="Employee Date Hired (yyyy-mm-dd): ").grid(row=5, column=0, sticky="w")
    label_gender = Label(level, text="Employee Gender: ").grid(row=6, column=0, sticky="w")
    label_phonenumber = Label(level, text="Employee Phone Number: ").grid(row=7, column=0, sticky="w")

    box_id = Entry(level)
    box_id.grid(row=0, column=1)
    box_ssn = Entry(level)
    box_ssn.grid(row=1,column=1)
    box_firstname = Entry(level)
    box_firstname.grid(row=2, column=1)
    box_middlein= Entry(level)
    box_middlein.grid(row=3,column=1)
    box_lastname = Entry(level)
    box_lastname.grid(row=4, column=1)
    box_datehired = Entry(level)
    box_datehired.grid(row=5, column=1)
    box_gender = Entry(level)
    box_gender.grid(row=6, column=1)
    box_phonenumber = Entry(level)
    box_phonenumber.grid(row=7, column=1)

    btn_add = Button(level, text="Add Employee To Database", command=add_to_db)
    btn_add.grid(row=8,column=1, sticky="w")
    btn_clear_fields = Button(level, text="Clear Fields", command=clear_fields)
    btn_clear_fields.grid(row=8, column=2)
    btn_delete = Button(level, text="Delete From DB (Only Enter Employee ID#", command=delete)
    btn_delete.grid(row=8, column=3)
    btn_update = Button(level, text="Update Employee Information", command=update)
    btn_update.grid(row=8, column=0, sticky = "w")
    btn_search_by_id = Button(level, text="Search by ID#", command=search)
    btn_search_by_id.grid(row=9, column=0, sticky="w")
    searchResults = "{SSN FirstName MiddleInitial LastName DateHired Gender PhoneNumber}  ->"
    label_search = Label(level, text=searchResults)
    label_search.grid(row=9, column=2, sticky="w")
    box_search = Entry(level)
    box_search.grid(row=9, column=1)

#METHOD -----------------------Open Window Method---------------------------------------------
def open():
    level= Toplevel()
    level.title(clicked.get())
    level.geometry("1000x500")
    #If structure for window selection from dropdown
    if clicked.get() == "Appointment":
        level.geometry("1000x200")
        appointment_crud(level)
    if clicked.get() == "Bill":
        level.geometry("700x150")
        bill_crud(level)
    if clicked.get() == "Medical Record":
        level.geometry("1000x200")
        mr_crud(level)
    if clicked.get() == "Equipment":
        level.geometry("700x150")
        eq_crud(level)
    if clicked.get() == "Patient":
        level.geometry("1150x250")
        patient_crud(level)
    if clicked.get() == "Doctor":
        level.geometry("1100x250")
        doctor_crud(level)
    if clicked.get() == "Nurse":
        level.geometry("950x200")
        nurse_crud(level)
    if clicked.get() == "Secretary":
        level.geometry("950x200")
        secretary_crud(level)
    if clicked.get() == "Custodian":
        level.geometry("1000x200")
        custodian_crud(level)
    if clicked.get() == "Room":
        level.geometry("1000x175")
        room_crud(level)
    if clicked.get() == "Building":
        level.geometry("1000x175")
        building_crud(level)
    if clicked.get() == "Department":
        level.geometry("1000x175")
        dept_crud(level)
    if clicked.get() == "Perscription":
        level.geometry("900x200")
        perscription_crud(level)
    if clicked.get() == "Distributor":
        level.geometry("900x200")
        distributor_crud(level)
    if clicked.get() == "Employee":
        level.geometry("1100x250")
        employee_crud(level)
    #CLOSES WINDOW WHEN "Close Window Clicked"
    #tnClose = Button(top, text="Close Window", command=top.destroy)

#Button To Open Second Window With CRUD Options--------------------------------------------------
buttonConfirmTable = Button(root, text="Open CRUD", command=open).pack()

#Keeps Windows Running
mainloop()
#Closes Connection To DB
conn.close()