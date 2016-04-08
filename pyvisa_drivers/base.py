# -*- coding: utf-8 -*-


import visa as vs


class GPIBInstrumentBase:
    def __init__(self, gpib_address):
        self.gpib_instrument = None
        if not hasattr(self, 'rm'):
            GPIBInstrumentBase.rm = vs.ResourceManager()
        idstr = self._idstr(gpib_address)
        self.gpib_instrument = self.rm.open_resource(idstr)

    @staticmethod
    def _idstr(addr):
        return 'GPIB::{}::INSTR'.format(addr)

    def __getattr__(self, name):
        return getattr(self.gpib_instrument, name)
