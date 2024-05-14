def Trung_Hang(mang):
    n = len(mang)
    
    # Kiểm tra xem mang có phải là ma trận vuông không
    for hang in mang:
        if len(hang) != n:
            return False
    
    # Duyệt qua các cặp hàng
    for i in range(n):
        for j in range(i+1, n):
            if mang[i] == mang[j]:
                return True
    
    return False

mang1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

mang2 = [[1, 3, 5],
         [2, 4, 6],
         [1, 3, 5]]

print(Trung_Hang(mang1))  # False
print(Trung_Hang(mang2))  # True