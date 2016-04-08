# -*- coding: utf-8 -*-


from pyvisa_drivers.base import GPIBInstrumentBase


class Keithley2401(GPIBInstrumentBase):
    def __init__(self, gpib_address):
        super().__init__(gpib_address)
        self.gpib_instrument.values_format.use_ascii('f', ',')
        self.V_IND = 0
        self.I_IND = 1
        self.R_IND = 2
        self.T_IND = 3
        self.S_IND = 4

    def read_resistance2(self):
        """Read the resistance being measured."""
        return self.read_one_point()[self.R_IND]

    def read_resistance(self):
        """Read the voltage and current and return the ratio."""
        point = self.read_one_point()
        return point[self.V_IND]/point[self.I_IND]

    def read_resistances(self, n):
        """Read n resistances sequentially."""
        return [self.read_resistance() for i in range(n)]

    def read_one_point(self):
        return self.query_values(':READ?')
