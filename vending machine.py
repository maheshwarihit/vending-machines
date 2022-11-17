print("....Welcome to....\n HiTech Global Services") 
SmartCard_Number=int(input("Enter your smart card number :"))
def option(): 
   print("1. Medical first Aid kit \n2. Medical accessories")
   Option=int(input("Enter your option :"))
   if(Option ==1): 
        print("You're First Aid Kit= Rs.550.00")
        print("1.pay \n2.cancel\n3.back to menu")
        choice=int(input("Enter your choice :"))
        if(choice==1):
            print("Deposit your cash amount \you're items was dispensed\nThank you")
        elif(choice==2): 
            print("Thank you! visit us again!")
        else: 
            option()
    else:
        print("1.Tablets\n2.oilments\n3.accessories")
        choices=int(input("Enter your choices:")) 
  
        if(choices==1): 
            print("1.dolo-Rs.10\n2.paracetamol-Rs-10")
            print("your amount is : Rs.20")
            print("pay your cash!\nyou're items was dispensed\nThank you!")
        elif(choices==2): 
            print("1.potric = Rs.40\n2.benoquin= Rs.50\n3.hydrogen quik relif=Rs.120")
            print("your amount is = Rs.105")
            print("pay your cash!\nyou're items was dispensed\n Thank you!") 
        else: 
            print("1.bandages=Rs.10\n2.adhesive tape = Rs.15\n3.cotton swab = Rs.20")
            print("your amount is = Rs.45" )
            print("pay your cash!\nyou're items was dispensed\nThankyou!")
    option() 
 
 
  
