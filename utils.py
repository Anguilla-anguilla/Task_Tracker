import json


def id_auto_increment(json_file):
    with open(json_file, 'rt', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []

        if len(data) == 0:
            return 1
        else:
            last_id = data[-1]['id']
            id = int(last_id) + 1
            return id


def print_pattern(id, description, status, created_at, updated_at):
    print(f'{id}. {description}. - {status}')
    print(f'Created at: {created_at}')
    print(f'Last update: {updated_at}')
