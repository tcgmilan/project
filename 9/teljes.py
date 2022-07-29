# 'x', 'y' változó 'int' típussal (típusjelölés nem kötelező!)
x : int = int(input("Első szám: "))
y : int = int(input("Második szám: "))
# 't' (list) tároló tömb, melyben a helyes számokat tároljuk.
t : list = []

# ciklus amely 'x' és 'y' közötti számokon megy végig, melyet az 'i' változó jelöl
for i in range(x, y + 1):
    # ha 'i' páros (tehát kettővel osztva nincs maradék)...
    if i % 2 == 0:
        t.append(str(i)) # a 't' tároló tömbhöz hozzáadom az 'i' értékét 'string', azaz 'szöveg' formátumban.

print(t) # formázatlan kiíratás
print(", ".join(t)) # formázott kiíratás (vesszővel való elválasztás a 'join()' függvénnyel!)

