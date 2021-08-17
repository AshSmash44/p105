import csv
import math
with open("csv files\data.csv") as f:
    reader = csv.reader(f)
    fd = list(reader)
data = fd[0]
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean
sList = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    sList.append(a)
sum = 0
for i in sList:
    sum = sum+i
result = sum/(len(data)-1)
sd = math.sqrt(result)
print(sd)
