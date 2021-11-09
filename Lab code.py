documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}

#TASK 1

def p():
    document_num = input("Введите номер документа: ")
    for x in documents:
        if x['number'] == document_num:
            return x['name']
    return 'Документа с таким номером не существует'


def s():
    document_num = input("Введите номер документа: ")
    for k in directories:
        if document_num in directories[k]:
            return k
    return "Документ не найден в базе"


def l():
    for x in documents:
        num = 0
        for y in directories:
            if x['number'] in directories[y]:
                num = y
        print(f" №: {x['number']}, тип: {x['type']}, владелец: {x['name']}, полка хранения: {num}", end = '')
    return ''


def ads():
    number = input("Введите номер новой полки: ")
    for i in list(directories):
        if i == number:
            print ('Такая полка уже существует. Текущий перечень полок:', ','.join(list(directories)),
              end = '')
    directories[number] = number
    print('Полка добавлена, текущий список полок ')
    print(', '.join(list(directories)), end='')
    return '.'


def ds():
    shelf_number = input("Введите номер новой полки: ")
    if directories[shelf_number] == []:
        del directories[shelf_number]
        print('Полка удалена. Текущий перечень полок:', ', '.join(list(directories)), end='')
    else:
        print('На полке есть', len(directories[shelf_number]),
              'документа, удалите их перед удалением полки. Текущий перечень полок: ', ','.join(list(directories)),
              end='')
    return '.'

#TASK 2

def ad():
    if True:
        num_doc=input('Введите номер документа: ')
        typ=input('Введите тип документа: ')
        nam=input('Введите владельца документа: ')
        shelf=input('Введите полку для хранения: ')
        if shelf not in directories:
            print("Такой полки не существует. Добавьте полку командой as")
            print('Текущий список документов:\n')
            for x in documents:
                num=0
                for y in directories:
                    if x['number'] in directories[y]:
                        num=y
                print(f" №: {x['number']}, тип: {x['type']}, владелец: {x['name']}, полка хранения: {num}")
            return''
        new_dict={'type':typ, 'number':num_doc, 'name':nam}
        documents.append(new_dict)
        directories[shelf]+=[num_doc]
        print('Документ успешно добавлен!')
        print('Текущий список документов:\n')
        for x in documents:
            num=0
            for y in directories:
                if x['number'] in directories[y]:
                    num=y
            print(f" №: {x['number']}, тип: {x['type']}, владелец: {x['name']}, полка хранения: {num}")
        return''


def d():
    num = input('Введите номер документа: ')
    lenght = len(documents)
    for x in documents:
        if num in x.values():
            documents.remove(x)
            print('Успешно удалено!')
    if len(documents) == lenght:
        print('Такого документа нет')
    print('Текущий список документов:\n')
    for x in documents:
        print(f" №: {x['number']}, тип: {x['type']}, владелец: {x['name']}, полка хранения: {num}", end = '')
    return ''

def m():
    doc_num=input('Введите номер документа: ')
    shelf_num=input('Введите номер полки: ')
    if shelf_num not in directories.keys():
        return 'Такой полки не существует'
    exist=0
    for key,value in directories.items():
        if doc_num in value:
            exist+=1
            directories[shelf_num]+=[doc_num]
            value.remove(doc_num)
    if exist!=0:
        print('Документ перемещен')
        print('Текущий список документов:\n')
    else:
        print('Документ не существует')
        print('Текущий список документов:\n')
    for x in documents:
        for y in directories:
            if x['number'] in directories[y]:
                num=y
        print(f" №: {x['number']}, тип: {x['type']}, владелец: {x['name']}, полка хранения: {num}")
    return''

while True:
    command = input('Введите команду: ')
    if command == 'p':
        print(p())
    elif command == 's':
        print(s())
    elif command == 'l':
        print(l())
    elif command == 'ads':
        print(ads())
    elif command == 'ds':
        print(ds())
    elif command == 'ad':
        print(ad())
    elif command == 'd':
        print(d())
    elif command == 'm':
        print(m())
    elif command == 'q':
        break
    else:
        print('Такой команды не существует')
