nameAndAge = input("Будь ласка, введи своє ім'я та вік (використовуйте пробіл між введеними даними): \n").split(' ')


if len(nameAndAge) != 2:
    print ("Надані дані не відповідають початковому запиту. Перезапустіть програму.")
    exit()

check1 = str.isdigit(nameAndAge[0])
check2 = str.isdigit(nameAndAge[1])
if check1:
    age = int(nameAndAge[0])
    name = nameAndAge[1]
elif check2:
    age = int(nameAndAge[1])
    name = nameAndAge[0]
else :
    print ("Надані дані не відповідають початковому запиту. Перезапустіть програму.")
    exit()

conjugatedNoun = ""
if age <= 0:
    print("Неправильно введений вік. Спробуй ще раз.")
    exit()
elif age == 21:
    conjugatedNoun = "рік"
elif 22 <= age <= 24:
    conjugatedNoun = "роки"
elif 13 <= age <= 20:
    conjugatedNoun = "років"

if age > 25:
    print("Привіт пострижися, старий. Геть звідси!")
    exit()
elif age < 13:
    print("Лягай спать, дитино.")
    exit()
else:
    print(f"Так от, ти {name} і тобі {age} {conjugatedNoun}? Приємно! Вітаю на борту розумник/ця!")
    exit()

# в мене ще є провтик якщо дані було введено неправильно і в цих двох елементах немає числового значення то виходить дічь. Я ніби й пофіксив це чеками, але це зовсім не масштабована штука.
# ох.. Тупота досі не дає спокою...  Може ще є баги, але треба потестити..