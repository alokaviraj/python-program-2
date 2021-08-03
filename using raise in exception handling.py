try:
      a=int(input("enter the number"))
      b=int(input("enter the number"))
      if b is 0:
        raise ArithmeticError;
      else:
        print("div=",(a/b))
except:
    print("exception is generated")
    
