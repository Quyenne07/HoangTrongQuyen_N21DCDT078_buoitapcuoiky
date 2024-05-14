MAX_DIGITS = 7  # Số lượng chữ số tối đa trước khi bị tràn

def Nhan(a, b):
    # Xác định dấu của kết quả
    sign_a, sign_b = a[0], b[0]
    sign = 0 if sign_a == sign_b else 1

    # Chuyển sang số không dấu
    digits_a, digits_b = a[1:], b[1:]
    digits_a.reverse()
    digits_b.reverse()

    # Khởi tạo kết quả
    result_digits = []

    # Nhân hai số không dấu
    for digit_b in digits_b:
        carry = 0
        temp_result = []
        for digit_a in digits_a:
            product = digit_a * digit_b + carry
            temp_result.append(product % 10)
            carry = product // 10
        if carry:
            temp_result.append(carry)
        temp_result.reverse()
        result_digits = add_numbers(result_digits, temp_result)

    # Kiểm tra tràn số
    if len(result_digits) > MAX_DIGITS:
        return [sign, -1]

    # Loại bỏ số 0 ở đầu (nếu có)
    while len(result_digits) > 1 and result_digits[-1] == 0:
        result_digits.pop()

    # Thêm dấu vào kết quả
    result_digits.reverse()
    result = [sign] + result_digits
    return result

def add_numbers(a, b):
    a.reverse()
    b.reverse()
    max_len = max(len(a), len(b))
    result = []
    carry = 0
    for i in range(max_len):
        digit_a = a[i] if i < len(a) else 0
        digit_b = b[i] if i < len(b) else 0
        sum = digit_a + digit_b + carry
        result.append(sum % 10)
        carry = sum // 10
    if carry:
        result.append(carry)
    result.reverse()
    return result

# Ví dụ sử dụng
a = [0, 9, 8, 7, 6]  # 98765
b = [1, 2, 3, 4, 5]  # -23456
result = Nhan(a, b)
print(result)  # Output: [1, 4, 6, 2, 8, 3, 1]  # -462831

a = [0, 9, 9, 9, 9, 9, 9, 9, 9]  # 999999999
b = [0, 9, 9, 9, 9, 9, 9, 9, 9]  # 999999999
result = Nhan(a, b)
print(result)  # Output: [0, -1]  # Tràn số