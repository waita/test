weight=float(input("请输入您的体重（KG）:"))
hight=float(input("请输入您的升高（M）:"))
BMI=weight/(hight*hight)
print("您的体质为（BMI）为：",BMI)
if BMI<18.5:
    print("消瘦")
elif 18.5<=BMI<25:
    print("正常")
elif 25<=BMI<30:
    print("偏胖")
else:
    print("肥胖")