# 'x', 'y', 'z' változó 'int' típussal (típusjelölés nem kötelező!)
x : int = int(input("Első szám: "))
y : int = int(input("Második szám: "))
z : int = int(input("Harmadik szám: "))

# ha 'x' + 'y' egyenlő 'z'-vel...
if x + y == z: print(f"{x} + {y} = {z}")

# ha 'x' + 'z' egyenlő 'y'-al...
elif x + z == y: print(f"{x} + {z} = {y}")

# ha 'y' + 'z' egyenlő 'x'-el...
elif y + z == x: print(f"{y} + {z} = {x}")

# amennyiben egyik feltétel sem teljesül...
else: print("Nincs olyan lehetőség ahol valamelyik 2 szám össze megegyezne a 3. számmal!")