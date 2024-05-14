def Doi_Xung(mang):
    # Kiểm tra xem mang có phải là ma trận vuông không
    n = len(mang)
    for hang in mang:
        if len(hang) != n:
            return False

    # Kiểm tra tính đối xứng
    for i in range(n):
        for j in range(i, n):
            if mang[i][j] != mang[j][i]:
                return False

    return True

mang1 = [[5, 2, 3],
         [2, 7, 5],
         [8, 5, 6]]

mang2 = [[1, 2, 3],
         [2, 4, 5],
         [3, 5, 1]]

print(Doi_Xung(mang1))  # False
print(Doi_Xung(mang2))  # True