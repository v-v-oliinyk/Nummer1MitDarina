name = input("Будь ласка, введіть ваше імʼя: \n")
nameLength = len(name)
conjugatedNoun = ""
if nameLength == 0:
    conjugatedNoun = ""
elif nameLength == 1 or nameLength == 21:
    conjugatedNoun = "літеру"
elif 2<=nameLength<=4 or 22<=nameLength<=24:
    conjugatedNoun = "літери"
elif 5<=nameLength<=20 or 25<=nameLength==30:
    conjugatedNoun = "літер"
else :
    conjugatedNoun = "ніхуя собі блять літер"
# Примітивний принцип вміщує до 30 літер. цього достатньо для більшості імен. Житель Тернополя з імʼям в 100 літер не зможе ввести своє імʼя :D
if not nameLength :
    print("Ви ввели імʼя неправильно. Перезапустіть програму")
else :
    print ("Ваше імʼя : " + name + ". воно містить " + f"{nameLength} " + conjugatedNoun)

# кілька випадків з якими стикнувся
# print ("Ваше імʼя : " + name + ". воно містить " + f"{nameLength} " + conjugatedNoun) тут не давало просто "+ nameLength +" написати через якийсь конфлікт типів str->int чому так?
#