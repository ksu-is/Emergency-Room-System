def emergencyroomsystem():
    list_patientID = ["4554", "8861", "9254"]
    list_name = [ "Bennet", "Gilbert", "Johnson"]
    list_age = ["18", "21", "45"]
    list_blood_type = ["O","A","B"]
    list_waiting_time = ["00:56:00", "01:36:00", "02:03:00"]


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
    Enter A To search for a patient  
    Enter B To add a new patient record
    Enter C To calculate the average waiting time of all patients
		
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
                waiting_time = list_waiting_time[index]
                print("Age: " , patient_age)
                print("Blood Type: ", blood_type)
                print("Patient ID: ", patient_id)
                print("Waiting Time: ", waiting_time)
            elif name_or_ID.upper()=="D":
                patient_id = input("Enter the patinet ID please: ")
                index = list_patientID.index(patient_id)
                last_name = list_name[index]
                patient_age = list_age[index]
                blood_type = list_blood_type[index]
                waiting_time = list_waiting_time[index]
                print("Patient's last name: ", last_name)
                print("Age: ", patient_age)
                print("Blood type: ", blood_type)
                print("Waiting Time: ", waiting_time)
            else:
                print("That is an invalid input, please try again")
                pass
            
        elif option_one.upper()=="B":
            print("Enter the new comma separated record like this: 'PatientID,LastName,Age,Bloodtype,waitingtime' ")
            record = input("Enter a new patient record: ")
            list_values = record.split(",")
            list_patientID.append(list_values[0])
            list_name.append(list_values[1])
            list_age.append(list_values[2])
            list_blood_type.append(list_values[3])
            list_waiting_time.append(list_values[4])
            print(list_patientID)
            print(list_name)
            print(list_age)
            print(list_blood_type)
            print(list_waiting_time)
        else:
            print("That is an invalid input, please read the instructions and try again ")
            pass
        
    
        
    elif clearance_level=="2":
        while True:
            pwd = input("Enter your 4 digit level two clearance password: ")
            if pwd == '1987':
                print("You have the clearnace to calculate the averge waiting time.")
                option_two = input("Enter 'A', 'B' or 'C': ")
                if option_two.upper()=="A":
                    name_or_ID = input("Enter 'C' if you would like to seach using a last name or 'D' to search with ID number: ")
                    if name_or_ID.upper()=="C":
                        last_name = input("Enter the last name of the patient: ")
                        index = list_name.index(last_name)
                        patient_age = list_age[index]
                        blood_type = list_blood_type[index]
                        patient_id = list_patientID[index]
                        waiting_time = list_waiting_time[index]
                        print("Age: " , patient_age)
                        print("Blood Type: ", blood_type)
                        print("Patient ID: ", patient_id)
                        print("Waiting time: ", waiting_time)
                    elif name_or_ID.upper()=="D":
                        patient_id = input("Enter the patinet ID please: ")
                        index = list_patientID.index(patient_id)
                        last_name = list_name[index]
                        patient_age = list_age[index]
                        blood_type = list_blood_type[index]
                        waiting_time = list_waiting_time[index]
                        print("Patient's last name: ", last_name)
                        print("Age: ", patient_age)
                        print("Blood type: ", blood_type)
                        print("Waiting time: ", waiting_time)
                    else:
                        print("That is an invalid input, please try again")
                        pass
            
                elif option_two.upper()=="B":
                    print("Enter the new comma separated record like this: 'PatientID,LastName,Age,Bloodtype,waitingtime' ")
                    record = input("Enter a new patient record: ")
                    list_values = record.split(",")
                    list_patientID.append(list_values[0])
                    list_name.append(list_values[1])
                    list_age.append(list_values[2])
                    list_blood_type.append(list_values[3])
                    list_waiting_time.append(list_values[4])
                    print(list_patientID)
                    print(list_name)
                    print(list_age)
                    print(list_blood_type)
                    print(list_waiting_time)
                elif option_two.upper()=="C":
                    from datetime import timedelta
                    times = list_waiting_time
                    print("The average waiting time for the emergency room is: ", str(timedelta(seconds=sum(map(lambda f: int(f[0])*3600 + int(f[1])*60 + int(f[2]), map(lambda f: f.split(':'), times)))/len(times))))

                else:
                    print("That is an invalid input, please read the instructions and try again ")
                    break
        
            
            else: 
                print("The password you entered is incorrect")
            
            
            
           
    else:
        pass
    restart = input("Would you like to start again? ").lower()
    if restart=="yes":
        emergencyroomsystem()
    else:
        exit()
emergencyroomsystem()
