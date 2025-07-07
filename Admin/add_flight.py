import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from DataBase.Data import DataOperation


data = DataOperation()
class AddFlight:
    def __init__(self):
        self.f_name  = input("Enter flight name      : ")
        self.f_number= input("Enter flight number    : ")
        self.f_st    = input("Enter start point      : ")
        self.f_end   = input("Enter end   point      : ")
        self.date    = input("Enter Date(yyyy-mm-dd) : ") # yyyy-mm-dd 
        self.time    = input("Enter Time(HH:MM:SS)   : ")
    def add_flights(self):
        sql = "INSERT INTO Flight VALUE(%s, %s, %s, %s, %s, %s)"
        data.insert_data_params(sql, (self.f_number,self.f_name, self.f_st, self.f_end, self.date, self.time))

# a = AddFlight()
# a.add_flights()