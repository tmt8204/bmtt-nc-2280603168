from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while(1 == 1):
    print("\nQUAN LI SINH VIEN")
    print("------------------  MENU  ------------------")
    print("\t1. Them sinh vien")
    print("\t2. Cap nhat thong tin sinh vien")
    print("\t3. Xoa sinh vien")
    print("\t4. Tim kiem theo ten")
    print("\t5. Sap xep theo diem TB")
    print("\t6. Sap xep theo ten chuyen nganh")
    print("\t7. Hien thi danh sach")
    print("\t8. Thoat")
    print("--------------------------------------------")

    key = int(input("Nhap lua chon: "))
    if (key == 1):
        print("Them sinh vien")
        qlsv.nhapSinhVien()
        print("Them sinh vien thanh cong")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("Cap nhat sinh vien")
            print("Nhap ID sinh vien can cap nhat: ")
            ID = int(input("ID: "))
            qlsv.updateSinhVien(ID)
        else:
            print("Khong co sinh vien nao de cap nhat")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("Xoa sinh vien")
            print("Nhap ID sinh vien can xoa: ")
            ID = int(input("ID: "))
            if (qlsv.deleteByID(ID)):
                print("Sinh vien co ID = {} da bi xoa".format(ID))
            else:
                print("Khong tim thay sinh vien co ID = {}".format(ID))
        else:
            print("Khong co sinh vien nao de xoa")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("Tim kiem sinh vien")
            print("Nhap ten sinh vien can tim: ")
            name = input("Ten: ")
            searchResult = qlsv.findByName(name)
            qlsv.getListSinhVien(searchResult)
        else:
            print("Khong co sinh vien nao de tim kiem")
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("Sap xep sinh vien theo diem TB")
            qlsv.sortByDiemTB()
            qlsv.getListSinhVien(qlsv.listSinhvien)
        else:
            print("Khong co sinh vien nao de sap xep")
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("Sap xep sinh vien theo ten")
            qlsv.sortByName()
            qlsv.getListSinhVien(qlsv.listSinhvien)
        else:
            print("Khong co sinh vien nao de sap xep")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("Hien thi danh sach sinh vien")
            qlsv.getListSinhVien(qlsv.listSinhVien)
        else:
            print("Khong co sinh vien nao de hien thi")
    elif (key == 0):
        print("Ban da thoat chuong trinh")
        break
    else:
        print("Lua chon khong hop le")
    print("========================================")
    print("Ban co muon tiep tuc khong? (Y/N)")
    cont = input("Nhap Y de tiep tuc, N de thoat: ")
    if (cont.upper() == "N"):
        print("Ban da thoat chuong trinh")
        break
    elif (cont.upper() != "Y"):
        print("Lua chon khong hop le")
