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
def p(document_num):
    for x in documents:
        if x['number'] == document_num:
            return (x['name'])
    return "Документа с таким номером не существует"


























def s(document_num):
    for k in directories:
        if document_num in directories[k]:
            return k
    return "Документ не найден в базе"
def add_shelf():
    number = int(input("Введите номер новой полки: "))
    for i in directories:
        if i['number']==number:
            return 'Такая полка уже существует'
        else:
            directories[number] = []
            print('полка добавлена, текущий список полок ')
            for i in directories:
                print(directories[number], end=' ')
print(add_shelf())

