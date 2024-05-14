class TuDien:
    def __init__(self):
        self.dict = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        key = tu[0].lower()  # Hàm băm lấy ký tự đầu tiên của từ làm khóa
        if key not in self.dict:
            self.dict[key] = {}
        self.dict[key][tu] = (dong_nghia, trai_nghia)

    def TraTu(self, tu):
        key = tu[0].lower()
        if key in self.dict and tu in self.dict[key]:
            dong_nghia, trai_nghia = self.dict[key][tu]
            return dong_nghia, trai_nghia
        else:
            return None, None

# Ví dụ sử dụng
tu_dien = TuDien()

# Nhập một số từ vào từ điển
tu_dien.NhapTu("Học", "Tìm hiểu", "Lười")
tu_dien.NhapTu("Hạnh phúc", "Vui vẻ", "Buồn")
tu_dien.NhapTu("Xinh", "Đẹp", "Xấu")
tu_dien.NhapTu("Xấu", "Không có", "Xinh")

# Tra cứu từ trong từ điển
dong_nghia, trai_nghia = tu_dien.TraTu("Học")
print("Từ 'Học' có từ đồng nghĩa:", dong_nghia, "và từ trái nghĩa:", trai_nghia)

dong_nghia, trai_nghia = tu_dien.TraTu("Hạnh phúc")
print("Từ 'Hạnh phúc' có từ đồng nghĩa:", dong_nghia, "và từ trái nghĩa:", trai_nghia)

dong_nghia, trai_nghia = tu_dien.TraTu("Xinh")
print("Từ 'Xinh' có từ đồng nghĩa:", dong_nghia, "và từ trái nghĩa:", trai_nghia)

dong_nghia, trai_nghia = tu_dien.TraTu("Xấu")
print("Từ 'Xấu' có từ đồng nghĩa:", dong_nghia, "và từ trái nghĩa:", trai_nghia)
