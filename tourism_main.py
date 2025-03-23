from tourism import Tourism
from invalid_place_exception import InvalidPlaceException

def main():
    tourism = Tourism()
    
    n = int(input("Enter the number of registrations:\n"))
    
    for i in range(n):
        details = input(f"Enter the registration details {i+1}:\n").strip()
        passenger_name, place, no_of_days, no_of_tickets = details.split(":")
        
        try:
            if tourism.validate_place_name(place):
                tourism.add_passenger_details(
                    passenger_name, 
                    place, 
                    int(no_of_days), 
                    int(no_of_tickets)
                )
        except InvalidPlaceException as e:
            print("Invalid Place Name\n")
            continue
    
    search_place = input("Enter the Place that needs to be searched:\n")
    matching_passengers = tourism.view_passenger_details(search_place)
    
    if not matching_passengers:
        print("No Passengers found")
    else:
        for passenger in matching_passengers:
            print(f"Passenger Name {passenger.get_passenger_name()}")
            print(f"Number Of Days {passenger.get_no_of_days()}")
            print(f"Number Of Tickets {passenger.get_no_of_tickets()}")
            print(f"Bill Amount {passenger.get_bill_amount()}")

if __name__ == "__main__":
    main()
