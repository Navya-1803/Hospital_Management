SHOW DATABASES;
CREATE DATABASE hospital;
USE hospital;
CREATE TABLE Patient (
    Patient_ID INT PRIMARY KEY,
    Patient_Name VARCHAR(100),
    D_O_B Date,
    Age INT,
    PhoneNo VARCHAR(15) UNIQUE,
    RoomNo INT
);
CREATE TABLE Doctor (
    Doctor_ID INT PRIMARY KEY,
    Doctor_Name VARCHAR(100),
    Specialization VARCHAR(15),
    Dept_ID INT
);
CREATE TABLE Department (
    Dept_ID INT PRIMARY KEY,
    Dept_Name VARCHAR(100)
);

CREATE TABLE Staff (
    Staff_ID INT PRIMARY KEY,
    Staff_Name VARCHAR(100),
    Staff_Role VARCHAR(100),
    Dept_ID INT
);


CREATE TABLE Appointment (
    Appointment_ID INT PRIMARY KEY,
    Patient_ID INT,
    Doctor_ID INT,
    Date DATE,
    Time VARCHAR(10),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
    FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID)
);

CREATE TABLE Surgery (
    Surgery_ID INT PRIMARY KEY,
    Patient_ID INT,
    Doctor_ID INT,
    Date DATE,
    Type VARCHAR(100),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
    FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID)
);
CREATE TABLE Pharmacy (
    Medicine_ID INT PRIMARY KEY,
    Medicine_Name VARCHAR(100) UNIQUE,
    Price DECIMAL(10,2),
    Stock INT
);

CREATE TABLE Insurance (
    Policy_ID INT PRIMARY KEY,
    Patient_ID INT,
    Provider VARCHAR(100),
    Coverage_Amount DECIMAL(10,2),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

CREATE TABLE Visitor (
    Visitor_ID INT PRIMARY KEY,
    Visitor_Name VARCHAR(100),
    Relationship VARCHAR(50),
    Patient_ID INT,
	PhoneNo VARCHAR(15) UNIQUE,
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

CREATE TABLE Emergency (
	Case_ID INT,
    Patient_ID INT,
    Date DATE,
    Details TEXT,
    PhoneNo VARCHAR(15) UNIQUE,
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

CREATE TABLE Room (
    RoomNo INT PRIMARY KEY,
    Room_Type VARCHAR(50),
    Patient_ID INT UNIQUE,
    Room_Status TEXT,
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

CREATE TABLE Medical_Record (
    Record_ID INT PRIMARY KEY,
    Patient_ID INT,
    Doctor_ID INT,
    Date DATE,
    Diagnosis TEXT,
    Treatment TEXT,
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

CREATE TABLE LabTest (
    TestName VARCHAR(100),
    Patient_ID INT,
    Doctor_ID INT,
    Result TEXT,
    UNIQUE (TestName, Patient_ID),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
    FOREIGN KEY (Doctor_ID) REFERENCES Doctor(Doctor_ID)
);

CREATE TABLE Billing (
    Billing_ID INT PRIMARY KEY,
    Patient_ID INT,
    Amount DECIMAL(10,2),
    Date DATE,
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

CREATE TABLE Blood_Bank (
    Blood_ID INT PRIMARY KEY,
    Patient_ID INT,
    Blood_Type VARCHAR(50),
    Availability VARCHAR(50),
    Donor_name VARCHAR(50),
    UNIQUE (Patient_ID, Blood_Type),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);
INSERT INTO Patient VALUES (1, 'Asher', '1985-07-12', 39, '9876543210', 101);
INSERT INTO Patient VALUES (2, 'Navya', '1990-05-23', 34, '9876543211', 102);
INSERT INTO Patient VALUES (3, 'Chaitanya', '1975-08-14', 49, '9876543212', 103);
INSERT INTO Patient VALUES (4, 'Ashish', '2000-03-30', 24, '9876543213', 104);
INSERT INTO Patient VALUES (5, 'Archit', '1995-12-22', 29, '9876543214', 105);

INSERT INTO Doctor VALUES (1, 'Dr. Souvik', 'Cardiology', 1);
INSERT INTO Doctor VALUES (2, 'Dr. Shreyash', 'Neurology', 2);
INSERT INTO Doctor VALUES (3, 'Dr. Vishwank', 'Orthopedics', 3);
INSERT INTO Doctor VALUES (4, 'Dr. Jayabhrata', 'Pediatrics', 4);
INSERT INTO Doctor VALUES (5, 'Dr. Ruchir', 'Dermatology', 5);

INSERT INTO Department VALUES (1, 'Cardiology');
INSERT INTO Department VALUES (2, 'Neurology');
INSERT INTO Department VALUES (3, 'Orthopedics');
INSERT INTO Department VALUES (4, 'Pediatrics');
INSERT INTO Department VALUES (5, 'Dermatology');

INSERT INTO Staff VALUES (1, 'Vigneshwar', 'Nurse', 1);
INSERT INTO Staff VALUES (2, 'Sahil', 'Technician', 2);
INSERT INTO Staff VALUES (3, 'Siddhant', 'Receptionist', 3);
INSERT INTO Staff VALUES (4, 'Sameer', 'Janitor', 4);
INSERT INTO Staff VALUES (5, 'Rajesh', 'Pharmacist', 5);

INSERT INTO Appointment VALUES (1, 1, 1, '2025-03-11', '10:00 AM');
INSERT INTO Appointment VALUES (2, 2, 2, '2025-03-12', '11:00 AM');
INSERT INTO Appointment VALUES (3, 3, 3, '2025-03-13', '12:00 PM');
INSERT INTO Appointment VALUES (4, 4, 4, '2025-03-14', '01:00 PM');
INSERT INTO Appointment VALUES (5, 5, 5, '2025-03-15', '02:00 PM');

INSERT INTO Surgery VALUES (1, 1, 1, '2025-04-01', 'Heart Bypass');
INSERT INTO Surgery VALUES (2, 2, 2, '2025-04-02', 'Brain Surgery');
INSERT INTO Surgery VALUES (3, 3, 3, '2025-04-03', 'Knee Replacement');
INSERT INTO Surgery VALUES (4, 4, 4, '2025-04-04', 'Appendectomy');
INSERT INTO Surgery VALUES (5, 5, 5, '2025-04-05', 'Skin Graft');

INSERT INTO Pharmacy VALUES (1, 'Paracetamol', 50.00, 100);
INSERT INTO Pharmacy VALUES (2, 'Ibuprofen', 75.00, 200);
INSERT INTO Pharmacy VALUES (3, 'Amoxicillin', 120.00, 150);
INSERT INTO Pharmacy VALUES (4, 'Metformin', 90.00, 80);
INSERT INTO Pharmacy VALUES (5, 'Aspirin', 30.00, 300);

INSERT INTO Insurance VALUES (1, 1, 'HealthPlus', 50000.00);
INSERT INTO Insurance VALUES (2, 2, 'MediCare', 60000.00);
INSERT INTO Insurance VALUES (3, 3, 'Wellness Insurance', 70000.00);
INSERT INTO Insurance VALUES (4, 4, 'CareShield', 80000.00);
INSERT INTO Insurance VALUES (5, 5, 'LifeSecure', 90000.00);

INSERT INTO Visitor VALUES (1, 'Vidhyanshu', 'Mother', 1, '9988776655');
INSERT INTO Visitor VALUES (2, 'Saksham', 'Brother', 2, '9988776656');
INSERT INTO Visitor VALUES (3, 'Ayush', 'Sister', 3, '9988776657');
INSERT INTO Visitor VALUES (4, 'Yashasvi', 'Father', 4, '9988776658');
INSERT INTO Visitor VALUES (5, 'Savarna', 'Friend', 5, '9988776659');

INSERT INTO Emergency VALUES (1, 1, '2025-03-01', 'Heart Attack', '9776655443');
INSERT INTO Emergency VALUES (2, 2, '2025-03-02', 'Seizure', '9776655444');
INSERT INTO Emergency VALUES (3, 3, '2025-03-03', 'Broken Arm', '9776655445');
INSERT INTO Emergency VALUES (4, 4, '2025-03-04', 'Food Poisoning', '9776655446');
INSERT INTO Emergency VALUES (5, 5, '2025-03-05', 'Severe Allergic Reaction', '9776655447');

INSERT INTO Room VALUES (101, 'Private', 1, 'Occupied');
INSERT INTO Room VALUES (102, 'Semi-Private', 2, 'Occupied');
INSERT INTO Room VALUES (103, 'ICU', 3, 'Occupied');
INSERT INTO Room VALUES (104, 'General Ward', 4, 'Occupied');
INSERT INTO Room VALUES (105, 'Deluxe', 5, 'Occupied');

INSERT INTO Medical_Record VALUES (1, 1, 1, '2025-02-01', 'High BP', 'Medication');
INSERT INTO Medical_Record VALUES (2, 2, 2, '2025-02-02', 'Migraine', 'Painkillers');
INSERT INTO Medical_Record VALUES (3, 3, 3, '2025-02-03', 'Fracture', 'Cast and Rest');
INSERT INTO Medical_Record VALUES (4, 4, 4, '2025-02-04', 'Fever', 'Antibiotics');
INSERT INTO Medical_Record VALUES (5, 5, 5, '2025-02-05', 'Skin Rash', 'Ointment');

INSERT INTO LabTest VALUES ('Blood Test', 1, 1, 'Normal');
INSERT INTO LabTest VALUES ('MRI', 2, 2, 'Minor Issue');
INSERT INTO LabTest VALUES ('X-Ray', 3, 3, 'Fracture Detected');
INSERT INTO LabTest VALUES ('CT Scan', 4, 4, 'Clear');
INSERT INTO LabTest VALUES ('Skin Biopsy', 5, 5, 'Benign');

INSERT INTO Billing VALUES (1, 1, 1500.00, '2025-02-10');
INSERT INTO Billing VALUES (2, 2, 2000.00, '2025-02-11');
INSERT INTO Billing VALUES (3, 3, 2500.00, '2025-02-12');
INSERT INTO Billing VALUES (4, 4, 3000.00, '2025-02-13');
INSERT INTO Billing VALUES (5, 5, 3500.00, '2025-02-14');

INSERT INTO Blood_Bank VALUES (1, 1, 'A+', 'Available', 'Khushi');
INSERT INTO Blood_Bank VALUES (2, 2, 'B-', 'Not Available', 'Yashasvi');
INSERT INTO Blood_Bank VALUES (3, 3, 'O+', 'Available', 'Lavanya');
INSERT INTO Blood_Bank VALUES (4, 4, 'AB-', 'Not Available', 'Zainab');
INSERT INTO Blood_Bank VALUES (5, 5, 'A-', 'Available', 'Arnav');



DESCRIBE Patient;
SELECT * FROM Patient;

DESCRIBE Doctor;
SELECT * FROM Doctor;

DESCRIBE Department;
SELECT * FROM Department;

DESCRIBE Staff;
SELECT * FROM Staff;

DESCRIBE Appointment;
SELECT * FROM Appointment;

DESCRIBE Surgery;
SELECT * FROM Surgery;

DESCRIBE Pharmacy;
SELECT * FROM Pharmacy;

DESCRIBE Insurance;
SELECT * FROM Insurance;

DESCRIBE Visitor;
SELECT * FROM Visitor;

DESCRIBE Emergency;
SELECT * FROM Emergency;

DESCRIBE Room;
SELECT * FROM Room;

DESCRIBE Medical_Record;
SELECT * FROM Medical_Record;

DESCRIBE LabTest;
SELECT * FROM LabTest;

DESCRIBE Billing;
SELECT * FROM Billing;

DESCRIBE Blood_Bank;
SELECT * FROM Blood_Bank;