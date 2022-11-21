# flaot_maly = 3.1415456456456456123123123
# flaot_duzy = 3.86712313123123131
#
# print(flaot_maly,flaot_duzy)
# print("\n")
# print(int(flaot_maly),int(flaot_duzy))
# print("\n")
# print(abs(flaot_maly),abs(-flaot_duzy))
# print("\n")
# print(round(flaot_maly,2),round(flaot_duzy,2),round(flaot_duzy,3))
# print("\n")
# print(min(flaot_maly,flaot_duzy),max(flaot_maly,flaot_duzy))
# lista = [1,2,3,4,5,4,4,3]
# print(sum(lista),len(lista))
# print(sum(lista)/len(lista))
# print("\n")
# print(round(2.675,2))

#LAB
percent = [2.606255012, 1.222935044, 1.283079391, 3.628708901, 6.856455493, 4.911788292,
           2.886928629, 0.781876504, 0.962309543, 2.265437049, 6.816359262, 3.688853248,
           3.468323978, 5.633520449, 4.530874098, 1.984763432, 0.922213312, 3.327987169,
           4.190056135, 5.493183641, 1.864474739, 10.60545309, 2.425821973, 2.726543705,
           8.740978348, 6.174819567]

countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal', 'United Kingdom', 'Serbia', 'Germany', 'Albania',
             'France', 'Czech Republic', 'Denmark', 'Australia', 'Finland', 'Bulgaria',
             'Moldova', 'Sweden', 'Hungary', 'Israel', 'Netherlands', 'Ireland',
             'Cyprus', 'Italy']

sumOfPoints = 4988

print(min(percent))
print(max(percent))
print("---------------")
for i in range(len(countries)):
    print(percent[i])
    print(int(percent[i]))
    print(round(percent[i]))
    print(round(percent[i])*sumOfPoints/100,0)
    print(countries[i])
    print("----------")

