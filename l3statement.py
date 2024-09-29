# print() have to use one space or tab. it is indextation
if True:
    print("Yes")
else:
    print("No")

if False:
    print("Yes")
else:
    print("No")

if 5 == 5:  #Must be one space 5 == 5
    print("Yes")
else: 
    print("No")

if 5 != 5:
    print("yes")
else:
    print("No")

if 5 > 1:
    print("yes")
else:
    print("No")

if 5 >= 5:
    print("yes")
else:
    print("No")


if 5 < 1:
    print("yes")
else:
    print("No")

if 5 <= 5:
    print("yes")
else:
    print("No")




a = [10,20,30]
b = a
c = [1000,2000,3000]

print(a is b) #True
print(a is c) # False
print(a is not c) # True

x = [10,20,30,40,50]
print(20 in x) # True 
print(5 in x) # False


# value must be same | case sensitive
print("e" in "student") # True
print("o" not in "orange") # True

girls = ["su su","yu yu","nu nu"]
print("yu yu" in girls) # True
print("Yu Yu" in girls) # False
print("yu" in girls) # False



# => isinstance(val,type) | Is this yes[true]
if isinstance("Hello",str):
    print("Yes")
else:
    print("No")

if isinstance(5,int):
    print("Yes")
else:
    print("No")

if isinstance(5.67,float):
    print("Yes")
else:
    print("No")

if isinstance(False,bool):
    print("Yes")
else:
    print("No")

if isinstance(["su su"],list):
    print("Yes")
else:
    print("No")

if isinstance({"name" : "nu nu"},dict):
    print("yes")
else:
    print("No")

# ------------------------------------------------------
# def = function 
def sayname():
    print("Hello Aung Aung")

sayname() # function die after one time invoke | invoke = function recall
sayname()

# 29FN

#comparison Operators
# == Equal
# != No Equal 
# > Greater Than
# < Less Than 
# >= Greater Than or Equal To 
# <= Less Than or Equal To 
# is , is not Identity Operators 
# in , not in Membership Operators 




# Function
# 1. Simple function with No parametrs 
# 2. Function with Parameter
    # (i) Single Parameter Function
    # (ii) Multi Parameter Function
#3. Function with Default Parameter
#4. function witgh a Return Value 
#5. Function with multi Return Values
#6. Lambda Function (Anonymous Function)
    
