inputThings = []
a = input()
while a != '!!!!!':
    inputThings += [' ']
    inputThings += a
    a = input()
wordCount = []
inputThingsCount = len(inputThings)
inputThingsCountMinusOne = int(inputThingsCount) - 1
wordStartSpace = 0
wordEndPlace = 0
inputThings.insert(0, " ")
inputThings.insert(len(inputThings), " ")
flag = 0
for whichLetter in range(len(inputThings)):
    if inputThings[whichLetter - 1] == ' ' and inputThings[whichLetter] != ' ':
        flag += 1
        wordStartSpace = whichLetter
    if inputThings[whichLetter] != ' ' and inputThings[whichLetter + 1] == ' ':
        flag += 1
        wordEndPlace = whichLetter
    if flag == 2:
        sub = inputThings[wordStartSpace:wordEndPlace + 1]
        sub = "".join(sub)
        flag = 0
        if sub not in wordCount:
            wordCount += [sub]
print(len(wordCount))
wordCount.sort() 
if len(wordCount) > 10:
    for whichOne in range(10):
        print(wordCount[whichOne])
else:
    for whichOne in range(len(wordCount)):
        print(wordCount[whichOne])
