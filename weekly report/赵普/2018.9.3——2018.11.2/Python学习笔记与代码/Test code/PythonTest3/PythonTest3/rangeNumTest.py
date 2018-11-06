for value in range(1,5):
    print(value)
number=list(range(1,6,1))
print(number)
squares=[]
for value in range(1,11,1):
    squares.append(value**2) #用for循环和range配合生成数值数组的方法
print(squares)
print(min(squares))#数值操作相关
print(max(squares))
print(sum(squares))

squares=[value**3 for value in range(1,11,1)]#“列表分析”，专有名词，用该方法也可生成列表
print(squares)

print(squares[:2])#切片
print(squares[4:7])
print(squares[4:-1])#还是坐标的前一个为止
print(squares[-1:2])#切片并不会帮你循环输出，只可以输出从前往后的任意n个且不可反向 坐标反向不代表顺序反向

new_squares= squares[0:11]#只有使用切片才可复制  不使用切片表示意思是变量名等价 操作的是同一个数组 new_squares=suqares
new_squares= squares[:]
print(new_squares)