
class Car1:
    def __inti__(self,barnd,Model_no,price):
        self.barnd=barnd
        self.model_no=Model_no
        self.price=price
        
    def display_fullName(self):
        return f"{self.barnd} {self.model_no}"


class Super_car(Car1):
    def __inti__(self,barnd,Model_no,Price,run_with):
        super.__inti__(barnd,Model_no,Price)
        self.run_with=run_with

# class Super_electric(Super_car):
#     def __inti__(self,barnd,Model_no,Price,run_with,number_of_battery):
#         super.__inti__(barnd,Model_no,Price,run_with)
#         self.number_of_battery=number_of_battery


sk = Super_car('SK', '110DKP', 10000,'electric')

print(sk.display_fullName())