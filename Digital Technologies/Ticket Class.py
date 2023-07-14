# LESSON 1 PRACTICE TASK

# Submit your response to the same post from which you downloaded this code

# You have been hired to create a ticket-ordering system for a mass-transit provider.

# Your goal is to read the following specification and create a class definition
# that reflects all of the client's requirements

# HINT: you can copy the above code for the Account class
# and modify/extend as you see fit to meet this practice task

# Submit your code to Google Classroom via the relevant post

# Your client has specified that tickets must have:
# - name: of the person traveling
# - different modes of transport: bus, train, ferry
# - different levels of comfort: first, business, economy
# - dates: of departure and arrival
# - cities: Australian cities representing the origin, destination
#
# For each of these points, make sure your Ticket class has 
# the relevant attributes; pay close attention to your constructor

# Your employer has specified that tickets must be able to:
# - *print* all of the above details in a nicely formatted way
# - *check* itself for the following issues:
# - - bus tickets do not have a first or business class
# - - there is no business class for anyone traveling to Melbourne
# - - no ticket can have the same city in the origin and destination fields
#
# For each of these points, make sure your Ticket class has 
# the relevant methods

class Ticket:
    def __init__(self, name, transport, comfort, dates, origin, destination):
        self.name = name
        self.transport = transport
        self.comfort = comfort
        self.dates = dates
        self.destination = destination
        self.origin = origin
        
    def print(self):
        print(self.name, 'is travelling by', self.transport, 'in', self.comfort, 'on', self.dates, 'from', self.origin, 'to', self.destination)
        
    def check(self):
        if self.transport == 'bus':
            if self.comfort == 'Business class' or  self.comfort == 'First class':
                print('INVALID TICKET\nThere is no Business class or First class for Buses')

        if self.destination == 'Melbourne' and self.comfort == 'Business class':
            print('No buisness class for anyone going to Melbourne')

        if self.origin == self.destination:
            print('INVALID TICKET\nCannot travel to the same destination as your origin!')

        
        
#person = Ticket('Rafe', 'bus', 'Economy class', '05/02/09', 'Canberra', 'Perth') # ---> Prints normal sentence
#person = Ticket('Rafe', 'bus', 'Business class', '05/02/09', 'Sydney', 'Perth') # ---> Prints 'INVALID TICKET' as bus tickets to not include business class
#person = Ticket('Rafe', 'train', 'Business class', '05/02/09', 'Sydney', 'Melbourne') # --> There is no business class for anyone travelling to Melbourne, regardless of vehicle
person = Ticket('Rafe', 'train', 'Business class', '05/02/09', 'Sydney', 'Sydney') # --> Prints 'INVALID TICKET' as the origin and destination are the same
person.print()
person.check()
