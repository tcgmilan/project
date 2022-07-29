# 'x', 'y', 'z' változó 'int' típussal (típusjelölés nem kötelező!)
x : int = int(input("Első szám: "))
y : int = int(input("Második szám: "))
z : int = int(input("Harmadik szám: "))

a = max(x, y, z) # legnagyobb szám megkeresése a 'max()' függvénnyel!

print(f"A legnagyobb szám: {a}") # f"abcde {valtozo}" -> 'f string' változó beleírása szövegbe '{}' jelek közé!