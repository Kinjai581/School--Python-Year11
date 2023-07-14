class TV:
    def __init__(self, power, channel, volume):
        self.power = power
        self.channel = channel
        self.volume = volume

    def toggle_power(self):
        if self.power == self.power:
            print("TV is on.")
        else:
            print("TV is off.")
            

    def change_channel(self, channel):
        self.channel = channel
        print(f"Changed to channel {self.channel}")

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume increased to {self.volume}")
        else:
            print("Maximum volume reached.")

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume decreased to {self.volume}")
        else:
            print("Minimum volume reached.")

tv = TV(True, 4, 15)

tv.increase_volume()
#tv.decrease volume()
#tv.change_channel