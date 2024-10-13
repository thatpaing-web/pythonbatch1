# Function
# 1. Simple function with No parametrs 
# 2. Function with Parameter
    # (i) Single Parameter Function
    # (ii) Multi Parameter Function
#3. Function with Default Parameter
#4. function witgh a Return Value 
#5. Function with multi Return Values
#6. Lambda Function (Anonymous Function)


# : = to be continute
# + = concat

#-------------------------------------------

#1. Simple function with No Parameter
def sayname():
    print("Helo Aung aung")

sayname()
sayname()

#-------------------------------------------


# 2. Function with Parameter
#   (i) Single Parameter Function
def saycity(city):
    print("Hello " + city)

saycity("Yangon")
saycity("Mandalay")

#-------------------------------------------

# 3. Function with Default Prameter 
def country(country="Thailand"):
    print(f"Hello {country}")

country()
country("Myanmar")
country("Indonesia")

#-------------------------------------------

# return function is used to call other location [use to call again and again inside of other function]
# both return function & print out function are not same

# 4. Function with a Return Value 

def sayname():
    return "I am 25 years old"

print(sayname())


def saynickname():
    result = "Daw Pu"
    return result

print(saynickname())

def saynum(num1 = 20):
    return num1

print(saynum(100))  #100
print(saynum()) # 20

###########
def greeting(value="yamin"):
    return f"Hello {value}"

print(greeting("Su Su"))
print(greeting())


def funone(num1,num2):
    result = num1 + num2
    return result

print(funone(10,20))

def funtwo(num1,num2=200):
    result = num1 + num2
    return f"Total value is = {result}"

print(funtwo(10))  # 210
print(funtwo(10,20)) # 30



#-------------------------------------------

# 5. Function with multi Return VAlues     ,  [ same with object destructuring in jsES6 but in python no need to same keyname]

def saynameandage():
    name = "Honey"
    age = 26 
    city = "Yangon"
    return name,age,city

print(saynameandage())  #('Honey', 26)

name,age,city = saynameandage()
print(name)  # Honey 
print(age) # 26
print(city)

#-------------------------------------------

# 6. Lambda Function (Anonymous Function) [single line only]
addresult = lambda num1,num2,num3 : num1+num2+num3
print(addresult(200,300,400))

sumresult = lambda num1,num2 = 200 ,num3 = 500 : num1+num2+num3
print(sumresult(200,300)) # 1000
print(sumresult(100)) # 800

# prompt
# interval = input("Enter Your Name = ")
# msg = "Hello " + interval
# msg = "Hello %s " % interval # version-2 [don't use]
# msg = f"Hello {interval}" # Version-3
# print(msg)

firstname = input("Enter First Name = ")
lastname = input("Enter Last Name = ")
# fullname = "Hello %s%s" % (firstname,lastname) # v-2 
# fullname = "Hello %s %s" % (firstname,lastname) # v-2
fullname = f"Hello {firstname} {lastname}" # v-3

print(fullname)



#-------------------------------------------

