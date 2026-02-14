for x in range(20):
    if x % 2 != 0:
            print("odds even are:",x)
result = 0
for x in range(5):
      result += x
      
print(result)
      
result = 1
for x in range(5):
      if x != 0:
      
         result = result * x
print(result)

s = "Hellopython"
s = "hi"+" " + s[5:]
print(s)
s = "hello"
print(len(s))
s = "hello , world"
print(s.replace("world","python"))#just temporary matra
print(s)#original immutable cannot be changed
s = "HellopythonhHhhHHhh"
counter = 0
for x in s.lower():
     if "h"== x :
          counter += 1
          print("h")
s = "          hello wirld    "
print(s.lstrip())
print(s.rstrip())

s = "x   hello world  xxxxxxx"
print(s.strip("x"))

name = "hello    world"
name = name.split()
print(name)

name=['hello','world','dam']
name = "  ".join(name)#list to string matra use hunxa 
print(name)

s = "12334"
print(s.isdigit())

name = "ABCCAA"
print(name.count("A"))

name = "#"*3#string lai 3 le multiply gareko xa integer le vaneko output string auxa###
print(name)