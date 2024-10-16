#Создаем матрицу как сам лабиринт, где 88 - это стены, а 0 пустота 
a = [
    [88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88],
    [88, 0,88, 0, 0, 0, 0, 0, 0,88, 0, 0, 0, 0, 0, 0, 0, 0, 0,88],
    [88, 0,88, 0,88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,88],
    [88, 0,88, 0,88,88,88,88, 0,88, 0, 0, 0, 0, 0, 0, 0, 0, 0,88],
    [88, 0,88, 0, 0, 0, 0,88, 0,88, 0, 0, 0, 0,88, 0,88,88,88,88],
    [88, 0,88,88,88,88,88,88, 0,88, 0, 0, 0, 0,88, 0, 0, 0, 0,88],# <--- Вот тут конец 
    [88, 0, 0, 0, 0, 0, 0,88, 0,88, 0, 0, 0, 0,88,88,88,88,88,88],
    [88,88,88, 0, 0, 0, 0, 0, 0,88, 0, 0, 0, 0, 0, 0, 0, 0, 0,88],
    [88,88,88, 0, 0, 0, 0, 0, 0,88, 0, 0, 0, 0, 0, 0, 0, 0, 0,88],
    [88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88],
]

# Даем начальную точку откуда и будет весь путь 
a[2][1] = 1


# эта функция делает матрицу более читаемой
def print_table(a):
    for y in a:
        for x in y:
            if len(str(x)) == 2:
                end_mark = ' '
            else:
                end_mark = '  '
            if x == "##":
                end=end_mark
            elif x == 88:
                end=end_mark
            else:
                 end=end_mark
        print()

print_table(a)
  # Эта функция самих шагов, в которой мы проверяем клетки по всем сторонам  на наличее нуля и если он есть, то возврощаем True
def step(step):
    for y in range(len(a)):
        for x in range(len(a[y])):
            if a[y][x] == step-1:              
            # Ячейка сверху 
                if a[y - 1][x] == 0: 
                    a[y -1][x] = step 
                    if x == 18 and y-1 == 5:
                        return True

            #Ячейка снизу 
                if a[y + 1][x] == 0:
                    a[y + 1][x] = step
                    if x == 18 and y+1 == 5:
                         return True

            #Ячейка слева
                if a[y][x - 1] == 0:
                    a[y][x - 1] = step
                    if x-1 == 18 and y == 5:
                        return True

            #Ячейка справа
                if a[y][x + 1] == 0:
                    a[y][x + 1] = step
                    if x+1 == 18 and y == 5:
                        return True
              # в этом цикле мы ловим значение True из функций и на месте нулей ставим число шага, который мы делаем 
for i in range(2, 100):
    if step(i) == True:
        print(f'Дошли {i}')
        break

# в этой функций мы вычисляем самый короткий путь, возврощаясь назад по пути уменшения 
def step_back(st_b):
    x = st_b[0]
    y = st_b[1]
    step_back = a[y][x]
    if a[y - 1][x] == step_back -1:
        return [x,y - 1]
    if a[y + 1 ][x] == step_back -1:
        return [x, y + 1]
    if a[y][x - 1] == step_back -1:
        return[x - 1, y]
    if a[y][x + 1] == step_back -1:
        return [x + 1 ,y]
      
path = []
st_b = [18, 5]
for i in range(31):
    path.append(st_b)
    st_b = step_back(st_b)
# переворачиваем путь и выделяем короткий путь знаками '##'
path.reverse()
for i in range(31):
    q = path[i]
    x = q[0]
    y = q[1]
    a[y][x] = '##'
print_table(a)
