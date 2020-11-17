import random

i = 0
lista = []
one = ""
two = ""
facit = ""
antalHint = 5
hintList = []
randList = []
correct = 0
tries = 0


dic = {
    'А': 'a',
    'Б': 'b',
    'В': 'v',
    'Г': 'g',
    'Д': 'd',
    'E': 'ye',
    'Ё': 'yo',
    'Ж': 's*',
    'З': 'z',
    'И': 'ee',
    'Й': 'y',
    'К': 'k',
    'Л': 'l',
    'М': 'm',
    'Н': 'n',
    'О': 'o',
    'П': 'p',
    'Р': 'r',
    'С': 's',
    'Т': 't',
    'У': 'oo',
    'Ф': 'f',
    'Х': 'ch*',
    'Ц': 'ts',
    'Ч': 'ch',
    'Щ': 'sh',
    'Ы': 'u',
    'Э': 'e',
    'Ю': 'ou',
    'Я': 'ya'}

for key in dic:
    lista.append(key)

def fillHintList():
    for x in range (antalHint):
        hintList.append("")

def findRandomRus():
    temp = random.randint(0,27)
    facit = dic[lista[temp]]
    print(lista[temp])
    return facit

def randEng():
    return dic[lista[random.randint(0,(len(lista) - 1))]]

def engHint(facit):
    temp = random.randint(0, (antalHint - 1))
    hintList[temp] = facit
    randList.append(temp)
    for x in range (antalHint - 1):
        while True:
            temp = random.randint(0, (antalHint - 1))
            if ((temp in randList) == False):
                break
        while True:
            temp2 = randEng()
            if ((temp2 in hintList) == False):
                break
        hintList[temp] = temp2
        randList.append(temp)
    print(hintList)


print("answer in what language")
while True:
    one = input("rus(r) / eng(e): ").lower()
    if one == "r" or one == "e":
        break


if one == "e":
    print("Input english sound/letter")
    print("'exit' / 'help' / 'hint'")
    print("====================")
    while True:
        randList = []
        hintList = []
        hint = False
        fillHintList()
        facit = findRandomRus()
        while True:
            two = input("Answer: ").lower()
            if two != "hint" or two != "exit":
                tries+=1
            if two == "exit":
                break
            elif two == "help":
                percentCorrect = (correct / tries)*100
                print(facit + "\n=================== " + str(round(percentCorrect)) + "%")
                break
            elif two == facit:
                correct+=1
                percentCorrect = (correct / tries)*100
                print("Correct\n=================== " + str(round(percentCorrect)) + "%")
                break
            elif two == "hint" and hint == False:
                engHint(facit)
                hint = True
        if two == "exit":
            break
                


##NOT FINNISHED
elif one == "r":
    print("======================================")
    print(lista)
    

##if "model" in thisdict:
##  print("Yes, 'model' is one of the keys in the thisdict dictionary")
    
##print("А, Б, В, Г, Д, Е, Ё, Ж, З, И, Й, К, Л, М, Н, О, П, Р, С, Т, У, Ф, Х, Ц, Ч, Ш, Щ, Ъ, Ы, Ь, Э, Ю, Я")
    

print("out")

