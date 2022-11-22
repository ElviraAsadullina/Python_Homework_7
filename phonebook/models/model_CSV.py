# ['id', 'first_name', 'last_name', 'patronymic', 'birt#hday', 'phone_person', 'phone_work', 'email', 'group', 'city'])
import csv
from gb_groupwork.phonebook import view
from gb_groupwork.phonebook.controller import DB_PATH, DB_CSV_NAME
import os



class CSV_model:
    def __init__(self):
        self.DB_CSV_PATH_FULL = DB_PATH + DB_CSV_NAME + '.csv'

    def checkDB(self):
        if os.path.exists(self.DB_CSV_PATH_FULL) == True:
            view.showInfo('blue', 'Файл БД НАЙДЕН')
        else:
            view.showInfo('blue', 'Файл БД НЕ НАЙДЕН, БУДЕТ СОЗДАНА БД')
            self.set_CSV_CreateDB()


    def getReadyDict(self):
        some_header = ['id', 'first_name', 'last_name', 'patronymic', 'phone_person', 'phone_work', 'email', 'group', 'city']
        some_data = []
        for i in some_header:
            j = input(f'Введите {i}: ')
            some_data.append(j)
            if len(some_data) == len(some_header):
                break
        return some_data



    def set_NewContact(self):
        data = self.getReadyDict()
        self.set_WriteFile(data)
        view.showInfo('green', 'Контакт успешно записан!')

    def exceptValueError(self):
        while True:
            try:
                col = input(f'Введите параметр поиска контакта: ')
                if not col in self.show_CSV_Column():
                    raise ValueError
            except ValueError:
                view.showInfo('red', 'ОШИБКА! Неверно введенный параметр!')
                continue
            return col

    def show_CSV_Column(self):
        with open(self.DB_CSV_PATH_FULL, 'r', encoding='UTF8') as f:
            reader = csv.DictReader(f)
            return reader.fieldnames

    # show_CSV_Column()

    def show_PhoneBook_all(self):
        view.showInfo('white', 'СПИСОК КОНТАКТОВ: ')
        with open(self.DB_CSV_PATH_FULL, 'r', encoding='UTF8', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                view.showInfo('white', ' '.join(row))


    def get_FoundContact(self):
        column = self.exceptValueError()
        result = input(f'Введите {column} для поиска: ')
        filtered_rows = []
        with open(self.DB_CSV_PATH_FULL, 'r', encoding='UTF8') as f:
            reader = csv.reader(f)
            filtered_rows = [row for idx, row in enumerate(reader) if str(idx) == result]
            if not filtered_rows:
                view.showInfo('red', f'Контакт с {column} = "{result}" не найден')
            else:
                view.showInfo('white', 'НАЙДЕНЫ КОНТАКТЫ: ')
                view.showInfo('white', ' '.join(*filtered_rows))

    def get_DeleteContact(self):
        self.show_PhoneBook_all()
        view.inputStr('РЕЖИМ УДАЛЕНИЯ КОНТАКТА')
        field = view.inputStr('Введите ID контакта: ')
        with open(self.DB_CSV_PATH_FULL, 'r+', encoding='UTF8', newline='') as in_file:
            reader = csv.reader(in_file)
            rows = [row for row in csv.reader(in_file) if field not in row]
            in_file.seek(0)
            in_file.truncate()
            writer = csv.writer(in_file)
            writer.writerows(rows)
            view.showInfo('green', f'Выбранный контакт с ID "{field}" удалён!')

    def set_WriteFile(self, fields):
        with open(self.DB_CSV_PATH_FULL, 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
