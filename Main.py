#loops
numbers = [1, 2, 3, 4, 5, 6, 7]
#for each
for i in numbers:
    print (i)

#while loop
i = 0
while i < 10:
    i += 1

#if
num = 2
if num < 3:
    print ('Under 3')
elif num > 3:
    print ('Over 3')
else:
    print ('Equal 3')

#Class, Inheritance, and Modules
from Rectangle import Rectangle

rec = Rectangle(10, 20)
rec.move(20, 10)


#error testing
try:
    num = 3/0
except ZeroDivisionError:
    print ("Cannot divide by zero")
except ValueError:
    print ("Enter a number")
except IOError:
    print ("File not found")
finally:
    print ("done")

