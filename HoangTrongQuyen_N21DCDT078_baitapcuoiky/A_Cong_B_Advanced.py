MAX_DIGITS = 5  # Số lượng chữ số tối đa trước khi bị tràn

def Cong(a, b):
    # Xác định dấu của kết quả
    sign_a, sign_b = a[0], b[0]
    sign = 0 if sign_a == sign_b else 1

    # Chuyển sang số không dấu
    digits_a, digits_b = a[1:], b[1:]
    digits_a.reverse()
    digits_b.reverse()

    # Cộng hai số không dấu
    result_digits = []
    carry = 0
    max_len = MAX_DIGITS - 1
    for i in range(max_len):
        digit_a = digits_a[i] if i < len(digits_a) else 0
        digit_b = digits_b[i] if i < len(digits_b) else 0
        sum = digit_a + digit_b + carry
        result_digits.append(sum % 10)
        carry = sum // 10

    # Kiểm tra tràn số
    if carry or len(result_digits) > max_len:
        return [sign, -1]

    # Thêm dấu vào kết quả
    result_digits.reverse()
    result = [sign] + result_digits
    return result

# Ví dụ sử dụng
a = [0, 9, 9, 9]
b = [1, 1, 0, 0]
result = Cong(a, b)
print(result)  # Output: [1, 1, 0, 9, 9]

a = [0, 9, 9, 9, 9]
b = [0, 1]
result = Cong(a, b)
print(result)  # Output: [0, -1]