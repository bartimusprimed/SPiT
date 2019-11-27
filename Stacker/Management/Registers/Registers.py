from Stacker.Management.Registers.Register import Register as R
from collections import OrderedDict
class Registers:
    def __init__(self):
        self.registers = OrderedDict(
            set([("EIP", R.EIP), 
            ("EBP", R.EBP), 
            ("ESP", R.ESP), 
            ("EAX", R.EAX), 
            ("EBX", R.EBX), 
            ("ECX", R.ECX), 
            ("EDX", R.EDX), 
            ("ESI", R.ESI), 
            ("EDI", R.EDI)]
        ))
    def load_register(self, register, value):
        self.registers[register].set_Value(value)
    def view_registers(self):
        for (reg_name, reg_value) in self.registers.items():
            print("{0} -> {1}".format(reg_name, reg_value.register_value))