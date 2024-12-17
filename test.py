import os
import sys
import tkinter as tk
from tkinter import messagebox, Scrollbar
import sys
import json

class AirlineSystem:
    def __init__(self):
        pass
    def __str__(self):
        return "This is the parent class AirlineSystem"


class Flight(AirlineSystem):
    def __init__(self, flight_number, destination, departure_time, rows=None, cols=None, avai=None):
        super().__init__()
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        if avai:
            self.available_seats = avai
        else:
            self.available_seats = [[0]*cols]*rows
        self.passengers = []

class Passenger(AirlineSystem):
    def __init__(self, name, age, passport_number, reserv=None):
        super().__init__()
        self.__name = name
        self.__age = age
        self.__passport_number = passport_number
        self.reservation = reserv
        
    def get_passport_number(self):
        return self.__passport_number
    def set_passport_number(self, new):
        self.__passport_number = new
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    
      
class Reservation(AirlineSystem):
    def __init__(self, flight, seat_number, res_id):
        super().__init__()
        self.flight_number = flight
        self.seat_number = seat_number
        self.__res_id = res_id


    def get_res_id(self):
        return self.__res_id
    
if os.path.isfile('json.data'):
    with open('json.data', 'r') as f:
        data = json.load(f)
    reservations = {}
    for i, r in data['reservations'].items():
        reservations[i] = Reservation(r['flight_number'], r['seat_number'], r['_Reservation__res_id'])
    passengers = {}
    for n, i in data['passengers'].items():
        passengers[n] = Passenger(i['_Passenger__name'], i['_Passenger__age'], i['_Passenger__passport_number'], i['reservation'])
    passport_numbers = [i for i in passengers.keys()]
    flights = {}
    for n, f in data['flights'].items():
        flights[n] = Flight(f['flight_number'], f['destination'], f['departure_time'], avai=f['available_seats'])
else:
    ## this is sample data for the program, please colapse it
    data = {
	"passengers": {
		"234": {
			"_Passenger__name": "234",
			"_Passenger__age": 234,
			"_Passenger__passport_number": "234",
			"reservation": None
		},
		"4567485": {
			"_Passenger__name": "fdgh",
			"_Passenger__age": 56,
			"_Passenger__passport_number": "4567485",
			"reservation": "KS000002"
		},
		"35745674": {
			"_Passenger__name": "sdfgdfg",
			"_Passenger__age": 43,
			"_Passenger__passport_number": "35745674",
			"reservation": "KS000003"
		},
		"209384029384": {
			"_Passenger__name": "kjsadfjk",
			"_Passenger__age": 23,
			"_Passenger__passport_number": "209384029384",
			"reservation": None
		}
	},
	"passport_numbers": [
		"234",
		"4567485"
	],
	"flights": {
		"AA123": {
			"flight_number": "AA123",
			"destination": "New York",
			"departure_time": "10:00 AM",
			"available_seats": [
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					1
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				]
			]
		},
		"BA456": {
			"flight_number": "BA456",
			"destination": "London",
			"departure_time": "12:00 PM",
			"available_seats": [
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					1,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				]
			]
		},
		"CA789": {
			"flight_number": "CA789",
			"destination": "Toronto",
			"departure_time": "02:00 PM",
			"available_seats": [
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0
				]
			]
		},
		"VN2345": {
			"flight_number": "VN2345",
			"destination": "Vietnam",
			"departure_time": "13:45 PM",
			"available_seats": [
				[
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0,
					0
				]
			],
			"passengers": []
		}
	},
	"reservations": {
		"4567485": {
			"flight_number": "AA123",
			"seat_number": [
				3,
				5
			],
			"_Reservation__res_id": "KS000002"
		},
		"35745674": {
			"flight_number": "BA456",
			"seat_number": [
				7,
				2
			],
			"_Reservation__res_id": "KS000003"
		}
	}
}

if __name__ == '__main__':
    mode = 0
    if len(sys.argv) < 2:
            print('''Please choose mode 
    1. User Interface for passenger (view flight, reserve flight, cancel flight)
    2. User Interface for admin (add flight, view passengers)
    3. Prompt interact for passenger
                
    Enter 1, 2 or 3 to choose
                ''')
            mode = input()
    else:
        mode = sys.argv[1]
    
    if mode == '1':
        pass
    elif mode == '2':
        pass
    elif mode == '3':
        pass
    else:
        print("Please rerun the program and choose an appropriate mode")
