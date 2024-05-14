class Mang:
    def __init__(self, mang):
        self.mang = mang

    def Dao(self):
        def dfs(i, j):
            if i < 0 or i >= len(self.mang) or j < 0 or j >= len(self.mang[0]) or self.mang[i][j] != 1:
                return 0, 0, 0, 0

            self.mang[i][j] = -1
            left = right = top = bottom = 1

            for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                l, r, t, b = dfs(i + di, j + dj)
                left = max(left, l)
                right = max(right, r)
                top = max(top, t)
                bottom = max(bottom, b)

            return left + right - 1, right, top, bottom

        max_area = 0
        for i in range(len(self.mang)):
            for j in range(len(self.mang[0])):
                if self.mang[i][j] == 1:
                    area, _, _, _ = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area

# Ví dụ
mang = [[0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1]]

obj = Mang(mang)
max_area = obj.Dao()
print("Diện tích lớn nhất của đảo hình chữ nhật là:", max_area)