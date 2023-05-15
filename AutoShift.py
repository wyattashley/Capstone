

class AutoShift:

    def __init__(self, downShiftCurrent=40, downShiftVoltage=8, upShiftCurrent=20, upShiftVoltage=14):
        self.down_shift_current = downShiftCurrent
        self.down_shift_voltage = downShiftVoltage
        self.up_shift_current = upShiftCurrent
        self.up_shift_voltage = upShiftVoltage

    def update(self, current, voltage):
        if current > self.down_shift_current and voltage < self.down_shift_voltage:
            return False
        elif current < self.up_shift_current and voltage > self.up_shift_voltage:
            return True
        else:
            return None
