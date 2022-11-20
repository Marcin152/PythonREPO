itRains = False

if itRains:
    print("we stay a home")
else:
    print("we go out")

print("we stay at home" if itRains else "no")

#exec

musclePain = False
fever = True
weakness = True

print("suspicion of infuenza" if musclePain == True and fever == True and weakness == True else "the flu in unlikel")