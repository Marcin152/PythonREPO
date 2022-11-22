# osoby = ['Amia', "Maciek@sales.com", "Sebastian", "Margaret", "Svetlana@mycompany.eu", "Raphael"]
#
# domena = 'mycompany.com'
#
# emails = []
#
# for osoba in osoby:
#
#     if '@' in osoba:
#         emails.append(osoba)
#         continue
#
#     email = osoba+'@'+domena
#     emails.append(email)
#
# for email in emails:
#     print(email)
#
# for osoba in osoby:
#     if '@' in osoba:
#         emails.append(osoba)
#     else:
#         email = osoba + '@' +domena
#         emails.append(email)
# print("------------------------------------------------")
# #LAB
#
# #1
# menu = '''
# Choose what you want me to do for you:
# 1 - COFFEE
# 2 - TEA
# 3 - MAKE ME SMILE
# ---------------
# To stop this script select 0
# '''
# print(menu)
# smile = '''
#
#                           oooo$$$$$$$$$$$$oooo
#                       oo$$$$$$$$$$$$$$$$$$$$$$$$o
#                    oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
#    o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
# oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
# "$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
#   $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
#   $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
#    "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
#     $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
#    o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
#    $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
#   o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
#   $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
#  """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
#             "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
#               $$$o          "$$""$$$$$$""""           o$$$
#                $$$$o                                o$$$"
#                 "$$$$o      o$$$$$$o"$$$$o        o$$$$
#                   "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
#                      ""$$$$$oooo  "$$$o$$$$$$$$$"""
#                         ""$$$$$$$oo $$$$$$$$$$
#                                 """"$$$$$$$$$$$
#                                     $$$$$$$$$$$$
#                                      $$$$$$$$$$"
#                                       "$$$""""
# '''
#
# while True:
#
#     print(menu)
#     letter = input()
#
#     if letter == '1':
#         print("Function COFFE not implemented")
#         input("Please enter:")
#         continue
#     if letter == '2':
#         print("Function TEA not implemented ")
#         input("Please enter:")
#         continue
#     if letter == '3':
#         print(smile)
#         input("Please enter:")
#         continue
#     if letter == '0':
#         break
#     else:
#         print("You need to make a choice, press enter and try again!")
#
# print("--------------------------------------------------")
# #DODATEK
# #1
#
# initialCapital = 20000
# percent = 0.03
# maxTimeYears = 10
#
# for odsetki in range(1,maxTimeYears+1):
#     odds = initialCapital * percent
#     initialCapital = initialCapital+odds
#     print('Twoj kapital w kolejnych latach:',odsetki,(round(initialCapital)))
#     if odsetki >=10:
#         x = initialCapital - 20000
#         print("Twoja zarobiona kwota po 10 latach wynosi: ",round(x))
#
# #3
# text = '''United Space Alliance: This company provides major support to NASA for
# various projects, such as the space shuttle. One of its projects is to
# create Workflow Automation System (WAS), an application designed to
# manage NASA and other third-party projects. The setup uses a central
# Oracle database as a repository for information. Python was chosen over
# languages such as Java and C++ because it provides dynamic typing and
# pseudo-code–like syntax and it has an interpreter. The result is that
# the application is developed faster, and unit testing each piece is easier.'''
#
# print("-------------------------------------------------")
# wordList = text.replace('\n',' ').split(' ')
# print()
# shortWords = 0
# longWords = 0
# wordLength = 6
#
# for word in wordList:
#     if len(word) > wordLength:
#         longWords+=1
#         #print(longWords)
#
#     if len(word) <= wordLength:
#         shortWords+=1
#        #print(shortWords)
#
# print("Words longer than 6:",longWords,"\nWords shorter than 6:",shortWords)
#
#
# #2
# number = 20730906
# zmienna = number
# sumaCyfr = 0
#
# while zmienna > 0:
#     cyfra = zmienna % 10
#     sumaCyfr += cyfra
#     zmienna = zmienna//10
# else:
#     print(number, sumaCyfr)
#4

# fibonacciIterations=20
# a1 = 0
# a2 = 1
# a3 = 0
#
# for x in range(fibonacciIterations):
#     a1 = a2
#     a2 = a3
#     a3 = a1+a2
#     print(a3)

#5

text = '''Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.'''

for words in text:
   print(words,words.lower())


