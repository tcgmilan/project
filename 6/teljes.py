# 'x', 'y', 'z' változó 'int' típussal (típusjelölés nem kötelező!)
x : int = int(input("Első szám: "))
y : int = int(input("Második szám: "))
z : int = int(input("Harmadik szám: "))

# Módszer 1 (haladó):
print("Mindhárom szám páros") if x % 2 == 0 and y % 2 == 0 and z % 2 == 0 else print("A számok között van egy (vagy több) páratlan!")

# Módszer 2 (egyszerűbb):
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print("Mindhárom szám páros!")
else:
    print("A számok között van egy (vagy több) páratlan!")