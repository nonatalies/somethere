def perevod_v_nnuu_ss(a, c):
    global b
    while a > 0:
        b = str(a % c) + b
        a //= c
    return b
flag = True
while flag:
    try:
        base = int(input("Введите основание системы счисления, в которую необходимо перевести число: "))
    except ValueError:
        print('Ошибка')
    else:
        flag = False
flag = True
while flag:
    try:
        n = float(input("Введите число: "))
    except ValueError:
        print('Ошибка.')
    else:
        if n == int(n):
            n = int(n)
        flag = False

b = ""
if type(n) == int:
    perevod_v_nnuu_ss(n, base)
    print(f'{n} в {base} системе счисления : {b}')
if type(n) == float:
    befor_dot_part = int(n)
    after_dot_part = n - int(n)
    perevod_v_nnuu_ss(befor_dot_part, base)
    b += "."
    i = 0
    while i < 10:
        i += 1
        after_dot_part *= base
        b = b + str(int(after_dot_part))
        after_dot_part -= int(after_dot_part)
    print(f'{n} в {base} системе счисления приблизительно равно {b}')
