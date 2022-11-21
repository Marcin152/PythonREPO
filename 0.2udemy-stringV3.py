numer = "1000"
print(numer)
#print(numer+1)# nie działa bo zmienna przyjmuje wartość jak string a nie int
print (int(numer)+1)
x = numer +str(1)
print(x)
print(type(numer)) #ukazuje zmiennąi jej typ czyli string
print(type(int(numer)+1)) #zamienia zmienną na ing

#exec
article = "Monty Python (also collectively known as the Pythons) were a British surreal comedy troupe who created " \
          "the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. " \
          "Forty-five episodes were made over four series. The Python phenomenon developed from the television " \
          "series into something larger in scope and influence, including touring stage shows, films, albums, " \
          "books and musicals. The Pythons' influence on comedy has been compared to the Beatles' influence on music." \
          " Regarded as an enduring icon of 1970s pop culture, their sketch show has been referred to as being "\
            "an important moment in the evolution of television comedy"

print(article.upper())

print(article.lower().replace("monty","flying"))
print(article.split(" "))
print("Words Python appears: " + str(article.count("Python")))
print("to print the \\ you need to put \\ twice in your text like  this \\\\")
print("The best hits of '80s!!!")
print('The best hits of \'80s!!!')

amountPLN = 234
USD = 3.65
EUR = 4.23
print("cur ","exchange ","amount", sep="\t")
print("USD  ",USD, amountPLN/USD, sep="\t")
print("EUR  ",EUR, amountPLN/EUR, sep="\t")

ValueAsText = "123.45"
factor = 1.23
print("value is",ValueAsText,"factor is ",factor,"value*factor", float(ValueAsText)*factor)

