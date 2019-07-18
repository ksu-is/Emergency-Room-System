print(""" 
 ########################################################
# ====================================================== # 
# ======== Welcome To Emergency Room System	======== #
# ====================================================== #
 ########################################################

First enter your clearance level
Enter 1 if you have level one clearance 
Enter 2 if you have level two clearance

Then: 
Enter A To view patient list
Enter B To add a new patient  
Enter 3 To search for a patient 
Enter 4 To caculate the average wating time of all patients
		
		""")

clearance_level = input("Please enter your clearance level here: ")
if clearance_level=="1":
    print("You are allowed to add a patient record or search for a patinet record")
    option_one = input("Enter 'A', or 'B': ")
    if option_one.upper()=="A":
        name_or_ID = input("Enter 'C' if you would like to seach using a last name or 'D' to search with ID number: ")
        if name_or_ID.upper()=="C":
            last_name = input("Enter the last name of the patient: ")
            index = list_name.index(last_name)
            patient_age = list_age[index]
            blood_type = list_blood_type[index]
            patient_id = list_patientID[index]
            print("Age: " , patient_age)
            print("Blood Type: ", blood_type)
            print("Patient ID: ", patient_id)
        elif name_or_ID.upper()=="D":
            patient_id = input("Enter the patinet ID please: ")
            index = list_patientID.index(patient_id)
            last_name = list_name[index]
            patient_age = list_age[index]
            blood_type = list_blood_type[index]
            print("Patient's last name: ", last_name)
            print("Age: ", patient_age)
            print("Blood type: ", blood_type)
        else:
            print("That is an invalid input, please try again")
            pass
            
    elif option_one.upper()=="B":
        record = input("Enter a new patient record: ")
        list_values = record.split(",")
        list_patientID.append(list_values[0])
        list_name.append(list_values[1])
        list_age.append(list_values[2])
        list_blood_type.append(list_values[3])
        print(list_patientID)
        print(list_name)
        print(list_age)
        print(list_blood_type)
    else:
        print("That is an invalid input, please read the instructions and try again ")
        pass
        
    
        
elif clearance_level=="2":
    while True:
        pwd = input("Enter your 4 digit level two clearance password: ")
        if pwd== "1987":
            print("Welcome")
            break
        else: 
            print("The password you entered is incorrect")
            option_two = input("Enter 'A', 'B' or 'C': ")
            print(option_two)
else:
    pass
