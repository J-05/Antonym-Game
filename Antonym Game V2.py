##### ANTONYM GAME #####

import random
qNum = 1
correct = 0
keyNumList = []

##### SUBROUTINES #####

#open file and locate all keys
def locateLineNum(x,locate,store):
    with open(x) as file:
        for (i,line) in enumerate(file):
            if locate in line:
                store.append(i)

#choose and remove key
def chooseKey(x):
    key = random.choice(x)
    x.remove(key)
    return key

#get line from lineNum
def getLine(x,lineNum):
    with open(x) as file:
        for (i,line) in enumerate(file):
            if i == lineNum:
                return str(line).strip()
            
#check if has [x]
def cleanWord1(word):
    if "[" and "]" in word:
        first = word.index("[")
        last = word.index("]")
        return str.title(word.replace("KEY:","").replace(",","").replace(".","").replace(word[first:last+1],"").strip())
    elif "\\" in word:
        first = word.index("\\")
        last = word.rindex("\\")
        return str.title(word.replace("KEY:","").replace(",","").replace(".","").replace(word[first:last+1],"").strip())
    elif "_" in word:
        return str.title(word.replace("KEY:","").replace(",","").replace(".","").replace("_").strip())
    else:
        return str.title(word.replace("KEY:","").replace(",","").replace(".","").strip())

#puts into cleaned list
def cleanWordList2(file,key,x):
    x = getLine(file,key)
    xList = str.lower(x.replace("ANT:","").strip().replace(".","")).split(", ")
    for word in xList:
        if "[" in word:
            xList.remove(word)
            
    return xList

#find valid word1
def getValidKey():
    while True:
        hold = []
        #find example key
        key = chooseKey(keyNumList)
        #get word1 from example key
        word = getLine("AntonymText.txt",key)
        word = cleanWord1(word)
        hold.append(key)
        hold.append(word)
        if word != None:
            if "ANT" in getLine("AntonymText.txt",key+4):
                return hold
            
#ask question format
def ask(e1,eList,q1):
    print("-"*100+"\nQ"+str(qNum)+": "+e1+" is to "+random.choice(eList)+", as "+str.lower(q1)+" is to ...?")

for i in range(10):
    ##### FINDS PAIRS OF PHRASES #####

    locateLineNum("AntonymText.txt","KEY",keyNumList)

    #get wordE1 and wordQ1
    tempList = getValidKey()
    keyE1 = int(tempList[0])
    wordE1 = str(tempList[1])
    tempList = getValidKey()
    keyQ1 = int(tempList[0])
    wordQ1 = str(tempList[1])

    #get wordListE2 and wordListQ2
    keyE2 = keyE1 + 4
    keyQ2 = keyQ1 + 4

    wordListE2 = None
    wordListE2 = cleanWordList2("AntonymText.txt",keyE2,wordListE2)
    wordListQ2 = None
    wordListQ2 = cleanWordList2("AntonymText.txt",keyQ2,wordListQ2)

    ##### INPUT TO USER #####
    ask(wordE1,wordListE2,wordQ1)
    userAns = input("")

    ##### CHECK ANSWER #####
    if userAns in wordListQ2:
        correct+=1
        print("[Correct]")
    else:
        print("[Incorrect] These were the possible answers : "+str(wordListQ2).strip("[").strip("]").replace("'","")+".")
    qNum += 1

##### OUTPUT SCORE #####
print("-"*100+"\nYour Score: "+str(correct))
