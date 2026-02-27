def even_numbers(start, end):
    if start % 2 == 0:
        for i in range(start, end + 1, 2):
            yield i
    else:
        start = start + 1
        for i in range(start, end + 1, 2):
            yield i
        
            
                
gen = even_numbers(1, 20)
print("First even:", next(gen))
print("Second even:", next(gen))
print("Third even:", next(gen))