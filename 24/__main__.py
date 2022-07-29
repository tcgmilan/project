f = open("24/temp.txt", "r", encoding = "utf-8").read()

print("A 'Debrecen' szó megtalálható a 'temp.txt'-ben!") if "Debrecen" in f else print("A 'Debrecen' szó nem található meg a 'temp.txt'-ben!")
