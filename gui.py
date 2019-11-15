from tkinter import *

class Gui(Tk):


  # initialise window
  def __init__(self):
    super().__init__()

    # set window attributes
    self.title("Newsletter")
    self.configure(bg="#999999 ",
                   height=500, 
                   width=500)
                   
    self.__add_heading_label()


  def __add_heading_label(self):
    # create   
    self.heading_label = Label()
    self.heading_label.place(x=0, y=0)
    
    # style
    self.heading_label.configure(font="Arial 24",
                                 text="Recieve Our Newsletter!")
    

  def add_heading_label(self):
      #create
      self.heading_label = Label()
      slef.heading_label.pack()

      #style
      self.heading_label.configure(font="Arial 24",
                                   text="This is a heading.")


                          
    

    


  
