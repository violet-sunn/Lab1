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

def i():
    for x in documents:
        num=0
        for y in directories:
            if x['number'] in directories[y]:
                num=y
        print(f" №: {x['number']}, тип: {x['type']}, владелец: {x['name']}, полка хранения: {num}")

def ads():
    number = input("Введите номер новой полки: ")
    for i in list(directories):
        if i==number:
            return 'est'
    directories[number] = number
    print('Полка добавлена, текущий список полок ')
    print(', '.join(list(directories)), end = '')
    return '.'

def ds():
    shelf_number = input("Введите номер новой полки: ")
    if directories[shelf_number] == []:
        del directories[shelf_number]
        print('Полка удалена. Текущий перечень полок:', ', '.join(list(directories)), end = '')
    else:
        print('На полке есть', len(directories[shelf_number]), 'документа, удалите их перед удалением полки. Текущий перечень полок: ', ','.join(list(directories)), end ='')
    return '.'


while input() != 'q':
    funcs = {
        'p': p(),
        's': s(),
        'i': i(),
        'ads': ads(),
        'ds': ds()
    }