# 'x', 'y', 'z' változó 'int' típussal (típusjelölés nem kötelező!)
x : int = int(input("Első szám: "))
y : int = int(input("Második szám: "))
z : int = int(input("Harmadik szám: "))

a = min(x, y, z) # legkisebb szám megkeresése a 'min()' függvénnyel!

print(f"A legkisebb szám: {a}") # f"abcde {valtozo}" -> 'f string' változó beleírása szövegbe '{}' jelek közé!