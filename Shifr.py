
alfa = []
lang = -1

while lang != 1 and lang != 0:
    lang = int(input('Выберите язык eng(1) или rus(0): '))
    if lang == 1:
        for i in range(26):
            alfa.append(chr(i + 97))
    elif lang == 0:
        a = ord('а')
        alfa = [chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)]
        # for i in range(33):
        #     alfa.append(chr(i + 1072))


# Добавление буквы Ё
# for i in range(0, 6):
#     alfa_false[i] = chr(i + 1072)
#     alfa.append(alfa_false[i])
# alfa_false[6] = chr(1105)
# alfa.append(alfa_false[6])
# for i in range(7, 33):
#     alfa_false[i] = chr(i + 1071)
#     alfa.append(alfa_false[i])


# Шифр Цезаря
def cesar(alfa, msg):
    shift = int(input('Введите сдвиг нижней строки: '))
    code_word = []
    alfa_b = []
    for _ in range(shift):
        alfa_b.append(alfa[_])
    alfa_b = alfa[shift:] + alfa_b
    for i in msg:
        for j, symb in enumerate(alfa):
            if i == symb:
                code_word.append(alfa_b[j])
    return code_word


def disCesar(alfa, code_word):
    shift = int(input('Введите сдвиг нижней строки: '))
    msg = []
    alfa_b = []
    for _ in range(shift):
        alfa_b.append(alfa[_])
    alfa_b = alfa[shift:] + alfa_b
    for i in code_word:
        for j, symb in enumerate(alfa_b):
            if i == symb:
                msg.append(alfa[j])
    return msg


# Ё-frendly
def yo(yo_alfa):
    if 'ё' in yo_alfa:
        for i, char in enumerate(yo_alfa):
            if ord(char) > 1078:
                yo_alfa.pop()
                yo_alfa.insert(i-1, 'ё')
                break
    return yo_alfa


# antiDubl
def antiDubl(d_alfa):
    uniq_alfa = []
    for i in d_alfa:
        if i not in uniq_alfa:
            uniq_alfa.append(i)
    return uniq_alfa


# Лозунговый шифр
def lozung(alfa, msg):
    alfa_b = antiDubl(list(input('Введите лозунг: ')))
    code_word = []
    temp_alfa = yo(sorted(list(set(alfa) - set(alfa_b))))
    alfa_b = alfa_b + temp_alfa
    print(alfa)
    print(alfa_b)
    for i in msg:
        for j, symb in enumerate(alfa):
            if i == symb:
                code_word.append(alfa_b[j])
    return code_word


def disLozung(alfa, code_word):
    alfa_b = antiDubl(list(input('Введите лозунг: ')))
    msg = []
    temp_alfa = yo(sorted(list(set(alfa) - set(alfa_b))))
    alfa_b = alfa_b + temp_alfa
    print(alfa)
    print(alfa_b)
    # print(def_alfa)
    # print(def_alfa_b)
    for i in code_word:
        for j, symb in enumerate(alfa_b):
            if i == symb:
                msg.append(alfa[j])
    return msg


# Полибианский квадрат
def polibiy(alfa, msg):
    size = 0
    i = 1
    code_word = []
    while size == 0:
        if len(alfa) <= i*i:
            size = i
        i = i + 1
    mx = [['' for i in range(size)] for a in range(size)]
    k = 0
    for i in range(size):
        for j in range(size):
            if k < len(alfa):
                mx[i][j] = alfa[k]
            else:
                mx[i][j] = chr(33 + k - len(alfa))
            k = k + 1
    # for _ in mx:
        # print(*_, sep='  ')

    for i in msg:
        for id_j, j in enumerate(mx):
            for id_a, a in enumerate(j):
                if i == a:
                    code_word.append(id_j + 1)
                    code_word.append(id_a + 1)
    return code_word


def disPolibiy(alfa, code_word):
    size = 0
    i = 1
    def_msg = []
    while size == 0:
        if len(alfa) <= i*i:
            size = i
        i = i + 1
    mx = [['' for i in range(size)] for a in range(size)]
    k = 0
    for i in range(size):
        for j in range(size):
            if k < len(alfa):
                mx[i][j] = alfa[k]
            else:
                mx[i][j] = chr(33 + k - len(alfa))
            k = k + 1
    # for _ in mx:
    #     print(*_, sep='  ')

    for b in range(0, len(code_word), 2):
        for id_j, j in enumerate(mx):
            if int(code_word[b]) == int(id_j + 1):
                for id_a, a in enumerate(j):
                    if int(code_word[b + 1]) == int(id_a + 1):
                        def_msg.append(a)
    return def_msg


# Основная часть
if int(input('Зашировать(1) или расшифровать(0)? ')) == 1:
    msg = list(input('Введите сообщение: '))
    solver = int(input('Выберите метод шифрования: '
                        '\n[0] Шифр Цезаря'
                        '\n[1] Лозунговый шифр'
                        '\n[2] Полибианский квадрат'
                        '\n'))
    if solver == 0:
        print(*cesar(alfa, msg))
    elif solver == 1:
        print(*lozung(alfa, msg))
    elif solver == 2:
        print(*polibiy(alfa, msg), sep='')
else:
    code_word = list(input('Введите шифр: '))
    solver = int(input('Выберите метод расшифровки: '
                       '\n[0] Шифр Цезаря'
                       '\n[1] Лозунговый шифр'
                       '\n[2] Полибианский квадрат'
                       '\n'))
    if solver == 0:
        print(*disCesar(alfa, code_word))
    elif solver == 1:
        print(*disLozung(alfa, code_word))
    elif solver == 2:
        print(*disPolibiy(alfa, code_word), sep='')


