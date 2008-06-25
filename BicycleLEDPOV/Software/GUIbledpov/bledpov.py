#!/usr/bin/env python""" bledpov.py --
"""
 UI generated by GUI Builder Build 146 on 2008-06-25 19:12:03 from:
    /home/lameiro/python/bledpov/bledpov.ui
 This file is auto-generated.  Only the code within
    '# BEGIN USER CODE (global|class)'
    '# END USER CODE (global|class)'
 and code inside the callback subroutines will be round-tripped.
 The 'main' function is reserved.
"""

from Tkinter import *
from bledpov_ui import Bledpov
import serial

# BEGIN USER CODE global



def scan():
    """scan for available ports. return a list of tuples (num, name)"""
    available = []
    for i in range(256):
        try:
            s = serial.Serial(i)
            available.append( (i, s.portstr))
            s.close()   
        except serial.SerialException:
            pass
    return available

ports = scan()


# END USER CODE global

class CustomBledpov(Bledpov):


    pass

    # BEGIN CALLBACK CODE
    # ONLY EDIT CODE INSIDE THE def FUNCTIONS.

    # b_scan_command --
    #
    # Callback to handle b_scan widget option -command
    def b_scan_command(self, *args):
    	
        self.serial_listbox.delete(0, END) # this delete all items on the listbox (refresh)
        
        # A loop that inserts the diferent serial port avaiable into the serial_listbox
        
        for item in ports:
    		self.serial_listbox.insert(END, item)
    	# A loop that inserts the diferent commands into the cmd_listbox
    	
    	for item in ['Command 0', 'Command 1', 'Command 2', 'Command 3', 'Command 4']:
			self.cmd_listbox.insert(END, item)

    # b_send_command --
    #
    # Callback to handle b_send widget option -command
    def b_send_command(self, *args):
        pass

    # cmd_listbox_xscrollcommand --
    #
    # Callback to handle cmd_listbox widget option -xscrollcommand
    def cmd_listbox_xscrollcommand(self, *args):
        pass

    # cmd_listbox_yscrollcommand --
    #
    # Callback to handle cmd_listbox widget option -yscrollcommand
    def cmd_listbox_yscrollcommand(self, *args):
        pass

    # serial_listbox_xscrollcommand --
    #
    # Callback to handle serial_listbox widget option -xscrollcommand
    def serial_listbox_xscrollcommand(self, *args):
        pass

    # serial_listbox_yscrollcommand --
    #
    # Callback to handle serial_listbox widget option -yscrollcommand
    def serial_listbox_yscrollcommand(self, *args):
        pass

    # _button_1_command --
    #
    # Legacy command found in callback code. Add user comments inside body.
    def _button_1_command(self, *args):
        pass

    # _button_2_command --
    #
    # Legacy command found in callback code. Add user comments inside body.
    def _button_2_command(self, *args):
        pass

    # _listbox_2_xscrollcommand --
    #
    # Legacy command found in callback code. Add user comments inside body.
    def _listbox_2_xscrollcommand(self, *args):
        pass

    # _listbox_2_yscrollcommand --
    #
    # Legacy command found in callback code. Add user comments inside body.
    def _listbox_2_yscrollcommand(self, *args):
        pass

    # seriallistbox_xscrollcommand --
    #
    # Legacy command found in callback code. Add user comments inside body.
    def seriallistbox_xscrollcommand(self, *args):
        pass

    # seriallistbox_yscrollcommand --
    #
    # Legacy command found in callback code. Add user comments inside body.
    def seriallistbox_yscrollcommand(self, *args):
        pass

    # END CALLBACK CODE

    # BEGIN USER CODE class
    
    	
    

    # END USER CODE class






def main():
    # Standalone Code Initialization
    # DO NOT EDIT
    try: userinit()
    except NameError: pass
    root = Tk()
    demo = CustomBledpov(root)
    root.title('bledpov')
    try: run()
    except NameError: pass
    root.protocol('WM_DELETE_WINDOW', root.quit)
    root.mainloop()

if __name__ == '__main__': main()
	


