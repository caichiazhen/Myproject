'''
grades = [[5, 14, 7], [23, 36, 28], [88, 80, 92]]
print('數學成績:',grades[2])

print('國文平均:',sum(grades[0])/len(grades[0]), '英文平均:',sum(grades[1])/len(grades[1]), '數學平均:',sum(grades[2])/len(grades[2]))
grades.append([94, 90, 96])
print(grades)
grades[0][2] = 20
print(grades)


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 3, 4, 5, 6)
print(tuple1+tuple2)
print(sorted(tuple1, reverse=True))
print(8 in tuple1)
tuple3 = ()
print(tuple3)
print(tuple1[3])
print(tuple1.index(4))
print(tuple1.count(3))
'''
'''
tuple1 = (88, 12, 20)
x, y, z = tuple1
print(x)
print(y)
print(z)

gradesTuple = ((5, 14, 7), (23, 36, 28), (88, 80, 92))
print("數學成績:", gradesTuple[2])
print('國文平均:',sum(gradesTuple[0])/len(gradesTuple[0]), '英文平均:',sum(gradesTuple[1])/len(gradesTuple[1]), '數學平均:',sum(gradesTuple[2])/len(gradesTuple[2]))
'''
"""
family={
    "dad": "Homer",
    "mom": "Marge",
    "son": "Bart",
    "daughter": "Lisa"
}
print(family["dad"])
print(family.get("dog"))
print("dad" in family)
print("dog" in family)
print(family.keys())
print(family.values())
print(family.items())#可省略items直接print(family)
for item in family.items():
    print(item)
    """
"""
family = {}
print(family)
family["cousin"] = "Max"
print(family)
family["cousin"] = "Eric"
print(family)
family.update({
    'uncle': 'Martin',
    'aunt':'May'
})
print(family)
del family["uncle"]
print(family)
family.pop("cousin")
print(family)
"""
"""
gradesDict = {
    'chinese':[5, 14, 7],
    'english':[23, 36, 28],
    'math':[88, 80, 92]

}
print("數學成績:",gradesDict['math'])
print('國文平均:',sum(gradesDict['chinese'])/len(gradesDict['chinese']), '英文平均:',sum(gradesDict['english'])/len(gradesDict['english']), '數學平均:',sum(gradesDict['math'])/len(gradesDict['math']))
gradesDict.update({
    'science':[94, 90, 96]
})

print(gradesDict)
"""

fruits = {
    "apple",
    "banana",
    "guava",
    "guava"
}
fruits1 = {
    "strawberry",
    "papaya",
    "banana"
}
"""
print(fruits | fruits1)
print(fruits & fruits1)
print(fruits - fruits1)
print(fruits)
fruits.add("watermelon")
print(fruits)
fruits.remove("banana")#如果沒有該字會出錯
fruits.discard("apple")#如果沒有該字不會出錯
print(fruits)
fruits.clear()
print(fruits)

print(sorted(fruits, reverse = True))
"""
"""

allStudents = {
    "John",
    "Eva",
    "Jill",
    "Eric",
    "Andy",
    "Albert",
    "Polina",
    "Kristin",
    "Angela"
}
guitarClub = {
    "John",
    "Eva",
    "Jill",
    "Eric",
    "Andy"
}
danceClub = {
    "Andy",
    "Eric",
    "Albert",
    "Polina",
    "Kristin"
}
print(danceClub & guitarClub)
print(guitarClub - danceClub)
both = guitarClub | danceClub
print(allStudents-both)
"""
"""
x = 70
if x >= 60:
    print("pass")
    x = x + 10
else:
    print("fale")
"""
"""
x = 4 ** 0.5
print(x)

import math
y = math.sqrt(9)
print(y)

pi = 3.14
r = 3
area = r**2*pi
print(area)

grade = [10, 30, 40, 90, 100, 61]
ave = sum(grade)/len(grade)
print(ave)

ave = round(ave)
print(ave)

#要有一個新的區間就多加一個elif
score = 57
if score >= 60:
    print("pass")
elif 55 <= score and score < 60:
    print("教授拜託調個分")
elif 50 <= score < 55:
    print("可惡差一點點")
else:
    print("fail")

score = 87
if score >= 60:
    print("pass")
    if score >= 90:
        print("讚讚讚")
    else:
        print("小垃圾")
elif 55 <= score < 60:
    print("教授拜託調分吧")
else:
    print("fail")

print("Hello world")
print("Hello", "world", "!")
print("Hello\nworld\n!")
print("123", end=" ")
print("456")
#method1
x = 42
print(f"value of x is {x}")#前面一定要有f他會直接找到{}
y = 42
print("value of y is y")

#method2
mathScores = [60, 70, 10, 20, 81, 63, 4]
print(mathScores[0])
firstItem = f"first item in mathScores is {mathScores[3]}"
print(f"the mathScores has {len(mathScores)} items")

for i in range (0, 10):
    print(i)

for a in range (10):
    print(a)

for b in range (0, 10, 2):#開始值,結束值,間隔
    print(b)

mathScores = [60, 70, 10, 20, 81, 63, 4]
for i in range(len(mathScores)):
    print(i, mathScores[i])
for a in mathScores:#依序印出索引值
    print(a)

family={
    "dad": "Homer",
    "mom": "Marge",
    "son": "Bart",
    "daughter": "Lisa"
}
for member in family.items():#tuple的型態
    print(member)
for key, value in family.items():#分離key和value
    print(f"my {key} is {value}")

import math
mathScores = [60, 70, 10, 20, 81, 63, 4]
for times in mathScores:
    times2 = math.sqrt(times)*10
    print(times2)

    print(i)
[print(i) for i in range(10)]#與上方程式碼相同
for i in range(10):

import math
mathScores = [60, 70, 10, 20, 81, 63, 4]
[print(math.sqrt(x)*10) for x in mathScores]

count = 0
while count < 10:
    print(count)
    count += 1
else:
    print("loop end")

for score in mathScores:
    if score > 80:
        continue
    print(score)

import  random
i = random.randint(1,50)
print(i)

x = eval(input("How many rows:"))
print(type(x))

#1
for i in range(1,10):
    for j in range(1,10):
        print(f"{i}*{j}=",i*j)
#2
str = 0
while str < 51:
    print("你好", end=", ")
    str += 1
else:
    print("我說完了拉")
#3
keyin = input("輸入一個數值: ")
keyin2 = int(keyin)
for a in range(1,keyin2,2):
    print(a)
#3
 num = eval(input("Enter a number: "))
for i in range(1, num+1):
    if i % 2 == 1:
        print(i)

#4
import random
ls = []
rows = eval(input("How many rows: "))
columns = eval(input("How many columns: "))
for i in range(rows):
    ls.append([])
    for j in range(columns):
        num = random.randint(1, 100)
        ls[i].append(num)
for x in range(rows):
    for y in range(columns):
        print(f"{ls[x][y]}",end=' ')
    print()
#5
total = 0

"""
weight1 = 100
weight2 = 80

def add_weight(w1, w2=2):
    result = w1 + w2
    result1 = w1 / w2

    return result, result1
x1, x2 =add_weight(weight1,weight2)
print(x1, x2)

y1,y2 = add_weight(w2=weight1,w1=weight2)
print(y1, y2)

x = add_weight(weight1,weight2)
y = add_weight(weight1)
#出錯因為函式規定要兩個變數除非將def add_weight(w1, w2=1)設定預設值
print(x,y)

a = 15

