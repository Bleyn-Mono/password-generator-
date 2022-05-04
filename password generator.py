import random
digits = '23456789'
lowercase_letters = "abcdefghjkmnpqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKMNPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
badsimbols = 'il1L0oO'
flag2 = False
flag = False
counter = 0
chars = ''

print("Привет! Это генератор безопасных паролей")

def fool_protection(variable):
    flag1 =  False
    while flag1 == False:
        if not (variable == "д" or variable == "н"):
            variable = input("Необходимо нажать 'д' или 'н', попробуйте снова: ")
        else:
            flag1 = True
    return variable
        
n = input("Введите количество паролей для генерации: ")
while flag == False:
    if not n.isdigit():
        print("Необходимо ввести число")
        n = input("Попробуйте снова: ")
    else:
        flag = True

add_digit = input("Включить цифры? (д = да, н = нет) ")
if fool_protection(add_digit) == 'д':
    chars += digits
    counter += 1

add_lowercase = input("Включить прописные буквы? (д = да, н = нет) ")
if fool_protection(add_lowercase) == 'д':
    chars += lowercase_letters
    counter += 1
    
add_upperrcase = input("Включить заглавные буквы? (д = да, н = нет) ")
if fool_protection(add_upperrcase) == 'д':
    chars += uppercase_letters
    counter += 1
        
add_punctuation = input("Включить символы такие как '!#$%&*+-=?@^_'? (д = да, н = нет) ")
if fool_protection(add_punctuation) == 'д':
    chars += punctuation
    counter += 1

remove_badsimbols = input("Исключить неоднозначные символы 'il1L0oO'? (д = да, н = нет) ")
if fool_protection(remove_badsimbols) == 'н':
    chars += badsimbols
    counter += 1
    
long, flag = input("Введите длинну пароля: "), False
while flag == False:
    if not long.isdigit():
        print("Необходимо ввести число")
        long = input("Попробуйте снова: ")
    elif int(long) > 76:
        print("Пароль не может содержать больше 76 символов")
        long = input("Попробуйте снова: ")
    elif int(long) == 0:
        print("Пароль не может содержать 0 символов")
        long = input("Попробуйте снова: ")
    elif int(long) < counter:
        print("Пароль не может содержать меньше", counter, "символов")
        long = input("Попробуйте снова: ")
    else:
        flag = True

def correctnes_password(array):
    for i in list:
        if i in array:
            return True
        
for i in range(int(n)):
    f = 0
    while not(f == counter) :
        list, f = ''.join(random.sample(chars, int(long))), 0
        if add_digit == "д":
            if (correctnes_password(digits)):
                f += 1    
        if add_lowercase == "д":
            if (correctnes_password(lowercase_letters)):
                f += 1
        if add_upperrcase == "д":
            if (correctnes_password(uppercase_letters)):
                f += 1
        if add_punctuation == "д":
            if (correctnes_password(punctuation)):
                f += 1
        if remove_badsimbols == "н":
            if (correctnes_password(badsimbols)):
                f += 1
        if f == counter:
            print(list)