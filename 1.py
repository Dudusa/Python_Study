#encoding = utf-8
#python3  6种标准数据类型

#数值
'''
a,b =123, 567
print(a*b)
print(a+b)
'''


#字符串
'''
c = 'hello world'
print(c)
#截取字符串，关系是大于等于，小于
print(c[:3])     #输出是hel
print(c[1:3])    #输出是el
print(c[3:-1])   #输出是lo worl
print(c*3)       #输出3遍c
print(c+"Dusa")  #字符串后面加上“Duda”
d = c.split(" ") #用空格切割字符串,产生的是字符数组
print(d)        
print(c[1])      #输出是e
print(d[1])      #输出是world
print(c[c.index('h'):c.index('r')])  #输出是hello wo
'''


#列表
'''
list = ['数学', '语文', '英语', 120]
list2 = ['化学', '物理']
print(list)
print(list[2:])
print(list+list2)
list[3] = 150
print(list)
del list[3]
print(list)
list.append(110)
list.append(110)
print(list)
print(list.count(110)) #数110出现的次数
print(list.index('语文'))
list.insert(2,'nb')    #在2之前插入nb
print(list)
list.reverse()         #列表反转
print(list)
'''

#元组
'''
tup = (1,2,3,4)
print(tup[1])
print(tup[1:3])
print(tup[1:5])
print(tup[1:2])        #元组切割出一个字符会出现‘,’，但是直接输出就没有了
#tup[0] = 5            #会出错，元组不支持修改
print(max(tup))        #元组的最大值，最小值同理用min
'''

#字典
'''
stus = {'no':'111','name':'Dusa'}
print(stus)
print(stus['no'] )
stus['no'] = '000'
print(stus)
del stus['no']
print(stus)
print('no' in stus)   #判断no是否在stus里面
stus2 = {'no':'111','name':'Dusa','hobby':['抽烟','喝酒','烫头']}
print(stus2['hobby'])
stus2['school'] = 'OUC'
print(stus2)
'''

#set集合     无序，不重复，优点：查阅速度快
''''
list = [1,2,3,4,5,6,6]
set1 = set(list)
print(set1)
#print(set[0])  #出错，因为set是无序的
set2 = set(['a','b'])
print(set1.union(set2))    #将set和set2链接在一起
print(len(set2))
'''

#顺序结构
'''
a=1
b=2
print(a+b)
'''

#判断结构  0-60不及格   60-80良好    >=80优秀
'''
count = int(input("请输入您的分数："))
if count >=  60 and count <80:
    print('良好')
elif count >= 80:
    print('优秀')
else:
    print('不及格')
'''

#循环结构  1+2+3+...+100
#while循环
'''
index = 1
sum = 0
while index <= 100:
    print(index)
    sum = sum + index
    index = index + 1
print(sum)
'''

#for循环
'''
sum  = 0
for index in range(101):
    print(index)
    sum = sum + index
print(sum)
'''
#练习  累加列表和
list = [0,1,2,3,4,5,6,6,7]
sum = 0
'''
for index in range(len(list)):
    sum = sum + list[index]
'''
'''
for num in list:      
    sum = sum + num
'''
'''
for num in list:
    if num != 6:
        sum = sum + num
print(sum)
'''
'''
for index in range(len(list)):
    if index >3:
        break;
    print(index)
    sum = sum + list[index]
print(sum)
'''
#continue跳出本次循环
for index in range(len(list)):
    if index == 4:
        continue;   #“;”可要可不要
    print(index)
    sum = sum + list[index]
print(sum)