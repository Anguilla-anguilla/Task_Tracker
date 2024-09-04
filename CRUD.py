import json
import os
import pprint as pp
from utils import id_auto_increment, print_pattern

JSON_FILE = 'tasks.json'

#status
NOT_DONE = 'NOT DONE'
DONE = 'DONE'
IN_PROGRESS = 'IN PROGRESS'


def create_file():
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'wt', encoding='utf-8') as file:
            json.dump([], file)


def create(description, created_at):

    id = id_auto_increment(JSON_FILE)

    new_task = {'id': id,
                'description': description,
                'status': NOT_DONE,
                'created_at': created_at,
                'updated_at': '-',
                }
    with open(JSON_FILE, 'rt', encoding='utf-8') as file:
        data = json.load(file)
        data.append(new_task)

    with open(JSON_FILE, 'wt', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def read(choice):
    with open(JSON_FILE, 'rt', encoding='utf-8') as file:
        if choice == 11:
            data = json.load(file)
        if choice == 12:
            load_json = json.load(file)
            data = [item for item in load_json if item['status'] == IN_PROGRESS]
        if choice == 13:
            load_json = json.load(file)
            data = [item for item in load_json if item['status'] == NOT_DONE]
        if choice == 14:
            load_json = json.load(file)
            data = [item for item in load_json if item['status'] == DONE]
        for item in data:
            id = item['id']
            description = item['description']
            status = item['status']
            created_at = item['created_at']
            updated_at = item['updated_at']
            print_pattern(id,
                        description,
                        status,
                        created_at,
                        updated_at)


def update():
    pass


def delete():
    pass