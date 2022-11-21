values = [10,12,45,12,42,78,45,23,67,43,76,98,23,65,98,34]
i = 0
max = len(values)-2

while i<max:
    print(i,values[i],values[i+1],values[i+2])

    if (values[i]<values[i+1] and values[i+1]<values[i+2]):
        print('\tFound: ',values[i]<values[i+1] and values[i+1]<values[i+2])

    i+=1
print("----------------------------------------------")
#exec

numbers = [8,18,2,4,16,5,25,4,22,3,3,5,3,9,81]

c = 0
maxi = len(numbers)-2

while c < maxi:
    print(c, numbers[c],numbers[c+1],numbers[c+2])

    if numbers[c]**2 == numbers[c+1] and  numbers[c+1]**2 == numbers[c+2]:
        print('\tFound: ',c,numbers[c],numbers[c+1],numbers[c+2])

    c+= 1
print("----------------------------------------------")

texts = ['zero','one','two','three','four','five','six','seven','eight','nine']

t = 0
maxed = len(texts)-1

while t < maxed:
    print(t,texts[t],texts[t+1])


if len(texts[t]) == len(texts[t+1]):
    print('\f Found: ')
    t+=1










