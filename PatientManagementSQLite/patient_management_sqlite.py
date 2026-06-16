# File Name: patient_management_sqlite.py

from abc import ABC, abstractmethod
import sqlite3


# ============================================================
# DATABASE SETUP
# ============================================================

DB_NAME = "hospital.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT UNIQUE,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            disease TEXT NOT NULL,
            patient_type TEXT NOT NULL,
            consultation_fee REAL DEFAULT 0,
            emergency_charges REAL DEFAULT 0,
            medicine_charges REAL DEFAULT 0,
            total_bill REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ============================================================
# ABSTRACT CLASS
# ============================================================

class PatientDesc(ABC):

    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def update_disease(self, new_disease):
        self.disease = new_disease
        print("Disease updated successfully for patient", self.patient_id)

    def show_details(self):
        print("\n========== Patient Details ==========")
        print("Patient ID:", self.patient_id)
        print("Patient Name:", self.name)
        print("Patient Age:", self.age)
        print("Disease:", self.disease)

    @abstractmethod
    def calculate_bill(self):
        pass


# ============================================================
# OPD PATIENT CLASS
# ============================================================

class OPDPatient(PatientDesc):

    def __init__(self, patient_id, name, age, disease, consultation_fee):
        super().__init__(patient_id, name, age, disease)
        self.consultation_fee = consultation_fee

    def calculate_bill(self):
        total_bill = self.consultation_fee
        return total_bill


# ============================================================
# EMERGENCY PATIENT CLASS
# ============================================================

class EmergencyPatient(PatientDesc):

    def __init__(self, patient_id, name, age, disease, consultation_fee, emergency_charges, medicine_charges):
        super().__init__(patient_id, name, age, disease)

        # Emergency patient mein bhi consultation fee hogi
        self.consultation_fee = consultation_fee

        # Emergency extra charges
        self.emergency_charges = emergency_charges

        # Medicine charges
        self.medicine_charges = medicine_charges

    def calculate_bill(self):
        total_bill = self.consultation_fee + self.emergency_charges + self.medicine_charges
        return total_bill


# ============================================================
# INPUT HELPER FUNCTIONS
# ============================================================

def get_int_input(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Invalid input. Please number enter karein.")


def get_float_input(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Invalid input. Please amount number mein enter karein.")


def get_patient_basic_details():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = get_int_input("Enter Patient Age: ")
    disease = input("Enter Patient Disease: ")

    return patient_id, name, age, disease


# ============================================================
# DATABASE FUNCTIONS
# ============================================================

def save_patient_to_db(patient, patient_type):
    total_bill = patient.calculate_bill()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        if patient_type == "OPD":
            cursor.execute("""
                INSERT INTO patients (
                    patient_id, name, age, disease, patient_type,
                    consultation_fee, emergency_charges, medicine_charges, total_bill
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                patient.patient_id,
                patient.name,
                patient.age,
                patient.disease,
                patient_type,
                patient.consultation_fee,
                0,
                0,
                total_bill
            ))

        elif patient_type == "Emergency":
            cursor.execute("""
                INSERT INTO patients (
                    patient_id, name, age, disease, patient_type,
                    consultation_fee, emergency_charges, medicine_charges, total_bill
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                patient.patient_id,
                patient.name,
                patient.age,
                patient.disease,
                patient_type,
                patient.consultation_fee,
                patient.emergency_charges,
                patient.medicine_charges,
                total_bill
            ))

        conn.commit()
        print("\nPatient data successfully database mein save ho gaya.")

    except sqlite3.IntegrityError:
        print("\nError: Yeh Patient ID already database mein mojood hai.")

    finally:
        conn.close()


def show_all_patients():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()

    conn.close()

    if not patients:
        print("\nAbhi database mein koi patient record nahi hai.")
        return

    print("\n========== All Patients From Database ==========")

    for patient in patients:
        print("\nDatabase ID:", patient[0])
        print("Patient ID:", patient[1])
        print("Name:", patient[2])
        print("Age:", patient[3])
        print("Disease:", patient[4])
        print("Patient Type:", patient[5])
        print("Consultation Fee:", patient[6])
        print("Emergency Charges:", patient[7])
        print("Medicine Charges:", patient[8])
        print("Total Bill:", patient[9])


def find_patient_by_id(patient_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
    patient = cursor.fetchone()

    conn.close()

    return patient


# ============================================================
# ADD PATIENT FUNCTIONS
# ============================================================

def add_opd_patient():
    print("\n========== Add OPD Patient ==========")

    patient_id, name, age, disease = get_patient_basic_details()

    consultation_fee = get_float_input("Enter Consultation Fee: ")

    opd_patient = OPDPatient(
        patient_id,
        name,
        age,
        disease,
        consultation_fee
    )

    opd_patient.show_details()

    total_bill = opd_patient.calculate_bill()
    print("OPD Patient Bill is:", total_bill)

    save_patient_to_db(opd_patient, "OPD")


def add_emergency_patient():
    print("\n========== Add Emergency Patient ==========")

    patient_id, name, age, disease = get_patient_basic_details()

    consultation_fee = get_float_input("Enter Consultation Fee: ")
    emergency_charges = get_float_input("Enter Emergency Charges: ")
    medicine_charges = get_float_input("Enter Medicine Charges: ")

    emergency_patient = EmergencyPatient(
        patient_id,
        name,
        age,
        disease,
        consultation_fee,
        emergency_charges,
        medicine_charges
    )

    emergency_patient.show_details()

    total_bill = emergency_patient.calculate_bill()
    print("Emergency Patient Bill is:", total_bill)

    save_patient_to_db(emergency_patient, "Emergency")


# ============================================================
# UPDATE PATIENT FUNCTION
# ============================================================

def update_patient():
    print("\n========== Update Patient ==========")

    patient_id = input("Enter Patient ID to update: ")

    old_patient = find_patient_by_id(patient_id)

    if old_patient is None:
        print("\nPatient record nahi mila.")
        return

    print("\nOld Patient Record:")
    print("Patient ID:", old_patient[1])
    print("Name:", old_patient[2])
    print("Age:", old_patient[3])
    print("Disease:", old_patient[4])
    print("Patient Type:", old_patient[5])
    print("Consultation Fee:", old_patient[6])
    print("Emergency Charges:", old_patient[7])
    print("Medicine Charges:", old_patient[8])
    print("Total Bill:", old_patient[9])

    print("\nEnter New Details")

    name = input("Enter New Patient Name: ")
    age = get_int_input("Enter New Patient Age: ")
    disease = input("Enter New Patient Disease: ")

    print("\nSelect New Patient Type")
    print("1. OPD")
    print("2. Emergency")

    choice = input("Enter your choice: ")

    if choice == "1":
        patient_type = "OPD"

        consultation_fee = get_float_input("Enter New Consultation Fee: ")
        emergency_charges = 0
        medicine_charges = 0

        updated_patient = OPDPatient(
            patient_id,
            name,
            age,
            disease,
            consultation_fee
        )

        total_bill = updated_patient.calculate_bill()

    elif choice == "2":
        patient_type = "Emergency"

        consultation_fee = get_float_input("Enter New Consultation Fee: ")
        emergency_charges = get_float_input("Enter New Emergency Charges: ")
        medicine_charges = get_float_input("Enter New Medicine Charges: ")

        updated_patient = EmergencyPatient(
            patient_id,
            name,
            age,
            disease,
            consultation_fee,
            emergency_charges,
            medicine_charges
        )

        total_bill = updated_patient.calculate_bill()

    else:
        print("\nInvalid patient type.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE patients
        SET name = ?,
            age = ?,
            disease = ?,
            patient_type = ?,
            consultation_fee = ?,
            emergency_charges = ?,
            medicine_charges = ?,
            total_bill = ?
        WHERE patient_id = ?
    """, (
        name,
        age,
        disease,
        patient_type,
        consultation_fee,
        emergency_charges,
        medicine_charges,
        total_bill,
        patient_id
    ))

    conn.commit()
    conn.close()

    print("\nPatient record successfully update ho gaya.")


# ============================================================
# DELETE PATIENT FUNCTION
# ============================================================

def delete_patient():
    print("\n========== Delete Patient ==========")

    patient_id = input("Enter Patient ID to delete: ")

    patient = find_patient_by_id(patient_id)

    if patient is None:
        print("\nPatient record nahi mila.")
        return

    print("\nPatient Found:")
    print("Patient ID:", patient[1])
    print("Name:", patient[2])
    print("Disease:", patient[4])
    print("Patient Type:", patient[5])

    confirm = input("\nKya aap is patient ko delete karna chahte hain? yes/no: ")

    if confirm.lower() == "yes":
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM patients WHERE patient_id = ?", (patient_id,))

        conn.commit()
        conn.close()

        print("\nPatient record successfully delete ho gaya.")
    else:
        print("\nDelete cancel ho gaya.")


# ============================================================
# MAIN MENU
# ============================================================

def main():
    create_table()

    while True:
        print("\n========== Patient Management System ==========")
        print("1. Add OPD Patient")
        print("2. Add Emergency Patient")
        print("3. Show All Patients")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_opd_patient()

        elif choice == "2":
            add_emergency_patient()

        elif choice == "3":
            show_all_patients()

        elif choice == "4":
            update_patient()

        elif choice == "5":
            delete_patient()

        elif choice == "6":
            print("\nProgram closed successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")


# Program yahan se start hoga
main()