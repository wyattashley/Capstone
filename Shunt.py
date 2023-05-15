from ina219 import INA219
from time import time
from ina219 import DeviceRangeError


class Shunt:

    def __init__(self, resistance_ohm=0.00075, max_amps=100, address=0x40):
        self.ina = INA219(resistance_ohm, max_amps, address=address)
        self.ina.configure(self.ina.RANGE_32V, self.ina.GAIN_AUTO)
        self.voltage_val = 0
        self.power_val = 0
        self.current_val = 0
        self.shunt_voltage_val = 0
        self.Ah = 0
        self.last_update = time()

    def voltage(self):
        return self.voltage_val

    def power(self):
        return self.power_val

    def current(self):
        return self.current_val

    def shunt_voltage(self):
        return self.shunt_voltage_val

    def resistance(self):
        return self.voltage_val / self.current_val

    def Ah(self):
        return self.Ah

    def update(self):
        try:
            self.voltage_val = self.ina.supply_voltage()
        except DeviceRangeError:
            self.voltage_val = 24.0

        try:
            self.current_val = self.ina.current() / 1000.0
        except DeviceRangeError:
            self.current_val = 100.0

        try:
            self.shunt_voltage_val = self.ina.shunt_voltage()
        except DeviceRangeError:
            self.shunt_voltage_val = 100.0

        try:
            self.power_val = self.ina.power() / 1000.0
        except DeviceRangeError:
            self.power_val = 24 * 100.0

        self.Ah += self.current_val * ((time() - self.last_update) / (60.0 * 60.0))

        self.last_update = time()
