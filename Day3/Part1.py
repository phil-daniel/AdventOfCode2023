with open("input") as file:
    lines = file.readlines()
    content = [[] for _ in range(len(lines))]
    for i in range (len(lines)):
        for j in range(len(lines[0])-1):
            content[i].append(lines[i][j])
ans = 0
toCheck = [[-1,-1], [-1,0], [-1,1], [0,1], [0,-1], [1,1], [1,0], [1, -1]]
for i in range (len(content)):
    curr, adj = 0, False
    for j in range (len(content[0])):
        if 48 <= ord(content[i][j]) <= 57:
            curr = (curr * 10) + int(content[i][j])
            if not adj:
                for check in toCheck:
                    posY, posX = i + check[0], j + check[1]
                    if 0 <= posY < len(content) and 0 <= posX < len(content[0]):
                        if content[posY][posX] != '.' and not (48 <= ord(content[posY][posX]) <= 57):
                            adj = True
                            break
        else:
            if adj:
                ans += curr
            curr, adj = 0, False
    if adj:
        ans += curr


print (ans)