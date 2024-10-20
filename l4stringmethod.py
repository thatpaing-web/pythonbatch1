name = "Aung Kyaw"

# can call by index_number , start - 0
# to call from last use minus "-" , start - 1
print(name)
print(name[0]) #a
print(name[3]) #g
print(name[8]) #w
print(name[-1]) #w 
print(name[-2]) #a 
print(name[-8]) #u

#start:end:step

print(name[0:1]) #a
print(name[0:2]) #au
print(name[0:3]) #aun
print(name[0:4]) #aung

print(name[1:4]) #ung
print(name[1:7]) #ung ky
print(name[0:9]) #aung kyaw

print(name[0:9:1]) #aung kyaw
print(name[0:9:2]) #an yw
print(name[0:9:3]) #agy

# minut 1 [-1] is the last one
# reference
fullname = name # Aung Kyaw
fullname = name[:] #Aung Kyaw
fullname = name[0:4] # Aung 
fullname = name[::-1] # wayK gnuA

print(fullname)


# -------------------

# upper() , lower() , capitalize() , title() , strip() , lstrip() , rstrip() , replace(,)

# len() means length
getlength = len(name)
print(getlength) # 9

text = "hello friend"
print(text.upper()) # HELLO FRIEND

print(text.capitalize()) # Hello friend
print(text.title()) # Hello Friend

task = "HAVE TO GO"
print(task.lower()) # have to go
print(task.casefold()) # have to go


todo = "Have To Shop"
print(todo.swapcase()) # hAVE tO sHOP

hifi = "         hello friend          "
print(hifi) #          hello friend         
print(hifi.strip()) # hello friend
print(hifi.lstrip()) # hello friend         
print(hifi.rstrip()) #          hello friend

# replace(,)  | this is casesensative
greet = "hello friend"
print(greet.replace("friend","sir")) # hello sir
print(greet.replace("Friend","sir")) # hello friend

# startswith()  | case sensative
print(greet.startswith("h")) # True
print(greet.startswith("he")) # True 
print(greet.startswith("H")) # False 
print(greet.startswith("He")) # False 


# endswith()
print(greet.endswith("nd")) # True 
print(greet.endswith("friend")) # True 
print(greet.endswith("Friend")) # False

# isupper() 
mobile = "OPPO"
print(mobile.isupper()) # True

# islower()
print(mobile.islower()) # False 

num1 = 528
num2 = "1500"
num3 = "ten"
num4 = "number ten"
num5 = "hay!"

# isdigit() & str()
# print(num1.isdigit()) # error cuz of sidigit() can check only fo rstring 
print(str(num1).isdigit()) # True 
print(num2.isdigit()) # True 
print(num3.isdigit()) # False

# isalpha()
print(num2.isalpha()) # False
print(num3.isalpha()) # True

#isnumeric()
print(num2.isnumeric()) # True
print(num3.isnumeric()) # False


#isalnum() | al = alpha , num = numeric [use to restric special character]
print(num2.isalnum()) # True
print(num3.isalnum()) # True

print(num4.isalnum()) # false [cuz space]
print(num5.isalnum()) # False [cuz !]


# isspace()  | can check only one space
nickname = "Aung Moe"
print(nickname.isspace()) # False 

# istitle()
print(nickname.istitle()) # True


# split()
sayhi = "Hi My Friend"
print(sayhi.split()) # ['Hi', 'My', 'Friend']

# rsplit()
color = "red,green,blue,white,black" 
print(color.rsplit()) # ['red,green,blue,white,black']

# splitlines() = newline | \n
sayhello = "Hello\nFriend"
print(sayhello.splitlines()) # ['Hello', 'Friend']

#partition(" ") | at least need one space
sayhifi = "Hello Friend Mr.Maung"
print(sayhifi.partition(" ")) # ('Hello', ' ', 'Friend Mr.Maung')
print(sayhifi.partition("."))  # ('Hello Friend Mr', '.', 'Maung')

post = "Read"
# ljust(,)
print(post.ljust(10,"-")) # Read------

# rjust(,)
print(post.rjust(10,"-")) # ------Read

# center(,)
print(post.center(10,"-")) # ---Read---

#format()
city = "Hello {}"
print(city.format("Mandalay")) # Hello Mandalay

country = "Hello {} {}" 
print(country.format("Mandalay","Myanmar")) # Hello Mandalay Myanmar


print("Hello my{}. are you {}!".format("friend","Aung Aung")) # Hello myfriend. are you Aung Aung!
val1 = "sister"
val2 = "Su Su"
print("Hello my {}. are you {}".format(val1,val2)) # Hello my sister. are you Su Su



# dictionary 

# format_map()
student = {"name" : "Su Su"}
sayname = "Dear, {name}"
print(sayname.format_map(student)) # Dear, Su Su





# 13SM