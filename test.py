import tkinter as tk
from tkinter import messagebox, Scrollbar, PhotoImage
import os, sys
import json
import base64

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
			"reservation": null
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
			"reservation": null
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
		},
		"KS20394": {
			"flight_number": "KS20394",
			"destination": "VinUni",
			"departure_time": "12:34 PM",
			"available_seats": [
				[
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0
				],
				[
					0,
					0,
					0,
					0
				],
				[
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
        def update_data(action:str = None, d: dict= None):
            if action == 'add':
                for key, val in d.items():
                    if key == 'passengers':
                        for j in val.keys():
                            
                            data[key][j] = val[j]
                    if key == 'reservations':
                        for j in val.keys():
                            data[key][j] = val[j]
            elif action == 'remove':
                for key, val in d.items():
                    if key == 'passengers':
                        data[key].remove(val)
                    if key == 'reservations':
                        for j in val.keys():
                            del data[key][j]

        def pay(passport_number):
            for widget in root.winfo_children():
                widget.destroy()
            paying_frame = tk.Frame(root, padx=10, pady=10).pack()
            if reservations[passport_number].seat_number[0] <= 6:
                price = '$400 ~ 10.000.000 VND'
            else:
                price = '$200 ~ 5.000.000 VND'
            tk.Label(paying_frame, text="Price", font=("Arial", 14)).pack(padx=14,pady=10)
            tk.Label(paying_frame, text=price, font=("Arial", 16)).pack(padx=14,pady=10)
            tk.Label(paying_frame, text='20577267 ACB', font=("Arial", 20)).pack(padx=14,pady=10)
            if qr_img:
                tk.Label(paying_frame, image=qr_img).pack()
            tk.Label(paying_frame, text='Please include your Reservation ID in your tranfer', font=("Arial", 16)).pack(padx=14,pady=10)
            
            tk.Button(paying_frame, text="Back", command=lambda p=passport_number:display_flight_details(p)).pack(side = 'right')


        def display_flight_details(passport_number):
            # Clear the main window
            for widget in root.winfo_children():
                widget.destroy()

            reservation = reservations[passport_number]
            details_frame = tk.Frame(root, padx=10, pady=10)
            details_frame.pack(padx=10, pady=10, fill="both", expand=True)

            tk.Label(details_frame, text="Reservation Details", font=("Arial", 16)).pack(pady=10)
            tk.Label(details_frame, text=f"Reservation ID: {reservation.get_res_id()}").pack(pady=5)
            seat = str(reservation.seat_number[0]+1)+alphabet[reservation.seat_number[1]] 
            flight_info = f"Flight: {reservation.flight_number}, Seat: {seat}, Departure time: {flights[reservation.flight_number].departure_time}"
            tk.Label(details_frame, text=flight_info).pack(pady=5)
            
            # Btns = tk.Label(root).pack()
            tk.Button(details_frame, text="Back", command=sign_in_sign_up).pack(side = 'left')
            tk.Button(details_frame, text="Cancel", command=lambda p=passport_number: cancel_reservation(p)).pack(side='left')
            tk.Button(details_frame, text="Pay", command=lambda p=passport_number:pay(p)).pack(side='right')

            # tk.Button(details_frame, text="Exit", command=window_exit).pack(pady=10)

        def cancel_reservation(passport_number):
            cancel = messagebox.askyesno("Exit?", f"Are you sure you want to cancel reservation {reservations[passport_number].get_res_id()}?")
            if cancel:
                passengers[passport_number].reservation = None
                data['passengers'][passport_number]['reservation'] = None
                seat = reservations[passport_number].seat_number
                flights[reservations[passport_number].flight_number].available_seats[seat[0]][seat[1]] = 0
                messagebox.showinfo("Cancel", f"Cancelation of reservation {reservations[passport_number].get_res_id()} complete")
                del reservations[passport_number]
                del data['reservations'][passport_number]
                sign_in_sign_up()
            


        def choose_seat(flight_number, passport_number):
            # Clear the main window
            for widget in root.winfo_children():
                widget.destroy()

            flight = flights[flight_number]
            available_seats = flight.available_seats

            seat_frame = tk.Frame(root, padx=10, pady=10)
            seat_frame.pack(padx=10, pady=10, side=tk.LEFT, fill="both", expand=True)
            # seat_frame.grid(row=0, column=0)
            # scrollbar = Scrollbar(root)
            # scrollbar.pack( side = tk.RIGHT, fill='y')
            
            tk.Label(seat_frame, text="Choose Your Seat", font=("Arial", 16))

            def select_seat(row, col):
                res_id = f"KS{'0'*(6-len(str(len(reservations)+1)))}{len(reservations)+1}"
                reservations[passport_number] = Reservation(flight_number, [row, col], res_id)
                passengers[passport_number].reservation = res_id
                data['passengers'][passport_number]['reservation'] = res_id
                # print(reservations[passport_number].__dict__)
                update_data('add', {'reservations':{ passport_number:
                    reservations[passport_number].__dict__
                }})
                # print(flights[flight_number].__dict__)
                flights[flight_number].available_seats[row][col] = 1
                data['flights'][flight_number]['available_seats'][row][col] = 1
                seat = str(row+1)+alphabet[col]
                messagebox.showinfo("Seat Selected", f"You have selected seat {seat}.")
                display_flight_details(passport_number)
            def already():
                messagebox.showinfo("Seat Selected", "This seat is not available, please chooose another")
            buttons = []
            for row in range(len(available_seats)):
                buttons.append([])
                for col in range(len(available_seats[row])):
                    seat = str(row+1)+alphabet[col]
                    if available_seats[row][col] == 0:
                        buttons[-1].append(tk.Button(seat_frame, text=seat, command=lambda s=[row, col]: select_seat(s[0], s[1])))
                    # else:
                        # buttons[-1].append(tk.Button(seat_frame, text=seat, command=already, bg='blue'))
                    buttons[-1][-1].grid(row=row, column=col, sticky='news')
                # rows.pack(fill=tk.BOTH, expand=tk.TRUE)
            back_btn = tk.Button(root, text="Back", command=lambda s=passport_number: display_flight_board(s))
            back_btn.pack()
            root.config(height=buttons[0][0].winfo_height()*(row), width=buttons[0][0].winfo_width()*(col))
            # print(buttons[0][0].winfo_height()*(row), buttons[0][0].winfo_width()*(col))

        def display_flight_board(passport_number, fil=None):
            # Clear the main window
            for widget in root.winfo_children():
                widget.destroy()

            if passengers[passport_number].reservation:
                display_flight_details(passport_number)
            else:
                if fil:
                    print(fil)
                # Display flight data board with reservation option
                flight_board_frame = tk.Frame(root, padx=10)
                flight_board_frame.pack(padx=10, fill="both", expand=True)

                tk.Label(flight_board_frame, text="Flight Data Board", font=("Arial", 16)).pack(pady=10)

                def reserve_flight(flight_number):
                    choose_seat(flight_number, passport_number)
                filt_entr = tk.Entry(root, width=30)
                filt_entr.pack(side='left', padx=10, pady=10)
                filt_button = tk.Button(root, text="Filter", command= lambda: display_flight_board(passport_number, filt_entr.get())).pack(side='right', padx=10, pady=10)
                num = 0
                for flight_number, flight in flights.items():
                    if fil and fil not in flight.destination:
                        continue
                    flight_info = f"Flight: {flight.flight_number}, Destination: {flight.destination}, Time: {flight.departure_time}"
                    frame = tk.Frame(flight_board_frame)
                    frame.pack(pady=2, fill="x")
                    tk.Label(frame, text=flight_info).pack(side="left")
                    tk.Button(frame, text="Reserve", command=lambda f=flight.flight_number: reserve_flight(f)).pack(side="right")
                    num += 1
                if num == 0:
                    tk.Label(frame, text="No flight to your destination.").pack(side="left")

                tk.Button(flight_board_frame, text="Exit", command=window_exit).pack(pady=10)

        def sign_in(passport_number):

            if passport_number:
                if passport_number in passport_numbers:
                    messagebox.showinfo("Sign In", f"Welcome back! {passengers[passport_number].get_name()}")
                    display_flight_board(passport_number)
                else:
                    messagebox.showerror("Error", "This ID has not been registered.")
            else:
                messagebox.showerror("Error", "Please enter your Passport ID to sign in.")

        def sign_up(name, age, passport_number):

            if name and age and passport_number:
                print(age)
                try:
                    age = int(age)
                    new_p = Passenger(name, age, passport_number)
                    print(new_p.__dict__)
                    update_data('add', {'passport_numbers':passport_number, 'passengers':{passport_number: new_p.__dict__}})
                    passport_numbers.append(passport_number)
                    messagebox.showinfo("Sign Up", f"Sign Up Successful!\nName: {name}\nAge: {age}\nPassport ID: {passport_number}")
                    passengers[passport_number] = new_p
                except ValueError as e:
                    print(e)
                    messagebox.showerror("Error", "Age must be a number.")
                for widget in root.winfo_children():
                    widget.destroy()
                sign_in_sign_up()
            else:
                messagebox.showerror("Error", "Please fill out all fields to sign up.")


        # Create the main window
        root = tk.Tk()
        # root.geometry("500x500")

        root.title("Sign In or Sign Up")
        def sign_in_sign_up():
            root.config(width=400, height=450)
            for widget in root.winfo_children():
                widget.destroy()
            # Sign In Frame
            sign_in_frame = tk.LabelFrame(root, text="Sign In", padx=10, pady=10)
            sign_in_frame.pack(padx=10, pady=10, fill="x")

            sign_in_label = tk.Label(sign_in_frame, text="Passport ID:")
            sign_in_label.grid(row=0, column=0, sticky="w")

            sign_in_passport_number = tk.Entry(sign_in_frame, width=30)
            sign_in_passport_number.grid(row=0, column=1, padx=5, pady=5)

            sign_in_button = tk.Button(sign_in_frame, text="Sign In", command=lambda: sign_in(passport_number = sign_in_passport_number.get()))
            sign_in_button.grid(row=1, column=0, columnspan=2, pady=5)

            # Sign Up Frame
            sign_up_frame = tk.LabelFrame(root, text="Sign Up", padx=10, pady=10)
            sign_up_frame.pack(padx=10, pady=10, fill="x")

            sign_up_name_label = tk.Label(sign_up_frame, text="Name:")
            sign_up_name_label.grid(row=0, column=0, sticky="w")

            sign_up_name = tk.Entry(sign_up_frame, width=30)
            sign_up_name.grid(row=0, column=1, padx=5, pady=5)

            sign_up_age_label = tk.Label(sign_up_frame, text="Age:")
            sign_up_age_label.grid(row=1, column=0, sticky="w")

            sign_up_age = tk.Entry(sign_up_frame, width=30)
            sign_up_age.grid(row=1, column=1, padx=5, pady=5)

            sign_up_passport_number_label = tk.Label(sign_up_frame, text="Passport ID:")
            sign_up_passport_number_label.grid(row=2, column=0, sticky="w")

            sign_up_passport_number = tk.Entry(sign_up_frame, width=30)
            sign_up_passport_number.grid(row=2, column=1, padx=5, pady=5)

            sign_up_button = tk.Button(sign_up_frame, text="Sign Up", command=lambda :sign_up(name = sign_up_name.get(), age = sign_up_age.get(), passport_number = sign_up_passport_number.get()))

            sign_up_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Run the application
        try:
            if os.path.isfile('qr.png'):
                qr_img = PhotoImage(file='qr.png').subsample(4)
            else:
                qr_img = None
            alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            filename = "data.json"
            with open(filename) as f:
                data = json.load(f)
            # print(data)
            # print(data['passengers'])
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
            sign_in_sign_up()
            print(reservations)
            print(passport_numbers)
            print(passengers)
            def window_exit():
                close = messagebox.askyesno("Exit?", "Are you sure you want to exit?")
                if close:
                    root.destroy()
                    root.quit()
                    # print(data)
                    with open(filename, "w") as f:
                        json.dump(data, f)

            root.protocol("WM_DELETE_WINDOW", window_exit)

            root.mainloop()
        except KeyboardInterrupt:
            with open(filename, "w") as f:
                json.dump(data, f)
            print("catch Keyboard Interrupt")
            pass
    elif mode == '2':
        def update_data(action:str = None, d: dict= None):
            if action == 'add':
                for key, val in d.items():
                    if key == 'passengers':
                        for j in val.keys():
                            
                            data[key][j] = val[j]
                    if key == 'reservations':
                        for j in val.keys():
                            data[key][j] = val[j]
            elif action == 'remove':
                for key, val in d.items():
                    if key == 'passengers':
                        data[key].remove(val)
                    if key == 'reservations':
                        for j in val.keys():
                            del data[key][j]

        def create_new_fl(num, dest, time, row, col):
            if num and dest and time and row and col:
                try:
                    row = int(row)
                    col = int(col)
                    if ':' not in time or ('AM' not in time and "PM" not in time):
                        messagebox.showerror("Error", "Please enter an appropriate time.")
                    else:
                        new_f = Flight(num, dest, time, row, col)
                        data['flights'][num] = new_f.__dict__
                        flights[num] = new_f
                        display_flight_board()
                except ValueError as e:
                    print(e)
                    messagebox.showerror("Error", "Number of Row and column must be a number.")
            else:
                messagebox.showerror("Error", "Please fill out all fields to add a new flight.")

        def add_flight():
            for widget in root.winfo_children():
                widget.destroy()
            
            add_flight = tk.LabelFrame(root, text="Add a new flight", padx=10, pady=10)
            add_flight.pack(padx=10, pady=10, fill="x")

            flight_num_label = tk.Label(add_flight, text="Flight number:")
            flight_num_label.grid(row=0, column=0, sticky="w")

            flight_num_entr = tk.Entry(add_flight, width=30)
            flight_num_entr.grid(row=0, column=1, padx=5, pady=5)

            flight_dest = tk.Label(add_flight, text="Destination:")
            flight_dest.grid(row=1, column=0, sticky="w")

            flight_dest_entr = tk.Entry(add_flight, width=30)
            flight_dest_entr.grid(row=1, column=1, padx=5, pady=5)

            filght_depart_time = tk.Label(add_flight, text="Departure time:")
            filght_depart_time.grid(row=2, column=0, sticky="w")

            filght_depart_time_entr = tk.Entry(add_flight, width=30)
            filght_depart_time_entr.grid(row=2, column=1, padx=5, pady=5)

            row_col = tk.LabelFrame(root, text='Number of rows and columns in the plane')
            # row_col.grid(row=3, column=0)
            row_col.pack()
            
            row = tk.Label(row_col, text="# rows:")
            row.grid(row=0, column=0, sticky="w")
            
            col = tk.Label(row_col, text="# cols:")
            col.grid(row=0, column=2, sticky="w")

            row_entr = tk.Entry(row_col, width=15)
            row_entr.grid(row=0, column=1, padx=5, pady=5)

            col_entr = tk.Entry(row_col, width=15)
            col_entr.grid(row=0, column=3, padx=5, pady=5)
            
            add_fl = tk.Button(row_col, text="Add!", command=lambda :create_new_fl(num=flight_num_entr.get(), 
                                                                        dest=flight_dest_entr.get(), 
                                                                        time=filght_depart_time_entr.get(), 
                                                                        row=row_entr.get(), 
                                                                        col=col_entr.get()))
            add_fl.grid(row=1, column=3, columnspan=2, pady=5)


            # tk.Button(details_frame, text="Exit", command=window_exit).pack(pady=10)

        def view_passenger_on_flight(flight_number):
            for widget in root.winfo_children():
                widget.destroy()
            passenger_board = tk.Frame(root, padx=10, pady=10)
            passenger_board.pack(padx=10, pady=10, fill="both", expand=True)
            num = 0
            for passport_number, resv in reservations.items():
                if resv.flight_number == flight_number:
                    num += 1
                    p = passengers[passport_number]
                    row, col = resv.seat_number
                    seat = str(row+1)+alphabet[col]
                    passenger_inf4 = f"Seat {seat}, Passenger name: {p.get_name()}, Age: {p.get_age()}"
                    frame = tk.Frame(passenger_board)
                    frame.pack(pady=2, fill="x")
                    tk.Label(frame, text=passenger_inf4).pack(side="left")
            if num == 0:
                passenger_inf4 = f"There are no passenger on this flight"
                frame = tk.Frame(passenger_board)
                frame.pack(pady=2, fill="x")
                tk.Label(frame, text=passenger_inf4).pack(side="left")
            tk.Button(root, text="Back", command=display_flight_board).pack(pady=10)

        def display_flight_board():
            # Clear the main window
            for widget in root.winfo_children():
                widget.destroy()

            # Display flight data board with reservation option
            flight_board_frame = tk.Frame(root, padx=10, pady=10)
            flight_board_frame.pack(padx=10, pady=10, fill="both", expand=True)

            tk.Label(flight_board_frame, text="Flight Data Board", font=("Arial", 16)).pack(pady=10)

            for flight_number, flight in flights.items():
                flight_info = f"Flight: {flight.flight_number}, Destination: {flight.destination}, Time: {flight.departure_time}"
                frame = tk.Frame(flight_board_frame)
                frame.pack(pady=2, fill="x")
                tk.Label(frame, text=flight_info).pack(side="left")
                tk.Button(frame, text="View", command=lambda f=flight.flight_number: view_passenger_on_flight(f)).pack(side="right")
            
            tk.Button(flight_board_frame, text="Add", command=add_flight).pack(side="right")
            tk.Button(flight_board_frame, text="Exit", command=window_exit).pack(side='left')

        def sign_in(password):

            if password == 'ok':
                    messagebox.showinfo("Sign In", f"Welcome back! Admin")
                    display_flight_board()
            else:
                messagebox.showerror("Error", "Wrong password!")

        # Create the main window
        root = tk.Tk()
        # root.geometry("500x500")

        root.title("Administrator sign in")
        def admin_sign_in():
            # password for admin is Team17got15points
            root.config(width=400, height=450)
            for widget in root.winfo_children():
                widget.destroy()
            # Sign In Frame
            sign_in_frame = tk.LabelFrame(root, text="Sign In", padx=10, pady=10)
            sign_in_frame.pack(padx=10, pady=10, fill="x")

            sign_in_label = tk.Label(sign_in_frame, text="Admin password:")
            sign_in_label.grid(row=0, column=0, sticky="w")

            sign_in_password = tk.Entry(sign_in_frame, width=30)
            sign_in_password.grid(row=0, column=1, padx=5, pady=5)

            sign_in_button = tk.Button(sign_in_frame, text="Sign In", command=lambda: sign_in(password = sign_in_password.get()))
            sign_in_button.grid(row=1, column=0, columnspan=2, pady=5)

        # Run the application
        try:
            alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            filename = "data.json"
            with open(filename) as f:
                data = json.load(f)
            # print(data)
            # print(data['passengers'])
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
            print(reservations)
            print(passport_numbers)
            print(passengers)
            admin_sign_in()
            def window_exit():
                close = messagebox.askyesno("Exit?", "Are you sure you want to exit?")
                if close:
                    root.destroy()
                    root.quit()
                    # print(data)
                    with open(filename, "w") as f:
                        json.dump(data, f)

            root.protocol("WM_DELETE_WINDOW", window_exit)

            root.mainloop()
        except KeyboardInterrupt:
            with open(filename, "w") as f:
                json.dump(data, f)
            print("catch Keyboard Interrupt")
            
    elif mode == '3':
        pass
    else:
        print("Please rerun the program and choose an appropriate mode")
