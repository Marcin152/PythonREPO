fruits = ["apple", "orange", "banana", "strawberry", "grapefruit", "pear", "peach", "raspberry", "plum"]

website = "fruityworld.com"

for fruit in fruits:
    email = fruit + "@" + website
    print("e-mail for you fruit",fruit, "is: ",email)
else:
    print("that's all")

#LAB
print("---------------------")
data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
#1
# for error in data:
#     print(error.upper())

#2
for error in data:
    elements = error.split(":")
    # elements = new_message
    # print(elements[0].upper())
    # print(elements[1])
    if elements[0] == "Error":
        print(elements[1].upper())
    else:
        print(elements[1])

