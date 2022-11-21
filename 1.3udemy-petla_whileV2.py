i = 10
imax = 0

while i >= imax: #warunek jest taki że pętla ma trwać do momentu kiedy i jest mniejsze badz rowne imax
    print("ile to jest razy")
    i-=2 #ustawienie o ile ma się zwiększać i w pętli
else:
    print("Now i =",i)

#exec
print("----------------------------------------------")
firstRow = 1
lastRow = 31
currentRow = firstRow

while currentRow<=lastRow:
    print("Row number is: ",currentRow)
    currentRow+=1
print("----------------------------------------------")
x=1
c=1
while x<=13:
    print(f"kwadrat liczby: {x} to", c*c)
    print(f"sześcian liczby: {x} to", c*c*c)

    c+=1
    x+=1
print("----------------------------------------------")
razy=1
zmienna=1
potega=zmienna

while razy<=16:
    print(f"liczba: {razy} do potęgi 2 to",zmienna*potega)

    razy+=1
    zmienna+=1
    potega+=1
print("----------------------------------------------")
znak = "x"
haft=1
while haft<=10:
    print(haft*"x")
    haft+=1
print("----------------------------------------------")
start = 0
end   = 16

while start<=end:
    print(f"potęga {start} liczby 2 to", 2**start)
    start+=1


