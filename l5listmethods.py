names = ["aung aung","maung maung","su su","yu yu","nandar"]
print(names)

mixeds = [1500,"hello",123.6,True,"world",False]
print(mixeds) # [1500, 'hello', 123.6, True, 'world', False]

print(mixeds[0]) # 1500
print(mixeds[3]) # True
print(mixeds[-1]) # False
print(mixeds[-2]) # world

print(mixeds[0:1])
print(mixeds[0:2])
print(mixeds[1:3])
print(mixeds[0:6])

#start:end:step
print(mixeds[0:6:2])
print(mixeds[0:6:3])

mix2 = mixeds
mix2 = mixeds[:]
mix2 = mixeds[0:4]
mix2 = mixeds[::-1] # [False, 'world', True, 123.6, 'hello', 1500]
print(mix2)

getlength = len(names) 
print(getlength) # 5


#----------------

# can't use if the value doesn't have
colors = ["red","green","blue"]
print(colors)

#colors[3] "silver" # error
#print(colors)

colors[0] = "pink"
print(colors)

#----------------
#add data from end (single)
#.append() [for single value]
colors.append("white")
#colors.append("black","violet") #error
print(colors)


#----------------

# add data from end (multi)

# .extend() [for multi value]
colors.extend(["gold"]) # ['pink', 'green', 'blue', 'white', 'gold']
colors.extend(["black","violet"]) # ['pink', 'green', 'blue', 'white', 'gold', 'black', 'violet']
print(colors)


#----------------

# insert(,)
colors.insert(0,"steelblue") # ['steelblue', 'pink', 'green', 'blue', 'white', 'gold', 'black', 'violet']
print(colors)


#----------------

# remove value and index 

#remove
colors.remove("green") # ['steelblue', 'pink', 'blue', 'white', 'gold', 'black', 'violet']
print(colors) 

#----------------

#remove from end value and index 
# pop()
colors.pop() # ['steelblue', 'pink', 'blue', 'white', 'gold', 'black']
print(colors)

#----------------

#remove value and index 
# del varavle[]
del colors[1] # ['steelblue', 'pink', 'blue', 'white', 'gold', 'black']
del colors[1:3] # ['steelblue', 'gold', 'black']
print(colors)

#----------------

# clear()
vals = [1,2,3,4,5]
print(f"Before clear values {vals}") # Before clear values [1, 2, 3, 4, 5]

vals.clear() 
print(f"After clear values {vals}") # After clear values []

#----------------
# sort()
boys = ["aung aung","zaw zaw","kyaw kyaw","hein min ","yae lay","min khant"]
boys.sort()
print(boys) # ['aung aung', 'hein min ', 'kyaw kyaw', 'min khant', 'yae lay', 'zaw zaw']


# reverse()
boys.reverse() 
print(boys) # ['zaw zaw', 'yae lay', 'min khant', 'kyaw kyaw', 'hein min ', 'aung aung']

nums = [10,115,11,1,50,30,75,25,65,90,110] # [1, 10, 11, 25, 30, 50, 65, 75, 90, 110, 115]
nums.sort()
print(nums)

nums.reverse() # [115, 110, 90, 75, 65, 50, 30, 25, 11, 10, 1]
print(nums)

#----------------

#count()
message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy Text ever since the 1500s lorem"
countoflorem = message.count("Lorem") # 2
print(countoflorem)

countoftext = message.count("text")
print(countoftext) # 1

ages = [18,25,30,18,25,25,20,18,25]
countof18 = ages.count(18)
print(countof18) # 3

countof20 = ages.count(20)
print(countof20) # 1

countof25 = ages.count(25)
print(countof25)  # 4

#----------------

# nested list 
numbers = [[1,2,3],[40,50,60],[700,800,900]]
print(len(numbers)) # 3
print(numbers[0]) # [1, 2, 3]
print(numbers[1]) # [40, 50, 60]
print(numbers[2]) # [700, 800, 900]

# print(numbers[3]) # Error

print(numbers[2][0]) # 700
print(numbers[2][2]) # 900

numbers.append([1000,2000])
print(numbers) # [[1, 2, 3], [40, 50, 60], [700, 800, 900], [1000, 2000]]

numbers.pop()
print(numbers) # [[1, 2, 3], [40, 50, 60], [700, 800, 900]]

numbers.pop(1)
print(numbers) # [[1, 2, 3], [700, 800, 900]]

# 20ME
 
