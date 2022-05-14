import os
from os import listdir
from os.path import isfile, join
from lib import vars


def delete_non_cuentos_files():
    if os.path.exists(f'{vars.database_location}Cuentos/.DS_Store'):
        os.remove(f'{vars.database_location}Cuentos/.DS_Store')
    else:
        pass


def get_cuentos():
    list_cuentos = []
    counter = 0
    remove_extension = '.py'
    list_files = [f for f in listdir(f'{vars.database_location}Cuentos') if isfile(join(f'{vars.database_location}Cuentos', f))]
    list_files = sorted(list_files)
    # print(list_files)

    for item in list_files:
        counter += 1
        item = item.replace(remove_extension, '')
        dict_cuento = {counter: item}
        list_cuentos.append(dict_cuento)

    print(list_cuentos)

    return list_cuentos


def set_cuento(cuento_number, list_cuentos):
    # print(cuento_number)
    num_cuentos = len(list_cuentos) + 1
    for item in list_cuentos:
        for x in range(num_cuentos):
            try:
                if item[x] == item[cuento_number]:
                    print(f'The \"Cuento\" to read will be {item[cuento_number]}')
                else:
                    pass
            except:
                pass

