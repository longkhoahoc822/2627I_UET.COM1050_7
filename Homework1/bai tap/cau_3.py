c=input("nhap mot ky tu: ")
if "a"<=c<="z":
    m=ord(c)-32
    print(chr(m))
elif "A"<=c<="Z":
    m=ord(c)+32
    print(chr(m))
else:
    print("khong phai la mot chu cai")
