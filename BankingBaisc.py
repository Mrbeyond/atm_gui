import mysql.connector as DB
from string import Template
from datetime import datetime
class BankingBasic:
    def __init__(self):
        self.dBase=  DB.connect( host='localhost', user='root', password='')
        self.tabs =  DB.connect( host='localhost', user='root', password='', database='atm_gui')
        self.mockCustomer = ('beyond', 'Beyond', '12345678')

    def checkDatabase(self, dbName):
        try:

            # convertToTuple = (dbName)
            cursor = self.dBase.cursor()
            cursor.execute("SHOW DATABASES")
            # print(cursor.fetchall())

            if (dbName,) not in cursor.fetchall():
                print(dbName, 'Database does\'nt exist')
                return True
            else:
                print(dbName, 'Database already exists')
                return False
        except DB.Error as err:
            print(f"The is error and the error is \n {err}")

    def newDatabase(self, dbName):
        try:
            if self.checkDatabase(dbName):
                self.dBase.cursor().execute("CREATE DATABASE "+ dbName)
                print(dbName, 'Database is created')
        except DB.Error as err:
            print(f"There is error and the error is \n {err}")

    def checkTable(self, tableName):
        try:
            cursor = self.tabs.cursor()
            cursor.execute("SHOW TABLES")
            if tuple((tableName,)) not in cursor.fetchall():
                print(f'Table {tableName} does\'nt exist')
                return True
            else:
                print(f'Table {tableName} already exist')
                return False
        except DB.Error as err:
            print(f"There is error and the error is \n {err}")
            return False

    def createCustomerTable(self, tbName):
        try:
            if self.checkTable(tbName):
                cursor = self.tabs.cursor()
                cursor.execute(Template("CREATE TABLE $table( \
                    `id` INT NOT NULL AUTO_INCREMENT PRIMARY kEY,\
                    `firstName` VARCHAR(225) NOT NULL, \
                    `lastName` VARCHAR(225) NOT NULL,\
                    `password` VARCHAR(225) NOT NULL, \
                    `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP) \
                ").substitute(table=tbName))
        except DB.Error as err:
            print(f"There is error and the error is \n {err}")

    def createAccountTable(self, tbName):
        try:
            if self.checkTable(tbName):
                cursor = self.tabs.cursor()
                cursor.execute(Template("CREATE TABLE $table ( \
                    `id` INT NOT NULL AUTO_INCREMENT PRIMARY kEY,\
                    `customer` INT NOT NULL, \
                    `type` INT NOT NULL, \
                    `accountNumber` VARCHAR(12) NOT NULL,\
                    `balance` INT DEFAULT 20000,\
                 `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP) \
                ").substitute(table=tbName))
        except DB.Error as err:
            print(f"There is error and the error is \n {err}")
    def createTransactionTable(self, tbName):
        try:
            if self.checkTable(tbName):
                cursor = self.tabs.cursor()
                cursor.execute(Template("CREATE TABLE $table ( \
                    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,\
                    `customer` INT NOT NULL,\
                    `initialAmount` INT NOT NULL, \
                    `operation` VARCHAR(225) NOT NULL, \
                    `details` VARCHAR(225) NOT NULL,\
                    `currentAmount` INT NOT NULL,\
                    `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP) \
                ").substitute(table=tbName))            
        except DB.Error as err:
            print(f"There is error and the error is \n {err}")  
            
    def postTransaction(self, data):
        try:
            # The following method creates the TRANSACTIONS table if not created before:
            self.createTransactionTable('transactions')
            
            cursor = self.tabs.cursor() 
            cursor.execute("INSERT INTO `transactions` (\
                `customer`, `initialAmount`, `operation`, `details`, `currentAmount`) VALUES(\
                %s, %s, %s, %s, %s)", (data))  
            self.tabs.commit()
            print('Transaction was posted')
            return True
        except DB.Error as err:
            print(f"There is error and the error is \n {err}")
            return False
        # finally:
        #     pass
            
            #closing database connection.
            # if(self.tabs.is_connected()):
            #     cursor.close()
            #     self.tabs.close()
            #     print("\33[33m connection is closed \33[0m")

    def registerCustomer(self, data, typy):
        """ 
          CUSTOMER TABLE IS CREATED IF NOT EXISTS WITH PROVIDED DATA
        """
        try:
            # The following method creates the CUSTOMERS table if not created before:
            self.createCustomerTable('customers')
            
            cursor = self.tabs.cursor()
            cursor.execute("INSERT INTO `customers` (`firstName`, `lastName`, `password` ) VALUES (%s, %s, %s) ", (data))
            customerId = cursor.lastrowid
            accNum =  str(int(datetime.timestamp(datetime.now())*1000000))[5:15][::-1]
            print(accNum, typy, customerId)
            
            """            CREATE THE ACCOUNT TABLE TOGETHER WITH THE CUSTOMER TABLE IF NOT EXISTS      """
            # The following method creates the ACCOUNTS table if not created before:
            self.createAccountTable('accounts')
            
            cursor.execute("INSERT INTO `accounts` (`type`, `customer`, `accountNumber` ) VALUES (%s, %s, %s) ", (2, customerId, accNum ))
            lastId = cursor.lastrowid
            postData= (customerId, 0, "Deposit", "Initial bonus", 20000)
            post = self.postTransaction(postData)
            if(not post):
                self.tabs.rollback()
                return False
            else:
                cursor.execute("SELECT * FROM `customers` WHERE id=%s", (customerId,))
                customer = cursor.fetchall()
                customer= customer[0]+(accNum,)
                print(customer, " is customer")
                self.tabs.commit()
                print(f"\n \33[4m\33[32m Welcome {data[0]}! You have successfully registered and your account number is {accNum} \33[0m \n")
                return customer
        except DB.Error as err:
            print(f"\n \33[31m There is error and the error is: \n {err} \33[0m \n")
            self.tabs.rollback()
            return False
        finally:
            pass
            
            #closing database connection.
            # if(self.tabs.is_connected()):
            #     cursor.close()
            #     self.tabs.close()
            #     print("\33[33m connection is closed \33[0m")
                
    def login(self, data):
        try:
            cursor = self.tabs.cursor()
            cursor.execute("SELECT * FROM `customers` WHERE `firstName` = %s AND `password` = %s  LIMIT 1", (data))
            allRecords =cursor.fetchall()
            print(f'\n\33[34m all is \n {allRecords} \33[0m\n')
            if(len(allRecords) > 0):
              return allRecords[0]
            else:
              return False
        except DB.Error as err:
            print(f"There is error and the error is \n {err}")
            self.tabs.rollback()
            return False
        finally:
            
            #closing database connection.
            if(self.tabs.is_connected()):
                cursor.close()
                # self.tabs.close()
                print("\n\33[33m connection is closed \33[0m\n")

    def withdraw(self, data):
        try:
            cursor = self.tabs.cursor()
            cursor. execute("SELECT `balance` FROM `accounts` WHERE `customer` = %s ", (data[0],))
            
            result = cursor.fetchall()
            if(len(result) > 0):
                current = result[0][0]

                if(current - data[1] < 0):
                    print('insufficient_balance')
                    return 'insufficient_balance'
                else:
                    balance = current - data[1]
                    cursor.execute("UPDATE `accounts` SET `balance` = %s WHERE `customer`= %s", (balance, data[0]))
                    postData= (data[0], current, "Withdrawal", f"Debited by {data[1]}", balance)
                    post = self.postTransaction(postData)
                    print(post)
                    self.tabs.commit()
                    print(cursor , 'done')
                    return f"Your operation was successful \n Your account balance is #{balance}"
            else:
                print('wrong')
                return False
        except DB.Error as err:
            print(f"There is error and the error is \n {err}")
            self.tabs.rollback()
            return False
        finally:            
            #closing database connection.
            if(self.tabs.is_connected()):
                cursor.close()
                # self.tabs.close()
                print("\n\33[33m connection is closed \33[0m\n")

    def transfer(self, data):
        try:
            cursor = self.tabs.cursor()
            cursor. execute("SELECT `balance` FROM `accounts` WHERE `customer` = %s ", (data[0],))
            
            result = cursor.fetchall()
            if(len(result) > 0):
                current = result[0][0]

                if(current - data[1] < 0):
                    print('insufficient_balance')
                    return 'insufficient_balance'
                else:
                    balance = current - data[1]
                    cursor.execute("UPDATE `accounts` SET `balance` = %s WHERE `customer`= %s", (balance, data[0]))
                    postData= (data[0], current, "Transefer", f"Transefer of {data[1]} made to {data[2]}", balance)
                    post = self.postTransaction(postData)
                    print(post)
                    self.tabs.commit()
                    print(cursor , 'done')
                    return f"Your operation was successful \n Your account balance is #{balance}"
            else:
                print('wrong')
                return False
        except DB.Error as err:
            print(f"There is error and the error is \n {err}")
            self.tabs.rollback()
            return False
        finally:            
            #closing database connection.
            if(self.tabs.is_connected()):
                cursor.close()
                # self.tabs.close()
                print("\n\33[33m connection is closed \33[0m\n")

    def checkBalance(self, data):
        try:
            cursor = self.tabs.cursor()
            cursor. execute("SELECT `balance` FROM `accounts` WHERE `customer` = %s ", (data[0],))            
            result = cursor.fetchall()
            if(len(result) > 0):
                current = result[0][0]
                print(current)
                return f"Your account balance is #{current}"
            else:
                print('wrong')
                return False
        except DB.Error as err:
            print(f"There is error and the error is \n {err}")
            return False



mockCustomer = ('beyond', 'Beyond', '12345678')
uses = ('beyond', '12345678')
# BankingBasic().newDatabase("atm_gui")
# BankingBasic().registerCustomer( mockCustomer,2)
# BankingBasic().postTransaction((1,0, "Deposit", "Creditted by 5000 ", 5000))
# print(BankingBasic().login(uses))
data = (1,500)
# BankingBasic().withdraw(data)
# data = (1,500, 1234567890)
# BankingBasic().transfer(data)
# BankingBasic().checkBalance(data)


