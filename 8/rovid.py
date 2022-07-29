x : int = int(input("Szám: "))
t = []

for y in reversed(range(0, x + 3)[::3]):
    t.append(str(y))

t.pop(0)
print(", ".join(t))