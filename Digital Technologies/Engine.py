'''Finish and test a running Car implementation by following these steps:
o Complete an Engine class
▪ Attributes:
• cylinders : integer (sorry, no rotaries)
• turbocharged : boolean
▪ Methods:
• accelerate() : int # returns a speed increase

# If engine is turbocharged, calls spool()
• spool() : void # makes (prints) a cool sound

o Write two Engine objects in your python code, one turbocharged and one not
o Write two Car objects to test both engines
o Drive the cars along an imaginary track and check the print messages
o Add more classes which can be composed into the car (e.g., Wheel, Transmission,
etc.). Write code to Car so that tasks are delegated to your new classes.'''




class Engine: 
    def __init__(self, cylinder, turbocharged):
        self.cylinder = cylinder
        self.turbocharged = turbocharged

    def accelerate(self):
        if self.turbocharged:
            self.spool()
        return 100

    def spool(self):
        print("strstrsrtr (a cool sound)")