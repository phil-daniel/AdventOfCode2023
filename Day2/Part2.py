ans  = 0
with open("input") as file:
    lines = file.readlines()
    for line in lines:
        removeSlash = line.split("\n")
        splitOne = removeSlash[0].split(": ")
        gameId = int((splitOne[0].split(" "))[-1])
        possible = True
        game = splitOne[-1].split("; ")
        maxi = {"red" : 0, "green" : 0, "blue" : 0}
        for i in range (len(game)):
            round = game[i].split(", ")
            for color in round:
                splitcolor = color.split(" ")
                maxi[splitcolor[1]] = max(maxi[splitcolor[1]], int(splitcolor[0]))
        toAdd = 1
        for color in maxi.keys():
            toAdd *= maxi[color]
        ans += toAdd

print (ans)