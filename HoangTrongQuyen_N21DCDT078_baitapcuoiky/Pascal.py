def Pascal(n):
    n = int(n)
    triangle = []
    triangle.append([1])

    for i in range(1, n +1):
        row = [1] * (i+1)

        for j in range(1,i):
            row[j]= triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)


    for row in triangle:
        print(" "*(n-len(row)+1), end="")
        for val in row:
            print(f"{val:>3}", end="")
        print()
Pascal(4)