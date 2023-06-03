CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel = 1

    def first_channel(self):
        self.current_channel = 1
        return self.channels[0]

    def last_channel(self):
        self.current_channel = len(self.channels)
        return self.channels[-1]

    def turn_channel(self, N):
        if 1 <= N <= len(self.channels):
            self.current_channel = N
            return self.channels[N - 1]
        else:
            return "Invalid channel number"

    def next_channel(self):
        self.current_channel = (self.current_channel % len(self.channels)) + 1
        return self.channels[self.current_channel - 1]

    def previous_channel(self):
        self.current_channel = (self.current_channel - 2) % len(self.channels) + 1
        return self.channels[self.current_channel - 1]

    def current_channel(self):
        return self.channels[self.current_channel - 1]

    def is_exist(self, option):
        if isinstance(option, int):
            if 1 <= option <= len(self.channels):
                return "Yes"
            else:
                return "No"
        elif isinstance(option, str):
            if option in self.channels:
                return "Yes"
            else:
                return "No"
        else:
            return "Invalid channel number"

if __name__ == "__main__":
    controller = TVController(CHANNELS)

    print(controller.first_channel() == "BBC")
    print(controller.last_channel() == "TV1000")
    print(controller.turn_channel(1) == "BBC")
    print(controller.next_channel() == "Discovery")
    print(controller.previous_channel() == "BBC")
    print(controller.current_channel == "BBC")
    print(controller.is_exist(5) == "No")
    print(controller.is_exist("Discovery") == "Yes")
    print(controller.is_exist("TVSport") == "No")
