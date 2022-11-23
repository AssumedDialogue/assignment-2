###############
#Name of programmer: Areeba Minhaj
#Date: November 2022
#Programming principles
#program: creating and imitate a bank and bank accounts like acvings accounts and chequing accounts
##############


class Program: #handles the interaction with the user
    def showAccountMenu(self):
        self.AMChoice= ("1","2","3","4")
        while True:
            self.User3=input("Select one fromt the following menu:"+'\n'+"1. Check balance"+'\n'+"2. Deposit"+'\n'+"3. Withdraw Money"+'\n'+"4. Exit Account")
            if self.User3 in self.AMChoice:
                break    
    def showMainMenu(self):
        self.MMChoice= ("1","2")
        while True:
            self.user1=input("Welcome to the Bank! (please select an option)"+'\n'+"1. Select account (type 1)"+'\n'+"2. Exit Program (type 2)")
            if self.user1 in self.MMChoice:
                if self.user1 == "1":
                    self.SAChoice= ("1","2","3","4","5")
                    while True:
                        self.User2 = input("Select an Account from the following menu:"+'\n'+"1.account 1"+'\n'+"2.account 2"+'\n'+"3.account 3"+'\n'+"4.account 4"+'\n'+"5.account 5")
                        if self.User2 in self.SAChoice:
                            Program.showAccountMenu(self)
                            break
                        else:
                            print("sorry you did not enter a valid option please try again")
                break
            else:
                print("sorry you did not enter a valid option please try again")
            
            if self.user1 == "2":
                exit
    def getA(self):
        return self.User2


            
    
class account:
    print()
class SavingsAccount:
    print()
class ChecquingAccount:
    print()
class Bank:
    print()
p=Program()
p.showMainMenu()

