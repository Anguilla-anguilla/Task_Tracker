import json
import os
from utils import id_auto_increment

JSON_FILE = 'tasks.json'


def create_file():
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'wt', encoding='utf-8') as file:
            json.dump([], file)


def create(description, status, created_at, updated_at):

    id = id_auto_increment(JSON_FILE)

    new_task = {'id': id,
                'description': description,
                'status': status,
                'created_at': created_at,
                'updated_at': updated_at
                }
    with open(JSON_FILE, 'rt', encoding='utf-8') as file:
        data = json.load(file)
        data.append(new_task)

    with open(JSON_FILE, 'wt', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def read():
    pass


def update():
    pass


def delete():
    pass