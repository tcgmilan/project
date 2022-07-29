i = None
t = []

while i != 0:
    i = int(input("Adj meg egy számot: "))
    t.insert(0, i)

t.pop(0)
print(t)
