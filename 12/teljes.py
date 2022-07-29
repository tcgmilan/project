# 'x' változó 'str' típussal (típusjelölés nem kötelező!)
x : str = input("Darabolandó szó: ")

# 'str' esetén a ciklus nem számokon hanem az adott szöveg karakterein megy át.
# az éppen aktuális karaktert jelen esetben az 'i' változó jelöli
# Python nyelvben minden 'print()' funkció új sort kezd.
for i in x:
    print(i)