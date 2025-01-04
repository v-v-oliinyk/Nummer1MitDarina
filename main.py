# print("kdjfl")
# name = "vadim"
# age = 12
# print(name)
# print(name+name+"sdlgnhksd")
# print(type(age))
# print ( f"{name} is {age} years old")
# a = input ("How old are you?\n")
# print("user is "+ a +" years old")


zakaz = input("Hello, what whoud you like to order\n")
utochnennia = input ("how much? (0.3, 0.5)\n")
if utochnennia == "0.3":
    price = 2
elif utochnennia == "0.5":
    price = 2.5
else :
    print ("Baran, vse huinia davai po novoi")
    exit()
print (f"z tebe {price} euro, kozel")
plus = input ("schos' sche?\n")

if plus == '' :
    print ("Chekai trohy")
elif plus :
    print (f"z tebe 100 euro, kozel")
    price = 100

abc = f"Os' vasche zamovlennia {zakaz}"
if  not plus :
    abc = abc + f" i {plus}"
print (abc)