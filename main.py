from Login_Signin.signup import SignUp
from Login_Signin.login  import Login


option1 = int(input("   1. User\n   2. Admin \nEnter your option : "))
if option1 == 1:
    option2 = int(input("   1. Login\n   2. Signiin \nEnter your option : "))
    if option2 == 1:
        login_obj = Login()
    elif option2 == 2 :
        signup_obj = SignUp()    
    else :
        print(" invalid optioon")    
else :
    option2 = int(input(" welcome Admin"))        
        

           