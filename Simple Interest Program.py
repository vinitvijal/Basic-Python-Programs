def simple_interest(p,t,r): 
    print('The principal is', p) 
    print('The time period is', t) 
    print('The rate of interest is',r) 
      
    si = (p * t * r)/100
      
    print('The Simple Interest is', si) 
    return si 
      
a = int(input("Enter Your Principal Amount : "))
b = float(input("Enter Your rate of interest : "))
c = int(input("Enter Your Time Period : "))
simple_interest(a, b, c)