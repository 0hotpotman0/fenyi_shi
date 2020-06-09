def phoneLetter(Letter_1):
    L = []
    letter = Letter_1
    for i in letter:
        if i == 'a' or i == 'b' or i == 'c' :L.append(2)
        if i == 'd' or i == 'e' or i == 'f' :L.append(3)
        if i == 'g' or i == 'h' or i == 'i' :L.append(4)
        if i == 'j' or i == 'k' or i == 'l' :L.append(5)
        if i == 'm' or i == 'n' or i == 'o' :L.append(6)
        if i == 'p' or i == 'q' or i == 'r' or i == 's' :L.append(7)
        if i == 't' or i == 'u' or i == 'v' :L.append(8)
        if i == 'w' or i == 'x' or i == 'y' or i == 'z' :L.append(9)
    return L
type_letter = str(input('type a letter: '))
C = map(str,phoneLetter(type_letter))
print("".join(C))