
# name= input("Enter your name ")
# print("Hello "+ name)
# age= input("Enter your age ")
# print("Your age is "+ age)


# number_one= int(input("Enter Fist number "))
# second_number= int(input("Enter Second Number "))
# total = number_one + second_number
# print("total is "+ str(total))


# number1 = str(4) #changing to string
# number3 = float("44") #changing to float
# number4 = int("33") #changing to interger 

# name, age ="Bikas", 21
# x=y=z=1
# print("hello " + name + " Your age "+ str(age))

# name,age = input("Enter your name and age ").split(",")

# print(name)
# print(age)


# name="Bikas"
# age="21"
# print("hello {} your age is {} ".format(name,age))#python 3

# print(f"hello {name} your age is {age}")#python 3.6


#string indexing
# language = "python"

# #positions(index number)
# # p = 0 , -6
# # y = 1 , -5
# # t = 2 , -4
# # h = 3 , -3
# # o = 4 , -2
# # n = 5 , -1


# print(language[4])


#slicing / selecting sub sequences
# lang = "python"
# #syntax - [statr argument: stop argumnent]

# print(lang[0:2])

#syntax - [start argument : stop argumnent -1 : step]
# print("Bikash"[0:5:2])
#print("Bikas"[5::-1])

#string Methods

# name= "BiKaS cHaUdHaRy"
# #1.len() function Count the string 

# length= len(name)
# print(length)
# #2. lower() Method
# print(name.lower())

# #3. upper() method
# print(name.upper())
# #4. title() method
# print(name.title())
# #5. count() method
# print(name.count("a"))


#strip method
# name="     Bikas        "
# name="  Bi  kas   "
# dots= "............."
# print(name)
# print(name.lstrip()+dots)
# print(name.rstrip()+dots)
# print(name.strip()+dots)
# x=name.replace(" ", "")
# print(x)



# name,char = input("enter comma sepertaed name and character: ").split(",")
# print(f"lenth of your name is{len(name)} ")
# print(f"character count: {name.strip().lower().count(char.strip().lower())}")

#string = "she is beautiful and she is good dancer"
# print(String.replace("is", "was" , 1))

# print(string.find("is", 1))
# val=string.find("is")
# print(string.find("is", int(val+1)))


#center Method
# name="Bikas"
# print(name.center(9,"*"))

# name=input("Enter your name ")
# print(name.center(len(name)+8 , "*"))


# #strings are immutable

# for letter in 'python':
#     if letter == 'h':
#         break
#     print(f"Current {letter}")

# var= 20
# while var < 0:
#     print(f"Current variable value: {var}")
#     var = var - 1
#     if(var== 5):
#         break
# print("Good bye!")



# age = input("Enter your age: ")
# age= int(age)
# if(age >= 14):
#     print("Your above 14")
# else:
#     print("Sorry you cannt play")

    

# name, age=input("Enter your name and age seprated by ,: ").split(',')
# n=name[0]

# age=int(age)
# if(n== "A" or n =="a" and age >=10):
#     print("You can watch Movie ")
# else:
#     print("Sorry you cannt ")
       

#checking empty or not
#important
# name= "abc"
# if name:#true if the string is empty
#     print("String is not emplty")
# else:
#     print("String is empty")

# i=2
# while i < 10:
#     print(f"Hello world {i}")
#     i = i + 1


# for i in range(2,10):
#     print(f"Hello world {i}")

# name= input("Enter your name: ")
# temp = ""
# for i in range(len(name)):
#     if(name[i] not in temp):
#         print(f"{name[i]}:{name.count(name[i])}")
#         temp +=name[i]

# for j in range(2,10,2):
#     print(j)

# name=input("Enter a number: ")

# for i in name:
#     print(i)

# def add_two(num1,num2):
#     return num1+num2

# a=int(input("Enter First Number "))
# b= int(input("ENter second number"))
# total = add_two(a,b)
# print(total)

# def odd_even(num):
#     if num%2==0:
#         return "even"
#     return "odd"
# print(odd_even(20))

# def is_even(num):
#     if num%2==0:
#         return True
#     else:
#         return False


# def is_even(num):
#     return num%2 ==0
# print(is_even(23))


# def greater3(num1,num2,num3):
#     if num1 <= num2 <= num3:
#         return num3
#     elif num2 <= num3 <= num1:
#         return num1
#     else:
#         return num2

# print(greater3(200,50,40))
# name=[]
# name.append("Bikas")
# name.append("Hari")
# name.append("shyam")
# print(name)


# fruit= ['mango','orange','apple']
# # fruit.insert(2,"grapes")
# # fruit1=['apple','banana']
# # fruit= fruit1 + fruit

# # fruit.extend(fruit1)

# # fruit.append(fruit1)

# #del fruit[1]

# # fruit.pop(1)
# fruit.remove('apple')
# print(fruit)

# if 'apple1' in fruit:
#     print("Present")
# else:
#     print("not")

#count
# sort method
# sorted function
# reverse
# clear
# copy

# print(fruit.count('oragne'))

# fruit.sort()

# print(fruit)
# print(sorted(fruit))



# numbers= list(range(1,4))
# # print(numbers)
# poppoed_items = numbers.pop()
# print(poppoed_items)
# print(numbers.index(1,11,14))

# def negative_list(l):
#     negative= []
#     for i in l:
#         negative.append(-i)
#         i= i+1
#     return(negative)



# print(negative_list(numbers))
# numbers=[1,2,3,4]
# i =0
# def square_list(l):
#     square1=[]
#     for i in l:
        
#         square1.append(i**2)
       
#     return square1

# print(square_list(numbers))

# number = [1,2,3,4]
# def reverse_list(l):
#     l.reverse()
#     return l

# def retun_of_list(l):
#     r_list=[]
#     for i in range(len(l)):
#         popped_itemed= l.pop()
#         r_list.append(popped_itemed)
#     return r_list

# print(retun_of_list(number))


# reversing string [::-1]
# def reverse_elements(l):
#     elements=[]
#     for i in l:
#         elemets_items= i[::-1]
#         elements.append(elemets_items)
#     return elements

# itmes= ["abc","def","ghi"]

# print(reverse_elements(itmes))


# def filter_odd_even(l):
#     odd_list=[]
#     even_list=[]
#     odd_even=[]
#     for i in l:
#         if i % 2 ==0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)
#     odd_even.append(even_list)
#     odd_even.append(odd_list)

#     return odd_even

# numbers=[1,2,3,4,5,6,7,8,9]
# numbers1=[1,3,4,6,0]

# print(filter_odd_even(numbers))

# def filter_list(l1,l2):
#     filter_list_items=[]
#     for i in l1:
#         for j in l2:
#             if(i == j):
#                 filter_list_items.append(i)
    
#     return filter_list_items


# print(filter_list(numbers,numbers1))

# print(max(numbers))
# print(min(numbers))


# def mixed_list(l):
#     count =0
#     for i in l:
#         if type(i) == list:
#             count = count+1
#     return count

# list1=[1,2,3,[1,2],[2,3,4]]

# print(mixed_list(list1))
    

# mixed=(1,2,3,4)
# # for loop and tuple
# for i in mixed:
#     print(i)

# # tuple with ine elemnt
# nums=(1,)

# words=('words',)

# # tuple unpacking

# guitarists =


 #list comperhensive
# squre =[]
# for i in ragne(1,11):
#     squre.append(i**2)

# squre = [i**2 for i in range(1,11)]
# print(squre)
  

# even_number =[i for i in range(1,11) if i%2==0]
# print(even_number)

# if elese

# mixed= [i*2 if (i%2==0) else -i for i in range(1,11)]
# print(mixed)

# new_list=[[i for i in range(1,4)] for j in range(3)]
# print(new_list)
 
# dictionar comperhension

#squre ={1:1,2:4,3:9 }


# squre ={num:num**2 for num in range(1,11)}
# print(squre)

# def add(a,b):
#     if (type(a) is int and type(b) is int):
#         return a+b
#     raise TypeError('OOP your are passing worng data type to function')

# print(add('2','3'))

while True:
    try:
        age = input(input('enter your age'))
        break
    except ValueError:
        print('maybe you entret strj f j stead od number, try again')
    except:
        print('unexpected error ... ')

if age < 18:
    print('you can\t play this game.')
else:
    print('you can play this game.')