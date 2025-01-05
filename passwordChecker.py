# не може бути порожнім
# не менше 16 символів
# хоча б одну цифру
# хоча б одну велику літеру
# маленьку літеру
# хоча б один спеціальний символ (₴#&_-@)

def check_password(password):
    upper_case, lower_case, special_chars, digits, length = 0, 0, 0, 0, 0

    for char in password:
        if len(password) > 16:
            length += 1
        elif char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
        elif char.isdigit():
            digits += 1
        elif char in "₴#&_-@!":
            special_chars += 1

    if upper_case != 0 and lower_case != 0 and digits != 0 and length != 0 and special_chars != 0 :
        print("Password is enough strong!")
    else:
        if not len(password):
            print("Поле пароля не може бути пустим.")
        if length == 0:
            print("Пароль має містити щонайменше 16 символів.")
        if special_chars == 0:
            print("Пароль має містити щонайменше один спеціальний символ! (#&_-@!)")
        if digits == 0:
            print("Пароль має містити щонайменше одне число!")
        if upper_case == 0:
            print("Пароль має містити щонайменше одну велику літеру!")
        if lower_case == 0:
            print("Пароль має містити щонайменше одну маленьку літеру!")


password_input = input(f"Будь ласка, введіть пароль що складається мінімум з 8 символів, містить мінімум одну маленьку, велику літеру, цифру та спеціальний символ (₴#&_-@) : \n")
check_password(password_input)

#я так і не додумався як це реалізувати виключно через цикли.. треба якось оболонку змінити, а як...

#https://codevisionz.com/lessons/python-code-example-check-password-strength/ - i used some part of this code for help. !"!