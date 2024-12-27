###Thêm thông tin sinh viên mới và sắp xếp vào môn học
def them_sinh_vien(ds_sinh_vien, ds_lop_hoc):
    print("Thêm thông tin sinh viên mới:")
    ma_sinh_vien = input("Nhập mã sinh viên: ")
    ten_sinh_vien = input("Nhập tên sinh viên: ")
    lop_hoc = input("Nhập tên lớp học: ")

    # Tìm lớp học và kiểm tra số lượng sinh viên
    lop_tim_duoc = None
    for lop in ds_lop_hoc:
        if lop['ten_lop'] == lop_hoc:
            lop_tim_duoc = lop
            break

    if lop_tim_duoc is None:
        print("Không tìm thấy lớp học này!")
        return

    if len(lop_tim_duoc['danh_sach_sinh_vien']) >= 60:
        print("Lớp học đã đầy, không thể thêm sinh viên mới!")
        return

    # Thêm sinh viên vào danh sách lớp
    sinh_vien_moi = {
        'ma_sinh_vien': ma_sinh_vien,
        'ten_sinh_vien': ten_sinh_vien
    }
    lop_tim_duoc['danh_sach_sinh_vien'].append(sinh_vien_moi)
    ds_sinh_vien.append(sinh_vien_moi)

    print(f"Thêm sinh viên {ten_sinh_vien} vào lớp {lop_hoc} thành công!")
