class TuDien:
    def __init__(self):
        self.dict = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        key = tu[0].lower()  # Hàm băm lấy ký tự đầu tiên của từ làm khóa
        if key not in self.dict:
            self.dict[key] = {}
        if dong_nghia is None:
            dong_nghia = []
        if trai_nghia is None:
            trai_nghia = []
        self.dict[key][tu] = (dong_nghia, trai_nghia)

    def DongNghia(self, tu):
        key = tu[0].lower()
        if key in self.dict and tu in self.dict[key]:
            dong_nghia, _ = self.dict[key][tu]
            return dong_nghia
        else:
            return []

    def TraiNghia(self, tu):
        key = tu[0].lower()
        if key in self.dict and tu in self.dict[key]:
            _, trai_nghia = self.dict[key][tu]
            return trai_nghia
        else:
            return []

# Ví dụ sử dụng
tu_dien = TuDien()

# Nhập một số từ vào từ điển
tu_dien.NhapTu("Học", ["Tìm hiểu", "Nghiên cứu"], ["Lười"])
tu_dien.NhapTu("Hạnh phúc", ["Vui vẻ"], ["Buồn", "Khổ"])
tu_dien.NhapTu("Xinh", ["Đẹp"], ["Xấu"])
tu_dien.NhapTu("Xấu", [], ["Xinh"])

# Tra cứu từ đồng nghĩa trong từ điển
dong_nghia = tu_dien.DongNghia("Học")
print("Từ 'Học' có các từ đồng nghĩa:", dong_nghia)

dong_nghia = tu_dien.DongNghia("Hạnh phúc")
print("Từ 'Hạnh phúc' có các từ đồng nghĩa:", dong_nghia)

# Tra cứu từ trái nghĩa trong từ điển
trai_nghia = tu_dien.TraiNghia("Xinh")
print("Từ 'Xinh' có các từ trái nghĩa:", trai_nghia)

trai_nghia = tu_dien.TraiNghia("Xấu")
print("Từ 'Xấu' có các từ trái nghĩa:", trai_nghia)