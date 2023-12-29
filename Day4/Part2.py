with open("input") as file:
    lines = file.readlines()
    ans = [1 for _ in range (len(lines))]
    for i in range(len(lines)):
        winCount = 0
        gameInfo = lines[i].split(": ")[1].split("\n")[0].split(" | ")
        winners = set(gameInfo[0].split(" "))
        cards = gameInfo[1].split(" ")
        for card in cards:
            if card != "":
                if card in winners:
                    winCount += 1
        for j in range(winCount):
            if i+1+j < len(ans):
                ans[i+1+j] += ans[i]
            else:
                break
    print (sum(ans))