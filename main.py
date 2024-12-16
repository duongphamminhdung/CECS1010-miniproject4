from utils import Passenger, Flight, Reservation
import tkinter as tk
from tkinter import messagebox, Scrollbar
import sys
import json

        
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


def display_flight_details(passport_number):
    # Clear the main window
    for widget in root.winfo_children():
        widget.destroy()

    reservation = reservations[passport_number]
    details_frame = tk.Frame(root, padx=10, pady=10)
    details_frame.pack(padx=10, pady=10, fill="both", expand=True)

    tk.Label(details_frame, text="Reservation Details", font=("Arial", 16)).pack(pady=10)
    tk.Label(details_frame, text=f"Reservation ID: {reservation.res_id}").pack(pady=5)
    seat = str(reservation.seat_number[0]+1)+alphabet[reservation.seat_number[1]] 
    flight_info = f"Flight: {reservation.flight_number}, Seat: {seat}, Departure time: {flights[reservation.flight_number].departure_time}"
    tk.Label(details_frame, text=flight_info).pack(pady=5)
    tk.Button(details_frame, text="Cancel", command=lambda p=passport_number: cancel_reservation(p)).pack(side="right")
    tk.Button(details_frame, text="Back", command=sign_in_sign_up).pack(side="left")

    # tk.Button(details_frame, text="Exit", command=window_exit).pack(pady=10)

def cancel_reservation(passport_number):
    cancel = messagebox.askyesno("Exit?", f"Are you sure you want to cancel reservation {reservations[passport_number].res_id}?")
    if cancel:
        passengers[passport_number].reservation = None
        data['passengers'][passport_number]['reservation'] = None
        seat = reservations[passport_number].seat_number
        flights[reservations[passport_number].flight_number].available_seats[seat[0]][seat[1]] = 0
        messagebox.showinfo("Cancel", f"Cancelation of reservation {reservations[passport_number].res_id} complete")
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
    root.config(height=buttons[0][0].winfo_height()*(row), width=buttons[0][0].winfo_width()*(col))
    # print(buttons[0][0].winfo_height()*(row), buttons[0][0].winfo_width()*(col))

def display_flight_board(passport_number):
    # Clear the main window
    for widget in root.winfo_children():
        widget.destroy()

    if passengers[passport_number].reservation:
        display_flight_details(passport_number)
    else:
        # Display flight data board with reservation option
        flight_board_frame = tk.Frame(root, padx=10, pady=10)
        flight_board_frame.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Label(flight_board_frame, text="Flight Data Board", font=("Arial", 16)).pack(pady=10)

        def reserve_flight(flight_number):
            choose_seat(flight_number, passport_number)

        for flight_number, flight in flights.items():
            flight_info = f"Flight: {flight.flight_number}, Destination: {flight.destination}, Time: {flight.departure_time}"
            frame = tk.Frame(flight_board_frame)
            frame.pack(pady=2, fill="x")
            tk.Label(frame, text=flight_info).pack(side="left")
            tk.Button(frame, text="Reserve", command=lambda f=flight.flight_number: reserve_flight(f)).pack(side="right")

        tk.Button(flight_board_frame, text="Exit", command=window_exit).pack(pady=10)

def sign_in(passport_number):

    if passport_number:
        if passport_number in passport_numbers:
            messagebox.showinfo("Sign In", f"Welcome back! {passengers[passport_number].name}")
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

    sign_in_button = tk.Button(sign_in_frame, text="Sign In", command=lambda: sign_in(    passport_number = sign_in_passport_number.get()))
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
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    filename = "data.json"
    with open(filename) as f:
        data = json.load(f)
    # print(data)
    # print(data['passengers'])
    reservations = {}
    for i, r in data['reservations'].items():
        reservations[i] = Reservation(r['flight_number'], r['seat_number'], r['res_id'])
    passengers = {}
    for n, i in data['passengers'].items():
        passengers[n] = Passenger(i['name'], i['age'], i['passport_number'], i['reservation'])
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
    