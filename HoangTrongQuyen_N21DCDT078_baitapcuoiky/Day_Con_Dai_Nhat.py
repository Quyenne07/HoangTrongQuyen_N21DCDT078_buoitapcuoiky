def DayConDaiNhat(a, b):
    n, m = len(a), len(b)
    max_len = 0
    start_idx = -1
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    start_idx = i - max_len
            else:
                dp[i][j] = 0

    if max_len == 0:
        return []
    else:
        return a[start_idx:start_idx + max_len]

# Ví dụ sử dụng
a = [1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5]
b = [6, 2, 5, 3, 7, 9, 8, 1, 5]
c = DayConDaiNhat(a, b)
print(c)  # Output: [6, 2, 5, 3, 7, 9]