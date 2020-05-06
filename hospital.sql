
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
b_capacity INT(6) NOT NULL,
b_numRooms INT(6) NOT NULL,
PRIMARY KEY(b_id)
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

CREATE TABLE IF NOT EXISTS Doctor
(
doc_title	VARCHAR(16)	NOT NULL,
doc_ssn	INT(9)	NOT NULL,
doc_id	INT(11)	NOT NULL	REFERENCES Employee(employee_id),
doc_salary	INT(11)	NOT NULL,
doc_departmentId	INT(11)	NOT NULL	REFERENCES Department(d_id),
PRIMARY KEY(doc_id)
);

CREATE TABLE IF NOT EXISTS Nurse
(
nurse_id	INT(11)	NOT NULL	REFERENCES Employee(employee_id),
nurse_ssn	INT(9)	NOT NULL,
nurse_title	VARCHAR(15) DEFAULT"Nurse",
nurse_worksRoom	SMALLINT(6) NOT NULL,
nurse_salary	INT(10)	NOT NULL,
nurse_departmentId	INT(11)	NOT NULL	REFERENCES Department(d_id),
PRIMARY KEY(nurse_id)
);

CREATE TABLE IF NOT EXISTS Secretary
(
s_title	VARCHAR(19) DEFAULT"Secretary",
s_ssn	INT(9)	NOT NULL,
s_id	INT(11)	NOT NULL	REFERENCES Employee(employee_id),
s_worksRoom	SMALLINT(6)	NOT NULL	REFERENCES Room(room_number),	
s_salary	INT(11)	NOT NULL,
s_departmentId	INT(11)	NOT NULL	REFERENCES Department(d_id),
PRIMARY KEY(s_id)
);

CREATE TABLE IF NOT EXISTS Custodian
(
c_title	VARCHAR(19) DEFAULT"Custodian",
c_ssn	INT(9)	NOT NULL,
c_id	INT(11)	NOT NULL	REFERENCES Employee(employee_id),
c_salary	INT(11)	NOT NULL,
c_departmentId	INT(11)	NOT NULL	REFERENCES Department(d_id),
PRIMARY KEY(c_id)
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
bill_issue	VARCHAR(50)	NOT NULL,
PRIMARY KEY(bill_id),
FOREIGN KEY(bill_patientId) REFERENCES Patient(p_id)
);

CREATE TABLE IF NOT EXISTS Equipment
(
eq_id	INT(11)	NOT NULL,
eq_desc	VARCHAR(75)	NOT NULL,
eq_name	VARCHAR(75) NOT NULL,
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
mr_allergies	VARCHAR(100)	NOT NULL,
mr_pastIllnesses	VARCHAR(100)	NOT NULL,
PRIMARY KEY(mr_id),
FOREIGN KEY(mr_patientId) REFERENCES Patient(p_id),
FOREIGN KEY(mr_pastAppointment) REFERENCES Appointment(a_id)
);

CREATE TABLE IF NOT EXISTS Distributor
(
dist_name	VARCHAR(75)	NOT NULL,
dist_product	VARCHAR(30)	NOT NULL,
dist_id	INT(11)	NOT NULL,
dist_department	INT(11)	NOT NULL	REFERENCES Department(d_id),
PRIMARY KEY(dist_id,dist_product)
);

CREATE TABLE IF NOT EXISTS Hours
(
h_shiftId	INT(11)	NOT NULL,
h_employeeId	INT(11)	NOT NULL	REFERENCES Employee(employee_id),
h_hoursScheduled	INT(3) NOT NULL,
h_dateScheduled	DATE	NOT NULL,
PRIMARY KEY(h_shiftId)
);

CREATE TABLE IF NOT EXISTS Perscription
(
persc_id	INT(11)	NOT NULL,
persc_medicineName	VARCHAR(15)	NOT NULL,
persc_distributorId	INT(11)	NOT NULL	REFERENCES Distributor(dist_id),
persc_forPatient	INT(11)	NOT NULL	REFERENCES Patient(p_id),
persc_perscribedBy	INT(11)	NOT NULL	REFERENCES Employee(employee_id),
PRIMARY KEY(persc_id)
);


/*ADD PATIENT DATA*/

INSERT INTO Patient(p_firstName,p_middleIn,p_lastName,p_gender,p_ssn,p_insuranceNum,p_id,p_phoneNum)
VALUES('James', 'E','Borg','M', 888665555, 546962594, 504994142, '599-576-7909');
INSERT INTO Patient(p_firstName,p_middleIn,p_lastName,p_gender,p_ssn,p_insuranceNum,p_id,p_phoneNum)
VALUES('Jennifer', 'S','Wallace','F', 987654321, 900316848, 930073251, '774-832-2342');
INSERT INTO Patient(p_firstName,p_middleIn,p_lastName,p_gender,p_ssn,p_insuranceNum,p_id,p_phoneNum)
VALUES('Ahmad', 'V','Jabbar','M', 987987987, 569341818, 635684037, '335-321-8143');
INSERT INTO Patient(p_firstName,p_middleIn,p_lastName,p_gender,p_ssn,p_insuranceNum,p_id,p_phoneNum)
VALUES('Alicia', 'J','Zelaya','F', 999887777, 208164197, 806984547, '670-925-9464');



/*ADD ROOM DATA*/

INSERT INTO Room(currentPatient_id,room_number,room_type,room_capacity,room_vacant)
VALUES(504994142, 6405, 'single', '10', 'N');
INSERT INTO Room(currentPatient_id,room_number,room_type,room_capacity,room_vacant)
VALUES(930073251, 3009, 'double', '20', 'Y');
INSERT INTO Room(currentPatient_id,room_number,room_type,room_capacity,room_vacant)
VALUES(635684037, 6657, 'single', '10', 'N');
INSERT INTO Room(currentPatient_id,room_number,room_type,room_capacity,room_vacant)
VALUES(806984547, 6825, 'double', '20', 'Y');



/*ADD BUILDING DATA*/

INSERT INTO Building(b_id,b_name,b_capacity,b_numRooms)
VALUES(323845818, 'West', 1000, 1000);
INSERT INTO Building(b_id,b_name,b_capacity,b_numRooms)
VALUES(481574404, 'South', 1000, 1000);
INSERT INTO Building(b_id,b_name,b_capacity,b_numRooms)
VALUES(082207790, 'East', 1000, 1000);



/*ADD EMPLOYEE DATA*/

/*Doctors*/
INSERT INTO Employee(employee_id,employee_ssn,employee_firstName,employee_middleIn,employee_lastName,employee_hired,employee_gender,employee_phone)
VALUES(130376847, 264698709, 'John', 'B', 'Smith', '2018-05-28', 'M', '832-398-6508');
INSERT INTO Employee(employee_id,employee_ssn,employee_firstName,employee_middleIn,employee_lastName,employee_hired,employee_gender,employee_phone)
VALUES(973440056, 802005820, 'Franklin', 'T', 'Wong', '2010-03-10', 'M', '364-519-3215');
INSERT INTO Employee(employee_id,employee_ssn,employee_firstName,employee_middleIn,employee_lastName,employee_hired,employee_gender,employee_phone)
VALUES(591242254, 499268085, 'Joyce', 'A', 'English', '2006-04-16', 'F', '842-166-0271');

/*Nurses*/
INSERT INTO Employee(employee_id,employee_ssn,employee_firstName,employee_middleIn,employee_lastName,employee_hired,employee_gender,employee_phone)
VALUES(785352590, 824490405, 'Rahmesh', 'K', 'Narayan', '2015-08-30', 'M', '524-192-9678');
INSERT INTO Employee(employee_id,employee_ssn,employee_firstName,employee_middleIn,employee_lastName,employee_hired,employee_gender,employee_phone)
VALUES(384319608, 999801534, 'Sally', 'L', 'Baker', '2000-03-15', 'F', '123-456-7896');
INSERT INTO Employee(employee_id,employee_ssn,employee_firstName,employee_middleIn,employee_lastName,employee_hired,employee_gender,employee_phone)
VALUES(497286743, 684174346, 'Victoria', 'M', 'Nelson', '2020-12-25', 'F', '345-623-9863');

/*Secretarys*/
INSERT INTO Employee(employee_id,employee_ssn,employee_firstName,employee_middleIn,employee_lastName,employee_hired,employee_gender,employee_phone)
VALUES(993837337, 637527074, 'Sam', 'M', 'Larkin', '2002-02-03', 'M', '826-845-0489');
INSERT INTO Employee(employee_id,employee_ssn,employee_firstName,employee_middleIn,employee_lastName,employee_hired,employee_gender,employee_phone)
VALUES(176246044, 705683048, 'Laura', 'A', 'Allen', '1999-09-01', 'F', '367-340-8624');
INSERT INTO Employee(employee_id,employee_ssn,employee_firstName,employee_middleIn,employee_lastName,employee_hired,employee_gender,employee_phone)
VALUES(649622117, 652353637, 'Christopher', 'J', 'Miller', '2005-04-04', 'M', '710-468-9370');

/*Custodians*/
INSERT INTO Employee(employee_id,employee_ssn,employee_firstName,employee_middleIn,employee_lastName,employee_hired,employee_gender,employee_phone)
VALUES(534303639, 570416365, 'Michael', 'S', 'Suter', '2003-02-03', 'M', '349-249-8357');
INSERT INTO Employee(employee_id,employee_ssn,employee_firstName,employee_middleIn,employee_lastName,employee_hired,employee_gender,employee_phone)
VALUES(024834875, 081150736, 'Gail', 'P', 'Bradley', '1999-01-09', 'F', '347-239-5358');
INSERT INTO Employee(employee_id,employee_ssn,employee_firstName,employee_middleIn,employee_lastName,employee_hired,employee_gender,employee_phone)
VALUES(602156440, 791061691, 'Rachel', 'E', 'Folmar', '2005-04-04', 'F', '528-535-9731');


/*ADD DEPARTMENT DATA*/

INSERT INTO Department(d_name,d_id,d_buildingId,d_managerId)
VALUES('Pediatrics', 477964823, 323845818, 130376847);
INSERT INTO Department(d_name,d_id,d_buildingId,d_managerId)
VALUES('GeneralSurgery', 444830538, 481574404, 973440056);
INSERT INTO Department(d_name,d_id,d_buildingId,d_managerId)
VALUES('Cardiovascular', 843808901, 082207790, 591242254);



/*ADD DOCTOR DATA*/

INSERT INTO Doctor(doc_title,doc_ssn,doc_id,doc_salary,doc_departmentId)
VALUES('Pediatrician', 264698709, 130376847, 6000000, 477964823);
INSERT INTO Doctor(doc_title,doc_ssn,doc_id,doc_salary,doc_departmentId)
VALUES('Surgeon', 802005820, 973440056, 7000000, 444830538);
INSERT INTO Doctor(doc_title,doc_ssn,doc_id,doc_salary,doc_departmentId)
VALUES('Cardiologist', 499268085, 591242254, 9000000, 843808901);



/*ADD NURSE DATA*/

INSERT INTO Nurse(nurse_id,nurse_ssn,nurse_title,nurse_worksRoom,nurse_salary,nurse_departmentId)
VALUES(785352590, 824490405, 'Nurse', 6405, 89000, 477964823);
INSERT INTO Nurse(nurse_id,nurse_ssn,nurse_title,nurse_worksRoom,nurse_salary,nurse_departmentId)
VALUES(384319608, 999801534, 'Nurse', 3009, 63000, 444830538);
INSERT INTO Nurse(nurse_id,nurse_ssn,nurse_title,nurse_worksRoom,nurse_salary,nurse_departmentId)
VALUES(497286743, 684174346, 'Nurse', 6657, 78000, 843808901);



/*ADD SECRETARY DATA*/

INSERT INTO Secretary(s_title,s_ssn,s_id,s_worksRoom,s_salary,s_departmentId)
VALUES('Secretary', 637527074, 993837337, 6405, 22000, 477964823);
INSERT INTO Secretary(s_title,s_ssn,s_id,s_worksRoom,s_salary,s_departmentId)
VALUES('Secretary', 705683048, 176246044, 3009, 35000, 444830538);
INSERT INTO Secretary(s_title,s_ssn,s_id,s_worksRoom,s_salary,s_departmentId)
VALUES('Secretary', 652353637, 649622117, 6657, 44000, 843808901);



/*ADD CUSTODIAN DATA*/

INSERT INTO Custodian(c_title,c_ssn,c_id,c_salary,c_departmentId)
VALUES('Custodian', 570416365, 534303639, 22000, 477964823);
INSERT INTO Custodian(c_title,c_ssn,c_id,c_salary,c_departmentId)
VALUES('Custodian', 081150736, 024834875, 35000, 444830538);
INSERT INTO Custodian(c_title,c_ssn,c_id,c_salary,c_departmentId)
VALUES('Custodian', 791061691, 602156440, 44000, 843808901);



/*ADD APPOINTMENT DATA*/

INSERT INTO Appointment(a_patientId,a_id,a_roomNum,a_startTime,a_date,a_doctor)
VALUES(504994142, 3542, 6405, '09:30:00', '2020-04-30', 130376847);
INSERT INTO Appointment(a_patientId,a_id,a_roomNum,a_startTime,a_date,a_doctor)
VALUES(930073251, 3295, 3009, '10:45:00', '2019-10-06', 973440056);
INSERT INTO Appointment(a_patientId,a_id,a_roomNum,a_startTime,a_date,a_doctor)
VALUES(635684037, 1294, 6657, '08:00:00', '2002-06-25', 591242254);



/*ADD BILL DATA*/

INSERT INTO Bill(bill_id,bill_amount,bill_patientId,bill_issue)
VALUES(3932, 2000, 504994142, 'Concussion');
INSERT INTO Bill(bill_id,bill_amount,bill_patientId,bill_issue)
VALUES(9998, 4000, 930073251, 'Broken arm');
INSERT INTO Bill(bill_id,bill_amount,bill_patientId,bill_issue)
VALUES(6472, 3500, 635684037, 'Heart replacement');



/*ADD EQUIPMENT DATA*/

INSERT INTO Equipment(eq_id,eq_desc,eq_name,eq_room)
VALUES(462192482, 'Object that keeps stats on patient', 'Patient Monitor', 6405);
INSERT INTO Equipment(eq_id,eq_desc,eq_name,eq_room)
VALUES(395553940, 'Object surgery is performed on', 'Surgical Table', 3009);
INSERT INTO Equipment(eq_id,eq_desc,eq_name,eq_room)
VALUES(567669247, 'Machine that keeps stats on patient heart', 'EKGs', 6657);



/*ADD MEDICAL RECORD DATA*/

INSERT INTO MedicalRecord(mr_id,mr_patientId,mr_pastAppointment,mr_bloodType,mr_allergies,mr_pastIllnesses)
VALUES(332296395, 504994142, 3542, 'A+', 'Peanut, Shellfish, Soy', 'Flu');
INSERT INTO MedicalRecord(mr_id,mr_patientId,mr_pastAppointment,mr_bloodType,mr_allergies,mr_pastIllnesses)
VALUES(530716302, 930073251, 3295, 'O-', 'Eggs, Pine Nut, Milk', 'Cancer');
INSERT INTO MedicalRecord(mr_id,mr_patientId,mr_pastAppointment,mr_bloodType,mr_allergies,mr_pastIllnesses)
VALUES(539625353, 635684037, 1294, 'AB-', 'Almonds, Wheat, Banana', 'Chickenpox');



/*ADD DISTRIBUTOR DATA*/

INSERT INTO Distributor(dist_name,dist_product,dist_id,dist_department)
VALUES('Owens & Minor, Inc.', 'Scrubs', 129184773, 477964823);
INSERT INTO Distributor(dist_name,dist_product,dist_id,dist_department)
VALUES('Henry Schein, Inc.', 'Wheel Chair', 484314482, 444830538);
INSERT INTO Distributor(dist_name,dist_product,dist_id,dist_department)
VALUES('Cardinal Health Inc.', 'EKGs', 944465809, 843808901);



/*ADD HOURS DATA*/

INSERT INTO Hours(h_shiftId,h_employeeId,h_hoursScheduled,h_dateScheduled)
VALUES(830931793, 130376847, 6, '2019-05-24');
INSERT INTO Hours(h_shiftId,h_employeeId,h_hoursScheduled,h_dateScheduled)
VALUES(550201109, 785352590, 12, '2020-09-16');
INSERT INTO Hours(h_shiftId,h_employeeId,h_hoursScheduled,h_dateScheduled)
VALUES(526774785, 534303639, 20, '2005-02-07');



/*ADD PERSCRIPTION DATA*/

INSERT INTO Perscription(persc_id,persc_medicineName,persc_distributorId,persc_forPatient,persc_perscribedBy)
VALUES(681559589, 'Amoxicillin', 129184773, 504994142, 129184773);
INSERT INTO Perscription(persc_id,persc_medicineName,persc_distributorId,persc_forPatient,persc_perscribedBy)
VALUES(805159456, 'Dapsone', 484314482, 930073251, 484314482);
INSERT INTO Perscription(persc_id,persc_medicineName,persc_distributorId,persc_forPatient,persc_perscribedBy)
VALUES(923117174, 'Enoxaparin', 944465809, 635684037, 944465809);








