from datetime import datetime
list_patientID = ["4554", "8861", "9254"]
list_name = [ "Bennet", "Gilbert", "Johnson"]
list_age = ["18", "21", "45"]
list_blood_type = ["O","A","B"]
list_waiting_time = ["00:56:00", "01:36:00", "02:03:00"]
def emergencyroomsystem():
   


    print(""" 
    ########################################################
    # ====================================================== # 
    # ======== Welcome To Emergency Room System ======== #
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
                    result = timedelta(seconds=sum(map(lambda f: int(f[0])*3600 + int(f[1])*60 + int(f[2]), map(lambda f: f.split(':'), times)))/len(times))
                    print("The average waiting time for the emergency room is: ", str(result))
                    compare_datetime_object = datetime.strptime('1:00:00', '%H:%M:%S')
                    delta=timedelta(hours=compare_datetime_object.hour, minutes=compare_datetime_object.minute, seconds=compare_datetime_object.second)
                    if (result>delta):
                        print ("""Your average waiting time is higher than the standard set for the hospital, here are some useful tips on how how you can reduce the waiting time for your patients.

You should schedule surgeries and other non-life-threatening procedures on days where the hospital’s less likely to have a spike in patient volume due to a busy evening in the Emergency Department.

Make reducing wait times a part of your hospital’s culture. Healthcare executives must make wait times a priority in their facility. This means they must implement specific policies designed to address problems that can lead to increased wait times, including staffing policies. They must also commit to regularly evaluating their hospitals’ workflow and be willing to invest in solutions to speed up care delivery, including automated systems designed to streamline scheduling.

Consider alternate methods of care delivery. To ease the burden of high wait times, your hospitals can try treating patients in various ways. Telemedicine may be one solution for the emergency room patients with less serious issues. Your hospital may also partner directly with nearby urgent care clinics and other healthcare entities so they can provide patients with an alternative to the emergency department to lower their wait time.""")
                    else:
                        print ("The average waiting time for your emergency room is lower than the standard set for the hospital. Keep up the good work!")
                        

                else:
                    print("That is an invalid input, please read the instructions and try again ")
                    break
        
            
            else: 
                print("The password you entered is incorrect")
            
            
            
           
    else:
        pass
    restart = input("Would you like to start again? Type 'yes' or 'no' ").lower()
    if restart=="yes":
        emergencyroomsystem()
    else:
        exit()
emergencyroomsystem()
