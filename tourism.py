from passenger import Passenger
from invalid_place_exception import InvalidPlaceException

class Tourism:
    def __init__(self):
        self.__passenger_list = []
    
    def get_passenger_list(self):
        return self.__passenger_list
    
    def set_passenger_list(self, passenger_list):
        self.__passenger_list = passenger_list
    
    def validate_place_name(self, place):
        valid_places = ["Beach", "Pilgrimage", "Heritage", "Hill Station", "Water Falls", "Adventures"]
        if place not in valid_places:
            raise InvalidPlaceException("Invalid Place Name")
        return True
    
    def add_passenger_details(self, passenger_name, place, no_of_days, no_of_tickets):
        passenger = Passenger()
        passenger.set_passenger_name(passenger_name)
        passenger.set_place(place)
        passenger.set_no_of_days(no_of_days)
        passenger.set_no_of_tickets(no_of_tickets)
        bill_amount = passenger.calculate_bill_amount(place)
        passenger.set_bill_amount(bill_amount)
        self.__passenger_list.append(passenger)
    
    def view_passenger_details(self, place):
        matching_passengers = [p for p in self.__passenger_list if p.get_place() == place]
        return matching_passengers
