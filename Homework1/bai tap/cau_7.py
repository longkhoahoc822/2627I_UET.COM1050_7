a=input("nhap chuoi ki tu: ")
if len(a)<20 or not a.isalpha() or not a.islower():
    print("chuoi ki tu khong hop le: ")
else:
    print(f"chu cai thu nam la {a[4]}\nchu cai thu chin la {a[8]}")