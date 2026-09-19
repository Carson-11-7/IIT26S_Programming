print('Program starting.')
print('Estimate how many minutes you spent on programming...')
print()
T=[]
for i in range(1,8): # range is used to generate a sequence of numbers, usually for a loop. Starts at 1 and stops before 8
    T.append(float(input(f"At_T{i}: ")))#append() add one value to the end of the created list. In this case T(the list).append()
print(f'In total you spent {sum(T)} minutes on programming.')
average = sum(T) / len(T)
rounded_average = int(round(average))
print(f'Average per task was {average:.2f} min and same rounded to the nearest interger {rounded_average} min.')
#   average:.2f measn to show exactly 2 digits after the decimal.3
print()
print('Program ending.')