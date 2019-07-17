Enter "1" for level one clearance
Enter "2" for level two clearance

clearance_level = input("Please enter your clearance level here: ")
if clearance_level==1:
    print("You are allowed to add a patient record or search for a patinet record")
    option_one = input("Enter 'A' to view patient list /n Enter 'B' to add a new patient /n Enter 'C' to search for a patient: ")
    print(option_one)
    if option_one == "A"
elif clearance_level==2:
    print("Your clearance level allows you to calculate the average waiting time for a patient in the Emergency Room")
    option_two = input("Enter 'A' to view patient list /n Enter 'B' to add a new patient /n Enter 'C' to search for a patient /n Enter 'D' to caculate the average wating time of all patients: ")
    print(option_two)
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
