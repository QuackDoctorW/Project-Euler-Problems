#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
#approach: 999x999, 998x999,998x998,997x999,997x998,997x999... to ensure highest possible <- wrong
def findpal(maxi,mini):
    palindrome = 0
    for i in range(maxi,mini-1,-1):                                                #find highest untested number in descending order
        for j in range(maxi,i-1,-1):                                              #find range of second number to multiply in decending order
            product = i*j                                                        #get product
            product = str(product)                                               #to string
            for x in range(len(product)//2):                                     #loop half of string to check first equals last
                if product[x]!=product[-x-1]:                                    #if doesnt equal, break - this is a product that doesn't work;
                    break
                elif x == len(product)//2-1:                                     #if it does work, check if this is the last round - meaning all previous checks should worked; 
                    palindrome = max(int(product),palindrome )
    return palindrome
print(findpal(999,100))
                
    
        