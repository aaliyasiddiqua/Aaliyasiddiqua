

"""""

1!=1*1

2!=2*1! ---->2*1

3!=3*2! ----->3*2*!

.

.

10!=10*9*8*...*1


formula-n*(n-1)!

"""





def fact_rect(n):
  
  if n==0 or n==1:
    
    return 1

    else:
    
    return n*fact_rect(n-1)


number=int(input("Enter a value:"))

rec=fact_rect(number)



print("The factorial of {} is {}".format(number,rec))
