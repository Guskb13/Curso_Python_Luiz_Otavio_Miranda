def fibonacci():
    a, b  = 1 , 1
    
    while True:
        yield a
        a, b = b, a + b
   
        


for fib in fibonacci():
    if fib > 100:
        print(f"The first Fibonacci number greater than 100 is: {fib}")
        break