#*args and **kwargs - only * matters, not the name kargs,vargs
def function1(*args1):
    if (len(args1)==3):
      print("The name of student is",args1[0], "age is",args1[1] ,"and rollnumber is ",args[2] )
    else:
       print("The name of student is",args1[0], "age is",args1[1])


def printmarks(**kwargs):
   print(type(kwargs))
   for key,value in kwargs.items():
      print(key,value)


def master(normal,*args,**kwargs):
   print(normal)
   for i in args:
      print(i)
   for key,value in kwargs.items():
      print(key,value)
  
lis = {"Harry",33,334567}  
marklist= {"Harry":100, "Rohan":97, "Aman":91, "Anjali":89}

#printmarks(**marklist)

master("normal args",*lis, **marklist)






