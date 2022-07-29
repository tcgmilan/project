# 'x' (int) lesz a szám amelynél keressük a kisebb, hárommal osztható számokat.
x : int = int(input("Határszám: "))
# 't' (list) tároló tömb, melyben a helyes számokat tároljuk.
t : list = []

# az 'i' (int) típusú változó tartalmazza a ciklus számait
# a 'reversed()' függvény mindent a visszájára fordít (pl.: lista elemeinek sorrendjét fordítja meg)
# a 'range()' egy listát hoz létre két szám között melyben az első szám a lista legkisebb értéke, míg a második a list legnagyobb értékénél EGYEL KISEBB!!!
# a '[::3]' pedig az úgynevezett 'step' azaz a 'lépésszámot' adja meg, tehát 'hányasával menjen' a list értéke.
# 
# Összegzés:
# Ez a ciklus hármasával visszafelé megy x től 0 ig, (pl.: x = 100) akkor [100, 99, 96, 93, 90, ...] 
# Az 'x' utáni '+ 3' nak matematikai oka van, így jön ki a feladat.
for i in reversed(range(0, x + 3)[::3]):
    t.append(str(i)) # a 't' tároló tömbhöz hozzáadom az 'i' értékét 'string', azaz 'szöveg' formátumban.

t.pop(0) # a tömb első elemének (ami jelen esetben mindig az 'x' értéke lesz) törlése

print(t) # formázatlan kiíratás
print(", ".join(t)) # formázott kiíratás (vesszővel való elválasztás a 'join()' függvénnyel!)