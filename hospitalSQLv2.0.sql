

SET FOREIGN_KEY_CHECKS=0;

CREATE TABLE IF NOT EXISTS Patient
(
p_firstName	VARCHAR(15)	NOT NULL,
p_middleIn	CHAR(1),
p_lastName	VARCHAR(15)	NOT NULL,
p_gender	CHAR(1)		NOT NULL,
p_ssn	INT(9)	NOT NULL,
p_insuranceNum	INT(11)	NOT NULL,
p_id	INT(11)	NOT NULL,
p_phoneNum	VARCHAR(15) NOT NULL,
PRIMARY KEY(p_id)
);

CREATE TABLE IF NOT EXISTS Room
(
currentPatient_id	INT(11),
room_number SMALLINT(6) NOT NULL,
room_type VARCHAR(30) NOT NULL,
room_capacity VARCHAR(20) NOT NULL,
room_vacant CHAR(1)	NOT NULL,
PRIMARY KEY(room_number),
FOREIGN KEY(currentPatient_id) REFERENCES Patient(p_id)
);

CREATE TABLE IF NOT EXISTS Building
(
b_id INT(11) NOT NULL,
b_name VARCHAR(15) NOT NULL,
b_capacity SMALLINT(6) NOT NULL,
b_numRooms SMALLINT(6) NOT NULL,
PRIMARY KEY(b_id)
);

CREATE TABLE IF NOT EXISTS Department
(
d_name	VARCHAR(15)	NOT NULL,
d_id	INT(11)	NOT NULL,
d_buildingId	INT(11)	NOT NULL,
d_managerId	INT(11)	NOT NULL,
PRIMARY KEY(d_id),
FOREIGN KEY(d_buildingId) REFERENCES Building(b_id),
FOREIGN KEY(d_managerId) REFERENCES Employee(employee_id)
);

CREATE TABLE IF NOT EXISTS Employee
(
employee_id	INT(11)	NOT NULL,
employee_ssn	INT(9)	NOT NULL,
employee_firstName	VARCHAR(15)	NOT NULL,
employee_middleIn	CHAR(1)	NOT NULL,
employee_lastName	VARCHAR(15)	NOT NULL,
employee_hired	DATE	NOT	NULL,
employee_gender	CHAR(1)	NOT NULL,
employee_phone	VARCHAR(15)	NOT NULL,
PRIMARY KEY(employee_id)
);

CREATE TABLE IF NOT EXISTS Nurse
(
nurse_id	INT(11)	NOT NULL,
nurse_title	VARCHAR(5) DEFAULT"Nurse",
nurse_worksRoom	SMALLINT(6) NOT NULL,
nurse_salary	INT(10)	NOT NULL,
nurse_departmentId	INT(11)	NOT NULL,
PRIMARY KEY(nurse_id,nurse_worksRoom),
FOREIGN KEY(nurse_id) REFERENCES Employee(employee_id),
FOREIGN KEY(nurse_departmentId) REFERENCES Department(d_id)
);

CREATE TABLE IF NOT EXISTS Doctor
(
doc_title	VARCHAR(6) DEFAULT"Doctor",
doc_id	INT(11)	NOT NULL,
doc_salary	INT(11)	NOT NULL,
doc_departmentId	INT(11)	NOT NULL,
PRIMARY KEY(doc_id),
FOREIGN KEY(doc_id) REFERENCES Employee(employee_id),
FOREIGN KEY(doc_departmentId) REFERENCES Department(d_id)
);

CREATE TABLE IF NOT EXISTS Secretary
(
s_title	VARCHAR(9) DEFAULT"Secretary",
s_id	INT(11)	NOT NULL,
s_worksRoom	SMALLINT(6)	NOT NULL,
s_salary	INT(11)	NOT NULL,
s_departmentId	INT(11)	NOT NULL,
PRIMARY KEY(s_id),
FOREIGN KEY(s_worksRoom) REFERENCES Room(room_number),
FOREIGN KEY(s_id) REFERENCES Employee(employee_id),
FOREIGN KEY(s_departmentId) REFERENCES Department(d_id)
);

CREATE TABLE IF NOT EXISTS Custodian
(
c_title	VARCHAR(9) DEFAULT"Custodian",
c_id	INT(11)	NOT NULL,
c_salary	INT(11)	NOT NULL,
c_departmentId	INT(11)	NOT NULL,
PRIMARY KEY(c_id),
FOREIGN KEY(c_id) REFERENCES Employee(employee_id),
FOREIGN KEY(c_departmentId) REFERENCES Department(d_id)
);

CREATE TABLE IF NOT EXISTS Appointment
(
a_patientId	INT(11)	NOT NULL,
a_id	SMALLINT(6)	NOT NULL,
a_roomNum	SMALLINT(6)	NOT NULL,
a_startTime	TIME	NOT NULL,
a_date	DATE	NOT NULL,
a_doctor	INT(11)	NOT NULL,
PRIMARY KEY(a_id),
FOREIGN KEY(a_patientId) REFERENCES Patient(p_id),
FOREIGN KEY(a_roomNum) REFERENCES Room(room_number),
FOREIGN KEY(a_doctor) REFERENCES Employee(employee_id)
);

CREATE TABLE IF NOT EXISTS Bill
(
bill_id	SMALLINT(6)	NOT NULL,
bill_amount	float	NOT NULL,
bill_patientId	INT(11)	NOT NULL,
bill_issue	VARCHAR(30)	NOT NULL,
PRIMARY KEY(bill_id),
FOREIGN KEY(bill_patientId) REFERENCES Patient(p_id)
);

CREATE TABLE IF NOT EXISTS Equipment
(
eq_id	INT(11)	NOT NULL,
eq_desc	VARCHAR(30)	NOT NULL,
eq_name	VARCHAR(30) NOT NULL,
eq_room	SMALLINT(6)	NOT NULL,
PRIMARY KEY(eq_id),
FOREIGN KEY(eq_room) REFERENCES Room(room_number)
);

CREATE TABLE IF NOT EXISTS MedicalRecord
(
mr_id	INT(11)	NOT NULL,
mr_patientId	INT(9)	NOT NULL,
mr_pastAppointment	SMALLINT(6)	NOT NULL,
mr_bloodType	VARCHAR(4)	NOT NULL,
mr_alLergies	VARCHAR(100)	NOT NULL,
mr_pastIllnesses	VARCHAR(100)	NOT NULL,
PRIMARY KEY(mr_id),
FOREIGN KEY(mr_patientId) REFERENCES Patient(p_id),
FOREIGN KEY(mr_pastAppointment) REFERENCES Appointment(a_id)
);

CREATE TABLE IF NOT EXISTS Distributors
(
dist_name	VARCHAR(15)	NOT NULL,
dist_product	VARCHAR(30)	NOT NULL,
dist_id	INT(11)	NOT NULL,
dist_department	INT(11)	NOT NULL,
PRIMARY KEY(dist_id,dist_product),
FOREIGN KEY(dist_department) REFERENCES Department(d_id)
);

CREATE TABLE IF NOT EXISTS Hours
(
h_shiftId	INT(11)	NOT NULL,
h_employeeId	INT(11)	NOT NULL,
h_hoursScheduled	INT(3) NOT NULL,
h_dateScheduled	DATE	NOT NULL,
PRIMARY KEY(h_shiftId),
FOREIGN KEY(h_employeeId) REFERENCES Employee(employee_id)
);

CREATE TABLE IF NOT EXISTS Perscription
(
persc_id	INT(11)	NOT NULL,
persc_medicineName	VARCHAR(15)	NOT NULL,
persc_distributorId	INT(11)	NOT NULL,
persc_forPatient	INT(11)	NOT NULL,
persc_perscribedBy	INT(11)	NOT NULL,
PRIMARY KEY(persc_id),
FOREIGN KEY(persc_distributorId) REFERENCES Distributor(dist_id),
FOREIGN KEY(persc_forPatient) REFERENCES Patient(p_id),
FOREIGN KEY(persc_perscribedBy) REFERENCES Employee(employee_id)
);













