import json
import os
import datetime as dt

from utils import id_auto_increment, print_pattern

JSON_FILE = 'tasks.json'

# status
NOT_DONE = 'NOT DONE'
DONE = 'DONE'
IN_PROGRESS = 'IN PROGRESS'


# Files
def create_file():
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'wt', encoding='utf-8') as file:
            json.dump([], file)


def delete_file():
    if os.path.exists(JSON_FILE):
        os.remove(JSON_FILE)
    else:
        print('Wrong command')


# Tasks
def create(description):

    id = id_auto_increment(JSON_FILE)
    created_at = dt.datetime.now().strftime('%d.%m.%Y')

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
        if choice == 1:
            data = json.load(file)
        if choice == 2:
            load_json = json.load(file)
            data = [item for item in load_json if item['status'] == IN_PROGRESS]
        if choice == 3:
            load_json = json.load(file)
            data = [item for item in load_json if item['status'] == NOT_DONE]
        if choice == 4:
            load_json = json.load(file)
            data = [item for item in load_json if item['status'] == DONE]

        for item in data:
            id = item['id']
            description = item['description']
            status = item['status']
            created_at = item['created_at']
            updated_at = item['updated_at']
            print_pattern(id=id,
                          description=description,
                          status=status,
                          created_at=created_at,
                          updated_at=updated_at)


def update(id, change_description=None, change_status=None):

    updated_at = dt.datetime.now().strftime('%d.%m.%Y')

    with open(JSON_FILE, 'rt', encoding='utf-8') as file:
        data = json.load(file)
        update_task = [item for item in data if item['id'] == id]
        if len(update_task) == 0:
            print('Wrong task id')
        else:
            update_task = update_task[0]
            update_task['updated_at'] = updated_at
        
            if change_status == None:
                update_task['description'] = change_description

            if change_description == None:
                if change_status == 1:
                    update_task['status'] = DONE
                if change_status == 2:
                    update_task['status'] = IN_PROGRESS
                if change_status == 3:
                    update_task['status'] = NOT_DONE

        with open(JSON_FILE, 'wt', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


def delete(id):
    with open(JSON_FILE, 'rt', encoding='utf-8') as file:
        data = json.load(file)
        delete_task = [item for item in data if item['id'] == id]
        if len(delete_task) == 0:
            print('Wrong task id')
        else:
            delete_task = delete_task[0]
            data.remove(delete_task)

    with open(JSON_FILE, 'wt', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
