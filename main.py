from customtkinter import CTk,CTkLabel
from time import strftime

class Clock(CTk,CTkLabel):
    def __init__(self,title):
        self.title = title

    def clock(self):
        '''Creates the entire graphic structure of the clock'''
        self.root = CTk()
        self.root.geometry("250x70")
        self.root.title("Relógio " + self.title)
        self.label = CTkLabel(self.root,font =('calibri', 60, 'bold'))
        self.label.pack(anchor = 'center',fill='both', expand=True)
        self.root.bind("<Configure>", self.update)
        self.update()
        self.root.mainloop()
    
    def update(self, event=None):
        '''Update the clock and responsiveness'''
        self.width = self.root.winfo_width()
        self.height = self.root.winfo_height()
        self.font = int(min(self.width, self.height) / 3)
        self.label.configure(font=('calibri', self.font, 'bold'))
        self.str = strftime("%H:%M:%S")
        self.label.configure(text = self.str)
        self.label.after(1000,self.update)
    
if __name__ == '__main__':   
    relogio = Clock("Desktop")
    relogio.clock()