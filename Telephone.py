import os

def addContact():
    os.system('cls')
    firstName = input('Имя: ')
    secondName = input('Фамилия: ')
    telephoneNumber = input('Номер телефона: ')
    contact = '{};{};'.format(firstName, secondName)
    contacts[contact] = telephoneNumber
    telephone = open('Семинары\Справочник\Telefon.txt','a')
    for key in contacts:
        telephone.write(f'{key}{contacts[key]} \n')
    telephone.close()
    os.system('cls')
    print('Контакт добавлен\n\n')
    

def showContacts():
    os.system('cls')
    telephone = open('Семинары\Справочник\Telefon.txt','r')
    for line in telephone:
        info = list(line.split(';'))
        if len(info) == 3:
            for i  in range(0,3):
                if  i == 0:
                    print(f'Имя: {info[i]}')
                elif i == 1:
                    print(f'Фамилия: {info[i]}')
                elif i == 2:
                    print(f'Номер телефона: {info[i]}')
    telephone.close()
    print()
    print()
    os.system('pause')
    os.system('cls')

def findContact():
    os.system('cls')
    name = input('Введите имя или фамилию для поиска: ')
    
    telephone = open('Семинары\Справочник\Telefon.txt')
    for line in telephone:
        info = list(line.split(';'))
        if name.lower() == info[0].lower() or name.lower() == info[1].lower():
            print(f'Имя: {info[0]}\nФамилия: {info[1]}\nНомер телефона: {info[2]}')
            return line
    telephone.close()
    os.system('pause')
    os.system('cls')

def deleteContact():
    contact = findContact()
    numbers = list()
    telephone = open('Семинары\Справочник\Telefon.txt', 'r')
    
    for line in telephone:
        if line != contact:
            numbers.append(line)
    telephone.close()
    telephone = open('Семинары\Справочник\Telefon.txt', 'w')
    for i in numbers:
        telephone.write(i + '\n')
    telephone.close()
    print('Контакт удалён')
    os.system('pause')
    os.system('cls')

run = True
while(run):
    contacts = {}
    print('Главное меню: ')
    print('1. Добавить контакт')
    print('2. Найти контакт')
    print('3. Удалить контакт')
    print('4. Показать список контактов')
    print('5. Закрыть справочник')
    choice = int(input('\nВыберите пункт меню(введите число): '))
    if choice == 1:
        addContact()
    elif choice == 2:
        findContact()
    elif choice == 3:
        deleteContact()
    elif choice == 5:
        run = False
    elif choice == 4:
        showContacts()