import random
import sys

def transferMoney():
    option = input('Transfer Money;\nSelect 1 for MoMo User\nSelect 2 for Non MoMo User\nselect 3 for Send with Care\nSelect 4 for Other Networks\nSelect 5 for Bank Account\nSelect 6 to end session\n')

def sessionControl(transferMoney):
     print(transferMoney)
     keepAlive=True
     while(keepAlive):
         pin1=(int(input('Enter Mobile Number:')))
         pin2=(int(input('Confirm Mobile Number:')))
         tries = 1
         if tries == 1 and pin1!= pin2:
             print('The number you enetered does not match! Back to Main Menu')
             break
         if pin1 == pin2 and tries == 1:
                 amount=input('Enter amount:')
         while pin1 == pin2:
             if tries < 3 and pin1!= pin2:
                 tries+=1
                 pin2=int(print('The number you enetered does not match'))
                 if tries == 3 and pin1!= pin2:
                     print()
             else:
                 if pin1 == pin2 and tries < 4:
                     input('Enter reference:')
                     print("You are about to transfer this amount GHc{} to this number +233{}".format(amount, pin1))
                     input('Enter 1 to confirm or 2 to cancel:')
                     input('Enter your pin: ')
                     print('You have transfered this amount GHc{} to this number +233{}'.format(amount, pin1))
                     pin=True


        
def payBill():
    option = input('Pay Bill;\nSelect 1 for Utilities\nSelect 2 for School Fees\nselect 3 for General Payment\nSelect 4 for EVD\nSelect 5 for MTN Bills\nSelect 6 to end session\n')
    
def Buyairtime():
    option = input('Buy Airtime;\nSelect 1 for Self\nSelecct 2 for Others\nSelect 3 to end session\n')
    
def checkwallet():
    option = input('Check Wallet;\nSelect 1 to Check Balance\nSelect 2 to Allow Cashout\nSelect 3 to Change & Reset PIN\nSelect 4 to end session\n')

def Buybundle():
    option = input('Buy Bundle;\nSelect 1 for Data Bundle\nSelect 2 end session\n')


def socialMediaBundle():
    option = input('socialMediaBundle;\nSelect 1, from GHC10\nSelect 2 for GHC20\nSelect 3 for GHC30\nSelect 4 to end session\n')
    if option =='4':
        keepAlive = False
    else:
        print('enter a valid number')
    

def midnightBundle():
    option = input('Midnight Bundle;\nSelect 1, from GHC10\nSelect 2 for GHC20\nSelect 3 for GHC30\nSelect 4 to end session\n')
    if option =='4':
        keepAlive = False
    else:
        print('enter a valid number')
    

def videoBundle():
    option = input('Video Bundle;\nSelect 1, from GHC10\nSelect 2 for GHC20\nSelect 3 for GHC30\nSelect 4 to end session\n')
    if option =='4':
        keepAlive = False
    else:
        print('enter a valid number')


def main():
    keepAlive=True
    while(keepAlive):
        option = input('Menu\nSelect 1 to Transfer Money\nSelect 2 to Pay Bill \nselect 3 to Buy Airtime\nSelect 4 to Buy bundle\nSelect 5 to check wallet\nSelect 6 Exit\n')
        if option =='1':
            sessionControl(transferMoney())
        elif option =='2':
            sessionControl(payBill())
        elif option =='3':
            sessionControl(Buyairtime())
        elif option =='4':
            sessionControl(Buybundle())
        elif option =='5':
            sessionControl(checkwallet())
        elif option =='6':
                        sys.exit()
        else:
            print('enter a valid number')


if __name__ == "__main__":
    main()


