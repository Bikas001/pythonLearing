# whate is init method ,construct

# class Person:
#     def __init__(self, first_name,last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

# p1 = Person('Bikas','chaudhary', 21)
# p2 = Person('Indu', 'Mahato', 20)

# print(p1.first_name)
# print(p2.first_name)
    

#instant method

# class Person:
#     def __init__(self, first_name,last_name, age):
#         self.first_name= first_name
#         self.last_name = last_name

#         self.age= age
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

# p1 = Person('Bikas','chaudhary',22)
# p1.full_name()
# print(p1.full_name())



# class Person:
#     cout_instance =0
#     def __init__(self,firstname,lastname,age):
#         Person.cout_instance +=1
#         self.firstName= firstname
#         self.lastName = lastname
#         self.age = age

#     @classmethod
#     def cout_instances(cls):
#         return f"You have created {cls.cout_instance} instances of {cls.__name__} class"
    
#     @classmethod
#     def from_string(cls,string):
#         # string.split(',')
#         first,last,age=string.split(',')

#         return cls(first,last,age)

    
    
#     def full_name(self):
#         return f"{self.firstName} {self.lastName}"
#     def is_above_18(self):
#         return self.age>18
    
#     @staticmethod
#     def hello():
#         print("hello static method call")

#     @property
#     def getFirst(self):
#         return self.firstName

#     @getFirst.setter 
#     def setFristName(self, new_name):
#         self.firstName=new_name
         





# p1=Person("Bikas","chaudhary",20)
# p2= Person.from_string("Bikas,chaudhary,20")

# Person.firstName= "Hari"
# Person.hello()
# print(Person.firstName)
# print(Person.cout_instances())

# # _name # convention pf private name
# # __name__ # dunder/magic methods     



#inherateage

class Phone: # base class /parent class
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price = price

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    def make_a_call(self,number):
        return f"calling {number}"

class Smartphone(Phone): # derived/ chid class
    def __init__(self, brand,model_name,price,ram,internal_memory,rear_camera):
        # Phone.__init__(self,brand,model_name,price)
        super.__init__(brand, model_name, price)
        self.ram=ram
        self.internal_memory= internal_memory
        self.rear_camera=rear_camera


class FlagShipPhone(Smartphone): # derived/ chid class
    def __init__(self, brand,model_name,price,ram,internal_memory,rear_camera,front_camera):

        super.__init__(ram,internal_memory,rear_camera)
        # super(Smartphone).__init__(brand,model_name,price)
        self.front_camera=front_camera

# class FlagshipPhone(Smartphone):
#     def __init__(self, brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
#         super.__init__( brand,model_name,price,ram,internal_memory,rear_camera)
#         self.front_camera= front_camera
    
     
onePlus= FlagShipPhone('onePlus','5',3000,'6 GB','64 GB','20 MP','12 MP')



     
# phone = Phone('nokia','1100',1000)
# Smartphone= FlagshipPhone('onePlus','5',30000,'6 GB','64GB','20 MP','10 MP')
# onePlus = FlagshipPhone('OnePlus','6', 40000,'6GB','128 GB','20 MP','10 MP')

# 
# print(phone.full_name())
print(onePlus.full_name())
# print(Smartphone.full_name())
