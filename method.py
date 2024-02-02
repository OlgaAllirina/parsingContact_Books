import csv
import re
from pprint import pprint

PHONE = '(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
SUB_PHONE = r'+7(\3)\6-\8-\10 \12\13'


# метод для считывания информации в адресной книге
def get_info():
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


# метод для обработки данных
def parse_method(contacts_list):
    upgrade_contacts = []
    for contacts in contacts_list:
        new_contacts = []
        # приводим файл в необходимый для дальнейшей работы формат
        full_text = ",".join(contacts[:3])
        # отделяем необходимую информацию(имя, фамилию, отчество)
        full_name = re.findall(r"\w+", full_text)
        # добавили 3ий пустой столбец там, где его не было(отчество)
        while len(full_name) < 3:
            full_name.append('')
        # добавим исправленные контакты в новый список
        new_contacts += full_name
        # дополним недостающие столбцы
        new_contacts.append(contacts[3])
        new_contacts.append(contacts[4])
        # приведём телефоны к нужному формату
        phone = re.compile(PHONE)
        new_phone = phone.sub(SUB_PHONE, contacts[5])
        new_contacts.append(new_phone)
        new_contacts.append(contacts[6])
        upgrade_contacts.append(new_contacts)
    return upgrade_contacts


# метод для удаления дублирующихся контактов
def del_dupl(upgrade_contacts):
    phone_book = dict()
    for contact in upgrade_contacts:
        if contact[0] in phone_book:
            contact_value = phone_book[contact[0]]
            for i in range(len(contact_value)):
                if contact[i]:
                    contact_value[i] = contact[i]
        else:
            phone_book[contact[0]] = contact
    return list(phone_book.values())


# метод для записи нового контактного списка в файл CSV
def new_date(upgrade_contacts):
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(upgrade_contacts)

