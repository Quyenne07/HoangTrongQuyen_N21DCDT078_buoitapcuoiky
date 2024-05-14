MAX_DIGITS = 10  # Số lượng chữ số tối đa trước khi bị tràn

def Tru(a, b):
    # Xác định dấu của kết quả
    sign_a, sign_b = a[0], b[0]
    sign = sign_a

    # Chuyển sang số không dấu
    digits_a, digits_b = a[1:], b[1:]
    digits_a.reverse()
    digits_b.reverse()

    # Trừ hai số không dấu
    result_digits = []
    borrow = 0
    max_len = MAX_DIGITS - 1
    for i in range(max_len):
        digit_a = digits_a[i] if i < len(digits_a) else 0
        digit_b = digits_b[i] if i < len(digits_b) else 0
        diff = digit_a - digit_b - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result_digits.append(diff)

    # Kiểm tra tràn số
    if borrow or len(result_digits) > max_len:
        return [sign, -1]

    # Loại bỏ số 0 ở đầu (nếu có)
    while len(result_digits) > 1 and result_digits[-1] == 0:
        result_digits.pop()

    # Thêm dấu vào kết quả
    result_digits.reverse()
    result = [sign] + result_digits
    return result

# Ví dụ sử dụng

a = [1, 9, 9, 9, 9]  # -9999
b = [0, 1, 2, 3, 4]  # 1234
result = Tru(a, b)
print(result)  # Output: [1, 8, 7, 6, 5]  

a = [0, 9, 9, 9, 9]  # 9999
b = [0, 9, 9, 9, 9]  # 9999
result = Tru(a, b)
print(result)  # Output: [0, 0]  # 0

a = [0, 1, 2, 3, 4]  # 1234
b = [0, 9, 9, 9, 9]  # 9999
result = Tru(a, b)
print(result)  # Output: [0, -1]  # Tràn số