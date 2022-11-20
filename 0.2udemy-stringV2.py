drive = 'c:\\' #aby pokazał się jeden backslash musimy wpisać go podwójnie
print(drive)
folder = 'scripts\\python\\' #podwójny backslashy pokażą się nam w debugerze pojedynczo
print(folder)
file = 'myscript.py'
path = drive + folder + file
print(path) #całą ścieżkę do pliku możemy wyświetlić dzięki konkatenacji

justText = "text with \nnewline " # w nowejlinii
print(justText)
justText = r"text with \nnewline " # surowy tekst
print(justText)

justText = "Mc Donald's" #pokazuje cały wyraz
print(justText)
#justText = 'Mc Donald's' #nie pokazuje, wywala błąd
print(justText)
justText = 'Mc Donald\'s' # brak błędu
print(justText)
linia = 'On powiedział "Ja lubie placki!"'
print(linia)

#exec
firstName = "Kasia "
familyName = "Sowa "
lastName = "Mrugała "
newName = firstName + familyName + lastName
print(newName)
newName = firstName+ ""+familyName+""+lastName
print(newName)

music = ' "Universal Fanfare" Jerry Goldsmith\n "Happy togeter" Garry Bonner\n "I\'m a Man" Steve Winwood'
print(music)

print("(\(\\")
print("( -.-)")
print('0_(")(")')