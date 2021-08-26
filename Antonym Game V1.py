##### ANTONYM GAME #####

import random
qNum = 1
correct = 0

##### SUBROUTINES #####
def ask(list1,list2,key1,key2):
    print("-"*50+"\nQ"+str(qNum)+": "+str.title(list1[key1])+" is to "+str.lower(list2[key1])+", as "+str.lower(list1[key2])+" is to ...?")

#choose and remove key
def chooseKey(x):
    key = random.choice(x)
    x.remove(key)
    return key

#convert to list all lowercase
def convertList(string,separate):
    array = string.split(separate)
    array = [str.lower(word) for word in array]
    return array

##### CONVERT TO LIST #####
wordList1 = convertList("hot, summer, hard, dry, simple, light, weak, male, sad, win, small, ignore, buy, succeed, reject, prevent, exclude",", ")
wordList2 = convertList("cold, winter, soft, wet, complex, darkness, strong, female, happy, lose, big, pay attention, sell, fail, accept, allow, include",", ")

##### CHOOSE PAIRS #####
keyList = []
for word in wordList1:
    keyList.append(wordList1.index(word))

##### DISPLAY QUESTION #####
try:
    while True:
        #ask q
        keyE = chooseKey(keyList)
        keyQ = chooseKey(keyList)

        ask(wordList1,wordList2,keyE,keyQ)
        userAns = str.lower(input(""))

        #check ans
        if wordList2[keyQ] == userAns:
            print("[Correct]")
            correct += 1
        else:
            print("[Incorrect] The answer was "+wordList2[keyQ]+".")
        #next q
        qNum += 1
        
except IndexError:
    print("-"*50+"\nYour Score: "+str(correct))



