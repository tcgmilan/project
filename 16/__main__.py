def calc(x : int):
    if x % 3 == 0 and x % 2 == 0: return True
    return False

if __name__ == "__main__":
    print(calc(int(input("Szám: "))))