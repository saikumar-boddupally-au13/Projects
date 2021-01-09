
import time
import datetime
current_date_time= datetime.datetime.now()

class vehicle_Parking:
    
    def __init__(self):
        pass

    def creating_parking_slots(self, create_parking_lot):# Method for creating parking slots
        
        for i in range(1, (create_parking_lot)+1):
            if i not in dicti:
                dicti['slot_'+str(i)]="a"
        print("Created a parking lot with", create_parking_lot, "slots")

    
    def parking_vehicle_at_slots(self, vehicle_for_parking):#Method for parking vehicle in the slot
        
        checking_parking_lot_is_full=0
        
        for i in range(1, (create_parking_lot)+1):
            checking_parking_lot_is_full+=1
            
            checking_given_car_in_parking_lot= 0
            for keys, values in dicti.items():
                if vehicle_for_parking[0] in values:
                    checking_given_car_in_parking_lot+=1
                    break
            

            if checking_given_car_in_parking_lot == 1:
                    print("Car already in parking slot, recheck your entry")
                    break
            
            if checking_given_car_in_parking_lot != 1:
                if dicti["slot_"+str(i)]=="a":
                    
                    dicti["slot_"+str(i)]=vehicle_for_parking
                    print("Allocated slot number:", i,"on",current_date_time.strftime('%d-%m-%Y'),current_date_time.strftime("%H:%M"))
                    # print(dicti)
                    break
            
            if checking_given_car_in_parking_lot!= 1:    
                if checking_parking_lot_is_full==create_parking_lot:
            
                        print("Sorry, parking lot is full")

        
    def Leaving_vehicle_from_parking_lot(self,Leave): #Method to leave the parked Vehicle
        dicti['slot_'+str(Leave)]="a"
        print("Slot number",Leave,"is free")


    def get_status_of_the_vehicle_in_parking_lot(self): # Method to check status of the parking lot
        print("This data as on:",current_date_time.strftime('%d-%m-%Y'),current_date_time.strftime("%H:%M"))
        print("Slot No. || Registration No || Colour")
        for keys,values in dicti.items():
            if values != "a":
                print(keys[5:] ,  values[0]  , values[1])
            

    def get_registration_numbers_for_cars_with_colour(self,colour): #Method to return the Vehicle registration no. from with colour
        str=""
        for keys, values in dicti.items():
            if colour in values:
                str+=values[0]+", "
        
        print(str[:-2])
        

    def get_slot_numbers_for_cars_with_colour(self,colour):#Method to return the allotted slot number for vehicle from colour
        str=""
        for keys,values in dicti.items():
            if colour in values:
                str+=keys[5:]+", "
        print(str[:-2])
        


    def get_slot_number_for_registration_number(self,registration_number):# Method to get the slot number from registration number
        for keys,values in dicti.items():
            if registration_number in values:
                return (keys[5:])
        else:
            return ("Not found")
    

    def show_line(self,user_input): # Method to take the input from user and functions based on the user_input
        user_input=user_input.split()
        
        
        if "create_parking_lot" in user_input:
            
            global create_parking_lot
            create_parking_lot=int(user_input[-1])
            parking.creating_parking_slots(create_parking_lot)
        
        
        if "park" in user_input:
            
            vehicle_for_parking= user_input[1]+" "+user_input[2]
            vehicle_for_parking=vehicle_for_parking.split()
            parking.parking_vehicle_at_slots(vehicle_for_parking)


        if "leave" in user_input:
            
            Leave = user_input[1]
            parking.Leaving_vehicle_from_parking_lot(Leave)

        
        if "status" in user_input:
            parking.get_status_of_the_vehicle_in_parking_lot()

        
        if "registration_numbers_for_cars_with_colour" in user_input:
            colour= user_input[-1]
            parking.get_registration_numbers_for_cars_with_colour(colour)

        
        if "slot_numbers_for_cars_with_colour" in user_input:
            colour=user_input[-1]
            parking.get_slot_numbers_for_cars_with_colour(colour)


        if "slot_number_for_registration_number" in user_input:
            registration_number = user_input[-1]
            parking.get_slot_number_for_registration_number(registration_number)
            print(parking.get_slot_number_for_registration_number(registration_number))


def main():
    
    global dicti
    dicti=dict()
    print("\n")
    print("---- ISSUANCE OF TICKET THROUGH AUTOMATED PARKING LOT SYSTEM ----")
    
    print("\n")
    time.sleep(2)
    print("Loading...............................")
    time.sleep(1)
    print("\n")
    user_input=input("How do you want to give input as - manual_input or stored_file ?: ")
    
    print("\n")
    if "manual_input" in user_input.lower():
        
        while True:
            print("******************************")
            user_input=input("Enter your request: ")
            if user_input=="exit":
                print("Thank you for using the AUTOMATED PARKING LOT SYSTEM!")
                print("\n")
                break
            parking.show_line(user_input)

    if "file" in user_input.lower():
   
        with open("E:\python-project-saikumar-boddupally-au9\input.txt","r") as f:
            for line in f:
                user_input=line
                parking.show_line(user_input)
            print("Thank you for using the AUTOMATED PARKING LOT SYSTEM!")


if __name__ == "__main__":
    
    
    parking= vehicle_Parking()
    main()

