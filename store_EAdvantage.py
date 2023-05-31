import pandas as pd
import requests
import sys
import os
import base64
from tkinter import *
from tkcalendar import DateEntry
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox
from tkinter.messagebox import *
import json

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))


class Menu(Tk):
    def __init__(self):
        super().__init__()

        self.__icon()
        self.title('Eadvantage')

        Label(self, text='Eadvantage', font=("Arial", 30)).pack()

        Button(self, text='Store node info', font=("Arial", 20), command=lambda: WindowNodeInfo(self)).pack()
        Button(self, text='Download meter data', font=("Arial", 20), command=lambda: WindowMeterData(self)).pack()
        Button(self, text='Delete meter', font=("Arial", 20), command=lambda: WindowDeleteMeter(self)).pack()

        self.mainloop()

    def __icon(self):
        #The Base64 icon version as a string
        icon = \
            '''
            AAABAAEAgIAAAAEAIAAoCAEAFgAAACgAAACAAAAAAAEAAAEAIAAAAAAAAAABABx2AAAcdgAAAAAAAAAA
            AACZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkB/5mZAf+ZmQH/mZkB/5mZAf+ZmQH/mZkB/5mZ
            Af+ZmQH/mZkB/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAf+amgH/mpoC/5qaA/+bmwT/m5sE/5qaBP+amgP/mpoC/5mZ
            AP+YmAD/mJgA/5iYAP+XlwD/l5cA/5eXAP+XlwD/mJgA/5iYAP+ZmQD/mpoB/5qaA/+bmwT/m5sE/5qa
            A/+amgL/mZkB/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAf+amgL/mpoE/5ubBP+amgP/mZkA/5eX
            AP+VlQD/k5MA/5KSAP+SkgD/k5MA/5SUAP+VlQD/mJgA/5ubA/+cnAn/np4N/5+fD/+goBL/oaET/5+f
            EP+eng3/nJwI/5qaAv+WlgD/lJQA/5KSAP+SkgD/k5MA/5aWAP+ZmQD/mpoD/5ubBP+amgL/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5qa
            BP+amgL/mJgA/5WVAP+SkgD/kpIA/5SUAP+ZmQP/oqIV/6urLv+3t0r/wsJo/83Ngf/X15r/39+v/+bm
            wP/s7M7/7+/Y//Pz4f/29uj/9/fs//n57//5+fD/+Pju//b26f/z8+D/7u7U/+joxf/f36//09OR/8XF
            b/+2tkj/pqYh/5qaBP+TkwD/kpIA/5aWAP+amgL/m5sE/5qaAf+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/kpIA/5WVAP+engz/rKww/76+W//Q0Ir/4eGz/+7u
            1f/5+fH////+////////////////////////////////////////////////////////////////////
            ///////////////////////////////////////////////////8/Pn/7+/Y/9vbpP/AwGL/pqYg/5aW
            AP+SkgD/l5cA/5ubA/+amgL/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5ub
            BP/Ly3z/5eW+//X15v////7//////////////////////////////////v78//7++//9/fv//f37//7+
            /P/+/vz//v79//7+/f/+/v3//v7+/////v////7////+/////v/+/v7//v79//7+/f/+/vz//v78//39
            +//9/fv//v79///////////////////////8/Pj/5ubA/8LCZ/+hoRP/kpIA/5aWAf+bmwP/mpoB/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAf+XlwD/n58Q//j47v/////////+/////v/+/vz//f37//7+
            /P/+/v3////+////////////////////////////////////////////////////////////////////
            ///////////////////////////////////////////////////////////+//7+/f/9/fv//v78////
            //////7///////j47v/T05H/pqYh/5KSAP+XlwL/m5sD/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkB/5iY
            AP+fnw7/9fXn///////+/vz/////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////////////////////////////+//7+/P/+/vz////+///////7+/b/0tKO/5+f
            Ev+TkwD/mpoD/5mZAf+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQH/l5cA/5+fDv/39+v///////7+/v//////////////
            ////////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////+/v7//v77//7+/f//////9fXm/7u7VP+TkwD/mJgD/5qaAv+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            Af+XlwD/n58O//f36////////v7+////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////////////////////////////////////////////////////////////+//7+
            +//+/v7//////9fXmv+ZmQf/lpYA/5qaAv+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkB/5eXAP+fnw7/9/fr///////+/v7/////////
            ////////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            //////////////////////////////////////////////7+/f/9/fv//////+joxP+fnxT/lpYA/5qa
            Av+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQH/l5cA/5+fDv/39+v///////7+/v//////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////9/fr//////+3t0v+goBf/lpYA/5qaAv+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAf+XlwD/n58O//f36////////v7+////
            ////////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////////////////////////////////////////////////////9/fv//////+np
            x/+amgr/mJgA/5qaAf+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkB/5eXAP+fnw7/9/fr///////+/v7/////////////////////////////////////////
            /////////////////////////////////v////7//v7+//7+/f/+/v3//v79//7+/f/+/v3////+////
            /v//////////////////////////////////////////////////////////////////////////////
            ///////////////////////////////////9/fr//////9nZof+UlAD/mpoC/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQH/l5cA/5+fDv/39+v///////7+
            /v///////////////////////////////////////v7+//7+/P/9/fv//f37//7+/P/+/v7/////////
            //////////////////////////////////////////////7+/f/9/fv//v77//7+/v//////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///+/vv//////7y8XP+TkwD/m5sD/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAf+XlwD/n58O//f36////////v7+///////////////+//7+/f/9/fv//v77////
            /v/////////////////////////////////9/fr/+fnx//X15f/x8dv/7+/W/+7u1P/v79f/8vLf//f3
            7P/9/fn///////////////////////7+/P/+/v3/////////////////////////////////////////
            //////////////////////////////////////////////7+/f//////8vLg/56eEf+YmAD/mZkB/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkB/5eXAP+fnw7/9/fr////
            ///+/vz//f37//7+/P/////////////////////////+//b26f/n58T/2Nie/8jId/+7u1X/sLA6/6en
            JP+hoRX/nZ0L/5ubBv+amgP/mZkB/5qaA/+cnAf/n58Q/6amIv+xsT3/w8No/9vbpP/19ef/////////
            /v/+/v3/////////////////////////////////////////////////////////////////////////
            //////////////39+///////ycl5/5KSAP+bmwP/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQH/mJgA/5+fDv/19ef//////////v////////////z89//s7M//1taa/7+/
            YP+trTH/n58O/5aWAP+TkwD/kpIA/5OTAP+UlAD/lpYA/5eXAP+YmAD/mJgA/5mZAP+ZmQD/mZkA/5iY
            AP+XlwD/lpYA/5SUAP+SkgH/k5MA/56eDP+/v1//8vLd///////+/vz/////////////////////////
            /////////////////////////////////////////////////////////v79///////x8dz/nJwK/5iY
            AP+ZmQH/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAf+XlwD/n58Q//j4
            7v//////8fHb/9jYnP+9vVr/pqYf/5iYAf+SkgD/kpIA/5WVAP+YmAD/mpoB/5qaBP+bmwT/mpoD/5qa
            A/+amgL/mpoB/5mZAf+ZmQH/mZkB/5mZAf+ZmQH/mZkB/5mZAf+amgL/mpoD/5ubBP+amgP/mJgB/5KS
            AP+cnAv/4OCx///////+/v3/////////////////////////////////////////////////////////
            /////////////////////////v79//////+3t07/k5MA/5qaA/+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkB/5iYAP+engv/yMh1/7CwOv+amgX/kpIA/5OTAP+WlgD/mZkB/5qa
            BP+bmwT/mpoC/5mZAf+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQH/m5sE/5aWAP+YmAf/6+vL///////+/v3/////////
            ///////////////////////////////////////////////////////////////////+/vv//////9bW
            mv+SkgD/mpoD/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+SkgD/lJQA/5iYAP+amgP/mpoE/5qaAv+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/m5sF/5KSAP+4uFH///////7+/f//////////////////////////////////////////////
            //////////////////////////////7+/f//////7e3T/5mZAf+ZmQD/mZkB/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5qaBP+amgP/mZkB/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQH/l5cA/6GhF//5+fD/////////
            /v/////////////////////////////////////////////////////////////////////////+////
            ///7+/X/pKQd/5aWAP+amgL/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAf+YmAD/nJwI//Hx3v///////v79////////////////////////////////////
            /////////////////////////////////////////v79//////+xsTz/lJQA/5qaA/+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkB/5iYAP+eng7/9fXn////
            ///+/v7/////////////////////////////////////////////////////////////////////////
            ///+/vz//////7q6U/+TkwD/mpoD/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+amgP/lZUA/66uO//////////+////////////////////////////////////
            //////////////////////////////////////////////7+/P//////wcFk/5KSAP+bmwT/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mpoB/5ubBf+RkQD/3Nyn////
            ///+/vz/////////////////////////////////////////////////////////////////////////
            /////////v77///////ExGv/kpIA/5ubBP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5ubA/+ZmQP/kJAA/8XFbv///////v79////////////////////////////////////
            ///////////////////////////////////////////////////+/vv//////8LCZ/+SkgD/m5sE/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5qaA/+amgL/k5MA/5qaB//R0Yz///////7+
            /f//////////////////////////////////////////////////////////////////////////////
            //////////////7+/P//////vLxY/5OTAP+amgT/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkB/5ub
            BP+ZmQL/k5MA/5aWAP+5uU//7+/Y///////+/vz/////////////////////////////////////////
            /////////////////////////////////////////////////////////v79//////+zs0D/lJQA/5qa
            A/+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mpoC/5ubBP+YmAH/kpIA/5eXAf+2tkj/6OjF//////////7//v78////
            ////////////////////////////////////////////////////////////////////////////////
            /////////////////v///////Pz3/6amIf+WlgD/mpoC/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mpoD/5qaA/+WlgD/kpIA/5yc
            Cv++vlv/6urK/////////////v78//7+/f//////////////////////////////////////////////
            /////////////////////////////////////////////////////////v79///////v79f/mpoE/5mZ
            AP+ZmQH/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQH/m5sE/5mZAv+UlAD/k5MA/6WlHP/Ly33/8/Ph/////////////v79//7+/P//////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////+/vv//////9jYnv+TkwD/mpoD/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+amgH/m5sE/5iYAf+SkgD/l5cB/7GxO//a2qP/+/v0////
            /////////v78//7+/P//////////////////////////////////////////////////////////////
            //////////////////////////////////////////////////////////////7+/f//////t7dP/5OT
            AP+amgP/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+amgL/m5sD/5eX
            Af+SkgD/nJwK/7+/Xf/q6sn///////////////7//v77//7+/f//////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////+/v3///////Dw2f+bmwj/mJgA/5mZAf+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+amgL/m5sD/5aWAf+SkgD/oaEW/8rKev/y8uD//////////v/+/v3//v77////
            /v//////////////////////////////////////////////////////////////////////////////
            //////////////////////////////////////////////////////////////39+///////xMRv/5KS
            AP+bmwP/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQH/m5sD/5aWAf+SkgD/pKQd/9DQ
            iv/4+O3//////////v/+/vz//v78////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////+/vz//////+zs0P+amgj/mZkA/5mZAf+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/m5sD/5iYAv+SkgD/o6Ma/9LSj//7+/T//////////v/+/vv//v79////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////////////////////////////////////////////+//7+/f////3/sbE//5SU
            AP+amgP/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mpoC/5qaA/+SkgD/nZ0O/87Og//6+vL///////7+
            /v/+/vv//v7+////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            /////////////////v/9/fv//////8bGc/+SkgD/m5sD/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5ub
            A/+WlgH/lZUA/7+/Xv/09OX///////7+/f/+/vv////+////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////////////////////////////////////+/v3//f37///////Q0In/k5MA/5qa
            A/+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAf+amgT/kpIA/6enJf/l5b3///////7+/v/+/vz////+////
            ////////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            /////////v78//7+/f//////ysp7/5OTAP+amgP/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQH/mZkD/5OT
            AP+/v17/+vry///////+/vv//v79////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            /////////////////////////////////////////v79//39+///////+fnw/7q6Uv+SkgD/mpoE/5mZ
            Af+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkB/5mZAv+UlAD/0NCK///////+/v3//v78////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////////////////////////////////////////////////////////////+//7+
            /P/+/v3//////+Tkuv+kpCD/k5MA/5ubBP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+amgP/k5MA/9HR
            jf///////f36//7+/v//////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            //////////////////////////////7+/P/+/v3///////f36v/BwWP/lZUA/5aWAf+bmwP/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/m5sD/5KSAP/FxXH///////39+v////7/////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            //////////////////////////////////////////////////////////////7+/P/+/v3///////39
            +v/W1pf/oKAW/5KSAP+amgP/mpoC/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5qaAv+UlAD/r686//7+
            +/////7////+////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            //////////////7+/P/+/v3////////////h4bP/q6st/5KSAP+XlwL/m5sD/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQH/mZkA/5mZBf/q6sr///////7+/P//////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////////////////////////////+//7++//+/v3////////////k5Lz/sbE8/5SU
            AP+VlQD/m5sD/5qaAv+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5ubA/+SkgD/wcFn////
            ///+/vv/////////////////////////////////////////////////////////////////////////
            ///////////////////////////////////////////////////////////////////////////+//39
            +//+/v7//////////v/j47r/s7M//5WVAP+UlAD/mpoD/5qaA/+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQH/mZkA/5qaBf/t7dP///////7+/f//////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            /////////////////////////v79//7++/////7///////39+v/e3q3/sLA4/5SUAP+UlAD/mpoC/5qa
            A/+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5qaA/+UlAD/tbVJ////
            ///+/v3/////////////////////////////////////////////////////////////////////////
            /////////////////////////////////////////////////////////v79//7+/P////7///////n5
            8f/V1Zf/qqop/5OTAP+UlAH/mpoC/5qaA/+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mpoD/5KSAP/W1pv///////7++///////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            /////////v78//7+/P////7///////X15v/MzH//o6Ma/5KSAP+VlQH/mpoD/5qaA/+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAf+ZmQD/mZkC/+7u
            1f///////v79////////////////////////////////////////////////////////////////////
            /////////////////////////////////////////v78//7+/f////7//////+/v1v/Dw2j/np4O/5KS
            AP+XlwH/m5sD/5qaAv+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mpoC/5aWAP+mpiD//Pz3//////////7/////////////////////////
            /////////////////////////////////////////////////////////////////////////v78//7+
            /f///////////+rqzP+8vFb/mZkG/5KSAP+YmAH/m5sE/5qaAv+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+amgP/lJQA/7Oz
            QP///////v79////////////////////////////////////////////////////////////////////
            ///////////////////////////+//7+/P///////////+joxf+3t0n/l5cC/5OTAP+ZmQH/m5sE/5mZ
            Af+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5qaBP+TkwD/vb1Z///////+/vz/////////////////////////
            /////////////////////////////////////////////////////////////////v/+/v3//////+vr
            zf+2tkf/lpYA/5OTAP+ZmQL/mpoE/5mZAf+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/m5sE/5KS
            AP/Dw2n///////7++///////////////////////////////////////////////////////////////
            //////////////////////7///////39+f/FxWz/l5cB/5OTAP+amgL/mpoD/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+bmwT/kpIA/8TEbP///////f37////////////////////
            //////////////////////////////////////////////////////////////7+/v//////vr5d/4+P
            AP+amgT/mpoD/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5ub
            BP+SkgD/wsJn///////+/vv/////////////////////////////////////////////////////////
            ///////////////////+/vz//////+Xlvv+UlAD/m5sE/5mZAf+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mpoE/5OTAP+8vFf///////7+/P//////////////
            //////////////////////////////////////////////////////////////39+///////yMh4/5KS
            AP+bmwT/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+amgP/lJQA/7KyP////////v79////////////////////////////////////////////////////
            /////////////////////////v77///////Cwmn/kpIA/5qaBP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQH/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5qaAv+WlgD/pqYh//z89//////////+////
            ///////////////////////////////////////////////////////////////////9/fv//////87O
            h/+SkgD/m5sE/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAf+amgP/mpoD/5iY
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkB/5mZAP+amgT/7+/Y///////+/v3/////////////////////////////////////////
            //////////////////////////////7+/f//////7OzO/5aWAf+amgL/mZkB/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkB/5qaA/+bmwT/mJgA/5SUAP+TkwD/np4M/5qaAv+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mpoD/5OTAP/Z2aL///////7+
            +/////////////////////////////////////////////////////////////////////////////7+
            /f//////xMRt/4+PAP+amgX/m5sE/5mZAf+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAf+amgP/m5sE/5qaA/+YmAD/lJQA/5KSAP+bmwb/srI+/9zc
            p//l5b7/mZkB/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+amgP/k5MA/7u7WP///////v78////////////////////////////////////
            ///////////////////////////////////////////////////+/v3/xcVs/5SUAP+TkwH/mJgA/5qa
            Av+bmwT/mpoE/5qaA/+amgP/mpoC/5qaAv+amgP/mpoD/5qaA/+bmwT/m5sE/5qaA/+ZmQH/l5cA/5SU
            AP+SkgD/lJQA/56eDf+0tEP/09OR//Hx3f/+/v3//////+zs0P+ZmQD/mZkA/5mZAf+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAf+YmAD/np4Q//T0
            4////////v7+////////////////////////////////////////////////////////////////////
            //////////////7+/f//////5ubB/7i4Tf+engz/lJQA/5KSAP+SkgD/k5MA/5SUAP+VlQD/lZUA/5SU
            AP+UlAD/k5MA/5KSAP+SkgD/k5MA/5eXAP+goBL/sLA5/8bGcv/f367/9vbo//////////////////39
            +///////7OzP/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5ubA/+SkgD/zc2E///////9/fv/////////////////////////
            ///////////////////////////////////////////////////////////+//7+/f////////////b2
            5//g4LL/zc2D/7+/X/+1tUf/sLA5/62tMv+trTH/rq41/7GxPP+4uE3/wcFj/83Ngv/b26X/6urK//j4
            7v///////////////////////v79//39+//+/v3//v78///////s7ND/mZkA/5mZAP+ZmQH/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mpoB/5eX
            AP+hoRf/9vbn///////+/v7/////////////////////////////////////////////////////////
            //////////////////////////////7+/P/+/vz/////////////////////////////////////////
            //////////////////////////////////////////////7+/v/9/fv//v78//7+/v//////////////
            ///+/v3//////+zs0P+ZmQD/mZkA/5mZAf+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/m5sD/5KSAP/AwGX///////39+///////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///+/v7//v78//39+//+/vz//v78//7+/v///////////////v/+/v3//v78//7+/P/9/fv//v77//7+
            /P////7///////////////////////////////////////7+/f//////7OzQ/5mZAP+ZmQD/mZkB/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mpoC/5SUAP/c3Kf///////39+v//////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            /////////v79///////s7ND/mZkA/5mZAP+ZmQH/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+amgH/mJgA/5ubC//o6Mb///////39
            +v//////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////////////////////////////////////+/v3//////+zs0P+ZmQD/mZkA/5mZ
            Af+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+amgL/lpYA/56eFP/q6sn///////39+v////7/////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            //////////////7+/f//////7OzQ/5mZAP+ZmQD/mZkB/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+amgL/lpYA/5ub
            Df/g4LD///////7+/P/+/vz/////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            /////////////////////////////////////////////////////////v79///////s7ND/mZkA/5mZ
            AP+ZmQH/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+amgL/mJgC/5WVAP/IyHT//Pz4///////+/vz//v78////
            ////////////////////////////////////////////////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////+/v3//////+zs0P+ZmQD/mZkA/5mZAf+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+amgH/mpoD/5KSAP+pqSr/4+O6/////////////v79//39+/////7/////////////////////////
            ////////////////////////////////////////////////////////////////////////////////
            ///////////////////////////////////////////////////////////+//39+///////6+vN/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQH/m5sD/5WVAf+VlQD/t7dJ/+fn
            w//////////////////+/vz//f37//7+/f////7/////////////////////////////////////////
            //////////////////////////////////////////////////////////////////////7//v79//7+
            /P/9/fv//f37//7+/f///////v79///////t7dL/mZkA/5mZAP+ZmQH/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mpoC/5qaAv+TkwD/lpYA/7GxPP/Z2aH/+Pjt//////////7/////////
            ///+/vz//f37//39+//+/vz//v79//7+/f/+/v7////+/////v////7////+//7+/v/+/v3//v79//7+
            /P/+/vz//f37//39+//+/vz////+//////////////////////////////////v79v/u7tX/4eG0/8TE
            a/+YmAD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5qa
            A/+amgL/lJQA/5OTAP+goBL/u7tU/9jYnf/v79b//f36////////////////////////////////////
            ////////////////////////////////////////////////////////////////////////+/v0//Hx
            3P/j47r/1NST/8PDaP+ysj//pKQc/5qaA/+TkwD/k5MA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+amgP/mpoD/5eXAP+TkwD/kpIA/5mZ
            BP+oqCT/ublP/8rKev/Y2J7/5OS8/+zs0P/y8t//9/fq//n58P/6+vL/+vry//n58P/39+v/8vLf/+3t
            0v/m5sH/3t6r/9LSj//Hx3L/urpT/66uNP+joxr/m5sF/5WVAP+SkgD/kpIA/5SUAP+WlgD/mZkA/5qa
            A/+amgP/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkB/5qaBP+amgT/mZkA/5aWAP+TkwD/kpIA/5OTAP+VlQD/mZkB/5yc
            B/+eng7/oaET/6KiF/+iohb/oKAS/5+fDv+cnAj/mZkB/5WVAP+TkwD/kpIA/5KSAP+TkwD/lJQA/5eX
            AP+YmAD/mpoC/5ubBP+bmwT/mpoD/5qaAv+ZmQH/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQH/mpoC/5qaA/+bmwT/mpoD/5qaAv+ZmQD/mJgA/5iYAP+XlwD/l5cA/5eXAP+XlwD/l5cA/5iY
            AP+ZmQD/mpoC/5qaA/+bmwT/m5sE/5qaA/+amgP/mpoB/5mZAf+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQH/mZkB/5mZAf+amgH/mpoB/5mZAf+ZmQH/mZkB/5mZAf+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZAP+ZmQD/mZkA/5mZ
            AP+ZmQD/mZkA/5mZAP+ZmQD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=
            '''
        icondata= base64.b64decode(icon)
        # The temp file is icon.ico
        iconfile= "icon.ico"
        # Extract the icon
        with open(iconfile,"wb") as f:
            f.write(icondata)
        self.iconbitmap(default=iconfile)
        # Delete the tempfile
        os.remove(iconfile)

class Window(Toplevel):
    def __init__(self, menu):
        self.master = menu
        super().__init__(self.master)

    def _get_token(self, backup=False):
        token_url = 'https://eadvantage.siemens.com/uaa/oauth/token'
        client_id = 'navigator.admin_1514.user_81261.All_Access_API'
        client_secret = '3@)vgyoc,D_k-[ZlNMH:AOJ~,.S08ixatA2S/Fxl$vf?C2l!qs6SaP.#1,9mAmQl'
        if backup:
            client_id = 'navigator.admin_67722.user_95074.Write_Acess_API'
            client_secret = '4)e#[V_Hq4iq.q8d78#Rd*h4ww#?CxyQp2h(].wRLLQ73o6w6uDGwbcTKf(GB5?b'
        token_response = requests.post(token_url, data={"grant_type": "client_credentials"}, auth=(client_id, client_secret))
        return token_response.json()['access_token']

class WindowNodeInfo(Window):
    def __init__(self, menu):
        self.master = menu
        super().__init__(self.master)

        self.title('Store info from Eadvantage')

        Label(self, text='Store info from Eadvantage', font=("Arial", 25)).grid()

        Label(self, text='Please export nodes from NDMT(without attributes) and select the exported excel file.').grid()

        self.excelpath_frame = Frame(self, width=450, height=30)
        self.excelpath_frame.grid()
        self.excelpath_frame.grid_propagate(0)
        self.excelpath_frame.columnconfigure((0, 1), weight=1)

        self.excelpath_box = Entry(self.excelpath_frame, width=60)
        self.excelpath_box.grid(sticky='e')
        Button(self.excelpath_frame, text='browse', command=lambda: (
            reportpath := askopenfilename(title='Select a file', parent=self, filetypes=[("Excel files", ".xlsx .xls")]),
            (self.excelpath_box.delete(0, 'end'), self.excelpath_box.insert('end', reportpath)) if reportpath else 0
        )).grid(row=0, column=1, sticky='w')
        
        Label(self, text='Please enter the node IDs and separate them with and only with next line.').grid()
        self.nodes_box = ScrolledText(self, width=30, height=26)
        self.nodes_box.grid()

        Label(self, text='Please select the path to save the file.').grid()

        self.folderpath_frame = Frame(self, width=450, height=30)
        self.folderpath_frame.grid()
        self.folderpath_frame.grid_propagate(0)
        self.folderpath_frame.columnconfigure((0, 1), weight=1)

        self.folderpath_box = Entry(self.folderpath_frame, width=60)
        self.folderpath_box.insert('end', cwd)
        self.folderpath_box.grid(sticky='e')
        Button(self.folderpath_frame, text='browse', command=lambda: (
            folderpath := askdirectory(initialdir=cwd, title='Select a folder', parent=self),
            self.update(),
            (self.folderpath_box.delete(0, 'end'), self.folderpath_box.insert('end', folderpath)) if folderpath else 0
        )).grid(row=0, column=1, sticky='w')

        Button(self, text='create', command=self.__get_data).grid()

        self.result_box = Label(self)
        self.result_box.grid()
        
        Button(self, text='back', command=self.destroy).grid()

        self.mainloop()

    def __get_data(self):
        folderpath = self.folderpath_box.get()
        excelpath = self.excelpath_box.get()
        if not os.path.isdir(folderpath):
            self.result_box.config(text='Folder does not exist.')
            return
        if not os.path.isfile(excelpath):
            self.result_box.config(text='Excel File does not exist.')
            return
        
        nodes = self.nodes_box.get('1.0','end').replace('\r', '').split('\n')
        nodes = [node for node in nodes if len(node) > 1]
        
        token = self._get_token()
        error_nodes = []

        for count, root in enumerate(nodes):
            self.result_box.config(text='progress '+str(count)+'/'+str(len(nodes))+' downloading '+root)
            self.update()

            link = 'https://eadvantage.siemens.com/remote/release/node/' + root + '/meters'
            response = requests.get(link, headers={'Authorization': 'bearer '+token})

            if response.status_code != 200:
                token = self._get_token(backup=True)
                response = requests.get(link, headers={'Authorization': 'bearer '+token})
                if response.status_code != 200:
                    print('cannot download the required data (' + root + ') with error code ' + str(response.status_code))
                    error_nodes.append(root)
                    continue

            meters = response.json()

            df = pd.read_excel(excelpath)
            df = df[df.pop('State') == 'Existing']
            df['Children'] = df.apply(lambda x: [], axis=1)

            tree_nodes = df[df['NodeID']==int(root)].to_dict('records')[0]

            def traverse(tree):
                for child in tree['Children']:
                    if 'Children' in child:
                        yield from traverse(child)
                yield tree

            def grow(row):
                for parent in traverse(tree_nodes):
                    if row['ParentID'] == parent['NodeID']:
                        parent['Children'].append(row.to_dict())

            df.apply(grow, axis=1)

            for node in traverse(tree_nodes):
                if node['NodeID'] == int(root):
                    root_name = node['Name']

            for meter in meters:
                for node in traverse(tree_nodes):
                    if meter['parentNodeId'] == node['NodeID']:
                        node['Children'].append(meter)
                        break

            with open(folderpath+'/'+root_name+'.json', 'w') as file:
                json.dump(tree_nodes, file, ensure_ascii=False, indent=4)

        if not error_nodes:
            result =  'File saved!'
        elif error_nodes != nodes:
            result =  'File saved! Cannot download: ' + ', '.join(error_nodes) + '. Plaese try other node IDs.'
        else:
            result =  'Cannot download any required data. Plaese try other node IDs or resolutions and check the time.'
        self.result_box.config(text=result)
        self.update()

class WindowMeterData(Window):
    def __init__(self, menu):
        self.master = menu
        super().__init__(self.master)

        self.title('Save data from Eadvantage')
        

        Label(self, text='Save data from Eadvantage', font=("Arial", 25)).grid(column=0, row=0, columnspan=4)
        
        Label(self, text='Please enter the meter IDs and separate them with and only with next line.').grid()
        self.meters_box = ScrolledText(self, width=30, height=26)
        self.meters_box.grid(column=0, row=2, rowspan=19)

        Label(self, text='Please select a starting date.').grid(column=1, row=1, columnspan=3)
        self.start_date_box = DateEntry(self, date_pattern='m/d/y')
        self.start_date_box.grid(column=1, row=2, columnspan=3)

        Label(self, text='Please select a starting hour.').grid(column=1, row=3, columnspan=3)
        self.start_hour_box = Spinbox(self, from_=00, to=23, format="%02.0f")
        self.start_hour_box.grid(column=1, row=4, columnspan=3)
        Label(self, text='Please select a starting minute.').grid(column=1, row=5, columnspan=3)
        self.start_minute_box = Spinbox(self, from_=00, to=60, format="%02.0f")
        self.start_minute_box.grid(column=1, row=6, columnspan=3)

        Label(self, text='Please select an ending date.').grid(column=1, row=7, columnspan=3)
        self.end_date_box = DateEntry(self, date_pattern='m/d/y')
        self.end_date_box.grid(column=1, row=8, columnspan=3)

        Label(self, text='Please select an ending hour.').grid(column=1, row=9, columnspan=3)
        self.end_hour_box = Spinbox(self, from_=00, to=23, format="%02.0f")
        self.end_hour_box.grid(column=1, row=10, columnspan=3)
        Label(self, text='Please select an ending minute.').grid(column=1, row=11, columnspan=3)
        self.end_minute_box = Spinbox(self, from_=00, to=60, format="%02.0f")
        self.end_minute_box.grid(column=1, row=12, columnspan=3)

        Label(self, text='''
            Please select an interval.\n
            Intervals other than 15 minuts are likely to fail.
        ''').grid(column=1, row=13, columnspan=3)
        self.resolution_table = {
            '1 minute':'10',
            '5 minutes':'20',
            '15 minutes':'40',
            '30 minutes':'50',
            '1 hour':'60',
            '1 day':'70',
            '1 month':'90'
        }
        self.interval_box = Combobox(self, values=list(self.resolution_table))
        self.interval_box.grid(column=1, row=14, columnspan=3)
        self.interval_box.current(2)

        Label(self, text='Please select the path to save the file.').grid(column=1, row=15, columnspan=3)

        self.folderpath_box = Entry(self, width=50)
        self.folderpath_box.insert('end', cwd)
        self.folderpath_box.grid(column=1, row=16, columnspan=2)
        Button(self, text='browse', command=lambda : (
            reportpath := askdirectory(initialdir=cwd, title='Select a folder', parent=self),
            (self.folderpath_box.delete(0, 'end'), self.folderpath_box.insert('end', reportpath)) if reportpath else 0
        )).grid(column=3, row=16)
        
        Label(self, text='Please enter the fliename.').grid(column=1, row=17, columnspan=3)
        self.filename_box = Entry(self, width=50)
        self.filename_box.insert('end', 'data_downloaded')
        self.filename_box.grid(column=1, row=18, columnspan=2)
        Label(self, text='.xlsx').grid(column=3, row=18)

        self.outliers_variable = BooleanVar(self)
        self.outliers_variable.set(False)
        Checkbutton(self, text='remove outliers', variable=self.outliers_variable).grid(column=2, row=19)

        Button(self, text='create', command=lambda : (
            start_time := str(self.start_hour_box.get()) + ':' + str(self.start_minute_box.get()) + ':00',
            start_datetime := self.start_date_box.get() + ' ' + start_time,
            end_time := str(self.end_hour_box.get()) + ':' + str(self.end_minute_box.get()) + ':00',
            end_datetime := self.end_date_box.get() + ' ' + end_time,
            filepath := self.folderpath_box.get()+'/'+self.filename_box.get()+'.xlsx',
            self.__get_data(start_datetime, end_datetime,filepath)
        )).grid(columnspan=4)

        self.result_box = Label(self)
        self.result_box.grid(columnspan=4)
        
        Button(self, text='back', command=self.destroy).grid(columnspan=4)

        self.mainloop()

    def __get_data(self, start_str, end_str, filepath):
        if not os.path.isdir(os.path.dirname(filepath)):
            self.result_box.config(text='Folder in the filepath does not exist.')
            self.update()
            return
        
        if os.path.isfile(filepath):
            if not askyesno(title='File Exist', message='File exist. Do you want to overwrite it?', parent=self):
                self.result_box.config(text='Cancelled')
                self.update()
                return
        
        meters = self.meters_box.get('1.0','end').replace('\r', '').split('\n')
        meters = [meter for meter in meters if len(meter) > 1]

        start_date = (pd.to_datetime(start_str) - pd.Timedelta(seconds=1)).strftime('%#m%%2F%#d%%2F%Y%%20%H%%3A%M%%3A%S')
        end_date = pd.to_datetime(end_str).strftime('%#m%%2F%#d%%2F%Y%%20%H%%3A%M%%3A%S')
        
        token = self._get_token()
        df = pd.DataFrame()
        error_meters = []

        for count, meter in enumerate(meters):
            self.result_box.config(text='progress '+str(count)+'/'+str(len(meters))+' downloading '+meter)
            self.update()

            baselink = 'https://eadvantage.siemens.com/remote/release/meter/' + meter + '/consumption'
            resolution  = self.resolution_table[self.interval_box.get()]
            link = baselink + '?dateFrom=' + start_date + '&dateTo=' + end_date + '&resolution=' + resolution
            response = requests.get(link, headers={'Authorization': 'bearer '+token})

            if response.status_code != 200:
                token = self._get_token(backup=True)
                response = requests.get(link, headers={'Authorization': 'bearer '+token})
                if response.status_code != 200:
                    print('cannot download the required data (' + meter + ') with error code ' + str(response.status_code))
                    error_meters.append(meter)
                    continue

            info = response.json()
            df_meter = pd.DataFrame(info.pop('items'))
            if df_meter.empty:
                print('the required data (' + meter + ') is empty')
                error_meters.append(meter)
                continue

            df_meter.set_index('timestamp', inplace=True)
            df_meter.rename(columns={'value':info['meterName']}, inplace=True)
            df = pd.concat([df, df_meter], axis=1)

        df.index = pd.to_datetime(df.index)

        if self.outliers_variable.get():
            self.result_box.config(text='processing outliers')
            self.update()

            def remove_outliers(col):
                if ('Temperature' in col.name) | ('Air' in col.name):
                    mean = col.mean()
                    sd = col.std()
                    return col.clip(max(0, mean-(3*sd)), mean+(3*sd))
                if 'On/Off' in col.name:
                    return col.clip(0, 1)
                if 'Freq' in col.name:
                    return col.clip(0, 50)
                if ('Valve' in col.name) | ('Humidity' in col.name):
                    return col.clip(0, 100)
                return col
            df = df.apply(remove_outliers)

        if error_meters == meters:
            result =  'Cannot download any required data. Plaese try other meter IDs or resolutions and check the time.'
            self.result_box.config(text=result)
            self.update()
            return
        
        # Write each dataframe to a different worksheet.
        self.result_box.config(text='saving data to excel')
        self.update()
        with pd.ExcelWriter(filepath, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Data')

        if not error_meters:
            result =  'File saved!'
        else:
            result =  'File saved! Cannot download: ' + ', '.join(error_meters) + '. Plaese try other meter IDs.'
        self.result_box.config(text=result)
        self.update()

class WindowDeleteMeter(Window):
    def __init__(self, menu):
        self.master = menu
        super().__init__(self.master)

        self.title('Delete meter from Eadvantage')

        Label(self, text='Delete meter from Eadvantage', font=("Arial", 25)).grid()
        
        Label(self, text='Please enter the meter IDs and separate them with and only with next line.').grid()
        self.meters_box = ScrolledText(self, width=30, height=26)
        self.meters_box.grid()

        Label(self, text='The meters will be deleted permanently.').grid()
        Label(self, text='Please type "DELETE" to confirm the deletion.').grid()

        self.delete_box = Entry(self, width=10)
        self.delete_box.grid()

        Button(self, text='delete', command=self.__delete_data).grid()

        self.result_box = Label(self)
        self.result_box.grid()
        
        Button(self, text='exit', command=self.destroy).grid()

        self.mainloop()

    def __delete_data(self):

        if self.delete_box.get() != 'DELETE':
            showerror(title='Error', message='Please input "DELETE" in the confirmation box', parent=self)
            return
        self.delete_box.delete(0, 'end')
        
        if not askyesno(title='Warning', message='Are you sure you want to delete these meters?', parent=self):
            return
        
        meters = self.meters_box.get('1.0','end').replace('\r', '').split('\n')
        meters = [meter for meter in meters if len(meter) > 1]
        
        token = self._get_token()
        error_meters = []

        for count, root in enumerate(meters):
            self.result_box.config(text='progress '+str(count)+'/'+str(len(meters))+' deleting '+root)
            self.update()

            link = 'https://eadvantage.siemens.com/remote/release/meter/' + root
            response = requests.delete(link, headers={'Authorization': 'bearer '+token})

            if response.status_code not in [200, 204]:
                token = self._get_token(backup=True)
                response = requests.delete(link, headers={'Authorization': 'bearer '+token})
                if response.status_code not in [200, 204]:
                    print('cannot delete the required data (' + root + ') with error code ' + str(response.status_code))
                    error_meters.append(root)
                    continue

        if not error_meters:
            result =  'Meters deleted!'
        elif error_meters != meters:
            result =  'Meters deleted! Cannot delete: ' + ', '.join(error_meters) + '. Plaese try other meters.'
        else:
            result =  'Cannot delete any required meter. Plaese try other meters.'
        self.result_box.config(text=result)
        self.update()


if __name__ == '__main__':
    sys.stdout = open(cwd+'/log.txt', 'a')
    sys.stderr = sys.stdout

    print('[' + str(pd.to_datetime('today')) + ']')
    Menu()

    sys.stdout.close()
    sys.stderr.close()
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__