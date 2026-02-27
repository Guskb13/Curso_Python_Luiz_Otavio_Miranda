def countdown(start):
    for i in range(start, 0, -1):
        yield i
        
 
    
for num in countdown(5):
    print(num)
        