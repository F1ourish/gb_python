import os
import shutil

pr_name = 'my_project'

try:
    for root, dirs, files in os.walk(pr_name):
        if 'templates' in dirs and root != pr_name:
            for entry in os.listdir(os.path.join(root, 'templates')):
                shutil.copytree(os.path.join(root, 'templates', entry),
                                os.path.join(pr_name, 'templates', os.path.basename(root)))

except FileExistsError:
    print('Папка уже существует')
