from Login_Signin.signup import SignUp
from Login_Signin.login  import Login
from Admin.add_flight    import AddFlight
from Admin.admin_login   import *


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
elif option1 == 2:
    admin_obj = admin()
    option2 = int(input(" \n\n welcome Admin \n1.Add flight \n2.Add Seats for Flight \nEnter your option : "))        
    if option2 == 1:
        flight_obj = AddFlight()
        flight_obj.add_flights()
    # elif option2 == 2:
    #     flight_ceat_obj    

           