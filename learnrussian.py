import random

i = 0
lista = []
one = ""
two = ""
facit = ""
antalHint = 5
hintList = []
randList = []


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
    temp2 = random.randint(0, (antalHint - 1))
    hintList[temp2] = facit
    randList.append(temp2)
    for x in range (antalHint - 1):
        while True:
            temp2 = random.randint(0, (antalHint - 1))
            if ((temp2 in randList) == False):
                break
        hintList[temp2] = randEng()
        randList.append(temp2)
    print(hintList)


while True:
    print("answer in what language")
    one = input("rus(r) / eng(e): ").lower()
    if one == "r" or one == "e":
        break


if one == "e":
    print("Skriv engelska bokstaven/lätet")
    print("'exit' / 'help' / 'hint'")
    print("====================")
    while True:
        randList = []
        hintList = []
        hint = False
        fillHintList()
        facit = findRandomRus()
        while True:
            two = input("svar: ").lower()
            if two == "exit":
                break
            elif two == "help":
                print(facit + "\n===================")
                break
            elif two == facit:
                print("RÄTT\n===================")
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

