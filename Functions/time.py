import datetime

def get_time():
    return datetime.datetime.now()

def get_result(num1, num2, num3):
    sum = num1 * num2
    sum = sum/num3
    print(sum)

def get_name():
    name = input("Enter your name:  ")
    print(name)

a = 50
b = 100
c = 2
get_result(a, b ,c)

get_name()

get_result(num1=25, num2=4, num3=2)

print(get_time())

get_name()
