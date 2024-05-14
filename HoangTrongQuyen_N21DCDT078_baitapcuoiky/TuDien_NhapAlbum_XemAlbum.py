class TuDien:
    def __init__(self):
        self.albums = {}

    def NhapAlbum(self, ten_album, danh_sach_bai_hat):
        if ten_album in self.albums:
            print(f"Album '{ten_album}' đã tồn tại trong từ điển.")
            return

        self.albums[ten_album] = danh_sach_bai_hat

    def XemAlbum(self, ten_album):
        if ten_album not in self.albums:
            print(f"Không tìm thấy album '{ten_album}' trong từ điển.")
            return

        print(f"Thông tin album '{ten_album}':")
        danh_sach_bai_hat = self.albums[ten_album]
        for i, bai_hat in enumerate(danh_sach_bai_hat, start=1):
            ten_bai_hat, ten_nhac_si, ten_ca_si = bai_hat
            print(f"{i}. Tên bài hát: {ten_bai_hat}")
            print(f"   Nhạc sĩ: {ten_nhac_si}")
            print(f"   Ca sĩ: {ten_ca_si}")

# Ví dụ sử dụng
tu_dien_album = TuDien()

# Nhập thông tin album 1
album1 = [
    ("Chúng Ta Của Tương Lai", "Sơn Tùng MTP", "Sơn Tùng MTP"),
    ("Có Chắc Yêu Là Đây", "Sơn Tùng MTP", "Sơn Tùng MTP"),
    ("Muộn Rồi Mà Sao Còn", "Sơn Tùng MTP", "Sơn Tùng MTP")
]
tu_dien_album.NhapAlbum("Album 1", album1)

# Nhập thông tin album 2
album2 = [
    ("Yêu Nắm", "BigDaddy x Emily", "BigDaddy x Emily"),
    ("Ngõ Chạm", "BigDaddy x Emily", "BigDaddy x Emily"),
    ("Mượn Rượu Tỏ Tình", "BigDaddy x Emily", "BigDaddy x Emily")
]
tu_dien_album.NhapAlbum("Album 2", album2)

# Xem thông tin album
tu_dien_album.XemAlbum("Album 1")
print()  # Dòng trống để tách biệt output
tu_dien_album.XemAlbum("Album 2")