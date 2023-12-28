with open("input") as file:
    lines = file.readlines()
    content = [[] for _ in range(len(lines))]
    for i in range (len(lines)):
        for j in range(len(lines[0])-1):
            content[i].append(lines[i][j])

def getNumbers(x, y):
    num, sides = 0, 0
    while 0 <= x + sides < len(content[0]) and 48 <= ord(content[y][x+sides]) <= 57:
        sides -= 1
    sides += 1
    while 0 <= x + sides < len(content[0]) and 48 <= ord(content[y][x+sides]) <= 57:
        num = (num * 10) + ord(content[y][x+sides]) - 48
        sides += 1
    return [num, sides]

ans = 0
toCheck = [[[1,-1], [1,0], [1,1]], [[0,-1]], [[0,1]], [[-1,-1], [-1,0], [-1,1]]]
for i in range (len(content)):
    for j in range (len(content[0])):
        if content[i][j] == '*':
            adj = []
            for row in toCheck:
                pos = 0
                while pos < len(row):
                    xPos, yPos = j + row[pos][1], i + row[pos][0]
                    if 0 <= yPos < len(content) and 0 <= xPos < len(content[0]) and content[yPos][xPos] != '.':
                        num = getNumbers(xPos, yPos)
                        pos += max(num[1]+1, 2)
                        adj.append(num[0])
                    else:
                        pos += 1
            if len(adj) == 2:
                ans += (adj[0] * adj[1])

print (ans)