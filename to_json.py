import json

ar = []

with open("XXX.txt", encoding="utf-8") as r:
    for i in r:
        n = i.lower().split("\n")[0] #перевод в нижний регистр
        if n != "": #проверяем на отсутствие пустой строки
            ar.append(n)

with open("XXX.json", "w", encoding="utf-8") as e:
    json.dump(ar, e)