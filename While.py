secret_word = "mysz"
guess = ""
trys = 0
trys_limit = 3
out_of_trys = False
while guess != secret_word and not(out_of_trys):
    if trys < trys_limit:
        guess = input("Enter guess: " )
        trys += 1
    else:
        out_of_trys = True
if out_of_trys:
    print("you lose")
else:
    print("you win")