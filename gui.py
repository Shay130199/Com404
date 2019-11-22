from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        self.configure(height=500,
                       width=500)
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
    def __add_heading_label(self):
        #create
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)

        # style
        self.heading_label.configure(font="Arial 24",
                                     text="ENTRANCE TICKET")

        
    def __add_instruction_label(self):
        #create
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0, sticky=W)

        #style
        self.heading_label.configure(font="Arial 20",
                                     text="How many tickets are needed?")
        
    def __add_tickets_entry(self):
        #create
         self.tickets_entry = Entry()
         self.tickets_entry.grid(row=2, column=0)
         self.tickets_entry.configure(width=40)
        
    def __add_buy_button(self):
        #create
        self.buy_button = Button()
        self.buy_button.grid(row=3, column=0,)
        self.buy_button.configure(bg="#fcc",
                                      text="Subscribe",
                                      width=40)

        
 	
