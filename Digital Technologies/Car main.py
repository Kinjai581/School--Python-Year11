from Engine import *
from Car import *

e = Engine(4, True)
c = Car('road', e)

c.accelerate()
c.driveStraight()
c.accelerate()
c.accelerate()
c.corner('left', 'dirt')
c.accelerate()
c.accelerate()
c.accelerate()
c.accelerate()
c.corner('right', 'dirt')