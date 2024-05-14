def Hieu(a, b):
    # Chuyển đổi mảng a và b thành tập hợp
    set_a = set(a)
    set_b = set(b)
    
    # Tính hiệu của hai tập hợp để loại bỏ các phần tử trùng nhau
    set_c = set_a - set_b
    
    # Chuyển đổi tập hợp kết quả thành danh sách và sắp xếp theo thứ tự tăng dần
    c = sorted(list(set_c))
    
    return c

# Ví dụ sử dụng
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Hieu(a, b)
print(c)  # Output: [1, 4, 5, 7]