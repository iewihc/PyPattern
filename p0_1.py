# 型態篇
# int,string,float型
age = 18 
weight = 62.51
name = "Tony"

# 佔位符輸出
print("My name is %s. " % (name))
print("My age is %s. " % (age))
print("My weight is %s. " % (weight))

# 型態直接被改變了(int-->string)
age=name
print('Type Changed int->string',type(age))

# 指向三塊相同內存空間
a=b=c=5
print('Before',id(a),id(b),id(c))

# a內存位置被改變
a=6
print('A is different',id(a),id(b),id(c))
