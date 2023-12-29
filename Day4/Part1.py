ans = 0
with open("input") as file:
    lines = file.readlines()
    for line in lines:
        winCount = -1
        gameInfo = line.split(": ")[1].split("\n")[0].split(" | ")
        winners = set(gameInfo[0].split(" "))
        cards = gameInfo[1].split(" ")
        for card in cards:
            if card != "":
                if card in winners:
                    winCount += 1
        if winCount >= 0:
            ans += 2 ** winCount
    print (ans)
        

