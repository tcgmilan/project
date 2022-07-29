x : int = int(input("Első szám: "))
y : int = int(input("Második szám: "))
z : int = int(input("Harmadik szám: "))

if x + y == z: print(f"{x} + {y} = {z}")
elif x + z == y: print(f"{x} + {z} = {y}")
elif y + z == x: print(f"{y} + {z} = {x}")
else: print("Nincs olyan lehetőség ahol valamelyik 2 szám össze megegyezne a 3. számmal!")