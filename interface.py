from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from validators import Validators as vld
from BankingBaisc import BankingBasic as api
from PIL import Image, ImageTk
class Interface:
  def __init__(self):
    self.main = Tk()
    self.image = Image.open("crown.jpg")
    self.image = self.image.resize((20,20), Image.ANTIALIAS)
    self.photo = ImageTk.PhotoImage(self.image) 

    self.customer = None
    self.accountNum = None
    # self.style = Style()
    # self.style.configure("BW.TLabel", foreground="white", background="blue")
    # self.but = Button(self.main,text="button", image=self.photo, compound=RIGHT, style="BW.TLabel")

    self.numKeys = Frame(self.main)
    self.stage = "default"
    self.lName = StringVar()
    self.lKey = StringVar()
    self.isLNError = True
    self.isLKError = True
    self.ufName = StringVar()
    self.ulName= StringVar()
    self.uKey = StringVar()
    self.postOperationMessage = StringVar()
    self.wAmount = StringVar()
    self.transAccount = StringVar()
    self.transAmount = StringVar()
    #Other Amount Error oAError
    self.oAError = True
    self.isUFNError = True
    self.isULNError = True
    self.isUKError = True
    self.isTACError = True
    self.isTAMError = True
    
    self.ScreenSty = Style()
    self.ScreenSty.configure("SCR.TFrame", bd=100, relief="sunken")
    self.screen = Frame(self.main, style="SCR.TFrame")
    self.screen.grid(row=0, column=1, rowspan=4, columnspan=9, sticky="nsew")
   
    self.loginStyle = Style()
    self.loginStyle.configure("Error.TLabel", foreground="red", font=('Helvetica', 8, 'bold'))
    



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
    self.rk1 = Button(self.rKeys, text="<", style="R.TButton", comman=self.rOne)
    self.rk1.grid(row=0, column=0, pady=4, ipady=10);
    self.rk2 = Button(self.rKeys, text="<", style="R.TButton", command=self.rTwo)
    self.rk2.grid(row=1, column=0, pady=4, ipady=10);
    self.rk3 = Button(self.rKeys, text="<", style="R.TButton",  command= self.rThree)
    self.rk3.grid(row=2, column=0, pady=4, ipady=10);
    self.rk4 = Button(self.rKeys, text="<", style="R.TButton", command=self.rFour)
    self.rk4.grid(row=3, column=0, pady=4, ipady=10);


  def welcomePart(self):
    """
      Default screen message for users before any activity
    """
    self.welSty = Style()
    self.welSty.configure("F.TFrame", font=('Helvetica', 10, 'bold'))
    self.initFrame = Frame(self.screen, style="F.TFrame")
    self.initFrame.grid(sticky='nsew')

    self.welSty = Style()
    self.welSty.configure("W.TLabel",  font=('Helvetica', 15, 'bold'))

    Label(self.initFrame, text="Please choose an option to continue", style="W.TLabel",\
      anchor=CENTER).grid( row=0, column=0, padx=(60,0), ipady=8, sticky='nsew')

    self.initUpLabel = Label(self.initFrame, text=" Sign Up ", style="W.TLabel")
    self.initUpLabel.grid(row=1, column=0, ipady=20,  sticky='nsew')

    self.initLoginLabel = Label(self.initFrame, text=" Login ", anchor=E  , style="W.TLabel")
    self.initLoginLabel.grid(row=1, column=1,  sticky='nsew')

  def rOne(self):
    if(self.stage=='mainwithdraw'):
      self.withdrawFrame.grid_remove()
      self.withdrawNow(20000)
    elif(self.stage == 'operations'):
      self.transFrame.grid_remove()
      self.transferPart()
      self.stage = 'transfer'
    else:
      pass

  def rTwo(self):
    if(self.stage == "default" and self.stage != 'login'):
      self.initFrame.grid_remove()
      self.loginPart()
      self.stage = "login"
    elif(self.stage == "newcustomer"):
      self.newCustomerFrame.grid_remove()
      self.operationsPart()
      self.stage = 'operations'
    elif(self.stage=='mainwithdraw'):
      self.withdrawFrame.grid_remove()
      self.withdrawNow(50000)
    elif(self.stage == "postoperation"):
      self.postOperationFrame.grid_remove()
      self.operationsPart()
      self.stage = "operations" 
    elif(self.stage == "operations"):
      self.transFrame.grid_remove()
      self.checkBalance() 
    else:
      pass
  
  def rThree(self):
    if(self.stage == "login"):
      self.submitLogin()
    elif(self.stage=='mainwithdraw'):
      self.withdrawFrame.grid_remove()
      self.withdrawNow(100000)
    elif(self.stage=='otherwithdraw'):
      if(not self.oAError):
        self.otherWithdrawFrame.grid_remove()
        self.withdrawNow(int(self.wAmount.get()))
    elif(self.stage == "postoperation"):
      self.postOperationFrame.grid_remove()
      self.operationsPart()
      self.stage = "operations" 
    elif(self.stage=='transfer'):
      self.transferFrame.grid_remove()
      self.transferNow() 
    else:
      pass

  def rFour(self):
    if(self.stage == "signup"):
      self.submitSignup()
    elif(self.stage=='mainwithdraw'):
      self.withdrawFrame.grid_remove()
      self.otherWithdrawPart()
      self.stage = "otherwithdraw"
    else:
      pass

  def lOne(self):
    if(self.stage == 'operations'):
      self.transFrame.grid_remove()
      self.withdrawPart()
      self.stage="mainwithdraw"
    elif(self.stage=='mainwithdraw'):
      self.withdrawFrame.grid_remove()
      self.withdrawNow(1000)
    else:
      pass

  def lTwo(self):
    if(self.stage == "default" and self.stage != "signup"):
      self.initFrame.grid_remove()
      self.signupPart()
      self.stage = "signup"
    elif(self.stage == "newcustomer"):
      self.newCustomerFrame.grid_remove()
      self.welcomePart()
      self.stage = 'default'
    elif(self.stage=='mainwithdraw'):
      self.withdrawFrame.grid_remove()
      self.withdrawNow(2000)
      pass
    

  def lThree(self):
    if( self.stage == "login"):
      print(self.lName.get())
      self.loginFrame.grid_remove()
      self.welcomePart()
      self.stage = "default"
    elif(self.stage=='mainwithdraw'):
      self.withdrawFrame.grid_remove()
      self.withdrawNow(5000)
    elif(self.stage=='otherwithdraw'):
      self.otherWithdrawFrame.grid_remove()
      self.operationsPart()
      self.stage = "operations"
    elif(self.stage == "postoperation"):
      self.postOperationFrame.grid_remove()
      self.welcomePart()
      self.customer = None
      self.accountNum = None
      self.lName.set("")
      self.lKey.set("")
      self.transAmount.set("")
      self.transAccount.set("")
      self.stage = "default"
    elif(self.stage=='transfer'):
      self.transferFrame.grid_remove()
      self.operationsPart()
      self.stage = 'operations' 
    else:
      pass

  def lFour(self):
    if( self.stage == "signup"):
      self.signupFrame.grid_remove()
      self.welcomePart()
      self.stage = "default"
    elif(self.stage=='mainwithdraw'):
      self.withdrawFrame.grid_remove()
      self.withdrawNow(10000)

    else:
      pass


  def loginPart(self):
    """
      Container for login section
    """
    self.loginStyle = Style()
    self.loginStyle.configure("Log.TLabel", font=('Helvetica', 13, 'bold'))
    self.loginFrame.grid(sticky="nsew")

    Label(self.loginFrame, text="First name",  style="Log.TLabel")\
      .grid(row=0, column=0,  ipady=15)
    self.loginNameEntry = Entry(self.loginFrame, textvariable=self.lName)
    self.loginNameEntry.grid(row=0, column=1, sticky="ew")
    self.loginNameEntry.focus_set()
    self.loginNameEntry.bind("<FocusOut>", self.loginNameValidator)

    Label(self.loginFrame, text="Password", style="Log.TLabel").grid(row=1, column=0, ipady=15)
    self.loginPasswordEntry = Entry(self.loginFrame, textvariable=self.lKey)
    self.loginPasswordEntry.grid(row=1, column=1, sticky="ew")
    self.loginPasswordEntry.bind("<FocusOut>", self.loginKeyValidator )

    Label(self.loginFrame, text="Back", style="Log.TLabel")\
      .grid(row=3, column=0, sticky='nsew')
    Label(self.loginFrame, text="Continue", style="Log.TLabel", anchor=E)\
      .grid(row=3, column=1, ipady=10,sticky='nsew')
    # self.loginValidator()

  def loginNameValidator(self, event):
    """"
      The validator method for login name
    """   
    # This validator value holder for login name  
    valid = vld.passnames(self.lName.get())
   
    if not(valid):
      self.isLNError = True
      print(3, self.isLNError)
      self.loginErrorMessage = Label(self.loginFrame, style="Error.TLabel")
      self.loginErrorMessage.grid(row=2, column=0, columnspan=2)
      self.loginErrorMessage['text']= "Minimum of three and only characters are are required for name"
    else:
      print(4)
      try:
        if (self.isLNError):
          self.loginErrorMessage.grid_remove()
        self.isLNError = False
      except:
        # print(NameError)
        pass


  def loginKeyValidator(self, event):
    """"
      The validator method for login passkey
    """
    print(self.isLNError)
    if not (self.isLNError):     
      valid = vld.passkeys(self.lKey.get())
      if not(valid):
        print(1)
        self.loginErrorMessage = Label(self.loginFrame, style="Error.TLabel")
        self.loginErrorMessage.grid(row=2, column=0, columnspan=2)
        self.loginErrorMessage['text']= "Minimum of seven is required, Alphanumerics and Undescores are allowed"
        self.isLKError = True
      else:
        print(2)
        try:
          if (self.isLKError):
            self.loginErrorMessage.grid_remove()
            self.isLKError = False
        except :
          pass

  def submitLogin(self):
    print(self.isLNError , self.isLKError, "here")
    if(vld.passkeys(self.lKey.get()) != False and vld.passnames(self.lName.get()) != False):
      data = (self.lName.get(), self.lKey.get())
      attempLogin = api().login(data)
      print("attemp is ", attempLogin)
      if(not attempLogin):
        self.loginErrorMessage = Label(self.loginFrame, style="Error.TLabel")
        self.loginErrorMessage.grid(row=2, column=0, columnspan=2)
        self.loginErrorMessage['text']= "No customer found"
      else:
        self.customer = attempLogin        
        self.loginFrame.grid_remove()
        self.operationsPart()        
        self.stage = "operations"



  def signupFNameValidator(self, event):
    """"
      The validator method for signup first name
    """
    valid = vld.passnames(self.ufName.get()) 
    print("valid is ", valid)  
    if not(valid):
      self.isUFNError = True
      print(1, self.isUFNError)
      self.signupError = Label(self.signupFrame, style="Error.TLabel")
      self.signupError.grid(row=3, column=0, columnspan=2)
      self.signupError['text']= "Minimum of three and only characters are are required for name"
    else:
      print(2)
      try:
        self.isUFNError = False 
        if (self.isUFNError):
          self.signupError.grid_remove()
      except:
        # print(NameError)
        pass
      finally:
        print(self.isUFNError, "inside")

  def signupLNameValidator(self, event):
    """"
      The validator method for signup last name
    """
    print(self.isUFNError, "is first")
    if(not self.isUFNError):
      valid = vld.passnames(self.ulName.get())
      print("valid is ", valid)
      if not(valid):
        self.isULNError = True
        print(3, self.isULNError)
        self.signupError = Label(self.signupFrame, style="Error.TLabel")
        self.signupError.grid(row=3, column=0, columnspan=2)
        self.signupError['text']= "Minimum of three and only characters are are required for name"
      else:
        print(4)
        try:
          if (self.isULNError):
            self.signupError.grid_remove()
            self.isULNError = False
        except:
          # print(NameError)
          pass

  def signupKeyValidator(self, event):
    """"
      The validator method for signup password
    """
    print(self.isUFNError, self.isULNError)
    if (not self.isUFNError and not self.isULNError):     
      valid = vld.passkeys(self.uKey.get())
      if not(valid):
        print(5)
        self.signupError = Label(self.signupFrame, style="Error.TLabel")
        self.signupError.grid(row=3, column=0, columnspan=2)
        self.signupError['text']= "Minimum of seven is required, Alphanumerics and Undescores are allowed"
        self.isUKError = True
      else:
        print(6)
        try:
          if (self.isUKError):
            self.signupError.grid_remove()
            self.isUKError = False
        except :
          pass

  def submitSignup(self):
    if(vld.passkeys(self.uKey.get()) != False 
    and vld.passnames(self.ufName.get()) != False 
    and vld.passnames(self.ulName.get()) != False):
      print("up up")

      data = (self.ufName.get(), self.ulName.get(), self.uKey.get())
      attempSignup = api().registerCustomer(data, 2)
      print("attempt register is ", attempSignup)
      if(not attempSignup):
        self.signupError = Label(self.signupFrame, style="Error.TLabel")
        self.signupError.grid(row=3, column=0, columnspan=2)
        self.signupError['text']= "Oop, something went wrong, please try again"
      else:
        self.customer = attempSignup
        self.accountNum = attempSignup[len(attempSignup)-1]        
        self.signupFrame.grid_remove()
        self.newCustomerPart()      
        self.stage = "newcustomer"
        print(self.accountNum)

  def signupPart(self): 
    """
      Container for signup section
    """
    print("here")
    self.loginStyle = Style()
    self.loginStyle.configure("Log.TLabel", font=('Helvetica', 13, 'bold'))

    self.signupFrame.grid(sticky="nsew")

    Label(self.signupFrame, text="First name", style="Log.TLabel").grid(row=0, column=0, ipady=15)
    self.signupFName = Entry(self.signupFrame, textvariable=self.ufName)
    self.signupFName.grid(row=0, column=1, sticky="ew")
    self.signupFName.focus_set()
    self.signupFName.bind('<FocusOut>', self.signupFNameValidator)

    Label(self.signupFrame, text="Last name", style="Log.TLabel").grid(row=1, column=0, ipady=15)
    self.signupLName = Entry(self.signupFrame, textvariable=self.ulName)
    self.signupLName.grid(row=1, column=1, sticky="ew")
    self.signupLName.bind('<FocusOut>', self.signupLNameValidator)

    Label(self.signupFrame, text="Password", style="Log.TLabel").grid(row=2, column=0, ipady=15)
    self.signupKey = Entry(self.signupFrame, textvariable=self.uKey)
    self.signupKey.grid(row=2, column=1,sticky="ew")
    self.signupKey.bind('<FocusOut>', self.signupKeyValidator)

    Label(self.signupFrame, text="Back", style="Log.TLabel").grid(row=4, column=0)
    Label(self.signupFrame, text="Continue", style="Log.TLabel", anchor=E)\
      .grid(row=4, column=1, ipady=10)

  def operationsPart(self):
    self.welSty = Style()
    self.welSty.configure("F.TFrame", font=('Helvetica', 10, 'bold'))
    self.transFrame.grid(sticky='nsew')
    Label(self.transFrame, text="Cash Withdrawal", style='W.TLabel', anchor=W).grid(row=1,column=0, ipady=13, sticky='nsew')
    Label(self.transFrame, text="Transfer", style='W.TLabel',  anchor=E).grid(row=1,column=1, ipady=13, sticky='nsew')
    Label(self.transFrame, text="Card settings", style='W.TLabel',  anchor=W).grid(row=2,column=0, ipady=13, sticky='nsew')
    Label(self.transFrame, text="Balance inquiry", style='W.TLabel',  anchor=E).grid(row=2,column=1, ipady=13,  sticky='nsew')
    Label(self.transFrame, text="Bill yayment", style='W.TLabel',  anchor=W).grid(row=3,column=0, ipady=13, sticky='nsew')
    Label(self.transFrame, text="Donation/Others", style='W.TLabel',  anchor=E).grid(row=3,column=1, ipady=13, sticky='nsew')
    
  def newCustomerPart(self):

    self.newCustomerFrame = Frame(self.screen)
    self.newCustomerFrame.grid()

    Label(self.newCustomerFrame, text=f"\t Congratulations {self.customer[0], }!!\n\
    Your account registration was successful with registration \n\
    bonus of #20,000 and your account number is {self.accountNum} \
      ", style='Log.TLabel', anchor=CENTER )\
    .grid(row=0, column=0, columnspan=2, )
    Label(self.newCustomerFrame, text='Back', style='W.TLabel', anchor=W).grid(row=1, column=0, sticky='nsew')
    Label(self.newCustomerFrame, text='Continue', style='W.TLabel', anchor=E).grid(row=1, column=1, sticky='nsew')

  def withdrawPart(self):
    self.withdrawFrame = Frame(self.screen)
    self.withdrawFrame.grid()

    Label(self.withdrawFrame, text="1000", style='W.TLabel', anchor=W).grid(row=0,column=0, ipady=13, sticky='nsew')
    Label(self.withdrawFrame, text="20,000", style='W.TLabel',  anchor=E).grid(row=0,column=1, ipady=13, sticky='nsew')
    Label(self.withdrawFrame, text="2000", style='W.TLabel',  anchor=W).grid(row=1,column=0, ipady=13, sticky='nsew')
    Label(self.withdrawFrame, text="50,000", style='W.TLabel',  anchor=E).grid(row=1,column=1, ipady=13,  sticky='nsew')
    Label(self.withdrawFrame, text="5,000", style='W.TLabel',  anchor=W).grid(row=2,column=0, ipady=13, sticky='nsew')
    Label(self.withdrawFrame, text="100,000", style='W.TLabel',  anchor=E).grid(row=2,column=1, ipady=13, sticky='nsew')
    Label(self.withdrawFrame, text="10,000", style='W.TLabel',  anchor=W).grid(row=3,column=0, ipady=13, sticky='nsew')
    Label(self.withdrawFrame, text="Other", style='W.TLabel',  anchor=E).grid(row=3,column=1, ipady=13, sticky='nsew')

  def otherWithdrawPart(self):
    self.otherWithdrawFrame = Frame(self.screen)
    self.otherWithdrawFrame.grid()
    Label(self.otherWithdrawFrame, text="Enter amount  ", style='W.TLabel', anchor=W).grid(row=0,column=0, ipady=15, sticky='nsew')
    self.otherAmount = Entry(self.otherWithdrawFrame, textvariable=self.wAmount)
    self.otherAmount.grid(row=0, column=1,sticky="ew")
    self.otherAmount.focus_set()
    self.otherAmount.bind('<FocusOut>', self.validateAmount)
    Label(self.otherWithdrawFrame, text="Back", style='W.TLabel', anchor=W).grid(row=2,column=0, pady=(55,0), sticky='nsew')
    Label(self.otherWithdrawFrame, text="Continue", style='W.TLabel', anchor=E).grid(row=2,column=1, pady=(55,0),  sticky='nsew')

  def wAmountErrorPart(self):
    self.wAmountErrorLabel = Label(self.otherWithdrawFrame, anchor=W, style="Error.TLabel")
    self.wAmountErrorLabel.grid(row=1, column = 1, columnspan=2, sticky="nsew")
    self.wAmountErrorLabel['text'] = "Only numbers are required "

  def validateAmount(self, event):
    valid = vld.passamount(self.wAmount.get())
    if(not valid):
      self.wAmountErrorPart()
      self.oAError = True
    else:
      try:
        if(self.oAError):
          self.oAError = False
          self.wAmountErrorLabel.grid_remove()
      except:
        pass

  def withdrawNow(self, amount):
    data = (self.customer[0], amount)
    # print(type(data))
    response = api().withdraw(data)
    if( not response):
      self.postOperationMessage.set("Something went wrong, Please try again")
    elif(response == "insufficient_balance"):
      self.postOperationMessage.set("You have insufficient balance")
    else:
      self.postOperationMessage.set(response)
    self.postOperationPart()
    self.stage = 'postoperation'

  def postOperationPart(self):
    self.postOperationFrame = Frame(self.screen) 
    self.postOperationFrame.grid()

    self.Lsty = Style()
    self.Lsty.configure("M.TLabel", font=('Helvetica', 10, 'bold'))
    self.Lsty.configure("P.TLabel", font=('Helvetica', 15, 'bold'))

    Label(self.postOperationFrame, textvariable=self.postOperationMessage, style='M.TLabel', anchor=CENTER)\
      .grid(row=0,column=0, rowspan=2, columnspan=2, ipady=13, sticky='nsew')
    Label(self.postOperationFrame, text="Exit", style='P.TLabel',  anchor=W).grid(row=2,column=0, pady=(63,0), sticky='nsew')
    Label(self.postOperationFrame, text="New operation", style='P.TLabel', anchor=E).grid(row=2,column=1, pady=(63,0), sticky='nsew')

  def transferPart(self):
    self.transferFrame = Frame(self.screen)
    self.transferFrame.grid()

    Label(self.transferFrame, text="Account number",  style="Log.TLabel")\
      .grid(row=0, column=0,  ipady=15)
    self.transAccountNumBox = Entry(self.transferFrame, textvariable=self.transAccount)
    self.transAccountNumBox.grid(row=0, column=1, sticky="ew")
    self.transAccountNumBox.focus_set()
    self.transAccountNumBox.bind("<FocusOut>", self.transferAcountValidator)

    Label(self.transferFrame, text="Amount", style="Log.TLabel").grid(row=1, column=0, ipady=15)
    self.transAmountBox = Entry(self.transferFrame, textvariable=self.transAmount)
    self.transAmountBox.grid(row=1, column=1, sticky="ew")
    self.transAmountBox.bind("<FocusOut>", self.tansferAmountValidator)

    Label(self.transferFrame, text="Back", style="Log.TLabel")\
      .grid(row=3, column=0, sticky='nsew')
    Label(self.transferFrame, text="Continue", style="Log.TLabel", anchor=E)\
      .grid(row=3, column=1, ipady=10,sticky='nsew')

  def transferAcountValidator(self, event):
    """"
      The validator method for login name
    """   
    # This validator value holder for login name  
    valid = vld.passAccountNum(self.transAccount.get())
   
    if not(valid):
      self.isTACError = True
      print(3, self.isTACError)
      self.transferErrorMessage = Label(self.transferFrame, style="Error.TLabel")
      self.transferErrorMessage.grid(row=2, column=0, columnspan=2)
      self.transferErrorMessage['text']= "Ten numbers are required"
    else:
      print(4)
      try:
        if (self.isTACError):
          self.transferErrorMessage.grid_remove()
        self.isTACError = False
      except:
        # print(NameError)
        pass


  def tansferAmountValidator(self, event):
    """"
      The validator method for login passkey
    """
    print(self.isTACError)
    if not (self.isTACError):     
      valid = vld.passamount(self.transAmount.get())
      if not(valid):
        print(1)
        self.transferErrorMessage = Label(self.transferFrame, style="Error.TLabel")
        self.transferErrorMessage.grid(row=2, column=0, columnspan=2)
        self.transferErrorMessage['text']= "Only numbers are required"
        self.isTAMError = True
      else:
        print(2)
        try:
          if (self.isTAMError):
            self.isTAMError = False
            self.transferErrorMessage.grid_remove()
        except :
          pass
  
  def transferNow(self):
    if( vld.passAccountNum(self.transAccount.get()) != False and vld.passamount(self.transAmount.get()) != False):
      data = (self.customer[0], int(self.transAmount.get()), self.transAccount.get() )
      response = api().transfer(data)
      if( not response):
        self.postOperationMessage.set("Something went wrong, Please try again")
      elif(response == "insufficient_balance"):
        self.postOperationMessage.set("You have insufficient balance")
      else:
        self.postOperationMessage.set(response)
      self.postOperationPart()
      self.stage = 'postoperation'

  def checkBalance(self):
    response = api().checkBalance((self.customer[0],))
    if(not response):
      self.postOperationMessage.set("Something went wrong, Please try again")
    else:
      self.postOperationMessage.set(response)
    self.postOperationPart()
    self.stage = 'postoperation'




  def start(self):
    self.leftButtonsSection()
    self.rightButtonsSection()
    self.welcomePart()
    # self.main.geometry("500x500")
    self.main.mainloop()
    


Interface().start()