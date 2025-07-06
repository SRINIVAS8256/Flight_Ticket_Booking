import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataBase.Data import DataOperation
data = DataOperation()


class Login:
    def __init__(self):
        self.mob_nor  = input("Enter the mobile: ")
        self.password = input("Enter the password: ")
    def login_sql(self):    
        sql = "SELECT EXISTS (SELECT 1 FROM Login_Signin WHERE User_mob = %s and User_pass = %s)"
        result = data.select_data(sql , (self.mob_nor, self.password)) # we have to use a parameterised queary 
        if result and result[0][0]  == 1:
            print("Login sucesfull")
        else :
            print("invalid mobile or password")    
# login = Login()        