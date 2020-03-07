lines = [
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod", 
    "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,",
    "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo",
    "consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse",
    "cillum dolore eu fugiat nulla pariatur. Excepteur sint accaecat cupidatat nom",
    "proident, sunt in culpa qui afficia deserunt mollit anim id est laborum."
    ]

f = open("lorem.txt", "w")
f.writelines(lines)
f.close()