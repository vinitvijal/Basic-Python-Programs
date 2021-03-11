def compound_interest(principle, rate, time): 

    Amount = principle * (pow((1 + rate / 100), time)) 
    CI = Amount - principle 
    print("Compound interest is", CI) 
  
      
a = int(input("Enter Your Principal Amount : "))
b = float(input("Enter Your rate of interest : "))
c = int(input("Enter Your Time Period : "))
compound_interest(a, b, c) 
  