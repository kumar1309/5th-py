def getMaxToys(prices, money):
    n = len(prices)
    left = 0  
    current_sum = 0  
    max_toys = 0 
    
    
    for right in range(n):
        current_sum += prices[right]
        
       
        while current_sum > money:
            current_sum -= prices[left]
            left += 1
        
        max_toys = max(max_toys, right - left + 1)
    
    return max_toys


n = 7
prices = [1, 4, 5, 3, 2, 1, 6]
money = 6

print(getMaxToys(prices, money))  
