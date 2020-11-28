word = input()

covToCap = False
cntUpperCase = 0
cntLowerCase = 0

for i in range(len(word)):
    if(word[i].isupper()):
        cntUpperCase+=1
    else:
        cntLowerCase+=1

if cntUpperCase> cntLowerCase:
    print(word.upper())
else:
    print(word.lower())

