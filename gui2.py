def __add_buy_button(self):

    # create
    self.buy_button = Button()
    self.buy_button.grid(row=3, column=0)
        
    # style
    self.buy_button.configure(text="Submit")
        
    # events
    self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)
        
 
def __buy_button_clicked(self, event):
     pass

from tkinter import *
from tkinter import messagebox

...

def __buy_button_clicked(self, event):
    messagebox.showinfo("Purchased!", "You have purchased the tickets!")
