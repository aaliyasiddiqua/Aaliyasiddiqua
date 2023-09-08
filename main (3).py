

def leap_yr(n):

  if((n%4==0 and n%100!=0 or n%400==0)):
  
 print("{} is a leap year".format(n))
 
 else:
   
 print("{} is not aleap year".format


n=int(input("Enter a year:"))

yr=leap_yr(n)