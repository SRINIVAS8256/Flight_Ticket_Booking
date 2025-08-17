import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataBase.Data import DataOperation
data = DataOperation()

class SignUp():
    def __init__(self):
        self.name    = input("Enter your name : ")
        self.email   = input("Enter your email: ")
        self.mob_no  = input("Enter your mobile number: ")
        self.pasword = input("enter your password: ")
    def signup_sql(self):    
        sql = "INSERT INTO Login_Signin VALUES(%s, %s, %s, %s)"
        data.insert_data_params(sql,(self.name, self.email, self.mob_no, self.pasword))        
        
    def pas(self):
        pass
# signup = SignUp(name, email, mob_no, pasword)
      