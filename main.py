matrice = {
    0: [1, 2, 3, 4],
    1: [11, 12, 13, 14],
    2: [21, 22, 23, 24],
    3: [31, 32, 33, 34],
    4: [41, 42, 43, 44]
}

for each in matrice[0]: 
    print(each)
for each in matrice:
    if each == 0:
        pass
    else:
        print(matrice[each][len(matrice[each])-1])


for each in matrice:
    if each == len(matrice):
        f = len(matrice[each])-1
        for each_el in matrice[len(matrice)-1]:
            print(matrice[each][f])
            f-=1
    else:
        pass


mynum = len(matrice)-1
myn = len(matrice[mynum])-1
for each in matrice[mynum]:
    if matrice[mynum][len(matrice[mynum])-1] == matrice[mynum][myn]:
        myn-=1
        pass
    else:
        print(matrice[mynum][myn])
        myn-=1

mynum = len(matrice)-1
for x in matrice:
    if mynum == 0 or mynum == len(matrice)-1:
        mynum-=1
        pass
    else:
        print(matrice[mynum][0])
        mynum-=1

for each in matrice:
    if each == len(matrice)-1 or each == 0:
        pass
    else:
        for each_element in matrice[each]:
            if each_element == matrice[each][0] or matrice[each][len(matrice[each])-1] == each_element:
                pass
            else:
                print(each_element)
