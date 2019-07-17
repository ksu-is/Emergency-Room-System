clearance_level = input("Please enter your clearance level here: ")
if clearance_level==1:
    print("You may add or search for a patient record")
elif clearance_level==2:
    print("You may calculate the average waiting time for a patient")
else:
    pass
list_patientID = ["4554", "8861", "9254"]
list_name = [ "Bennet", "Gilbert", "Johnson"]
list_age = ["18", "21", "45"]
list_blood_type = ["O","A","B"]

#get the age, patient ID number and bloodtype with last name

last_name = input("Enter the last name of the patient: ")
index = list_name.index(last_name)
age = list_age[index]
blood_type = list_blood_type[index]
patient_id = list_patientID[index]
print(age)
print(blood_type)
print(patient_id)

#get the name, age and bloodtype with the patient ID number

patient_id = input("Enter the patinet ID please: ")
index = list_patientID.index(patient_id)
last_name = list_name[index]
age = list_age[index]
blood_type = list_blood_type[index]
print(last_name)
print(age)
print(blood_type)
