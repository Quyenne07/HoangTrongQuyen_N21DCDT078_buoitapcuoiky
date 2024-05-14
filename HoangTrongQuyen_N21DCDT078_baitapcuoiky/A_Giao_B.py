def Giao(a, b):
    # Chuyển đổi mảng a và b thành tập hợp
    set_a = set(a)
    set_b = set(b)
    
    # Tính giao của hai tập hợp để lấy các phần tử chung
    set_c = set_a & set_b
    
    # Chuyển đổi tập hợp kết quả thành danh sách và sắp xếp theo thứ tự tăng dần
    c = sorted(list(set_c))
    
    return c[len(c)-2:len(c)]

# Ví dụ sử dụng
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Giao(a, b)
print(c)  # Output: [3, 9]