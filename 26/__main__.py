f = open("26/temp.txt", "r", encoding = "utf-8").read().split(" ")
print(", ".join(f[::2]))
