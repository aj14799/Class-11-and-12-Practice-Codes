# PYTHON program to find sum of all  
# divisors of a natural number 
import math 
      
# Function to calculate sum of all proper 
# divisors num --> given natural number 
def divSum(num) : 
      
    # Final result of summation of divisors 
    result = 0
      
    # find all divisors which divides 'num' 
    i = 2
    while i<= (math.sqrt(num)) : 
        
        # if 'i' is divisor of 'num' 
        if (num % i == 0) : 
        
            # if both divisors are same then 
            # add it only once else add both 
            if (i == (num / i)) : 
                result = result + i; 
            else : 
                result = result +  (i + num/i); 
        i = i + 1
          
    # Add 1 to the result as 1 is also  
    # a divisor 
    return (result + 1); 
   
# Driver program to run the case 
num = int(input("Enter number"))
print (divSum(num)) 
