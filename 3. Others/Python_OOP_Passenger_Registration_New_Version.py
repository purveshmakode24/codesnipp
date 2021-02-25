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
    def __init__(self, field):
        self.field = field
        
    def checkPassengerName(self):
        if not "".join(self.field.split()).isalpha():
            print("Please enter a valid name.")
        elif len(self.field)>50:
            print("Name should not exceed 50 characters.")
        else:
            return True

    def checkEmail(self):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,4}$'
        
        if not re.match(regex, self.field):
            print("Please enter a valid email.") 
        else:
            return True

    def checkPassword(self):    
        if not len(self.field)>7:
            print("Password should be greater than 7.")
        else:
            return True
        
    def checkConfirmPassword(self, password):
        if self.field != password:
            print("Password did not match.")
        else:
            return True
        
    def checkAddress(self):
        if len(self.field)>100:
            print("Address should not exceeds 100 characters.")
        elif not len(self.field):
            print("Address should not be empty.")
        else:
            return True

    def checkContact(self):
        if len(str(self.field))>10:
            print("Contact number should not exceeds 10 characters.")
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
        
        while True:
            passengerName = input("Enter the passenger name:")
            v = ValidateField(passengerName)
            if v.checkPassengerName():
                break
            
        while True:     
            email = input("Enter email:")
            v = ValidateField(email)
            if v.checkEmail():
                break

        while True:      
            password = input("Enter password:")
            v = ValidateField(password)
            if v.checkPassword():
                cpassword = input("Enter confirm password:")
                v = ValidateField(cpassword)
                if v.checkConfirmPassword(password):
                    break
                    
        while True:      
            v = ValidateField(cpassword)
            if v.checkPassword():
                break
            
        while True:    
            address = input("Enter address:").capitalize()
            v = ValidateField(address)
            if v.checkAddress():
                break

        while True:
            try:
                contact = int(input("Enter contact number:"))
                v = ValidateField(contact)
                if v.checkContact():
                    break
            except Exception:
                print("Please enter a valid contact number")
                         
        passengerObj = Passenger(passengerId, passengerName, email, cpassword, address, contact)

        if passengerObj:        
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
        c = int(input("Enter your choice:") or -1)
        if c==1:  
            registration(passengerList)
        elif c==2:
            displayPassengers(passengerList)
        else:
            break
            
        print("-"*52)    
    


