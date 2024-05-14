def sum_of_divisors(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    return sum(divisors)

def Number(x, y):
    for n in range(x, y+1):
        s = sum_of_divisors(n)
        if s < n:
            print(f"{n} is deficient")
        elif s == n:
            print(f"{n} is perfect")
        else:
            print(f"{n} is abundant")

# Nhập vào hai số nguyên dương x và y
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))

if x <= y:
    Number(x, y)
else:
    print("Giá trị x phải nhỏ hơn hoặc bằng y")