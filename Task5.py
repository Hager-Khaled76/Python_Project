#Task5: Smart Home Controller
#------------------------------

from abc import ABC, abstractmethod

class Device(ABC):

    def __init__(self, name):
        self.name = name
        self._on = False

    def toggle(self):
        self._on = not self._on

    def is_on(self):
        return self._on

    @abstractmethod
    def status(self):
        pass

class Light(Device):

    def __init__(self, name, brightness):
        super().__init__(name)
        self.brightness = brightness

    def status(self):
        if self.is_on():
            return f"{self.name}: ON ({self.brightness}%)"
        return f"{self.name}: OFF"


class AC(Device):

    def __init__(self, name, temp):
        super().__init__(name)
        self.temp = temp

    def status(self):
        if self.is_on():
            return f"{self.name}: ON ({self.temp}C)"
        return f"{self.name}: OFF"


if __name__ == '__main__':
    d1 = Light('Bedroom', 80)
    d2 = AC('Hall', 22)
    d3 = Light('Kitchen', 100)
    d4 = AC('Office', 18)

    devices = [d1, d2, d3, d4]

    d1.toggle()  # led1 is on
    d2.toggle()  # ac1 is on
    d4.toggle()  # ac2 is on

    on_devices = list(filter(lambda d: d.is_on(), devices))

    for dev in on_devices:
        print(dev.status())

    print(f"ON devices = {len(on_devices)}")