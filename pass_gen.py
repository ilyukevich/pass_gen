# coding=utf-8
# в процессе
# перебор всех возможных комбинаций из 4х списков:

import random

class Db(object):

    def __init__(self, unit):
        self.unit = unit
        self.create = unit * 4

    def __str__(self):
        pass


    def meth_create(self):
        forbidden_symbols = ["%", "`", " ", ".", ","]
        self.create = self.unit - 1
        self.list = []
        for i in range(self.unit):
            n = input(">>> Перечислите символы для генерации пароля в списке:" )
            print("У вас сталось символов для данного списка:", self.create)
            if n not in forbidden_symbols:
                self.list.append(n)
            else:
                print("Недопустимые символы!")
                self.unit += 1
            self.create -= 1
        return self.list

    def meth_generation(self, l1, l2, l3, l4):
        self.list1 = l1
        self.list2 = l2
        self.list3 = l3
        self.list4 = l4
        self.list5 = []
        for k in self.list1:
            for m in self.list2:
                for n in self.list3:
                    for i in self.list4:
                        self.list5.append(k + m + n + i)
        return self.list5

    def meth_pswd(self):
        passw = random.choice(self.list5)
        return passw

def ask(question, list_gen):
    response = None
    while response not in ("да", "нет"):
        response = input(question).lower()
        if response == "да":
            print()
            #print(list_gen)
            choice = random.choice(list_gen)
            print("Ваш случайно выбранный пароль:")
            print(choice)
        elif response == "нет":
            print("До свидания. Всего хорошего.")
        else:
            print("Ответ 'да' или 'нет'. Попробуйте еще раз!")

def main():
    print()
    print("\tПрограмма генерации пароля из пользовательских символов")
    print()
    unit = int(input(">>> Количество символов в каждом списке?: "))
    db1 = Db(unit)
    db2 = Db(unit)
    db3 = Db(unit)
    db4 = Db(unit)
    print("\tГенерируем первый список символов:")
    l1 = db1.meth_create()
    print("\tГенерируем второй список символов: ")
    l2 = db2.meth_create()
    print("\tГенерируем третий список символов:")
    l3 = db3.meth_create()
    print("\tГенерируем четвертый список символов:")
    l4 = db4.meth_create()
    print()
    print("Выведены все возможные комбинации из ваших символов:")
    list_gen = db1.meth_generation(l1, l2, l3, l4)
    print(list_gen)
    ask(">>> Хотите выбрать случайный пароль из сформированных комбинаций? (да/нет) : ", list_gen)

main()
