###############
#Name of programmer: Areeba Minhaj
#Date: November 2022
#Programming principles
#program: creating and imitate a bank and bank accounts like acvings accounts and chequing accounts
##############


class Program: #handles the interaction with the user
    def showMainMenu(self):
            self.MMChoice= ("1","2")
            while True:
                self.user1=input("Welcome to the Bank! (please select an option)",'\n',"1. Select account (type 1)",'\n',"2. Exit Program (type 2)")
                if self.user1 in self.MMChoice:
                    break
                if self.user1 == "1":
                    self.SAChoice = input("Select an Account from the following menu:",'\n',"1.account 1",'\n',"2.account 2",'\n',"3.account 3",'\n',"4.account 4",'\n',"5.account 5")
                if self.user1 == "2":
                    exit

            print("sorry you did not enter a valid option please try again")
    def showAccountMenu(self):
        self.AMChoice("Select one fromt the following menu:",'\n',"1. Check balance",'\n',"2. Deposit",'\n',"3. Withdraw Money", '\n',"4. Exit Account")

class account:
    jj
class SavingsAccount:
    kk
class ChecquingAccount:
    jj
class Bank:
    jj

