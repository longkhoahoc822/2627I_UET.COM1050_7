a = int(input("nhap so nam vao: "))
if a%400==0 or a%4==0 and not a%100==0:
    print(" day la nam nhuan ")
else:
    print(" day khong phai la nam nhuan")