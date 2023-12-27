file = open("input", "r")
total  = 0
while True:
    content = file.readline()
    if not content:
        break
    pos = 0
    while not (48 <= ord(content[pos]) <= 57):
        pos += 1
    total += int(content[pos]) * 10
    pos = len(content)-1
    while not (48 <= ord(content[pos]) <= 57):
        pos -= 1
    total += int(content[pos])
print(total)