from pandas import DataFrame, Timedelta, concat, to_datetime, ExcelWriter
import requests
import sys
import os
from tkinter import Tk, Entry, Label, Button, Spinbox, BooleanVar, Checkbutton
from tkcalendar import DateEntry
from tkinter.filedialog import askdirectory
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox
from tkinter.messagebox import askyesno

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))


def get_token():
    token_url = 'https://eadvantage.siemens.com/uaa/oauth/token'
    client_id = 'navigator.admin_1514.user_81261.All_Access_API'
    client_secret = '3@)vgyoc,D_k-[ZlNMH:AOJ~,.S08ixatA2S/Fxl$vf?C2l!qs6SaP.#1,9mAmQl'
    token_response = requests.post(token_url, data={"grant_type": "client_credentials"}, auth=(client_id, client_secret))
    return token_response.json()['access_token']


class Window_download(Tk):
    def __init__(self):
        super().__init__()

        self.title('Save data from Eadvantage')

        Label(self, text='Save data from Eadvantage', font=("Arial", 25)).grid(column=0, row=0, columnspan=4)
        
        Label(self, text='''
            Please enter the meter IDs and separate them with and only with next line.
        ''').grid(column=0, row=1)
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
        
        Button(self, text='exit', command=self.quit).grid(columnspan=4)

        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.mainloop()

    def __get_data(self, start_str, end_str, filepath):
        if not os.path.isdir(os.path.dirname(filepath)):
            self.result_box.config(text='Folder in the filepath does not exist.')
            self.update()
            return
        
        if os.path.isfile(filepath):
            if not askyesno(title='File Exist', message='File exist. Are you sure that you want to overwrite it?'):
                self.result_box.config(text='Cancelled')
                self.update()
                return
        
        meters = self.meters_box.get('1.0','end').replace('\r', '').split('\n')
        meters = [meter for meter in meters if len(meter) > 1]

        start_date = (to_datetime(start_str) - Timedelta(seconds=1)).strftime('%#m%%2F%#d%%2F%Y%%20%H%%3A%M%%3A%S')
        end_date = to_datetime(end_str).strftime('%#m%%2F%#d%%2F%Y%%20%H%%3A%M%%3A%S')
        token = get_token()
        df = DataFrame()
        error_meters = []

        for count, meter in enumerate(meters):
            self.result_box.config(text='progress '+str(count)+'/'+str(len(meters))+' downloading '+meter)
            self.update()

            baselink = 'https://eadvantage.siemens.com/remote/release/meter/' + meter + '/consumption'
            resolution  = self.resolution_table[self.interval_box.get()]
            link = baselink + '?dateFrom=' + start_date + '&dateTo=' + end_date + '&resolution=' + resolution
            print(link)

            response = requests.get(link, headers={'Authorization': 'bearer {}'.format(token)})

            if response.status_code != 200:
                token = get_token()
                response = requests.get(link, headers={'Authorization': 'bearer {}'.format(token)})
                if response.status_code != 200:
                    print('cannot download the required data (' + meter + ') with error code ' + str(response.status_code))
                    error_meters.append(meter)
                    continue

            info = response.json()
            df_meter = DataFrame(info.pop('items'))
            if df_meter.empty:
                print('the required data (' + meter + ') is empty')
                error_meters.append(meter)
                continue

            df_meter.set_index('timestamp', inplace=True)
            df_meter.rename(columns={'value':info['meterName']}, inplace=True)
            df = concat([df, df_meter], axis=1)

        df.index = to_datetime(df.index)

        if self.outliers_variable.get():
            self.result_box.config(text='processing outliers')
            self.update()

            def remove_outliers(col):
                if ('Temperature' in col.name) | ('Air' in col.name):
                    mean = col.mean()
                    sd = col.std()
                    return col.clip(mean-(3*sd), mean+(3*sd))
                if 'On/Off' in col.name:
                    return col.clip(upper=1)
                if 'Freq' in col.name:
                    return col.clip(upper=50)
                if 'Cooling Valve' in col.name:
                    return col.clip(upper=100)
                return col
            df = df.clip(lower=0).apply(remove_outliers)

        if error_meters == meters:
            result =  'Cannot download any required data. Plaese try other meter IDs or resolutions and check the time.'
            self.result_box.config(text=result)
            self.update()
            return
        
        # Write each dataframe to a different worksheet.
        self.result_box.config(text='saving data to excel')
        self.update()
        with ExcelWriter(filepath, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Data')

        if not error_meters:
            result =  'File saved!'
        else:
            result =  'File saved! Cannot download: ' + ', '.join(error_meters) + '. Plaese try other meter IDs.'
        self.result_box.config(text=result)
        self.update()

if __name__ == '__main__':
    # sys.stdout = open(cwd+'/log.txt', 'a')
    # sys.stderr = sys.stdout

    print('[' + str(to_datetime('today')) + ']')
    Window_download()

    # sys.stdout.close()
    # sys.stderr.close()
    # sys.stdout = sys.__stdout__
    # sys.stderr = sys.__stderr__