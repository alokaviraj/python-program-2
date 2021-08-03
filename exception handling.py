a=int(input("enter the number"))
b=int(input("enter the number"))
try:
    c=a/b
    print("division=",c)
except:#:(Exception):
    print("number not divide by 0")
finally:
    print("R u satisfied")
    
