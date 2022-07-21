import os
from tkinter import *
from tkinter import ttk
import sys
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

class Data_Functions:

    def __init__(self,file):
        self.file = file
        data = open(file)
        data_extract = data.read().split()
        self.north = data_extract[0]
        self.pitstop = data_extract[1]
        self.northmezz1 = data_extract[2]
        self.northmezz2 = data_extract[3]
        self.northmezz3 = data_extract[4]
        self.sheffield = data_extract[5]
        data.close()

    def run(self,ipaddress,widget,row_value):
        ping = os.system(f'ping {ipaddress} -n 1 -w 1')
        if ping == 1:
            widget = Label(image=red,borderwidth=0, highlightthickness=0)
            widget.grid(row = row_value, column = 1,padx=25)
            Tk.update(window)
        else:
            widget = Label(image=green,borderwidth=0, highlightthickness=0)
            widget.grid(row = row_value, column = 1,padx=25)
            Tk.update(window)

    def update(self,n,p,n1,n2,n3,s):
        self.north = n
        self.pitstop = p
        self.northmezz1 = n1
        self.northmezz2 = n2
        self.northmezz3 = n3
        self.sheffeld = s
        self.run(self.north,north_status, 1)
        self.run(self.pitstop,pitstop_status, 2)
        self.run(self.northmezz1,northmezz1_status, 3)
        self.run(self.northmezz2,northmezz2_status, 4)
        self.run(self.northmezz3,northmezz3_status, 5)
        self.run(self.sheffield,north_status, 6)
        Tk.update(window)

    def save(self,n,p,n1,n2,n3,s):
        data = open(self.file,'w')
        data.write(n+'\n')
        data.write(p+'\n')
        data.write(n1+'\n')
        data.write(n2+'\n')
        data.write(n3+'\n')
        data.write(s+'\n')
        data.close()
        self.update(n,p,n1,n2,n,s)


def Error(message):
    error = Tk()
    error.resizable(0,0)
    error.title('iTime Status: Settings')
    error['background']='#F48500'
    error.iconbitmap('logo.ico')
    logo = PhotoImage(file="error.png")
    error_image = Label(image=logo,borderwidth=0, highlightthickness=0)
    errormessage = Label(error,text=message,bg='#F48500')
    errormessage.config(font=('McLaren Bespoke Bold',14))
    error_image.grid(row = 0, column = 0,pady=15)
    errormessage.grid(row = 1, column = 0,padx=10)
    error.mainloop()
    sys.exit()

def Settings():  
    root = Toplevel(window)
    root.grab_set()
    root.title('iTime Status: Settings')
    root['background']='#F48500'
    root.iconbitmap('logo.ico')
    root.resizable(0,0)
    
    title = Label(root, text='  Settings',bg="#F48500")
    title.config(font=('McLaren Bespoke Bold',18))

    north_setting = Label(root, text='North: ',bg="#F48500")
    north_setting.config(font=('McLaren Bespoke',10))
    north_setting_input = ttk.Entry(root)
    north_setting_input.delete(0, END)
    north_setting_input.insert(0, data.north)

    pitstop_setting = Label(root, text='Pitstop: ',bg="#F48500")
    pitstop_setting.config(font=('McLaren Bespoke',10))
    pitstop_setting_input = ttk.Entry(root, text=data.pitstop)
    pitstop_setting_input.delete(0, END)
    pitstop_setting_input.insert(0, data.pitstop)

    northmezz1_setting = Label(root, text='NorthMezz1: ',bg='#F48500')
    northmezz1_setting.config(font=('McLaren Bespoke',10))
    northmezz1_setting_input = ttk.Entry(root, text=data.northmezz1)
    northmezz1_setting_input.delete(0, END)
    northmezz1_setting_input.insert(0, data.northmezz1)

    northmezz2_setting = Label(root, text='NorthMezz2: ',bg='#F48500')
    northmezz2_setting.config(font=('McLaren Bespoke',10))
    northmezz2_setting_input = ttk.Entry(root, text=data.northmezz2)
    northmezz2_setting_input.delete(0, END)
    northmezz2_setting_input.insert(0, data.northmezz2)

    northmezz3_setting = Label(root, text='NorthMezz3: ',bg='#F48500')
    northmezz3_setting.config(font=('McLaren Bespoke',10))
    northmezz3_setting_input = ttk.Entry(root, text=data.northmezz3)
    northmezz3_setting_input.delete(0, END)
    northmezz3_setting_input.insert(0, data.northmezz3)

    sheffield_setting = Label(root, text='Sheffield: ',bg='#F48500')
    sheffield_setting.config(font=('McLaren Bespoke',10))
    sheffield_setting_input = ttk.Entry(root, text=data.sheffield)
    sheffield_setting_input.delete(0, END)
    sheffield_setting_input.insert(0, data.sheffield)

    update_button = ttk.Button(root, text = 'Run',command= lambda: data.update(north_setting_input.get(),pitstop_setting_input.get(),northmezz1_setting_input.get(),northmezz2_setting_input.get(),northmezz3_setting_input.get(),sheffield_setting_input.get()))
    save_button = ttk.Button(root, text = 'Save',command= lambda: data.save(north_setting_input.get(),pitstop_setting_input.get(),northmezz1_setting_input.get(),northmezz2_setting_input.get(),northmezz3_setting_input.get(),sheffield_setting_input.get()))

    title.grid(row = 0, column = 0, columnspan = 2, padx=10, pady=10)
    north_setting.grid(row = 1,column = 0, pady=5, padx = 10, stick=W)
    north_setting_input.grid(row = 1, column = 1, pady=5,padx=18)
    pitstop_setting.grid(row = 2, column = 0, pady=5, padx = 10, stick=W)
    pitstop_setting_input.grid(row = 2, column = 1, pady=5, padx=18)
    northmezz1_setting.grid(row = 3, column = 0, pady=5, padx = 10, stick=W)
    northmezz1_setting_input.grid(row = 3, column = 1, pady=5, padx=18)
    northmezz2_setting.grid(row = 4, column = 0, pady=5, padx = 10, stick=W)
    northmezz2_setting_input.grid(row = 4, column = 1, pady=5, padx=18)
    northmezz3_setting.grid(row = 5, column = 0, pady=5, padx = 10, stick=W)
    northmezz3_setting_input.grid(row = 5, column = 1, pady=5, padx=18)
    sheffield_setting.grid(row = 6, column = 0, pady=5, padx = 10, stick=W)
    sheffield_setting_input.grid(row = 6, column = 1, pady=5, padx=18)
    update_button.grid(row = 7, column = 0, pady = 18, padx = 20, columnspan=2, sticky = W)
    save_button.grid(row = 7, column = 1, pady= 18, padx = 20, columnspan=2, sticky = E)

    root.mainloop()

try:   
    data = Data_Functions('ipaddress.txt')
except IndexError:
    Error('Error: No content in settings file')
except FileNotFoundError:
    Error('Error: Settings file not found')
except:
    sys.exit()

window = Tk()
window.resizable(0,0)
window.title('iTime Status')
window['background']='#F48500'
window.iconbitmap('logo.ico')

green = PhotoImage(file="Green_light.png")
red = PhotoImage(file="Red_light.png")
logo = PhotoImage(file="McLaren_Logo_1.png")
logo_label = Label(image=logo,borderwidth=0, highlightthickness=0)

title = Label(window, text='  iTime Status',bg="#F48500")
title.config(font=('McLaren Bespoke Bold',18))

north = Label(window, text='North ',bg="#F48500")
north.config(font=('McLaren Bespoke',14))
north_status = Label(window)

pitstop = Label(window, text='Pitstop ',bg="#F48500")
pitstop.config(font=('McLaren Bespoke',14))
pitstop_status = Label(window)

northmezz1 = Label(window, text='North Mezz 1 ',bg="#F48500")
northmezz1.config(font=('McLaren Bespoke',14))
northmezz1_status = Label(window)

northmezz2 = Label(window, text='North Mezz 2 ',bg="#F48500")
northmezz2.config(font=('McLaren Bespoke',14))
northmezz2_status = Label(window)

northmezz3 = Label(window, text='North Mezz 3 ',bg="#F48500")
northmezz3.config(font=('McLaren Bespoke',14))
northmezz3_status = Label(window)

sheffield = Label(window, text='Sheffield ',bg="#F48500")
sheffield.config(font=('McLaren Bespoke',14))
sheffield_status = Label(window)

settings_button = ttk.Button(window, text='Settings',command=Settings)

title.grid(row = 0, column = 0, padx=10,pady=10)
logo_label.grid(row = 0, column = 1)
north.grid(row = 1, column = 0,padx=10,sticky=W)
pitstop.grid(row = 2, column = 0,padx=10,sticky=W)
northmezz1.grid(row = 3, column = 0,padx=10,sticky=W)
northmezz2.grid(row = 4, column = 0,padx=10,sticky=W)
northmezz3.grid(row = 5, column = 0,padx=10,sticky=W)
sheffield.grid(row = 6, column = 0,padx=10,sticky=W)
settings_button.grid(row=7,column=0, columnspan=2, pady=18)

data.run(data.north,north_status, 1)
data.run(data.pitstop,pitstop_status, 2)
data.run(data.northmezz1,northmezz1_status, 3)
data.run(data.northmezz2,northmezz2_status, 4)
data.run(data.northmezz3,northmezz3_status, 5)
data.run(data.sheffield,north_status, 6)

window.mainloop()

