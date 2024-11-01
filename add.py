def add(a,b):
    return a+b

def multiply(a,b=1):
    return a*b

sum = add(100,1)
mul = multiply(2,3)
mul_default = multiply(100)

print("两个数的和为:", sum)
print("两个数相乘为", mul, "和", mul_default)

'''

再加一行
添加function
'''