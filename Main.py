###############
#Name of programmer: Areeba Minhaj
#Date: November 2022
#Programming principles
#program: Perform the object-oriented analysis process to find 
#    the objects a given a program is made of. Once the objects 
#    are found, complete the object-oriented design process to 
#    find the classes that correspond to the objects found. With
#    the object-oriented design finalized, implement the program 
#    using Visual Studio Code IDE
##############


import random

class Calcuations: #class manipulates the variables
    def __init__(self): #create new variable
        print("Welcome to Programming Principles Sample Product Inventory")
        self.PC = input("Please enter the Product Code: ") # left this as a string because the number doesn't represent a numeric value
        self.PN = input("Please enter the Product Name: ")
        self.CS = int(input("Please enter the Current Stock: "))
        self.SP = int (input("Please enter the Product Sale Price: "))
        self.MC = int(input("Please enter the Product Manufacture Cost: "))
        self.ESMP = int(input("Please enter Estimated Monthly Production: "))
        self.calc()  #calling other function
    def calc(self):
        #insert loop to do twelve times
        i = 0
        while i < 12:
            i += 1
            B=random.randrange(90,120)
            print("Month: ", i, "***************",'\n','\n', "Manufactured Units: ", self.ESMP, '\n', "Units Sold: ", B, '\n', "Current Stock: ", self.ESMP,'\n')  #set manufactured units, random num of sold, predicted stock
        

P1 = Calcuations()  #Instantiate an object (product 1)
P2 = Calcuations()  #second object(product 2)
