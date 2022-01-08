# age=int(input("Enter Your Age Here:- "))
# if age>=18:
#     print("you can vote")
# else:
#     print("you can't vote")

# number=int(input("Enter Number:- "))
# if number%2==0:
#     print (number,"is a even number")
# else:
#     print(number,"is a odd number")

# number=int(input("Enter number:- "))
# if number%7==0 and number!=0:
#     print(number,"is divisible by 7")
# else:
#     print(number,"is not divisible by 7")

number=int(input("Enter number:- "))
if number%5==0 and number>=5:
    print("hello")
else:
    print("bye")

# unit=int(input("enter unit:-"))
# if unit<=100:
#     print("no charges")
# elif unit>100 and unit<=200:
#     print((unit-100)*5)
# else:
#     print((100*5)+(unit-200)*10)

# num=int(input("enter number:- "))
# num1=num%10
# if num1%3==0 and num1!=0:
#     print("last digt of",num,"is divisible by 3")
# else:
#     print("last digt of",num,"is not divisible by 3")

# per=int(input("Enter your marks:- "))
# if per>90:
#     print("Grade A")
# elif per>80 and per<=90:
#     print("Grade B")
# elif per>60 and per<=80:
#     print("Grade C")
# else:
#     print("Grade D")

# cost=int(input("enter cost of bike:- "))
# if cost<=50000:
#     print("tax=",cost/100*5)
# elif cost>50000 and cost<=100000:
#     print("tax=",cost/100*10)
# elif cost>100000:
#     print("tax=",cost/100*15) 

year=int(input("Enter Year:- "))
if year%4==0 and year%100!=0 or year%400==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")

# city=input("enter name of the city:- ")
# if city.lower()=="delhi":
#     print("Monument name is : Red For")
# elif city.lower()=="agra":
#     print("monument name is : Taj mahal")
# elif city.lower()=="jaipur":
#     print("monument name is : Jal Mahal")
# else:
#     print("Enter Correct name of city")

# wd=int(input("Enter Total Working Days:- "))
# ad=int(input("Enter Total Days of absent:- "))
# pd=wd-ad
# print("Percentage of present:-",pd/wd*100)
# if pd>=75:
#     print("able to sit in exam")
# else:
#     print("not able to sit in exam")

# age=int(input("Enter your age(18 to 40):- "))
# sex=input("Enter you sex(M/F):- ")
# days=int(input("Enter your working days:- "))
# if age>=18 and age<30:
#     if sex.upper()=='M':
#         print(700*days)
#     elif sex.upper()=='F':
#         print(750*days)
# elif age>=30 and age<=40:
#     if sex.upper()=='M':
#         print(800*days)
#     elif sex.upper()=='F':
#         print(850*days)
# else:
#     print("enter appropriate age")

# en=int(input("marks in english:- "))
# math=int(input("marks in maths:- "))
# sci=int(input("marks in science:- "))
# sos=int(input("marks in social studies:- "))
# if en>80 and math>80 and sci>80 and sos>80:
#     print("Science Stream")
# elif en>80 and math>50 and sci>50:
#     print("Commerce Stream")
# elif en>80 and sos>80:
#     print("Humanities")
# else:
#     print("we can't alot you any stream")

# a=input("Enter your Password:- ")
# if a.isspace:
#     print("Strong")

print("praveen is don!")
