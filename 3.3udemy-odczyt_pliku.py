import os.path

# file = open("c:\\temp\\joke.txt","r")
#
# content = file.read()
# print(content)
# file.close()
# print("--------------------------")
# with open("c:\\temp\\joke.txt","r") as file:
#     content = file.read()
#     print(content)
# print("--------------------------")
# with open("c:\\temp\\joke.txt","r") as file:
#     for line in file:
#        print(line)
# print("--------------------------")
# file = open("c:\\temp\\joke.txt", "r")
# for line in file:
#     print(line)
# file.close()
# print("--------------------------")
# file = open("c:\\temp\\joke.txt", "r")
# for line in file.readlines():
#     print(line)
# file.close()
# print("--------------------------")
# file = open("c:\\temp\\joke.txt", "r")
# fragment = file.read(15)
# while fragment:
#     print(file.tell(),fragment)
#     fragment = file.read(15)
# file.close()


#Lab
# x = 10
# y = 'kot'
# z = '2012'
# t = True
#
# while t != False:
#     print(x)
#     break

file_path = "c:\\temp\\orders.csv"
print(os.path.isfile(file_path))

file2 = open("c:\\temp\\orders.csv", "r")
for line in file2:
    print(line)
file2.close()
