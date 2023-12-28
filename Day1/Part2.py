numbers = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

file = open("input", "r")
total  = 0
while True:
    content = file.readline()
    if not content:
        break

    pos, numFound = 0, False
    print ("new Word", content)
    while not numFound:
        if (48 <= ord(content[pos]) <= 57):
            numFound = True
            print ("shortword1", int(content[pos]))
            total += int(content[pos]) * 10
        
        check = pos - 4 if pos - 4 >= 0 else 0
        for i in range(check, pos-1):
            if content[i:pos+1] in numbers:
                print ("longword1", content[i:pos+1])
                total += (numbers[content[i:pos+1]] * 10)
                numFound = True
                break
        pos += 1

    pos, numFound = len(content)-1, False

    while not numFound:
        if (48 <= ord(content[pos]) <= 57):
            numFound = True
            print ("shortword2", int(content[pos]))
            total += int(content[pos])
        
        check = pos - 4 if pos - 4 >= 0 else 0
        for i in range(check, pos-1):
            if content[i:pos+1] in numbers:
                print ("longword2", content[i:pos+1])
                total += numbers[content[i:pos+1]]
                numFound = True
                break
        pos -= 1
print(total)