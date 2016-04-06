# -*- coding: utf-8 -*-


import visa as vs


class GPIBInstrumentBase:
    def __init__(self):
        self.gpib_instrument = None
        if not hasattr(self, 'rm'):
            GPIBInstrumentBase.rm = vs.ResourceManager()

    @staticmethod
    def _idstr(addr):
        return 'GPIB::{}::INSTR'.format(addr)

    def __getattr__(self, name):
        return getattr(self.gpib_instrument, name)


class Keithley2401(GPIBInstrumentBase):
    def __init__(self, gpib_address):
        super().__init__()
        idstr = self._idstr(gpib_address)
        self.gpib_instrument = self.rm.open_resource(idstr)
        self.gpib_instrument.values_format.use_ascii('f', ',')
