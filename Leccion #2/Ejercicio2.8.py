f = open("Poem2.txt", "w")
f.write("When I think about myself, \n ")
f.write("I almost laugh myself to death.\n")
f.close()
f = open("Poem2.txt", "r")
data = f.read()
print(data)