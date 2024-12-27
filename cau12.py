###Tìm kiếm môn học, năm học cho sinh viên:
def tim_kiem_sinh_vien(ds_diem):
    print("Tìm kiếm sinh viên theo môn học và năm học:")
    ma_mon_tim = input("Nhập mã môn học cần tìm: ")
    nam_hoc_tim = input("Nhập năm học cần tìm: ")

    # Lọc danh sách sinh viên
    ds_diem_loc = []
    for diem in ds_diem:
        if diem['ma_hoc_ky'] == ma_mon_tim and diem['nam_hoc'] == nam_hoc_tim:
            ds_diem_loc.append(diem)

    if len(ds_diem_loc) == 0:
        print("Không tìm thấy sinh viên nào thỏa mãn điều kiện!")
        return []

    print("Danh sách sinh viên thỏa mãn:")
    print("Mã sinh viên", "\t", "Tên sinh viên", "\t", "Điểm TB", "\t", "Mã môn học", "\t", "Năm học")
    for diem in ds_diem_loc:
        print(diem["ma_sinh_vien"], "\t", diem["ten_sinh_vien"], "\t", diem["diem_tb"], "\t", diem["ma_hoc_ky"], "\t", diem["nam_hoc"])
    
    return ds_diem_loc





###Chỉnh sửa điểm cho sinh viên
def chinh_sua_diem(ds_diem_loc):
    if len(ds_diem_loc) == 0:
        print("Danh sách sinh viên rỗng, không thể chỉnh sửa!")
        return

    print("Chỉnh sửa điểm sinh viên:")
    ma_sinh_vien_tim = input("Nhập mã sinh viên cần chỉnh sửa: ")

    # Tìm sinh viên cần chỉnh sửa
    sv_can_chinh_sua = None
    for diem in ds_diem_loc:
        if diem['ma_sinh_vien'] == ma_sinh_vien_tim:
            sv_can_chinh_sua = diem
            break

    if sv_can_chinh_sua is None:
        print("Không tìm thấy sinh viên cần chỉnh sửa!")
        return

    # Hiển thị thông tin trước khi chỉnh sửa
    print("Thông tin sinh viên trước khi chỉnh sửa:")
    print("Mã sinh viên:", sv_can_chinh_sua['ma_sinh_vien'])
    print("Điểm hs1.1:", sv_can_chinh_sua['diem_hs11'])
    print("Điểm hs1.2:", sv_can_chinh_sua['diem_hs12'])
    print("Điểm hs2.1:", sv_can_chinh_sua['diem_hs21'])
    print("Điểm hs2.2:", sv_can_chinh_sua['diem_hs22'])
    print("Điểm hs2.3:", sv_can_chinh_sua['diem_hs23'])
    print("Điểm TB:", sv_can_chinh_sua['diem_tb'])

    # Nhập các điểm mới
    print("Nhập thông tin điểm mới:")
    diem_hs11 = input("Nhập điểm hs1.1: ")
    diem_hs12 = input("Nhập điểm hs1.2: ")
    diem_hs21 = input("Nhập điểm hs2.1: ")
    diem_hs22 = input("Nhập điểm hs2.2: ")
    diem_hs23 = input("Nhập điểm hs2.3: ")

    # Cập nhật điểm
    sv_can_chinh_sua['diem_hs11'] = diem_hs11
    sv_can_chinh_sua['diem_hs12'] = diem_hs12
    sv_can_chinh_sua['diem_hs21'] = diem_hs21
    sv_can_chinh_sua['diem_hs22'] = diem_hs22
    sv_can_chinh_sua['diem_hs23'] = diem_hs23

    # Tính lại điểm trung bình
    sv_can_chinh_sua['diem_tb'] = round(
        (float(diem_hs11) + float(diem_hs12) +
         2 * (float(diem_hs21) + float(diem_hs22) + float(diem_hs23))) / 7,
        2
    )

    print("Chỉnh sửa thành công! Thông tin sau khi chỉnh sửa:")
    print("Mã sinh viên:", sv_can_chinh_sua['ma_sinh_vien'])
    print("Điểm hs1.1:", sv_can_chinh_sua['diem_hs11'])
    print("Điểm hs1.2:", sv_can_chinh_sua['diem_hs12'])
    print("Điểm hs2.1:", sv_can_chinh_sua['diem_hs21'])
    print("Điểm hs2.2:", sv_can_chinh_sua['diem_hs22'])
    print("Điểm hs2.3:", sv_can_chinh_sua['diem_hs23'])
    print("Điểm TB:", sv_can_chinh_sua['diem_tb'])
