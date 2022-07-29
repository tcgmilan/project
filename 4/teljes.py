x : int = int(input("Ellenőrizendő szám: ")) # 'x' változó tárolja a számot (int)

# ha a szám osztható hárommal...
if x % 3 == 0:
    print("A szám osztható hárommal!")

# ha a szám osztható öttel...
if x % 5 == 0:
    print("A szám osztható öttel!")

# ha a szám nem osztható sem öttel, sem hárommal...
# 'and' szó összeköti a feltételek mint a '&&' jel.
# 'or' szó esetén csak az egyik feltételnek kell teljesülni, mint a '||' jelnél.
if x % 3 != 0 and x % 5 != 0:
    print("A szám sem hárommal, sem öttel nem osztható!")