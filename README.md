# AUTOMATED PARKING LOT SYSTEM

## About the project
* Issuance of tickets for the parked vehicles in the alloted slots

## Reqirements of Vehicle to be parked:

* Registration number and colour of the Vehicle. 
* Slot number in which the Car has to be parked.

## About the code:
Automated Parking Slot project is done using Python Language. Recommended version is to use the latest python version (3.8) .

## Modules used:
* time
* datetime

## Methods(Functions)
* Create a Parking lot with n number of slots.

* Park the car in the available slot.

* Leave the parked car from the alloted slot.

* Status of the Parking lot. 


## How to run? 
This code can be executed in two modes
* Manual_mode: We can give required input manually through terminal 
* File_mode : It is difficult  always to enter the input for the user. So all the input is stored in a file and we can use the file for executing by just one click. 

## Giving Manual_input

To choose manual mode just we need to type ' manual_input '. So that it will ask you the input ( requests). 

### Commands used
The following are the commands in manual mode for getting the required output.

* create_parking_lot < size of lot > To create the parking lot with desired size.

Example: create_parking_lot 6

* park < REGISTRATION NUMBER > < COLOR >: To park a Vehicle by giving the registration number and colour of the vehicle.

Example: park KA-01-MM-0002 Red

* leave < SLOT NUMBER>: To remove a vehicle which was parked in a particular slot number.

Example: leave 3

* status: To get the status of the parking lot. 

Example: status
This data as on: 18-09-2020 13:02
Slot No. || Registration No || Colour"
The above output is when there are no vehicles parked.
## File mode

The file is passed in the code by providing the path(location) of the input file. Then code gets executed as per the text(commands) in the given file.
 
 



             


