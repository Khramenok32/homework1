import datetime
current_date = datetime.datetime.now()
current_date_1 = datetime.datetime.strftime(current_date, '%d-%m-%Y')
print(f'Сегодня: ', current_date_1)
while True:
    created_date = datetime.datetime.strptime(input("Введите дату создания заметки в формате 'ДД-ММ-ГГГГ': "), '%d-%m-%Y')
    issue_date = datetime.datetime.strptime(input("Введите дату истечения заметки в формате 'ДД-ММ-ГГГГ': "), '%d-%m-%Y')
    date_format = "%d-%m-%Y"
    created_date_1 = datetime.datetime.strftime(created_date, '%d-%m-%Y')
    issue_date_1 = datetime.datetime.strftime(issue_date, '%d-%m-%Y')
    if date_format == "%d-%m-%Y":
        print(f'Дата создания заметки: ', created_date_1)
        print(f'Дата истечения заметки: ', issue_date_1)
    delta = issue_date - current_date
    print('Дата заметки истекает через ', delta.days, 'дня(ей).')
    break
else:
    print('Введен не верный формат даты. Повторите ввод.')