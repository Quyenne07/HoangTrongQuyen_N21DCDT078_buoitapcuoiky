def Factorial(n): # Tinh giai thua cua n
    if n == 0:
        return 1
    else:
        return n * Factorial(n-1)

def Neper(n):
    sum = 0
    for k in range(n+1):
        sum += 1 / Factorial(k)
    return sum

n = int(input("Nhap so nguyen n >= 0: ")) #Nhap so nguyen n
result = Neper(n) # Tinh tong a0 +a1 + ... + an
print(f"Tong a0 + a1 + ... + a{n} = {result}")