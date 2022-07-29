f = open("25/szamok.txt", "w", encoding = "utf-8")
n = []

for x in range(0,101):
    if x % 3 == 0:
        n.append(str(x))
f.write(", ".join(n))
f.close()