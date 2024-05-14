def gcd_recursive(m,n):
    if n== 0:
        return m
    else:
        return gcd_recursive(n,m%n)

def gcd_iteratve(m,n):
    while n != 0:
        m,n = n,m %n
    return m

m = int(input("Nhap so nguyen duong m: "))
n = int(input("Nhap so nguyen duong n: "))
gcd_recursive_result = gcd_recursive(m,n)
print(f"Uoc chung lon nhat cua {m} va {n} (de quy): {gcd_recursive_result}")
gcd_iteratve_result = gcd_iteratve(m,n)
print(f"Uoc chung lon nhat cua {m} va {n} (vong lap): {gcd_iteratve_result}")


    