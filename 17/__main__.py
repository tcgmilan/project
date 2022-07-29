def calc(x : int, y : int, z : int):
    if x >= 1 and y >= 1 and z >= 1: return True
    return False

if __name__ == "__main__":
    print(calc(int(input("Első szám: ")), int(input("Második szám: ")), int(input("Harmadik szám: "))))