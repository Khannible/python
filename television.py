class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize the TV with power off, unmuted, min volume, and min channel."""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """Toggle the power status of the TV."""
        self.__status = not self.__status

    def mute(self):
        """Toggle mute status if the TV is on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """Increase the channel by one, wrap around if at max, only if TV is on."""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """Decrease the channel by one, wrap around if at min, only if TV is on."""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """Increase the volume by one if not at max and TV is on. Unmute if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """Decrease the volume by one if not at min and TV is on. Unmute if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """Return the string representation of the TV's current state."""
        vol = 0 if self.__muted else self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {vol}'

