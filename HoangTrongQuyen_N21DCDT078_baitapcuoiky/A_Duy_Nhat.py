def Duynhat(a):
    # Tạo một tập hợp để loại bỏ các phần tử trùng nhau
    unique_set = set(a)
    
    # Chuyển tập hợp thành danh sách và sắp xếp theo thứ tự tăng dần
    b = sorted(list(unique_set))
    
    return b

# Ví dụ sử dụng
a = [1, 5, 3, 7, 5, 9, 7]
b = Duynhat(a)
print(b)  # Output: [1, 3, 5, 7, 9]