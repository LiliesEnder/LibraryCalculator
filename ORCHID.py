import os.path
import os
from math import *
from tkinter import *
from tkinter import messagebox
import pyglet
pyglet.font.add_file('Roboto-Regular.ttf')
pyglet.font.add_file('NotoSansJP-Medium.otf')

c1 = 0
nomer = 0
koplate = 0

mas_God = []
mas_Koe = []

mas_number = []
mas_isd = []
mas_variable = []
mas_god = []
mas_stoim = []
mas_kol = []
mas_var = []
mas_cena = []
mas_del = []

summ=0
kopl = 0

#Работает с файлом

check_file = os.path.exists('KOEF.txt') # Этот блок проверяет наличие файла
if check_file == False:
    print('NO FILE')

f = open('KOEF.txt', 'r') # Открытие файла и запись построчно в переменную spisok
spisok = [line.strip() for line in f]

length = int(len(spisok)) #Считает сколько строк в списке

for i in range(length): # Формирует 2 отдельных массива: один с годом, другой с коэфициентом
    sp = spisok[i]
    Goda = int(sp[:4])
    Koe = float(sp[5:])
    mas_God.append(Goda)
    mas_Koe.append(Koe)

f.close() #Закрытие файла



# Работает с окошком
root = Tk()
root.title ("ОРХИДЕЯ")
root.geometry('800x400')
#root["bg"] = "lavenderBlush2"

#C = Canvas(root, height=0, width=0)
filename = PhotoImage(file = "fon2.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

master = Frame(root) # Создание красивого большого окошечка с надписью Лилия
master["bg"] = "lavender"
master.grid(row=2, column=1, columnspan=7)



# Тут надписи над столбцами таблицы

Number = Label (master, text = '№', fg = 'gray30') # Пишет надпись "номер"
Number.config(font = ('Roboto 15 italic'), bg="lavender", width=3)

Isd = Label (master, text = 'Издательство', fg = 'gray30') # Пишет надпись "Издательство"
Isd.config(font = ('Roboto 15 italic'), bg="lavender", width=13)

God = Label (master, text = 'Год', fg = 'gray33') # Пишет надпись "Год"
God.config(font = 'Roboto 15 italic', bg="lavender", width = 8,)

Stoim = Label (master, text = 'Стоимость', fg = 'gray30') # Пишет надпись "Стоимость"
Stoim.config(font = 'Roboto 15 italic', bg="lavender", width = 10)

Kolvo = Label (master, text = 'Кол-во', fg = 'gray30') # Пишет надпись "Кол-во"
Kolvo.config(font = 'Roboto 15 italic', bg="lavender", width = 6)

Cena = Label (master, text = 'Цена', fg = 'gray30') # Пишет надпись "Цена"
Cena.config(font = 'Roboto 15 italic', bg="lavender", width = 10)

Koplate = Label (root, text = 'К ОПЛАТЕ', fg = 'gray30') # Пишет надпись "К оплате"
Koplate.config(font = ('Noto Sans JP Medium', 19), width = 20, bg="lavender")

koplate = Label (root, text = f'{kopl:.2f}', fg = 'gray30')  # поле вывода "К оплате"
koplate.config(font = ('Noto Sans JP Medium', 19),width = 20, bg="lavender")



def b1(*args): # это чтобы постоянно обновлялось поле вывода цены
    global koplate
    kopl = 0
    for i in range(len(mas_stoim)):
        isdatelstvo = mas_variable[i].get() #Это считывается издательство из строки
        if not len(mas_stoim[i].get()):
            #строка пустая
            mas_cena[i].configure(text= "0")
            continue
            
        if isdatelstvo != 'ВОЕНМЕХ': # Если издательство не ВОЕНМЕХА, то нужно считать год
            if len(mas_god[i].get()):
                try:
                    g = int(mas_god[i].get())
                except Exception as e:
                    mas_cena[i].configure(text= "0")
                    continue
            else:
                mas_cena[i].configure(text= "0")
                continue
 
        n = float(mas_var[i].get()) # это считывается количество экземпляров из строки
        try: # тут мы проверяем что стоимость меняется
            s = float(mas_stoim[i].get().replace(',', '.'))
        except Exception as e:
            mas_cena[i].configure(text= "0")
            continue
        
        if isdatelstvo == 'ВОЕНМЕХ':# это алгоритм калькулятора если ВОЕНМЕХ
            c1 = s*5
            c1 = c1*n
            mas_cena[i].configure(text= f"{c1:.2f}")
            kopl += c1
        else:# Это если не наше издетельство алгоритм калькулятора
            if g in mas_God:
                i1 = mas_God.index(g)
                i2 = mas_Koe[i1]
                c1 = s*i2
                c1=c1*n
                mas_cena[i].configure(text= f"{c1:.2f}")
                kopl += c1
            elif g<mas_God[0]: #Тут задается, что надо делать если год меньше, указанного первым в файле
                i2 = mas_Koe[0]
                c1 = s*i2
                c1=c1*n
                mas_cena[i].configure(text= f"{c1:.2f}")
                kopl += c1
            else:
                mas_cena[i].configure(text= "0")
    #koplate.delete(0, END)
    #koplate.insert(0, str(kopl))
    koplate.configure(text = f'{kopl:.2f}')
def udal(event):
    global mas_number, mas_isd, mas_god, mas_stoim, mas_kol, mas_cena, mas_del, mas_var, mas_variable, nomer
    but2 = event.widget
    k = None
    for i in range(len(mas_del)):
        if mas_del[i] == but2:
            k = i
    for i in range(k, len(mas_del) - 1):
        mas_variable[i].set(mas_variable[i+1].get())
        mas_var[i].set(mas_var[i+1].get())
        mas_god[i].delete(0, END)
        mas_god[i].insert(0, mas_god[i+1].get())
        mas_cena[i].config(text=mas_cena[i+1].cget('text'))
        mas_stoim[i].delete(0, END)
        mas_stoim[i].insert(0, mas_stoim[i+1].get())
    mas_number[-1].destroy()
    mas_number.pop()
    mas_isd[-1].destroy()
    mas_isd.pop()
    mas_god[-1].destroy()
    mas_god.pop()
    mas_stoim[-1].destroy()
    mas_stoim.pop()
    mas_kol[-1].destroy()
    mas_kol.pop()
    mas_cena[-1].destroy()
    mas_cena.pop()
    mas_del[-1].destroy()
    mas_del.pop()
    
    mas_var.pop()
    mas_variable.pop()
    nomer -= 1
    b1()
    
def mycom(*args):
    global mas_number, mas_isd, mas_god, mas_stoim, mas_kol, mas_cena, mas_del, mas_var, mas_variable, nomer

    nomer += 1
    number1 = Label (master) # Выводит номер экземпляра
    number1.config(font = ('Noto Sans JP Medium', 16), width = 4, text = f"{nomer}",
    borderwidth=6, relief="flat", fg = 'gray25',bg="snow")
    mas_number.append(number1)
    
    OPTIONS1 = [ # Описание первой ячейки выбора: издательство
    "ВОЕНМЕХ",
    "ДРУГОЕ"
    ] 

    variable1 = StringVar(master) # Переменной будет присваиваться значение из выпадающего списка издательств
    variable1.set(OPTIONS1[0]) # default value

    isd1 = OptionMenu(master, variable1, *OPTIONS1) # Выводится список с издательством
    isd1.config(font = ('Noto Sans JP Medium', 16),width = 8, fg = 'gray25', bg="snow")
    mas_variable.append(variable1)
    mas_isd.append(isd1)
    
    god1 = Entry(master) #эта строка отвечает за поле ввода
    god1.config(font = ('Noto Sans JP Medium', 16), width = 7, borderwidth=6, relief="flat", fg = 'gray25', bg = 'snow')
    mas_god.append(god1)

    stoim1 = Entry(master) #эта строка отвечает за поле ввода
    stoim1.config(font = ('Noto Sans JP Medium', 16), width = 8, borderwidth=6, relief="flat", fg = 'gray25',
    bg = 'snow')
    mas_stoim.append(stoim1)
    
    cena1 = Label(master) # поле вывода "Цены"
    cena1.config(font = ('Noto Sans JP Medium', 19), width = 7, borderwidth=3, relief="flat", text = f"{c1:.2f}", fg = 'red4',
    bg="snow")
    mas_cena.append(cena1)
    Kol1 = [ # Описание первой ячейки выбора: Кол-во
    " 1 ",
    " 2 ",
    " 3 ",
    " 4 "
    ] 
    var1 = StringVar(master) # Переменной будет присваиваться значение из выпадающего списка количества
    var1.set(Kol1[0]) # default value
    
    kol1 = OptionMenu(master, var1, *Kol1)# Выводится список с кол-во
    kol1.config(font = ('Noto Sans JP Medium', 16),width = 2, fg = 'gray25',bg="snow")
    mas_var.append(var1)
    mas_kol.append(kol1)
    
    but1 = Button(master, text = 'Удалить') #кнопочка "удалить"
    but1.bind('<Button-1>', udal)
    but1.config(font = ('Noto Sans JP Medium', 12), width = 8, bg="honeydew2")
    mas_del.append(but1)

    # Это распаковщики
    
    number1.grid(row=len(mas_stoim) + 1,column=1)
    isd1.grid(row=len(mas_stoim) + 1,column=2)
    god1.grid(row=len(mas_stoim) + 1,column=3)
    stoim1.grid(row=len(mas_stoim) + 1,column=4)
    kol1.grid(row=len(mas_stoim) + 1,column=5)
    cena1.grid(row=len(mas_stoim) + 1,column=6)
    but1.grid(row=len(mas_stoim) + 1,column=7)

    # mas_number.append(number1)
    # mas_isd.append(variable1)
    # mas_god.append(god1)
    # mas_stoim.append(stoim1)
    # mas_kol.append(var1)
    # mas_cena.append(cena1)
    
    variable1.trace("w", b1)
    var1.trace("w", b1)



but1 = Button(root, text = 'Добавить', command = mycom) #кнопочка "Добавить"
but1.config(font = ('Noto Sans JP Medium', 12), width = 9, bg="honeydew2")


mycom()

# Это распаковщики

Number.grid(row=1,column=1)

Isd.grid(row=1,column=2)

God.grid(row=1,column=3)

Stoim.grid(row=1,column=4)

Kolvo.grid(row=1,column=5)

Cena.grid(row=1,column=6)





but1.grid(row=3,column=3)
Koplate.grid(row=3,column=1)
koplate.grid(row=3,column=2)


root.bind('<Key>', b1)
#C.grid()


master.grid()
root.mainloop()




