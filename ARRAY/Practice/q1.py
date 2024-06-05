# Find Number of days above temperature
# Using List:-
# days = int(input("Enter the number of days:"))
# temp = []
# for i in range(days):
#     temp.append(int(input("Enter day-{} temperature:".format(i+1))))

# average = sum(temp)/days
# print(temp)
# print("Average temperature:",average)

# above_temp = []
# count = 0
# for i in range(days):
#     if temp[i] > average:
#         above_temp.append(i)
#         count += 1
# print("Number of days above average temperature:",count)
# for i in above_temp:
#     print("day-{} is above average temperature".format(i+1))
    
# Using Array:-
import numpy as np
days = int(input("Enter number of days:"))
a = np.array(range(days))
sum = 0

for i in range(days):
    a[i] = int(input("Enter day-{} temperature:".format(i+1)))
    sum = sum + a[i]

average = sum / days
print("array:", a)
print("Average temperature:", average)
arr = np.zeros(days)
count = 0
for i in range(days):
    if a[i] > average: 
        arr[i] += 1
        count += 1
    
print("Number of days above average temperature:",count)
for i in range(days):
    if arr[i] == 1:
        print("day-{} is above average temperature".format(i+1))



