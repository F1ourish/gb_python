# ****** Задача 1 без звёздочки ******

# import os
#
# stracture = {'my_project': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}
#
# for var, val in stracture.items():
#     if not os.path.exists(var):
#         for dirs in val:
#             for i in dirs.keys():
#                 os.makedirs(os.path.join(var, i))


# ****** Задача 2 с библиотекой yaml, взял с урока на проработку, сам это задание не сделал ******

import yaml
import os

with open('config.yaml') as file:
    content = yaml.safe_load(file)


def create_path(val, prefix=''):
    for directory, paths in val.items():
        dir_path = os.path.join(prefix, directory)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(paths, dict):
            create_path(paths, dir_path)
        else:
            for i in paths:
                if isinstance(i, dict):
                    create_path(i, dir_path)
                elif isinstance(i, str):
                    with open(os.path.join(dir_path, f'{i}'), 'w') as _:
                        pass

create_path(content)