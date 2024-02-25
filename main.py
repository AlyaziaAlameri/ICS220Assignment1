class Passenger:
    def __init__(self, firstName, lastName, fromLocation, toLocation, electronicTicket):  # constructor '__init__'
        self.firstName = firstName
        self.lastName = lastName
        self.fromLocation = fromLocation
        self.toLocation = toLocation
        self.electronicTicket = electronicTicket  # 5 attributes

    # setter and getter
    def getFirstName(self):
        return self.firstName

    def setFirstName(self, firstName):
        self.firstName = firstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getFromLocation(self):
        return self.fromLocation

    def setFromLocation(self, fromLocation):
        self.fromLocation = fromLocation

    def getToLocation(self):
        return self.toLocation

    def setToLocation(self, toLocation):
        self.toLocation = toLocation

    def getElectronicTicket(self):
        return self.electronicTicket

    def setElectronicTicket(self, electronicTicket):
        self.electronicTicket = electronicTicket


class Flight:
    def __init__(self, flightNumber, fromLocation, toLocation, date, gate, terminal):  # constructor '__init__'
        self.flightNumber = flightNumber
        self.fromLocation = fromLocation
        self.toLocation = toLocation
        self.date = date
        self.gate = gate
        self.terminal = terminal

    # setter and getter
    def getFlightNumber(self):
        return self.flightNumber

    def setFlightNumber(self, flightNumber):
        self.flightNumber = flightNumber

    def getFromLocation(self):
        return self.fromLocation

    def setFromLocation(self, fromLocation):
        self.fromLocation = fromLocation

    def getToLocation(self):
        return self.toLocation

    def setToLocation(self, toLocation):
        self.toLocation = toLocation

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

    def getGate(self):
        return self.gate

    def setGate(self, gate):
        self.gate = gate

    def getTerminal(self):
        return self.terminal

    def setTerminal(self, terminal):
        self.terminal = terminal


class BoardingPass:
    def __init__(self, flightNumber, gate, date, boardingTime, arrivalTime, seatNumber, boardingTill):
        self._flightNumber = flightNumber
        self._gate = gate
        self._date = date
        self._boardingTime = boardingTime
        self._arrivalTime = arrivalTime
        self._seatNumber = seatNumber
        self._boardingTill = boardingTill

    # setter and getter
    def getFlightNumber(self):
        return self._flightNumber

    def setFlightNumber(self, flightNumber):
        self._flightNumber = flightNumber

    def getGate(self):
        return self._gate

    def setGate(self, gate):
        self._gate = gate

    def getDate(self):
        return self._date

    def setDate(self, date):
        self._date = date

    def getBoardingTime(self):
        return self._boardingTime

    def setBoardingTime(self, boardingTime):
        self._boardingTime = boardingTime

    def getArrivalTime(self):
        return self._arrivalTime

    def setArrivalTime(self, arrivalTime):
        self._arrivalTime = arrivalTime

    def getSeatNumber(self):
        return self._seatNumber

    def setSeatNumber(self, seatNumber):
        self._seatNumber = seatNumber

    def getBoardingTill(self):
        return self._boardingTill

    def setBoardingTill(self, boardingTill):
        self._boardingTill = boardingTill


class AirlineStaff:
    def updateSeatNumber(self, passenger, newSeat):  # function headers for updateSeatNumber and verifyElectronicTicket
        """
  Here we updates the seat number for the passenger James Smith to 4B.
  """
        passenger.setSeatNumber(newSeat)

    def verifyElectronicTicket(self, passenger):
        """
  Here we Verify the electronic ticket for the passenger.
  """
        if passenger.getElectronicTicket() == "Valid":
            return True
        else:
            return False

# Creating objects of Passenger class
passenger = Passenger("James", "Smith", "CHICAGO ORD", "NEW YORK JFK", "629")

# Creating objects of Flight class
flight = Flight("NA4321", "CHICAGO ORD", "NEW YORK JFK", "06 DEC 20", "03", 2)

# Creating objects of BoardingPass class
boarding_pass = BoardingPass("NA4321", "03", "06 DEC 20", "11:20", "13:30", "09A", "11:20")

# Populating the attributes
boarding_pass.setFlightNumber(flight.getFlightNumber())
boarding_pass.setGate(flight.getGate())
boarding_pass.setDate(flight.getDate())
boarding_pass.setArrivalTime("13:30")
boarding_pass.setSeatNumber("4B")  # The updated seat number to 4B
boarding_pass.setBoardingTill("11:20")

# Displaying passenger details
print("Passenger Details:")
print("First Name:", passenger.getFirstName())
print("Last Name:", passenger.getLastName())
print("From Location:", passenger.getFromLocation())
print("To Location:", passenger.getToLocation())
print("Electronic Ticket:", passenger.getElectronicTicket())

# Displaying flight details
print("\nFlight Details:")
print("Flight Number:", flight.getFlightNumber())
print("From Location:", flight.getFromLocation())
print("To Location:", flight.getToLocation())
print("Date:", flight.getDate())
print("Gate:", flight.getGate())
print("Terminal:", flight.getTerminal())

# Displaying boarding pass details
print("\nBoarding Pass Details:")
print("Flight Number:", boarding_pass.getFlightNumber())
print("Gate:", boarding_pass.getGate())
print("Date:", boarding_pass.getDate())
print("Boarding Time:", boarding_pass.getBoardingTime())
print("Arrival Time:", boarding_pass.getArrivalTime())
print("Seat Number:", boarding_pass.getSeatNumber())