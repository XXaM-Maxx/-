#Импортируем библиотеки дл более красивого вывода в термина и создания gif  изоброжения 
import termcolor as tc
from PIL import Image, ImageDraw

#сама матрица как лабиринт
a = [
    [88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88],
    [88, 0,88, 0, 0, 0, 0, 0, 0,88, 0, 0, 0, 0, 0, 0, 0, 0, 0,88],
    [88, 0,88, 0,88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,88],
    [88, 0,88, 0,88,88,88,88, 0,88, 0, 0, 0, 0, 0, 0, 0, 0, 0,88],
    [88, 0,88, 0, 0, 0, 0,88, 0,88, 0, 0, 0, 0,88, 0,88,88,88,88],
    [88, 0,88,88,88,88,88,88, 0,88, 0, 0, 0, 0,88, 0, 0, 0, 0,88],
    [88, 0, 0, 0, 0, 0, 0,88, 0,88, 0, 0, 0, 0,88,88,88,88,88,88],
    [88,88,88, 0, 0, 0, 0, 0, 0,88, 0, 0, 0, 0, 0, 0, 0, 0, 0,88],
    [88,88,88, 0, 0, 0, 0, 0, 0,88, 0, 0, 0, 0, 0, 0, 0, 0, 0,88],
    [88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88],
]

#Создаем пустой список для хранения изображений и задаем начальную позицию
images = []
a[2][1] = 1

#функция для отрисовки gif файла
def gif(a, path =[], i = 0):
    zoom = 25# Коэффициент масштабирования
    im = Image.new('RGB', (zoom*len(a[0]), zoom*len(a)), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.rectangle((0, 0, zoom*len(a[0]), zoom*len(a)), fill=(200, 200, 200))

    for y in range(len(a)):
        for x in range(len(a[y])):
            if a[y][x] == 88:
                draw.rectangle((zoom*x, zoom*y, zoom*x+zoom, zoom*y+zoom), fill=(0, 0, 0))
            if 0 < a[y][x] < 88:
                draw.rectangle((zoom*x+10, zoom*y+10, zoom*x+zoom-10, zoom*y+zoom-10), fill=(0, 255, 0))
    if  path != []:
        for e in range(i):
            x = path[e][0]
            y = path[e][1]
            draw.rectangle((zoom*x, zoom*y, zoom*x+zoom, zoom*y+zoom), fill=(0, 255, 0))
        
    
    images.append(im)
       
# Функция для того , что бы матрица была ровной и читаемой
def print_table(a):
    for y in a:
        for x in y:
            if len(str(x)) == 2:
                end_mark = ' '
            else:
                end_mark = '  '
            if x == "##":
                print(tc.colored(x, 'yellow'), end=end_mark)
            elif x == 88:                                           # /
                print(tc.colored(x, 'red'), end=end_mark)           #<------------ здесь мы регулируем матрицу и делаем вывод более красивым 
            else:                                                   # \
                print(tc.colored(x, 'black'), end=end_mark)
        print()

print_table(a)
         

def step(step): #сама функция шагов, которая проверяет клетки на ноличия нуля и делает шаги в "пустые" ячейки
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
for i in range(2, 100):# цикл для поиска и вывода шагов
    if step(i) == True:
        print(f'Дошли {i}')
        break
    gif(a)#функцию gif мы ставим сюда дабы gif была gif'кой

#Функция которая считает самый короткий путь назад по возврощению назад по точкам на уменшение.
#например с 31 мы переходи на 30 и так до начала 
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
      
        
path = []#Создаем пустой массив для координат обратного/короткого пути 
st_b = [18, 5]#задаем начальную точку
for i in range(31):#этот цикл нужен для того, что бы мы могли найти все координаты короткого пути 
    path.append(st_b)#добовляем в пустой массив координаты обратного пути
    st_b = step_back(st_b)

path.reverse()#переворачиваем массив для более красивого создания gif изоброжения 

#в этом цикле мы создаем gif изоброжения в нашей функций в начале 24 строка.
#если в первый вызов функций мы не передавали path и i, то мы их и не использывали, от этого функция и не дорисовывала картинку
#теперь же мы передаем эти значения и функция gif создаёт картинки и добовляет их в нашу gif'ку
for i in range(31):
    gif(a, path, i)# path это массив координат обратного пути, i это номер пути

for i in range(31):#здесь мы в терминале обозночаем самый короткий путь за ##
    q = path[i]
    x = q[0]
    y = q[1]
    a[y][x] = '##'

print_table(a)

images[0].save('file11.gif', save_all=True, append_images=images[1:], optimize=False, duration=1, loop=1)#сохроняем все картинки в одну gif'ку