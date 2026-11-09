while True:
    a=  int(input("nhap so nguyen vao: "))
    if a==0:
        print("gia tri khong phải la chan va le")
        break
    if a%2==0:
        print("so nay la so chan: ",a)
    else:
        print("so nay la so le: ",a)