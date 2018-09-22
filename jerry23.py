def is Power Of Two(n): 
    if (n == 0): 
        return False
    while (n != 1): 
            if (n % 2 != 0): 
                return False
            n = n // 2
    return True
  if(is Power Of Two(31)): 
    print('Yes') 
else: 
    print('No') 
if(isPowerOfTwo(64)): 
    print('Yes') 
else: 
    print('No') 
  
