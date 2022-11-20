import random
cargo = [40, 20, 4, 5, 6, 1, 22, 44, 11, 66, 9, 11, 1, 1]
cargo.sort()
cargo.reverse()
boxCapacity = 90

box = []
i = 0

while i<len(cargo) and boxCapacity - sum(box) >= min(cargo):
    if (boxCapacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1

print("The elements sorted are: ",cargo)
print("The collected items sum is: ", sum(box))
print("The elements are: ",box)



#LAB

number = 1
previousNumber = 0
x = 50

while number+previousNumber <= 50:
   print(number + previousNumber)
   previousNumber = number
   number+=1
print("--------------")

guess = -1
trials = 0
my_number = random.randint(0,20)
print(my_number)
print("Guess my number: ")

while guess != my_number:
    guess = int(input())
    trials += 1
    if guess >= my_number:
        print("guess is higher")
    elif guess <= my_number:
        print("your guess is lower")

if guess == my_number:
    print("you guessed right")
    print("you guessed after:", trials)
