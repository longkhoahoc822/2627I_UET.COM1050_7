a,b,c=map(float, input("nhap chieu dai 3 canh: ").split())
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    print(f"dien tich tam giac la: {s:.1f}")
else:
    print("Khong phai 3 canh cua tam giac")