
alfa = []
lang = -1

while lang != 1 and lang != 0:
    lang = int(input('Выберите язык eng(1) или rus(0): '))
    if lang == 1:
        for i in range(26):
            alfa.append(chr(i + 97))
    elif lang == 0:
        a = ord('а')
        alfa = [chr(i) for i in range(a, a + 6)] + \
               [chr(a + 33)] + \
               [chr(i) for i in range(a + 6, a + 32)]
        # for i in range(33):
        #     alfa.append(chr(i + 1072))


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
def antiDubl(dubl_alfa):
    uniq_alfa = []
    for i in dubl_alfa:
        if i not in uniq_alfa:
            uniq_alfa.append(i)
    return uniq_alfa


# Лозунговый шифр
def lozung(alfa, msg):
    alfa_b = antiDubl(list(input('Введите лозунг: ')))
    code_word = []
    temp_alfa = yo(sorted(list(set(alfa) - set(alfa_b))))
    alfa_b = alfa_b + temp_alfa
    # print(alfa)
    # print(alfa_b)
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


# Полибианский квадрат
def trisemus(alfa, msg):
    alfa_b = antiDubl(list(input('Введите лозунг: ')))
    code_word = []
    temp_alfa = yo(sorted(list(set(alfa) - set(alfa_b))))
    alfa_b = alfa_b + temp_alfa
    size = 0
    r = 1
    while size == 0:
        if len(alfa) <= r*r:
            size = r
        r = r + 1
    matrix = [['' for i in range(size)] for a in range(size)]
    k = 0
    for i in range(size):
        for j in range(size):
            if k < len(alfa_b):
                matrix[i][j] = alfa_b[k]
            else:
                matrix[i][j] = chr(33 + k - len(alfa_b))
            k = k + 1
    # for _ in mx:
        # print(*_, sep='  ')
    for i in msg:
        for id_j, j in enumerate(matrix):
            for id_a, a in enumerate(j):
                if i == a:
                    if id_j >= size-1:
                        code_word.append(matrix[0][id_a])
                    else:
                        code_word.append(matrix[id_j+1][id_a])
    return code_word


def disTrisemus(alfa, code_word):
    alfa_b = antiDubl(list(input('Введите лозунг: ')))
    msg = []
    temp_alfa = yo(sorted(list(set(alfa) - set(alfa_b))))
    alfa_b = alfa_b + temp_alfa
    size = 0
    r = 1
    while size == 0:
        if len(alfa) <= r*r:
            size = r
        r = r + 1
    matrix = [['' for i in range(size)] for a in range(size)]
    k = 0
    for i in range(size):
        for j in range(size):
            if k < len(alfa_b):
                matrix[i][j] = alfa_b[k]
            else:
                matrix[i][j] = chr(33 + k - len(alfa_b))
            k = k + 1
    # for _ in mx:
    #     print(*_, sep='  ')

    for i in code_word:
        for id_j, j in enumerate(matrix):
            for id_a, a in enumerate(j):
                if i == a:
                    if id_j == 0:
                        msg.append(matrix[size-1][id_a])
                    else:
                        msg.append(matrix[id_j-1][id_a])
    return msg


# Шифр Playfair
def playfair(alfa, msg):
    alfa_b = antiDubl(list(input('Введите лозунг: ')))
    symbol = input('Введите заранее оговоренный символ: ')
    code_word = []
    temp_alfa = yo(sorted(list(set(alfa) - set(alfa_b))))
    alfa_b = alfa_b + temp_alfa
    size = 0
    r = 1
    while size == 0:
        if len(alfa) <= r*r:
            size = r
        r = r + 1
    matrix = [['' for i in range(size)] for a in range(size)]
    k = 0
    for i in range(size):
        for j in range(size):
            if k < len(alfa_b):
                matrix[i][j] = alfa_b[k]
            else:
                matrix[i][j] = chr(33 + k - len(alfa_b))
            k = k + 1
    # for _ in mx:
        # print(*_, sep='  ')
    bigramma = []
    i = 0
    while i < len(msg):
    # for i in range(0, len(msg), 2):
        if i == len(msg) - 1:
            bigramma.append(msg[i])
            bigramma.append(symbol)
            break
        elif msg[i] == msg[i+1]:
            bigramma.append(msg[i])
            bigramma.append(symbol)
            bigramma.append(msg[i+1])
            bigramma.append(msg[i+2])
            i = i + 3
        else:
            bigramma.append(msg[i])
            bigramma.append(msg[i+1])
            i = i + 2
    print(bigramma)

    for id_char in range(0, len(bigramma), 2):
        for id_i, i in enumerate(matrix):
            for id_j, j in enumerate(i):
                if bigramma[id_char] == j:
                    temp_i = id_i
                    temp_j = id_j
        for id_i, i in enumerate(matrix):
            for id_j, j in enumerate(i):
                if bigramma[id_char+1] == j:
                    if temp_i == id_i:
                        if temp_j == size-1:
                            code_word.append(matrix[temp_i][0])
                            code_word.append(matrix[id_i][id_j+1])
                        elif id_j == size-1:
                            code_word.append(matrix[temp_i][temp_j+1])
                            code_word.append(matrix[id_i][0])
                        else:
                            code_word.append(matrix[temp_i][temp_j+1])
                            code_word.append(matrix[id_i][id_j+1])
                    elif temp_j == id_j:
                        if temp_i == size-1:
                            code_word.append(matrix[0][temp_j])
                            code_word.append(matrix[id_i+1][id_j])
                        elif id_i == size-1:
                            code_word.append(matrix[temp_i+1][temp_j])
                            code_word.append(matrix[0][id_j])
                        else:
                            code_word.append(matrix[temp_i+1][temp_j])
                            code_word.append(matrix[id_i+1][id_j])
                    else:
                        code_word.append(matrix[temp_i][id_j])
                        code_word.append(matrix[id_i][temp_j])
                    break
    return code_word


def disPlayfair(alfa, code_word):
    alfa_b = antiDubl(list(input('Введите лозунг: ')))
    symbol = input('Введите заранее оговоренный символ: ')
    msg = []
    temp_alfa = yo(sorted(list(set(alfa) - set(alfa_b))))
    alfa_b = alfa_b + temp_alfa
    size = 0
    r = 1
    while size == 0:
        if len(alfa) <= r*r:
            size = r
        r = r + 1
    matrix = [['' for i in range(size)] for a in range(size)]
    k = 0
    for i in range(size):
        for j in range(size):
            if k < len(alfa_b):
                matrix[i][j] = alfa_b[k]
            else:
                matrix[i][j] = chr(33 + k - len(alfa_b))
            k = k + 1

    bigramma = []
    for id_char in range(0, len(code_word), 2):
        for id_i, i in enumerate(matrix):
            for id_j, j in enumerate(i):
                if code_word[id_char] == j:
                    temp_i = id_i
                    temp_j = id_j
        for id_i, i in enumerate(matrix):
            for id_j, j in enumerate(i):
                if code_word[id_char+1] == j:
                    if temp_i == id_i:
                        if temp_j == 0:
                            bigramma.append(matrix[temp_i][size-1])
                            bigramma.append(matrix[id_i][id_j-1])
                        elif id_j == 0:
                            bigramma.append(matrix[temp_i][temp_j-1])
                            bigramma.append(matrix[id_i][size-1])
                        else:
                            bigramma.append(matrix[temp_i][temp_j-1])
                            bigramma.append(matrix[id_i][id_j-1])
                    elif temp_j == id_j:
                        if temp_i == 0:
                            bigramma.append(matrix[size-1][temp_j])
                            bigramma.append(matrix[id_i-1][id_j])
                        elif id_i == 0:
                            bigramma.append(matrix[temp_i-1][temp_j])
                            bigramma.append(matrix[size-1][id_j])
                        else:
                            bigramma.append(matrix[temp_i-1][temp_j])
                            bigramma.append(matrix[id_i-1][id_j])
                    else:
                        bigramma.append(matrix[temp_i][id_j])
                        bigramma.append(matrix[id_i][temp_j])
                    break
    for i in bigramma:
        if symbol != i:
            msg.append(i)
    return msg


# Magic Box
def m_b():
    matrix = [
         [7, 12, 1, 14],
         [2, 13, 8, 11],
         [16, 3, 10, 5],
         [9, 6, 15, 4]
    ]
    # matrix = [
    #     [1, 15, 14, 4],
    #     [12, 6, 7, 9],
    #     [8, 10, 11, 5],
    #     [13, 3, 2, 16]
    # ]
    sum_column = [0 for _ in range(4)]
    sum_row = [0 for _ in range(4)]
    sum_diag = 0
    sum_reverse = 0
    for id_i, i in enumerate(matrix):
        for id_j, j in enumerate(i):
            sum_column[id_j] = sum_column[id_j] + j
            sum_row[id_i] = sum_row[id_i] + j
        sum_diag = sum_diag + matrix[id_i][id_i]
        sum_reverse = sum_reverse + matrix[id_i][len(i)-id_i-1]
    if sum_diag == sum_reverse:
        for id_i, i in enumerate(sum_column):
            if sum_diag == i:
                if sum_row[id_i] == i:
                    request = "матрица является магическим квадратом:"
                else:
                    request = "не магический квадрат:"
    print(f'Суммы по строкам: {sum_row}\n'
          f'Суммы по столбцам: {sum_column}\n'
          f'Сумма по главной диагонали: {sum_diag}\n'
          f'Сумма по обратной диагонали: {sum_reverse}\n'
          f'Следовательно, {request}')
    return matrix


def magic_box(msg):
    code_word = [['' for i in range(4)] for _ in range(4)]
    temp_dict = {}
    matrix = m_b()
    print(*matrix, sep='\n')
    for i in range(4*4):
        if i < len(msg):
            temp_dict[i+1] = msg[i]
        else:
            temp_dict[i + 1] = '*'
    # print(temp_dict)
    for id_i, i in enumerate(matrix):
        for id_j, j in enumerate(i):
            code_word[id_i][id_j] = temp_dict[j]
    return code_word


def disMagic_box(code_word):
    msg = []
    temp_dict = {}
    matrix = m_b()
    print(*matrix, sep='\n')
    i_word = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            temp_dict[matrix[i][j]] = code_word[i_word]
            i_word = i_word + 1
    # print(temp_dict)
    for key, value in sorted(temp_dict.items()):
        if '*' != value:
            msg.append(value)
    return msg


# Шифр двойной перестановки
def double_mix(msg):
    size = 0
    i = 1
    # msg = list('методологиянауки')
    code_word = []
    while size == 0:
        if len(msg) <= i * i:
            size = i
        i = i + 1
    matrix = [['' for i in range(size)] for a in range(size)]
    col_matrix = [['' for i in range(size)] for a in range(size)]
    row_matrix = [['' for i in range(size)] for a in range(size)]
    k = 0
    route = int(input('Маршрут вписывания по строкам(1), по столбцам(0): '))
    if route == 1:
        for i in range(size):
            for j in range(size):
                if k < len(alfa):
                    matrix[i][j] = msg[k]
                else:
                    matrix[i][j] = '*'
                k = k + 1
    elif route == 0:
        for i in range(size):
            for j in range(size):
                if k < len(alfa):
                    matrix[j][i] = msg[k]
                else:
                    matrix[j][i] = '*'
                k = k + 1
    seq_column = list(input('Введите порядок перестановки столбцов: '))
    seq_row = list(input('Введите порядок перестановки строк: '))
    for i in range(size):
        for j in range(size):
            col_matrix[i][j] = matrix[i][int(seq_column[j])-1]

    for i in range(size):
        for j in range(size):
            row_matrix[i][j] = col_matrix[int(seq_row[i])-1][j]

    route_read = int(input('Маршрут считывания по строкам(1), по столбцам(0): '))
    if route_read == 1:
        for i in row_matrix:
            for j in i:
                code_word.append(j)
    else:
        for id_i, i in enumerate(row_matrix):
            for id_j, j in enumerate(i):
                code_word.append(row_matrix[id_j][id_i])
    print('Матрица с перестановкой столбцов: ')
    print(*col_matrix, sep='\n')
    print('Матрица с перестановкой столбцов и строк: ')
    print(*row_matrix, sep='\n')
    # print(*matrix, sep='\n')
    return code_word


def disDouble_mix(code_word):
    size = int(len(code_word)**(.5))
    # msg = list('методологиянауки')
    msg = []
    matrix = [['' for i in range(size)] for a in range(size)]
    col_matrix = [['' for i in range(size)] for a in range(size)]
    row_matrix = [['' for i in range(size)] for a in range(size)]

    route_read = int(input('Маршрут считывания по строкам(1), по столбцам(0): '))
    k = 0
    if route_read == 1:
        for i in range(size):
            for j in range(size):
                if k < len(alfa):
                    row_matrix[i][j] = code_word[k]
                else:
                    row_matrix[i][j] = '*'
                k = k + 1
    elif route_read == 0:
        for i in range(size):
            for j in range(size):
                if k < len(alfa):
                    row_matrix[j][i] = code_word[k]
                else:
                    row_matrix[j][i] = '*'
                k = k + 1

    seq_row = list(input('Введите порядок перестановки строк: '))
    seq_column = list(input('Введите порядок перестановки столбцов: '))
    for i in range(size):
        for j in range(size):
            col_matrix[int(seq_row[i])-1][j] = row_matrix[i][j]

    for i in range(size):
        for j in range(size):
            matrix[i][int(seq_column[j])-1] = col_matrix[i][j]

    route = int(input('Маршрут вписывания по строкам(1), по столбцам(0): '))
    if route == 1:
        for i in matrix:
            for j in i:
                msg.append(j)
    else:
        for id_i, i in enumerate(matrix):
            for id_j, j in enumerate(i):
                msg.append(matrix[id_j][id_i])

    print('Матрица с перестановкой столбцов и строк: ')
    print(*row_matrix, sep='\n')
    print('Матрица с перестановкой столбцов: ')
    print(*col_matrix, sep='\n')
    # print(*matrix, sep='\n')
    return msg


# Основная часть
if int(input('Зашировать(1) или расшифровать(0)? ')) == 1:
    msg = list(input('Введите сообщение: '))
    solver = int(input('Выберите метод шифрования: '
                        '\n[0] Шифр Цезаря'
                        '\n[1] Лозунговый шифр'
                        '\n[2] Полибианский квадрат'
                        '\n[3] Шифр Трисемуса'
                        '\n[4] Шифр Playfair'
                        '\n[8] Шифр двойной перестановки'
                        '\n[9] Magic Box'
                        '\n'))
    if solver == 0:
        print(*cesar(alfa, msg))
    elif solver == 1:
        print(*lozung(alfa, msg))
    elif solver == 2:
        print(*polibiy(alfa, msg), sep='')
    elif solver == 3:
        print(*trisemus(alfa, msg), sep='')
    elif solver == 4:
        print(*playfair(alfa, msg), sep='')
    elif solver == 8:
        print(*double_mix(msg), sep='')
    elif solver == 9:
        mb = magic_box(msg)
        for _ in mb:
            print(*_, sep='', end='')
        # print(*magic_box(msg), sep='\n')
else:
    code_word = list(input('Введите шифр: '))
    solver = int(input('Выберите метод расшифровки: '
                       '\n[0] Шифр Цезаря'
                       '\n[1] Лозунговый шифр'
                       '\n[2] Полибианский квадрат'
                       '\n[3] Шифр Трисемуса'
                       '\n[4] Шифр Playfair'
                       '\n[8] Шифр двойной перестановки'
                       '\n[9] Magic Box'
                       '\n'))
    if solver == 0:
        print(*disCesar(alfa, code_word))
    elif solver == 1:
        print(*disLozung(alfa, code_word))
    elif solver == 2:
        print(*disPolibiy(alfa, code_word), sep='')
    elif solver == 3:
        print(*disTrisemus(alfa, code_word), sep='')
    elif solver == 4:
        print(*disPlayfair(alfa, code_word), sep='')
    elif solver == 8:
        print(*disDouble_mix(code_word), sep='')
    elif solver == 9:
        print(*disMagic_box(code_word), sep='')


