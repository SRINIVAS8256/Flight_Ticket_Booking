import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from DataBase.Data import DataOperation
data = DataOperation() #Data base obj


a = 0
def admin():
    input1 = input("Enter the Admin id   : ") 
    input2 = input("Enter the Admin pass : ")
    sql = "SELECT EXISTS (SELECT 1 FROM Admin_login WHERE Admin_id = %s and Admin_pass = %s)"
    # sql = "insert into Admin_login value(%s, %s)" # add admin user
    data.insert_data_params(sql,(input1, input2))
    a = 1
a = admin()    