from datetime import datetime

datetime_object = datetime.now()
print(datetime_object)



name = input("what is your name? \n")
allowedUsers = ['Seyi','Dare','Love']
allowedPassword = ['passwordSeyi','passwordDare','passwordLove']



if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)
    
    

    if(password == allowedPassword[userId]):

        
        print('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Compliant')

        selectedOption = int(input('Please select an option:'))
        
        
        

        if(selectedOption == 1):
            print('you selected %s' % selectedOption)
            print('available withdrawal options:')
            print('1. 1000')
            print('2. 2000')
            print('3. 5000')
            
            withdrawalOption = int(input('How much would you like to withdraw:'))

            if(withdrawalOption == 1):
                print('you selected %s' % withdrawalOption)
                pass
            if(withdrawalOption == 2):
                print('you selected %s' % withdrawalOption)
                pass
            if(withdrawalOption == 3):
                print('you selected %s' % withdrawalOption)
                pass
            elif(withdrawalOption == 1 or 2 or 3):
                print('take your cash')
                pass
                
            
        if(selectedOption == 2):
            print('you selected %s' % selectedOption)
            print('available deposit options:')
            print('1. 5000')
            print('2. 10000')
            print('3. 20000')

            cashDeposit = int(input('how much would you like to deposit: '))

            if(cashDeposit == 1):
                print('you selected %s' % cashDeposit)
                pass
            if(cashDeposit == 2):
                print('you selected %s' % cashDeposit)
                pass
            if(cashDeposit == 3):
                print('you selected %s' % cashDeposit)
                pass
            elif(cashDeposit == 1 or 2 or 3):
                print('current balance')
                pass
            
        
        if(selectedOption == 3):
            print('you selected %s' % selectedOption)
            print('What issues would you like to report:')
            print('1. machine ejecting my card')
            print('2. account debited but i did not get my money')
            print('please report other issues to your neares bank')

            compliantOption = int(input('what issues would you like to report:'))
            
            if(compliantOption == 1):
                print('you selected %s' % compliantOption)
                pass
            if(compliantOption == 2):
                print('you selected %s' % compliantOption)
                pass
            elif(compliantOption == 1 or 2):
                print('Thank you for contacting us')
                pass
        
        
        else:
            print('Invalid Option selected, please try again')
       
    else:
        print('Password Incorrect, please try again')


else:
    print('Name not found, please try again')
