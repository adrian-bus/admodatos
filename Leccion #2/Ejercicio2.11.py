f = open("Poem2.txt", "a")
f.write("\nAlone, all alone. Nobody, but nobody. Can make it here alone.")
f.close()
data = open("Poem2.txt").read()

print(data)