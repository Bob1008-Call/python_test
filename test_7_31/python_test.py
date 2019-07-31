#!/ust/bin/python
# coding=utf-8

import time
import math
import string
import calendar
'''
a = 10
b = 20

if a or b:
  print a or b
else:

'''

'''
a = 10
b = 20
list = [1,2,3,4,5];

if(a in list):
  print "1 -- 变量a在给定的列表中"
else:
  print "1 -- 变量a不在给定的列表中"
'''

'''
num = 1
if num >= 0 and num <=2:
  print 'hello'

num = 10
if num < 0 or num > 10:
  print 'hello'
else:
  print 'no'v
'''

'''
a = 1
while a < 10:
  print(a)
  a += 2

numbers = [1,2,3,4,5,6]
even = []
od = []
while len(numbers) > 0:
  number = numbers.pop()
  if number % 2 == 0:
    even.append(number)
  else:
    od.append(number)
'''

'''
var = 1
while var == 1:
  num = raw_input("enter a number :")
  print "You entered：", num
'''

'''
i = 1
while i < 10:
  i += 1
  if i%2 > 0:
    continue
  print i
'''
'''
count = 0
while count < 5:
  print count,'is less than 5'
  count += 1
else:
  print count,'is more than 5'
'''

'''
flag = 1
while (flag): time.sleep(1); print '..............'
'''

'''
for letter in 'python':
  print '当前字母',letter
'''
'''
list = ['banana','apple','mango']
for index in range(len(list)):
  print '当前水果：',list[index]
'''
'''
list = ['banana','apple','mango']
for index in list:
  print '当前水果',index
'''

'''
for num in range(10,20):
  for i in range(2,int(math.sqrt(num))+1):
    if num%i == 0:
      j = num / i
      print '%d * %d = %d'%(i,j,num)
      break
  else:
    print num,'是一个质数'

'''
'''
i = 2
while i < 100:
  j = 2
  while j <= (i/j):
    if not(i%j): break
    j = j+1
  if j > i/j: print i, '是素数'
  i += 1
'''
'''
string = 'a,B'
string.capitalize()
print 'string:',string
'''
'''
str = 'runoob'
str.center(20,'*')
print 'str:',str
'''

'''
print ['Hi!'] * 4
'''
''''
alist = [1,2,3,'caozongkai']
blist = [4,5,6,'jiajiajia']
''''
'''
alist.extend(blist)
print alist
'''

'''
str = 'caozongkai'
print alist.index(str)
'''

'''
alist.insert(1,str)
print alist
'''

'''
alist.reverse()
print alist
'''
'''
dup1 = (1,2,3,4)
dup2 = (5,6,7,8)
new_dup = dup1 + dup2
print new_dup
'''

dict = {'Name': 'ZARA','Age':7,'Class':'First'}

'''
dict['Age'] = 8
dict['School'] = 'SUST'

print 'Name:',dict['Name']
print "Age:",dict["Age"]
'''

'''
print 'dict:',dict

dict.clear()

print 'dict:',dict

del dict

print 'dict:',dict
'''
'''
dict = {1:"name",2:"age"}

print 'dict:',dict

print 'dict[1]:',dict[1]
'''
'''
dict = {('Name'):'Zara','Age':7}

print 'dict[(Name)]:',dict[('Name')]
'''
'''
print 'dict[['Name']]',dict[['Name']]

print dict.items()
'''
'''
tick = time.time()

print "当前时间戳为: ",tick
'''
'''
ticks = time.time()

localtime = time.localtime(ticks)

print "本地时间为:",localtime
'''
'''
localtime = time.asctime(time.localtime(time.time()))

print '本地时间:',localtime
'''
'''
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
'''
cal = calendar.month(2019,7)

print "2015年1月的日历:"

print cal

