message1 = "Processing file %s"     # przypisanie wartosci
print(message1 % ("file_1.txt"))     # znak %s został zamieniony na wartość file_1.txt

message2 = "File%s has size %d KB"  # przypisujemy %s jako nazwę pliku a %d jako rozmiar pliku
print(message2 % ("file_1.txt",100))    # teraz zamiast %s wpisujemy nazwę a zamiast %d wielkość pliku
                                        # należy pamiętać aby nie zamienić miejscami wpisanych przez nas danych bo wywali bład

message3 = "File %20s has size %10d KB" # liczby 20 i 10 to ile znaków możemy przypisać
print (message3 % ("file1.txt",100))    #mimo, że nie wykorzystaliśmy wszystkich dostępnych znaków to zwrócony wynik zostawił puste miejsce

message4 = "Processing file {0:s}" #ten zapis jest podobny do %s
print(message4.format("file1.txt")) #taki sam wynik jak w przypadku %s

message5 = "File {0:s} has size {1:d} KB" #0:s czyli miejsce zerowe jest zarezerwowane dla napisu a miejsce 1 dla liczby
print(message5.format("file1.txt",100)) #ta metoda pozwala na zamianę inf. dot. plików
message5 = "File {1:s} has size {0:d} KB"
print(message5.format(100,"File1.txt"))

message6 = "File {0:20s} has size {1:10d} KB"
print(message6.format("Fil1.txt",100))

#exec
helloMessage = "Hello %s!"
print(helloMessage % ("Kate"))
print(helloMessage % ("Chris"))

helloMessage = "Hello {0:s}!"
print(helloMessage.format("Kate"))
print(helloMessage.format("Chris"))

helloMessage = "%s has %d %s"
print(helloMessage %("Kate",1,"animal"))
print(helloMessage %("Chris",100000,"$"))

helloMessage = "{0:s} has {1:d} {2:s}"
print(helloMessage.format("Kate",1,"animal"))
print(helloMessage.format("Chris",100000,"$"))

line = "%20s costs %6d €"
print(line % ("Ice Cream",3))
print(line % ("Trip to Venice",119))
print(line % ("Pizza Hawaii",6))



