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
print("******Programming Principles Sample Stock Statement******")

class Calcuations: #class manipulates the variables
    def __init__(self): #creat new variable
        print("Welcome to Programming Principles Sample Product Inventory")
        self.PC = input("Please enter the Product Code: ")
        self.PN = input("Please enter the Product Name: ")
        self.CS = input("Please enter the Current Stock: ")
        self.SP = input("Please enter the Product Sale Price: ")
        self.MC = input("Please enter the Product Manufacture Cost: ")
        self.ESMP = input("Please enter Estimated Monthly Production: ")
    def calcUnitsSold(self):
        mon=random.randrange(90,120)

P1 = Calcuations()  #Instantiate an object (product 1)
P2 = Calcuations()  #second object(product 1)
