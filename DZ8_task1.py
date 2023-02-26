# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для
# изменения и удаления данных

def inputText():
    with open('file.txt', 'a') as data:
        surname = data.write(input('Введите фамилию: '))
        data.write(' ')
        name = data.write(input('Введите имя: '))
        data.write(' ')
        fathername = data.write(input('Введите отчество: '))
        data.write(' ')
        phoneNumber = data.write(input('Введите номер телефона: '))
        data.write('\n')

def printText():
    path = 'file.txt'
    data = open('file.txt', 'r')
    for line in data:
        print(line)
    data.close()

def checkText(userInfo):
    path = 'file.txt'
    data = open('file.txt', 'r')

    for line in data.readlines():
        if userInfo in line:
            print(line)
    data.close()

def changeText(userInfo, newInfo):
    path = 'file.txt'
    file = open('file.txt', 'r')
    data = file.readlines()
    file.close()
    for i in range(len(data)):
        if userInfo in data[i]:
            data[i] = data[i].replace(userInfo, newInfo)
    file = open('file.txt', 'w')
    file.write("".join(data))
    file.close()

def deleteText(userInfo):
    path = 'file.txt'
    file = open('file.txt', 'r')
    data = file.readlines()
    file.close()
    a = []
    deleteIndex = -1
    for i in range(len(data)):
        if userInfo in data[i]:
            deleteIndex = i
            break
    if deleteIndex != -1:
        data.pop(deleteIndex)
    file = open('file.txt', 'w')
    file.write("".join(data))
    file.close()

inputText()
printText()
checkText(input('Введите данные: '))
changeText(input('Введите данные: '), input('Введите новые данные: '))
deleteText(input('Введите данные для удаления: '))