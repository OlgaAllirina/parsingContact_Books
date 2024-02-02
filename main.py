from pprint import pprint

import csv
from method import get_info, parse_method, del_dupl, new_date

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
n_list = get_info()
parse_contacts = parse_method(n_list)
del_duplicate = del_dupl(parse_contacts)
# TODO 2: сохраните получившиеся данные в другой файл
new_date(del_duplicate)






