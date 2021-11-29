
for x in range(0,151):
    print(x)

for x in range(0,1001,5):
    print(x)

def counting_dojo():
    for i in range (1,101,1):
        if i % 5 == 0 and i % 10 != 0:
            print('Coding')
        else:
            print(i)
        if i % 10 == 0:
            print('Coding Dojo')
counting_dojo()

i=1
sum=0
while i<=500000:
    if i%2!=0:
        sum=sum+i
    i=i+1
print (sum)

def count_down_four():
    number = 2018
    while number > 0:
        print (number)
        number = number - 4
count_down_four()


def flexible_counter(lowNum,highNum,mult):
    for j in range (lowNum,highNum):
        if j % mult == 0:
            print(j)
flexible_counter(0,169,3)









