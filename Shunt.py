from ina219 import INA219
from time import time
from ina219 import DeviceRangeError


class Shunt:

    def __init__(self, resistance_ohm=0.00075, max_amps=100, address=0x40):
        self.ina = INA219(resistance_ohm, max_amps, address=address)
        self.ina.configure(self.ina.RANGE_32V, self.ina.GAIN_2_80MV)
        self.voltage = 0
        self.power = 0
        self.current = 0
        self.shunt_voltage = 0
        self.Ah = 0
        self.last_update = time()

    def voltage(self):
        return self.voltage

    def power(self):
        return self.power

    def current(self):
        return self.current

    def shunt_voltage(self):
        return self.shunt_voltage

    def resistance(self):
        return self.voltage / self.current

    def Ah(self):
        return self.Ah

    def update(self):
        self.voltage = self.ina.voltage()
        self.power = self.ina.power()
        self.current = self.ina.current()
        self.shunt_voltage = self.ina.shunt_voltage()

        self.Ah += self.current * ((time() - self.last_update) / (60 * 60))

        self.last_update = time()
