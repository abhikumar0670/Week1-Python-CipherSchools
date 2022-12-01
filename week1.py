# print("OM NAMAH SHIVAY")
# '''print("om \"namah\"shivay")'''
# print("hello\nworld")
#  print("hello\t wor;d")
# print("this is singe slash\\ ND THIS IS DOUBLE\\\\")
# print("linr a \\n line b")
# <--------------exersice 1----------------->
# print("This is \\\\ double backslash")
# print("these are mountains/\\/\\/\\/\\")
# print("He is \t awesome")
# print("\\\" \\n \\t \\\'")
# print(r"This is \n backslash")
# number1=int(input())
# num2=int(input())
# total=number1+num2
# print("The total is",total)
# name="Abhishek"
# age=18
# print("hello {} your age is {}".format(name,age))
# <----------------------exersise2------------------->
# num1=int(input())
# num2=int(input())
# num3=int(input())
# #  num1,num2,num3=int(input("comma seperated num").split(","))                     used for strings to seperate
# print(f"average is{(num1+num2+num3)/3}") 
# <------------------------------string indexing----------------------------------->
# lang="helloabhishek"
# print(lang[2:5])
# print("Abhishek"[5::-1])
# <----------------exercise--------------------------------->
# name,char =input("comma sep name: ").split(",")
# print(f" length of your name{len(name)}")
# print(f"character count:{name.count(char)}")
# string="she is beautiful and she is good dancer"
# print(string.replace("is","-",1))
# is_pos=string.find("is")
# is_pos2=string.find("is",is_pos+1)
# print(is_pos2)
# name="Abhishek"
# print(name.center(8,"*"))
# name=input("enter your name:")
# print(name.center(len(name)+8,"*"))
# string="string"
# string[1]="T"            cannot give output because string are immutable
# print(string.replace("t","T"))           stored in new 
# print(string)
# name="harsh"
# name+="it"
# print(name)
# age = input("enter your age: ")
# age = int(age)
# if age>= 14:
#     print("your are about 14")
# else:
#     print("you are below 14")
#<---------------------------chapter3 exersise1--------------------------->
# winning_number = 27
# user_input= input("guess a number b/w 1 and 100 : ")
# user_input=int(user_input)
# if user_input == winning_number:
#     print("YOU WIN!!")
# else:
#     if user_input <winning_number:
#         print("too low")
#     else:
#         print("too high")
# name='abc'
# age =18
# if name=='abc' and age==18:
#     print("condition true")
# else:
#     print("false")
# name=input("enter your name: ")
# age=int(input("enter your age:"))
# if (name[0]=='a' or name[0]=='A')and age > 10:
#     print("you can watch")
# else:
#     print("you can naot watch")
#<-----------------------------------while loop---------------------------------->
# i=1
# while i<=10:
#     print(f"helooooooooo{i}")
#     i+=1
# total=0
# i=1
# while i<=10:
#     total=total+i
#     i=i+1
# print(total)
#<--------------exercise3>>>>>>>>>>>>>>>
# n=int(input("enter number"))
# total=0
# i=1
# while i<=n:
#     total+=i
#     i+=1
# print(total)
#<<<<<<<<<<<<<<<<<<<<exercise4>>>>>>>>>>>>>>>>>>>>>>>>
# n=input("enter a number")
# total=0
# # int(number[i])
# i=0
# while i<len(n):
#     total+=int(n[i])
#     i+=1
# print(total)
#<<<<<<<<<<<<<<<<<<<<exercise5>>>>>>>>>>>>>>>>>>>>>>>>
# name =input("enter your name:")
# temp_var=""
# i=0
# while i<len(name):
#     if name[i] not in temp_var:
#         temp_var +=name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
#     i+=1
#<<<<<<<<<<<<<<<<<<<<infinite loop>>>>>>>>>>>>>>>>>>>>>>>>
# i=0
# while i<=10:
#     print("hello world")
# while True:
#     print('hello world')