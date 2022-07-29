x : int = int(input("Szám: "))

if x % 3 == 0: print(f"{x} osztható 3-mal!")
elif x % 5 == 0: print(f"{x} osztható 5-tel!")
else: print(f"A(z) {x} nem osztható 3-mal, se 5-tel!")