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