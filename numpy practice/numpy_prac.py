import numpy as np
import pandas as pd

data=np.array([
    [10,20,30,40],
    [50,60,70,80],
    [5,10,15,20]
])
print(np.sum(data,axis=1))

data=np.array([5,6,7,8,9,10])
print(data[data>7])
print(data[(data>5)&(data<10)])
print(data[(data>6) & (data<9)])

data=np.array([11,12,13,14,15])
pata=np.array([20,30,40,50,60])
print(data+pata-5)
print(data-pata)
print(data*pata)

number=np.array([
    [10,20,30,40,50],
    [40,50,60,70,80]

])
print(number.shape)
print(number.ndim)
print(number.size)
print(number[0])
print(number[0,2])
print(number[0:2,2:5])
number[1,2]=100
print(number)
print(np.sum(number))
print(np.mean(number))
print(np.max(number))
print(np.min(number))
print(np.std(number))

print(np.zeros(5))
print(np.ones(3))
print(np.eye(5))
print(np.arange(10))
df=pd.DataFrame(number)
print(df)
print(number[1,:])
print(number[:,2])
print(np.sum(number,axis=1))
print(np.sum(number,axis=0))
print(number.reshape(5,2))
print(number[number>40])
print(number[(number>20) & (number<60)])

import numpy as np
marks = np.array([
    [78, 85, 92],
    [65, 72, 70],
    [90, 88, 95],
    [55, 60, 58],
    [82, 79, 85],
    [45, 52, 48]
])
print(marks.shape)
print(marks.ndim)
print(marks.size)
print(marks[2,0])
print(marks[4,0:3])
print(marks[0:6,2])
print(np.max(marks))
print(np.min(marks))
print(np.mean(marks[:,0]))
print(np.sum(marks,axis=1))
print(np.mean(marks,axis=0))
print(marks[marks>80])
print(marks[marks<60])
print(marks[(marks>=70) & (marks<=90)])

import numpy as np
sales = np.array([
    [12000, 15000, 18000],
    [22000, 19000, 25000],
    [14000, 17000, 16000],
    [30000, 28000, 32000]
])
print(sales.shape)
print(sales[1])
print(sales[:,2])
print(np.sum(sales,axis=1))
print(np.mean(sales,axis=0))
print(np.max(sales))
print(sales[sales>20000])
print(np.sum(sales))

data=np.array([10,20,30,40,50,60])
print(data.reshape(2,3))
print(data.reshape(3,2))
prices = np.array([100, 200, 300, 400])
result=prices+50
print(result)
prices = np.array([100, 200, 300])
result=prices+(prices*0.10)
print(result)
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 88]
])
result=marks+5
print(result)


        




















