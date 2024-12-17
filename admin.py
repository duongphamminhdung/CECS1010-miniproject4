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
    