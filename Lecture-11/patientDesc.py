# File Name: patientDesc.py

# abc module se ABC aur abstractmethod import kar rahe hain
# ABC ka use abstract class banane ke liye hota hai
# abstractmethod ka use abstract method banane ke liye hota hai
from abc import ABC, abstractmethod


# PatientDesc ek abstract class hai
# Abstract class ka direct object nahi ban sakta
# Is class ko parent/base class ki tarah use karenge
class PatientDesc(ABC):

    # Constructor method
    # Jab bhi child class ka object banega, yeh method automatically chalega
    def __init__(self, patient_id, name, age, disease):

        # Patient ka ID object ke andar save kar rahe hain
        self.patient_id = patient_id

        # Patient ka name save kar rahe hain
        self.name = name

        # Patient ki age save kar rahe hain
        self.age = age

        # Patient ki disease/problem save kar rahe hain
        self.disease = disease

    # Patient ki disease update karne ka method
    # Is method se patient ki disease ya condition change kar sakte hain
    def update_disease(self, new_disease):

        # New disease ko old disease ki jagah save kar rahe hain
        self.disease = new_disease

        # User ko message show kar rahe hain ke disease update ho gayi
        print("Disease updated successfully for patient", self.patient_id)

    # Patient ki details show karne ka method
    # Is method ka kaam patient ki complete information print karna hai
    def show_details(self):

        # Patient ka ID show kar rahe hain
        print("Patient ID:", self.patient_id)

        # Patient ka name show kar rahe hain
        print("Patient Name:", self.name)

        # Patient ki age show kar rahe hain
        print("Patient Age:", self.age)

        # Patient ki disease show kar rahe hain
        print("Disease:", self.disease)

    # Abstract method
    # Is method ki body parent class mein nahi hogi
    # Har child class ko apna calculate_bill method banana zaroori hoga
    @abstractmethod
    def calculate_bill(self):
        pass


# OPDPatient child class hai
# Yeh PatientDesc class se inherit kar rahi hai
class OPDPatient(PatientDesc):

    # Constructor method
    # OPD patient ke liye extra consultation fee bhi save karenge
    def __init__(self, patient_id, name, age, disease, consultation_fee):

        # Parent class ke constructor ko call kar rahe hain
        super().__init__(patient_id, name, age, disease)

        # OPD patient ki consultation fee save kar rahe hain
        self.consultation_fee = consultation_fee

    # OPD patient ka bill calculate karne ka method
    def calculate_bill(self):

        # OPD patient ka total bill consultation fee ke barabar hai
        total_bill = self.consultation_fee

        # OPD patient ka total bill show kar rahe hain
        print("OPD Patient Bill is", total_bill)


# EmergencyPatient child class hai
# Yeh bhi PatientDesc class se inherit kar rahi hai
class EmergencyPatient(PatientDesc):

    # Constructor method
    # Emergency patient ke liye emergency charges aur medicine charges save karenge
    def __init__(self, patient_id, name, age, disease, emergency_charges, medicine_charges):

        # Parent class ke constructor ko call kar rahe hain
        super().__init__(patient_id, name, age, disease)

        # Emergency charges save kar rahe hain
        self.emergency_charges = emergency_charges

        # Medicine charges save kar rahe hain
        self.medicine_charges = medicine_charges

    # Emergency patient ka bill calculate karne ka method
    def calculate_bill(self):

        # Total bill calculate kar rahe hain
        total_bill = self.emergency_charges + self.medicine_charges

        # Emergency patient ka total bill show kar rahe hain
        print("Emergency Patient Bill is", total_bill)


# OPDPatient ka object create kar rahe hain
# patient_id = P-01
# name = Shariq
# age = 25
# disease = Fever
# consultation_fee = 1500
p1 = OPDPatient("P-01", "Shariq", 25, "Fever", 1500)

# EmergencyPatient ka object create kar rahe hain
# patient_id = P-02
# name = Najam
# age = 30
# disease = Chest Pain
# emergency_charges = 5000
# medicine_charges = 2500
p2 = EmergencyPatient("P-02", "Najam", 30, "Chest Pain", 5000, 2500)


# OPD Patient ka section start kar rahe hain
print("\n========== OPD Patient ==========")

# OPD patient ki details show kar rahe hain
p1.show_details()

# OPD patient ka bill calculate kar rahe hain
p1.calculate_bill()

# OPD patient ki disease update kar rahe hain
p1.update_disease("Viral Fever")

# Update ke baad OPD patient ki details dobara show kar rahe hain
p1.show_details()


# Emergency Patient ka section start kar rahe hain
print("\n========== Emergency Patient ==========")

# Emergency patient ki details show kar rahe hain
p2.show_details()

# Emergency patient ka bill calculate kar rahe hain
p2.calculate_bill()

# Emergency patient ki disease update kar rahe hain
p2.update_disease("Heart Pain")

# Update ke baad emergency patient ki details dobara show kar rahe hain
p2.show_details()