def countDown(num):
    newList = []
for i in range(num, -1, -1):
    newList.append(i)
return newList
print(countDown(5))

def print_and_return(list):
    print(list[0])
return list[1]
print(print_and_return([5, 30]))

def first_plus_length(list):
    x = list[0] + len(list)
return x
print(first_plus_length([23, 46, 2]))

def length_and_value(size, value):
    newList = []
for i in range(size):
    newList.append(value)
return newList
print(length_and_value(3, 5))