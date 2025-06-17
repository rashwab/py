from collections import defaultdict
import sys
ddict=defaultdict(list)
ddict= {}

def parking_car():
    while True:
     print("Welcome to the parking system!")
 
    # Gets the license plate number
     license_plate = input("Enter your license plate number: ") 
     if len(license_plate) != 7:  # Check if the license plate is exactly 7 characters
        print("License plate number must be exactly 7 characters.")


        if license_plate in ddict: 
          print ("Number already in use")
        break
     else:
    # Gets the duration of stay
      how_long = input("How long do you plan on staying for (in minutes)? Time above 1 hour minutes will charge more: ")
    

     # Validate the duration input
     if not how_long.isdigit() or int(how_long) <= 0:  # Check if input is a positive integer
        print("Invalid time. Please enter a positive number.")
        sys.exit()
    
    
     how_long = int(how_long)
    
     if how_long > 1440:  # Check if the duration exceeds 24 hours
        print("Cannot be more than 24 hours (1440 minutes).")
        sys.exit()
    
     print("Thank you for your input.")
    
    # Assign a parking slot
     slot = len(ddict) + 1 
     ddict[f"slot{slot}"] = license_plate
    
     time= len(ddict)
     ddict[f"Time{time}"]=how_long
           #using the dictionary to add time to the dictonary so its slot number license and time 
     # Print the parking slots
     print(f"Assigned {f'slot{slot}'} to {license_plate}.")
     print("\nCurrent Parking Slots:")
     for slot, license_plate in ddict.items():
        print(f"{slot}: {license_plate}")


def remove_car():
 slot_number=input("What is your slot number: ")
 time = input("How long did you stay for")
 total= time 
 if total == "60":
  print ("") 
 if slot_number in ddict:
   del ddict[slot_number]
   
   if time in ddict:
     print("Your total is{total} ")
   print (ddict)
      #using the dictionary to add anothing

while True:
 options= input("""Chose your option
               1.Enter for a slot
               2.Leave a slot 
               3. Check All slots 
               4.Exit""")
      #options menu makes it easily accessible 
 if options== "1":
    parking_car()

 elif options =="2":
    remove_car()
 elif options =="3":
  print (ddict)
 elif options =="4":


    False
    sys.exit
          #Allows to choose what number needs to be picked for the option
