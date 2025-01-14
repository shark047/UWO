"""
******************************
CS 1026 - Assignment 4 – Air Travel
Code by: Yiwei Dong
Student ID: ydong445
File created: December 4, 2024
******************************
This file is the main program for processing and querying airport and flight data.
"""


# You must create the Flight.py and Airport.py files.
from Flight import *
from Airport import *

# Define your collections for all_airports and all_flights here.

all_airports = []
all_flights = {}

def load_data(airport_file, flight_file):
    global all_airports, all_flights

    try:

        with open(airport_file, "r") as af:

            for line in af.readlines():

                """ This is my origin code and i had test 34 time to find something wrong with this part.
                line = line.strip()
                parts = line.split("-")
                code = parts[0].strip()
                city = parts[1].strip()
                country = parts[2].strip()
                """
                line = line.strip()
                parts = line.split("-")
                code = parts[0].strip()
                country = parts[1].strip() #it should be country at first and then is city!!!!
                city = parts[2].strip()

                all_airports.append(Airport(code, city, country)) #process row data and upload to airports[]

        with open(flight_file, "r") as ff:

            for line in ff.readlines():
                line = line.strip()
                parts = line.rsplit("-", 3)
                flight_no = parts[0].strip()
                origin_code = parts[1].strip()
                dest_code = parts[2].strip()
                duration = parts[3].strip()
                #get flight_no, origin_code, dest_code and duration form file

                #use raw data to find origin and destination airport
                origin = ""
                destination = ""

                for airport in all_airports:
                    if airport.get_code() == origin_code:
                        origin = airport
                    if airport.get_code() == dest_code:
                        destination = airport

                if origin and destination:
                    flight = Flight(flight_no, origin, destination, duration)
                    if origin_code not in all_flights:
                        all_flights[origin_code] = []
                    all_flights[origin_code].append(flight)

                #turn code to flight class

        return True
    
    except Exception as e:
        print(f"Error loading data: {e}")
        return False


def get_airport_by_code(code): #use code to find airport
    for airport in all_airports:
        if airport.get_code().upper() == code:
            return airport
    raise ValueError(f"No airport with the given code: {code}")


def find_all_city_flights(city):
    result = []
    for flight_list in all_flights.values():#find city in all flights information
        for flight in flight_list:
            if flight.get_origin().get_city() == city or flight.get_destination().get_city() == city:
                result.append(flight)
    return result


def find_all_country_flights(country):
    result = []
    for flight_list in all_flights.values():# find country in all flights information
        for flight in flight_list:
            if flight.get_origin().get_country() == country or flight.get_destination().get_country() == country:
                result.append(flight)
    return result


def find_flight_between(orig_airport, dest_airport):
    #find direct flight
    direct_flight = None
    if orig_airport.get_code() in all_flights:
        for flight in all_flights[orig_airport.get_code()]:
            if flight.get_destination() == dest_airport:
                direct_flight = flight
                break
    
    if direct_flight:
        return f"Direct Flight: {orig_airport.get_code()} to {dest_airport.get_code()}"

    # find connecting flight
    connecting_airports = set()
    if orig_airport.get_code() in all_flights: #find all flights from origin airport
        for flight in all_flights[orig_airport.get_code()]:
            connecting_airports.add(flight.get_destination().get_code()) #find all flights' destination from origin airports

    possible_connections = []
    for code in connecting_airports:
        if code in all_flights:
            for flight in all_flights[code]:#from all flight which is from origin airports can connected
                if flight.get_destination() == dest_airport:
                    possible_connections.append(flight.get_origin().get_code())

    if possible_connections:
        return set(possible_connections)

    # No flights found
    raise ValueError(f"There are no direct or single-hop connecting flights from {orig_airport.get_code()} to {dest_airport.get_code()}")



def shortest_flight_from(orig_airport):
    if orig_airport.get_code() not in all_flights:
        return None
    flight_list = all_flights[orig_airport.get_code()]
    shortest_flight = flight_list[0]
    for flight in flight_list:
        if flight.get_duration() < shortest_flight.get_duration():
            shortest_flight = flight
    return shortest_flight #find the duration is the smallest

def find_return_flight(first_flight):
    return_flights = all_flights.get(first_flight.get_destination().get_code(), [])
    for flight in return_flights:
        if flight.get_destination() == first_flight.get_origin(): #switch destination and origin
            return flight
    raise ValueError(f"There is no flight from {first_flight.get_destination().get_code()} to {first_flight.get_origin().get_code()}")


if __name__ == "__main__":
    pass