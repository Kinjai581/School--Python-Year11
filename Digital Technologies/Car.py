from Engine import *

class Car:
	def __init__(self, surface, engine):
		self.speed = 0
		self.surface = surface	# Road or dirt
		self.engine = engine	# The composed object

	def accelerate(self):
		# You need to call the Engine's accelerate method to increase self.speed
		self.speed += self.engine.accelerate()

	def driveStraight(self):
		# Check self.speed and self.surface
		# Print the appropriate behavior here
		if self.surface == 'dirt':
			self.speed -= 5 # Assuming that the road is dirt, as if they are back on the road it would +- 5 every time. Unsure of what is reqruied here

	def corner(self, direction, surface):
		# Check self.speed and self.surface
		# Print the appropriate behavior here
        if self.surface == surface:
            return surface
    
		#unsure of what else to include for the speed of the corner
			