import math
a=float(input('输入三角形的一边长:'))
b=float(input('输入三角形的一边长:'))
c=float(input('输入三角形的一边长:'))
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print('三角形的面积是:',s)