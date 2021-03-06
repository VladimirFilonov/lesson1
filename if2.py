"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def str_an(str1, str2):
    res = 0
    if  type(str1) == str and type(str2) == str:
        if len(str1) == len(str2):
            res = 1
        elif str2 == 'learn':
            res = 3
        elif len(str1) > len(str2):
            res = 2
        else:
            res = 4

    return res

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    """
    print (str_an(1, 'gfgfg'))
    print(str_an('gfgfg', 'gfgfg'))
    print(str_an('gfgfgkdsk', 'gfgfg'))
    print(str_an('gfgfgkdsk', 'learn'))
    print(str_an('gfg', 'gfgfg'))
if __name__ == "__main__":
    main()
