from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from collections import defaultdict

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
for contact in contacts_list:
  contacts_splitted=(' '.join(contact[:3])).split(" ")
  contacts_splitted = [i for i in contacts_splitted if i]
  contact[0] = contacts_splitted[0]
  contact[1] = contacts_splitted[1]
  if len(contacts_splitted) == 3:
    contact[2] = contacts_splitted[2]
  pattern=r"(8|\+7)[-\s]?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})$"
  substitution=r"+7(\2)\3-\4-\5"
  pattern_dob=r"(8|\+7)[-\s]?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})[-\s]\(?доб.[-\s](\d+)\)?"
  substitution_dob=r"+7(\2)\3-\4-\5 доб.\6"
  result = re.sub(pattern, substitution, contact[5])
  result_dob = re.sub(pattern_dob, substitution_dob, result)
  contact[5]=result_dob


data = defaultdict(list)

for info in contacts_list:
  key = tuple(info[:2])
  for item in info:
    if item not in data[key]:
      data[key].append(item)

new_contact_list = list(data.values())
pprint(new_contact_list)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contact_list)