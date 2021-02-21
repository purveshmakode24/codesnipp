from random import randint
import re; import json

class Passenger:
    def __init__(self, passengerId, passengerName, email, password, address, contact):
        self.passengerId = passengerId
        self.passengerName = passengerName
        self.email = email
        self.password = password
        self.address = address
        self.contact = contact
            

class ValidateField:
    def __init__(self, passengerObj):
        self.passengerObj = passengerObj
        
    def checkPassengerName(self):
        if not "".join(self.passengerObj.passengerName.split()).isalpha():
            print("\nEnter a valid name.")
        elif len(self.passengerObj.passengerName)>50:
            print("\nName should not exceed 50 characters.")
        else:
            return True

    def checkEmail(self):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,4}$'
        
        if not re.match(regex, self.passengerObj.email):
            print("\nPlease enter a valid email.") 
        else:
            return True

    def checkPassword(self):    
        if not len(self.passengerObj.password)>7:
            print("\nPassword should be greater than 7.")
        else:
            return True

    def checkAddress(self):
        if len(self.passengerObj.address)>100:
            print("\nAddress should not exceeds 100 characters.")
        elif not len(self.passengerObj.address):
            print("\nAddress should not be empty.")
        else:
            return True

    def checkContact(self):
        if len(str(self.passengerObj.contact))>10:
            print("\nContact number should not exceeds 10 characters.")
        else:
            return True


def displayPassengers(passengerList): 
    if len(passengerList):
        print(json.dumps([p.__dict__ for p in passengerList], indent=4))
    else:
        print("\nNo data found.")   


def registration(passengerList):
    try:
        passengerId = int(randint(1000000,9999999) or 0000000)
        print("\nPassenger ID:", passengerId)    
        passengerName = input("Enter the passenger name:")
        email = input("Enter email:")
        password = input("Enter password:")
        address = input("Enter address:").capitalize()
        contact = int(input("Enter contact number:"))
                    
        passengerObj = Passenger(passengerId, passengerName, email, password, address, contact)

        v = ValidateField(passengerObj)
                    
        if v.checkPassengerName() and v.checkEmail() and v.checkPassword() and v.checkAddress() and v.checkContact():
            passengerList.append(passengerObj)
            print("\nPassenger Registration is Sucessful!")
                        
    except Exception as e:
        print("Error:", e)
   


if __name__ == '__main__':

    print("="*52+"\nPASSENGER REGISTRATION\n"+"="*52)
    print("1. Enter 1 to register a passenger.")
    print("2. Enter 2 to display all the registered passengers.")
    print("3. Enter -1 to exit.\n"+"-"*52)
      
    passengerList = []

    while True:
        c = int(input("Enter you choice:") or -1)
        if c==1:  
            registration(passengerList)
        elif c==2:
            displayPassengers(passengerList)
        else:
            break
            
        print("-"*52)    
    



