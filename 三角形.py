a=float(input("请输入第一条边的长度:"))
b=float(input("请输入第二条边的长度:"))
c=float(input("请输入第三条边的长度:"))
if a+b>c and a+c>b and b+c>a:
    print("可以组成三角形")
else:
    print("不可以组成三角形")