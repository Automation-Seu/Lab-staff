#元组是不可以修改的（）
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)
#dimension[0]=100 是不对的 不可幅值
dimensions=(100,50)#可以重新定义来修改
for dimension in dimensions:
    print(dimension)

