age=int(input("enter the age"))
job=input("job status ")
if(age>=21):
           if(job=="yes"):
               print("you are eligible for married")
           else:
               print("you are not eligible due to job")
else:
    print("not eligible due to age")
