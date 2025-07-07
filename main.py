from Login_Signin.signup import SignUp
from Login_Signin.login  import Login
from Admin.add_flight    import AddFlight


option1 = int(input("   1. User\n   2. Admin \nEnter your option : "))
if option1 == 1:
    option2 = int(input("   1. Login\n   2. Signiin \nEnter your option : "))
    if option2 == 1:
        login_obj = Login()
        login_obj.login_sql()
    elif option2 == 2 :
        signup_obj = SignUp() 
        signup_obj.signup_sql()    
    else :
        print(" invalid optioon")    
else :
    option2 = int(input(" \n\n welcome Admin \n1.Add flight \n2.Flight Seat  \nEnter your option : "))        
    if option2 == 1:
        add_flight = AddFlight()
        add_flight.add_flights()
        

           