# -*- coding: utf-8 -*-


from pyvisa_drivers.base import GPIBInstrumentBase


class NewportMM4005(GPIBInstrumentBase):
    def __init__(self, gpib_address, axis):
        super().__init__(gpib_address)
        self.axis = axis
        self.ax_str = '0%d' % axis

    def motor_on(self):
        self.write('MO')

    def motor_off(self):
        self.write('MF')

    def move_to(self, theta_abs):
        cmd_str = self.ax_str + 'PA' + str(theta_abs)
        self.write(cmd_str)

    def get_position(self):
        cmd_str = self.ax_str + 'TH'
        response = self.ask(cmd_str)
        return float(response[len(cmd_str):])

    def get_velocity(self):
        res = self.query(self.ax_str + 'DV')
        return float(res.strip()[4:])
        
        
mc = NewportMM4005(2, 3)

#class NewportMM4005(GpibInstrument):
#    def __init__(self, resource_name, axis, **kw):
#        self.ax, self.ax_str = self.parse_axis_param(axis)
#        super(NewportMM4005, self).__init__(resource_name, **kw)
#
#    def parse_axis_param(self, axis):
#        if type(axis) == type(''):
#            ax = int(axis)
#            ax_str = '0' + axis
#        elif type(axis) == type(0):
#            ax = axis
#            ax_str = '0' + str(axis)
#        return ax, ax_str
#
#    def motor_on(self):
#        self.write('MO')
#
#    def motor_off(self):
#        self.write('MF')
#
#    def move(self, theta):
#        cmd_str = self.ax_str + 'PR' + str(theta)
#        self.write(cmd_str)
#
#    def move_to(self, theta_abs):
#        cmd_str = self.ax_str + 'PA' + str(theta_abs)
#        self.write(cmd_str)
#
#    def move_to_right_travel_limit(self):
#        cmd_str = self.ax_str + 'MT+'
#        self.write(cmd_str)
#
#    def move_to_left_travel_limit(self):
#        cmd_str = self.ax_str + 'MT-'
#        self.write(cmd_str)
#
#    def set_velocity(self, v_in_units_per_s):
#        cmd_str = self.ax_str + 'VA' + str(v_in_units_per_s)
#        self.write(cmd_str)
#
#    def go_home(self):
#        cmd_str = self.ax_str + 'OR'
#        self.write(cmd_str)
#
#    def set_right_travel_limit(self, x):
#        cmd_str = self.ax_str + 'SR' + str(x)
#        self.write(cmd_str)
#
#    def set_left_travel_limit(self, x):
#        cmd_str = self.ax_str + 'SL' + str(x)
#        self.write(cmd_str)
#
#    def set_units(self, units_name):
#        if units_name.lower() == 'degrees':
#            units_name = 'Dg.'
#        if units_name.lower() == 'radians':
#            units_name = 'Rad'
#        names = ['Dg.', 'Gr.', 'Rad', 'mRd', 'μRd', 'Inc.']
#        if units_name not in names:
#            raise ValueError('unit name does not exist')
#        cmd_str = self.ax_str + 'SN' + units_name
#        self.write(cmd_str)
#
#    def get_position(self):
#        cmd_str = self.ax_str + 'TH'
#        response = self.ask(cmd_str)
#        return float(response[len(cmd_str):])
#
#if __name__ == '__main__':
#    mc = NewportMM4005(2, 3)
