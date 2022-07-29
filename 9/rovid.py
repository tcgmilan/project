x : int = int(input("Első szám: "))
y : int = int(input("Második szám: "))
t = []

for z in range(x, y + 1):
    if z % 2 == 0: t.append(str(z))

print(", ".join(t))