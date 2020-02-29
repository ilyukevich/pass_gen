# coding=utf-8
# simply
# in the process
# enumeration of all possible combinations from 4 lists:

import random

class Db(object):

    def __init__(self, unit):
        self.unit = unit
        self.create = unit * 4

    #in the process
    def __str__(self):
        pass

    # def meth_create(self):
    #     forbidden_symbols = ["%", "`", " ", ".", ","]
    #     self.create = self.unit - 1
    #     #print("Warning: ", self.name)
    #     self.list = []
    #     for i in range(self.unit):
    #         n = input(">>> List the characters for generating the password in the list:" )
    #         print("You have characters for this list:", self.create)
    #         if n not in forbidden_symbols:
    #             self.list.append(n)
    #         else:
    #             print("Unacceptable symbols!")
    #             self.unit += 1
    #         self.create -= 1
    #     return self.list
    
        def meth_create(self):
        forbidden_symbols = ["%", "`", " ", ".", ","]
        self.create = self.unit - 1
        self.list = []
        while self.unit != 0:
            n = input(">>> List the characters for generating the password in the list:" )
            print("You have characters for this list:", self.create)
            if n not in forbidden_symbols:
                self.list.append(n)
                self.unit -= 1
                self.create -= 1
            else:
                print("Unacceptable symbols!")
            if self.create <= 0:
                self.create = 0
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
    
    #in the process
    def meth_pswd(self):
        passw = random.choice(self.list5)
        return passw

def ask(question, list_gen):
    response = None
    while response not in ("yes", "no"):
        response = input(question).lower()
        if response == "yes":
            print()
            #print(list_gen)
            choice = random.choice(list_gen)
            print("Your randomly selected password:")
            print("< ", choice, " >")
        elif response == "no":
            print("Bye. Good luck.")
        else:
            print("The answer is 'yes' or 'no'. Try again!")

def main():
    print()
    print("\tUser character password program")
    print()
    unit = int(input(">>> The number of characters in each list?: "))
    db1 = Db(unit)
    db2 = Db(unit)
    db3 = Db(unit)
    db4 = Db(unit)
    print("\tGenerate the first list of characters:")
    l1 = db1.meth_create()
    print("\tGenerate the second list of characters: ")
    l2 = db2.meth_create()
    print("\tGenerate the third list of characters:")
    l3 = db3.meth_create()
    print("\tGenerate the fourth list of characters:")
    l4 = db4.meth_create()
    print()
    print("All possible combinations of the characters that you entered are generated:")
    list_gen = db1.meth_generation(l1, l2, l3, l4)
    print(list_gen)
    ask(">>> Want to choose a random password from the generated combinations? (yes/no) : ", list_gen)

main()
