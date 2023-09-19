try:
    filr =open("this.txt",'r')

except EOFError as e:
    print("eof error")
except IOError as e:
    print("We can handle the error")
               
finally:
    print("This will get printed irrespective of the exception occureneces")
