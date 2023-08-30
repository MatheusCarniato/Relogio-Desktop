from customtkinter import CTk,CTkLabel
from time import strftime
from datetime import date
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR')

class Clock(CTk,CTkLabel):
    def __init__(self, title):
        self.title = title

    def clock(self):
        '''Graphical interface, label position'''
        self.root = CTk()
        self.root.geometry("250x200")
        self.root.title("Relógio "+ self.title)
        self.label_clock = CTkLabel(self.root)
        self.label_clock.pack(anchor = 'center',fill='both', expand=True)
        self.label_date = CTkLabel(self.root)
        self.label_date.pack(anchor = 'center',fill='both', expand=True)
        self.label_day = CTkLabel(self.root)
        self.label_day.pack(anchor = 'center',fill='both', expand=True)
        self.root.bind("<Configure>", self.update)
        self.root.mainloop()

    def update(self, event=None):
        '''System update'''
        self.str = strftime("%H:%M:%S")
        self.date_now = date.today()
        self.date_now_for = self.date_now.strftime('%d/%m/%Y')
        self.day_now = self.date_now.strftime("%A")
        self.label_clock.configure(font=('calibri', self.responsiveness(), 'bold'), text= self.str )
        self.label_date.configure(font=('calibri', int(self.responsiveness())/2, 'bold'), text = self.date_now_for)
        self.label_day.configure(font=('calibri', int(self.responsiveness())/2, 'bold'), text = self.day_now)
        self.label_clock.after(1000,self.update)
    
    def responsiveness(self):
        '''Responsiveness'''
        self.width = self.root.winfo_width()
        self.height = self.root.winfo_height()
        self.font = int(min(self.width, self.height) / 3)
        return self.font

if __name__ == '__main__':    
    relogio = Clock("Descktop")
    relogio.clock()