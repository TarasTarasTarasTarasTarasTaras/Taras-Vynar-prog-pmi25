from Validation import Validation

class FlightBooking(object):
    array_of_names = ['AviaCompany', 'NoOfPeople', 'StartTime', 'EndTime', 'Date', 'FlightNumber']

    def __init__(self, _aviaCompany, _noOfPeople, _startTime, _endTime, _date, _flightNumber):
        self.aviaCompany = self.aviaCompany(_aviaCompany)
        self.noOfPeople = self.noOfPeople(_noOfPeople)
        self.startTime = self.startTime(_startTime)
        self.endTime = self.endTime(_endTime)
        self.date = self.date(_date)
        self.flightNumber = self.flightNumber(_flightNumber)


    def __str__(self):
        string = ""
        for i in range(len(self.array_of_names)):
            string += self.array_of_names[i] + ": " + str(self.__getattribute__(self.array_of_names[i]))
            if i < len(self.array_of_names) - 1: string += "\n"
        return string

    @property
    def aviaCompany(self):
        return self.aviaCompany

    @property
    def noOfPeople(self):
        return self.noOfPeople

    @property
    def startTime(self):
        return self.startTime

    @property
    def endTime(self):
        return self.endTime

    @property
    def date(self):
        return self.date

    @property
    def flightNumber(self):
        return self.flightNumber

    @noOfPeople.setter
    def noOfPeople(self, value):
        self.noOfPeople = Validation.validate_noOfPeople(value)

    @aviaCompany.setter
    def aviaCompany(self, value):
        self.aviaCompany = Validation.validate_aviaCompany(value)

    @flightNumber.setter
    def flightNumber(self, value):
        self.flightNumber = Validation.validate_flightNumber(value)

    @date.setter
    def date(self, value):
        self.date = Validation.validate_date(value)

    @startTime.setter
    def startTime(self, value):
        self.startTime = Validation.validate_time(value)

    @endTime.setter
    def endTime(self, value):
        if Validation.validate_two_times(self.startTime, value) is True:
            self.endTime = Validation.validate_time(value)
        