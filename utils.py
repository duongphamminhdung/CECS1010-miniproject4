class AirlineSystem:
    def __init__(self):
        pass    


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
    def display(self):
        return self.flight_number, self.destination, self.departure_time, self.available_seats
    def __str__(self):
        return self.flight_number, self.destination, self.departure_time, self.available_seats

    
class Passenger(AirlineSystem):
    def __init__(self, name, age, passport_number, reserv=None):
        super().__init__()
        self.name = name
        self.age = age
        self.passport_number = passport_number
        self.reservation = reserv
        
        
class Reservation(AirlineSystem):
    def __init__(self, flight, seat_number, res_id):
        super().__init__()
        self.flight_number = flight
        self.seat_number = seat_number
        self.res_id = res_id

    def cancel(self):
        self.flight[self.seat_number[0], self.seat_number[1]] = 0
        