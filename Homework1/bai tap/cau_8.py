def tien_dien(c):
    if 0 <= c <= 50:
        b = c * 1984
    elif 51 <= c <= 100:
        b = 50 * 1984 + (c - 50) * 2050
    elif 101 <= c <= 200:
        b = 50 * 1984 + 50 * 2050 + (c - 100) * 2380
    elif 201 <= c <= 300:
        b = 50 * 1984 + 50 * 2050 + 100 * 2380 + (c - 200) * 2998
    elif 301 <= c <= 400:
        b = 50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + (c - 300) * 3350
    elif c >= 401:
        b = 50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + 100*3350 + (c-400)*3460
    tong_tien = round(b * (1 + 0.08))
    return tong_tien


ten = input("ten chu ho: ")
m = float(input("chi so thang truoc: "))
n = float(input("chi so thang nay: "))
p = tien_dien(n - m)
print("Ho va ten: ", ten)
print("tong so tien phai tra: ", p)