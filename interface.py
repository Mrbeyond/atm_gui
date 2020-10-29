from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from PIL import Image, ImageTk
class Interface:
  def __init__(self):
    self.main = Tk()
    self.image = Image.open("crown.jpg")
    self.image = self.image.resize((20,20), Image.ANTIALIAS)
    self.photo = ImageTk.PhotoImage(self.image) 
    # self.style = Style()
    # self.style.configure("BW.TLabel", foreground="white", background="blue")
    # self.but = Button(self.main,text="button", image=self.photo, compound=RIGHT, style="BW.TLabel")

    self.numKeys = Frame(self.main)
    self.stage = "default"
    
    self.screen = Frame(self.main)
    self.screen.grid(row=0, column=1, rowspan=4, columnspan=9, sticky="nsew")
   



    self.signupFrame = Frame(self.screen)    
    self.loginFrame = Frame(self.screen)
    self.transFrame = Frame(self.screen)

  
  def leftButtonsSection(self):
    """
      collection screen's left side buttons
    """
    self.lKeys = Frame(self.main)
    self.lKeys.grid(row=0, column=0)

    self.Lsty = Style()
    self.Lsty.configure("L.TButton", font=('Helvetica', 10, 'bold'))
    self.lk1 = Button(self.lKeys, text=">", style="L.TButton", command=self.lOne)
    self.lk1.grid(row=0, column=0, pady=4, ipady=10);
    self.lk2 = Button(self.lKeys, text=">", style="L.TButton", command=self.lTwo)
    self.lk2.grid(row=1, column=0, pady=4, ipady=10);
    self.lk3 = Button(self.lKeys, text=">", style="L.TButton", command=self.lThree)
    self.lk3.grid(row=2, column=0, pady=4, ipady=10);
    self.lk4 = Button(self.lKeys, text=">", style="L.TButton", command=self.lFour)
    self.lk4.grid(row=3, column=0, pady=4, ipady=10);

  def rightButtonsSection(self):
    """
      collection screen's right side buttons
    """
    self.Lsty = Style()
    self.Lsty.configure("R.TButton", font=('Helvetica', 10, 'bold'))
    self.rKeys = Frame(self.main)
    self.rKeys.grid(row=0, column=10)
    self.rk1 = Button(self.rKeys, text="<", style="R.TButton")
    self.rk1.grid(row=0, column=0, pady=4, ipady=10);
    self.rk2 = Button(self.rKeys, text="<", style="R.TButton", command=self.rTwo)
    self.rk2.grid(row=1, column=0, pady=4, ipady=10);
    self.rk3 = Button(self.rKeys, text="<", style="R.TButton",)
    self.rk3.grid(row=2, column=0, pady=4, ipady=10);
    self.rk4 = Button(self.rKeys, text="<", style="R.TButton", command=self.rFour)
    self.rk4.grid(row=3, column=0, pady=4, ipady=10);


  def welcomePart(self):
    """
      Default screen message for users before any activity
    """
    self.welSty = Style()
    self.welSty.configure("F.TFrame", background="cyan", font=('Helvetica', 10, 'bold'))
    self.initFrame = Frame(self.screen, style="F.TFrame")
    self.initFrame.grid(row=0, column=0,rowspan=4, columnspan=9, sticky='nsew')

    self.welSty = Style()
    self.welSty.configure("W.TLabel",  font=('Helvetica', 15, 'bold'))

    self.initMessage = Label(self.initFrame, anchor=CENTER, text=" You are welcome please choose an option to continue ", style="W.TLabel")
    self.initMessage.grid(row=0, column=0, columnspan=10, ipady=8, sticky='nsew')

    self.initUpLabel = Label(self.initFrame, text=" Sign Up ", style="W.TLabel")
    self.initUpLabel.grid(row=1, column=0, ipady=20, sticky='nsew')

    self.initLoginLabel = Label(self.initFrame, text=" Login ", anchor=E  , style="W.TLabel")
    self.initLoginLabel.grid(row=1, column=9, sticky='nsew')

  def rOne(self):
    pass

  def rTwo(self):
    if(self.stage == "default" and self.stage != 'login'):
      self.initFrame.grid_remove()
      self.loginPart()
      self.stage = "login"
    else:
      pass
  
  def rTThree(self):
    pass

  def rFour(self):
    pass

  def lOne(self):
    pass

  def lTwo(self):
    if(self.stage == "default" and self.stage != "signup"):
      self.initFrame.grid_remove()
      self.signupPart()
      self.stage = "signup"
    else:
      pass
    

  def lThree(self):
    if( self.stage == "login"):
      self.loginFrame.grid_remove()
      self.welcomePart()
      self.stage = "default"
    else:
      pass

  def lFour(self):
    if( self.stage == "signup"):
      self.signupFrame.grid_remove()
      self.welcomePart()
      self.stage = "default"
    else:
      pass


  def loginPart(self):
    """
      Container for login section
    """
    self.loginStyle = Style()
    self.loginStyle.configure("Log.TLabel", font=('Helvetica', 13, 'bold'))
    self.loginFrame.grid(row=0, column=0,rowspan=4, columnspan=9, sticky="nsew")

    Label(self.loginFrame, text="First name", style="Log.TLabel").grid(row=0, column=0, ipady=15)
    self.loginNameEntry = Entry(self.loginFrame)
    self.loginNameEntry.grid(row=0, column=6, columnspan=3,sticky="ew")
    Label(self.loginFrame, text="Password", style="Log.TLabel").grid(row=1, column=0, ipady=15)
    self.loginPasswordEntry = Entry(self.loginFrame)
    self.loginPasswordEntry.grid(row=1, column=6, columnspan=3,sticky="ew")
    Label(self.loginFrame, text="Back", style="Log.TLabel").grid(row=2, column=0)
    Label(self.loginFrame, text="Continue", style="Log.TLabel", anchor=E).grid(row=2, column=9, ipady=10)

  def signupPart(self): 
    """
      Container for signup section
    """
    print("here")
    self.loginStyle = Style()
    self.loginStyle.configure("Log.TLabel", font=('Helvetica', 13, 'bold'))

    self.signupFrame.grid(row=0, column=0,rowspan=4, columnspan=9, sticky="nsew")

    Label(self.signupFrame, text="First name", style="Log.TLabel").grid(row=0, column=0, ipady=15)
    self.signupFName = Entry(self.signupFrame)
    self.signupFName.grid(row=0, column=6, columnspan=3,sticky="ew")

    Label(self.signupFrame, text="Last name", style="Log.TLabel").grid(row=1, column=0, ipady=15)
    self.signupLName = Entry(self.signupFrame)
    self.signupLName.grid(row=1, column=6, columnspan=3,sticky="ew")

    Label(self.signupFrame, text="Password", style="Log.TLabel").grid(row=2, column=0, ipady=15)
    self.loginPasswordEntry = Entry(self.signupFrame)
    self.loginPasswordEntry.grid(row=2, column=6, columnspan=3,sticky="ew")

    Label(self.signupFrame, text="Back", style="Log.TLabel").grid(row=3, column=0)
    Label(self.signupFrame, text="Continue", style="Log.TLabel", anchor=E).grid(row=3, column=9, ipady=10)

  def start(self):
    self.leftButtonsSection()
    self.rightButtonsSection()
    self.welcomePart()

    self.main.mainloop()


Interface().start()