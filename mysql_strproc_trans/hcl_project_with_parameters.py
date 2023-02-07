from hcl_database_connection import MysqlDatabaseConnection
class Booking(MysqlDatabaseConnection):
    def available_seats(self):
        try:
            mydata=(17213,)
            self.cursor.callproc("get_train_details",args=mydata)
            for r in self.cursor.stored_results():
                seats=r.fetchone()
            return seats
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
    def book(self):
        pass
b1=Booking()
b1.connect("localhost","root","Vasantha@123","train_ticket")
sts=b1.available_seats()
seat_avl={}

seat_avl['Train_name']=sts[0]
seat_avl['Seats']=sts[1]
print(seat_avl)
