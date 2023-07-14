class LightSwitch:
    def __init__(self, switch, colour, brightness):
        self.switch = switch
        self.brightness = brightness
        self.colour = colour
        
    def toggle_switch(self):
        if self.switch == True:
            print(f'The light is on and the brightness is {self.brightness}')
            self.switch = False
        elif self.switch == False:
            print('The light switch is off.')
            self.switch = True
            
    def get_colour(self, colour):
        if self.colour == str:
            print(self.colour)
        else:
            print('Please enter a string value for the colour')
    
    
    def toggle_brightness(self, brightness):
        if self.brightness == int:
            print(self.brightness)
        else:
            print('Please enter an integer value')

    
s = LightSwitch(True, 'Blue', 200)
s.toggle_switch()
s.get_colour()
s.toggle_brightness()
