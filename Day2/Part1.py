ans  = 0
with open("input") as file:
    lines = file.readlines()
    for line in lines:
        removeSlash = line.split("\n")
        splitOne = removeSlash[0].split(": ")
        gameId = int((splitOne[0].split(" "))[-1])
        possible = True
        game = splitOne[-1].split("; ")
        for i in range (len(game)):
            available = {"red" : 12, "green" : 13, "blue" : 14}
            round = game[i].split(", ")
            for color in round:
                splitcolor = color.split(" ")
                if available[splitcolor[1]] < int(splitcolor[0]):
                    possible = False
                    break
            if not possible:
                break
        if possible:
            ans += gameId
print (ans)

