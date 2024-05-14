def Fibonacci_Recursive(n): #Tinh so Fibonacci thu n bang de qui
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Recursive(n-1) + Fibonacci_Recursive(n-2)

def Fibonacci_Iterative(n): #Tinh so Fibonacci thu n bang vong lap
    if n <= 0:
        return 0
    elif n ==1:
        return 1
    else:
        a, b = 0, 1
        for i in range(n-1):
            a, b = b, a + b
        return b

n = int(input("Nhap so nguyen n >= 0: ")) #Nhap so nguyen n
print(f"So Fibonacci thu {n} (de qui): {Fibonacci_Recursive(n)} ") #Tinh so Fibonacci thu n bang de qui
print(f"So Fibonacci thu {n} (vong lap): {Fibonacci_Iterative(n)}") #Tinh so Fibonacci thu n bang vong lap


    



