def translator(zwrot):
    translation = ""
    for letter in zwrot:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translator(input("Wpisz zwrot: ")))