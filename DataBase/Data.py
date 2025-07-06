import mysql.connector



class DataOperation:
    def __init__(self):
        self.var = mysql.connector.connect(password = 'lalithrajr838@', user = 'root', database = 'FLIGHT_BOOKING', host = 'localhost')
        self.cur = self.var.cursor()   
                                                                                   # Insert data
    def insert_data_params(self,data_in,params):
                try:
                    self.insert = self.cur.execute(data_in, params)
                    self.var.commit()
                    print(" You have sucessfully registered")
                except mysql.connector.errors.IntegrityError:
                    print("You have already Registered.")     
                except mysql.connector.errors.DataError:
                    print("your entered huge data")           
    def insert_data(self,data_in):               
                self.insert = self.cur.execute(data_in)
                self.var.commit()
                print("You have sucessfully registered")
                      
    def select_data(self,data_in,params = None):
        if params: # here params = 1
            self.cur.execute(data_in, params)
        else:
            self.cur.execute(data_in)
        return self.cur.fetchall()