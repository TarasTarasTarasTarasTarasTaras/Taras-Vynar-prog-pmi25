from Validation import Validation
from FlightBooking import FlightBooking
from AviaCompanyEnum import AviaCompanyEnum

class FlightBookingContainer(object):
    def __init__(self, filename):
        self.__filename = filename
        self.__array_of_elements = []


    def __str__(self):
        string = ''
        for i in self.__array_of_elements:
            string += str(i) + '\n' + '-'*50 + '\n'
        return string


    def readFromFile(self, filename = 'not specified'):
        if filename == 'not specified': filename = self.__filename
        filename = Validation.validate_file(filename)
        file = open(filename)

        self.__array_of_elements = []
        number = success = 0

        array_values = [] 
        for i in file:
            if i[0] == "=": continue
            i = i.split()
            array_values.append(i[1])
            
        array_values.reverse()

        while len(array_values) > 0:
            number += 1
            array_attr = []
            for i in range(len(FlightBooking.array_of_names)):
                array_attr.append(array_values.pop())
            try:
                flightBooking = FlightBooking(*array_attr)
            except ValueError as message:
                print(message)
                print(f"FlightBooking number {number} is defective")
                while len(array_values) > 0 and len(array_values) % len(FlightBooking.array_of_names) != 0:
                    array_values.pop()
                continue
            self.__array_of_elements.append(flightBooking)
            success += 1
        print(f"\n {success} objects were successfully read from the file: {value}")


    def theLargestNumberOfFlights(self):
        dictCompanies = {AviaCompanyEnum.QatarAirlines : 0, AviaCompanyEnum.Ryanair : 0, AviaCompanyEnum.SkyUp : 0, AviaCompanyEnum.Wizzair : 0}
    
        for i in len(self.__array_of_elements):
            if self.__array_of_elements[i].startTime == 2021:
                dictCompanies[self.__array_of_elements[i].aviaCompany] += 1
        
        max_flights = 0
        key = ''
        for _key in dictCompanies:
            if dictCompanies[_key] > max_flights:
                max_flight = dictCompanies[_key]
                key = _key

        file = open('maxFlights.txt')
        file.write(key + ' >> ' + max_flight)
        file.close()

        




