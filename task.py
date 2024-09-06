import argparse
from CRUD import create, read, update, delete, create_file


def main():
    create_file()

    parser = argparse.ArgumentParser(prog='task',
                                     description='Task tracker')

    subparsers = parser.add_subparsers(dest='command')

    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('description', type=str, help='Task descripyion')

    parser_list = subparsers.add_parser('list', help='Tasks list')
    parser_list.add_argument('status', nargs='?', 
                             choices=['all', 'not-done', 'in-progress', 'done'],
                             help='Filter')

    parser_update = subparsers.add_parser('update', help='Update description')
    parser_update.add_argument('id', type=int, help='Task ID')
    parser_update.add_argument('description', type=str, help='Task description')

    parser_mark = subparsers.add_parser('mark', help='Change status')
    parser_mark.add_argument('id', type=int, help='Task ID')
    parser_mark.add_argument('status', nargs='?',
                             choices=['not-done', 'in-progress', 'done'],
                             help='Mark')

    parser_delete = subparsers.add_parser('delete', help='Delete task')
    parser_delete.add_argument('id', type=int, help='Task ID')


    args = parser.parse_args()

    if args.command == 'add':
        create(args.description)
    elif args.command == 'list':
        if args.status == 'all':
            read(1)
        elif args.status == 'in-progress':
            read(2)
        elif args.status == 'not-done':
            read(3)
        elif args.status == 'done':
            read(4)
        else:
            print('Wrong command.')
    elif args.command == 'update':
        update(args.id, change_description=args.description)
    elif args.command == 'mark':
        if args.status == 'done':
            update(args.id, change_status=1)
        elif args.status == 'in-progress':
            update(args.id, change_status=2)
        elif args.status == 'not-done':
            update(args.id, change_status=3) 
        else:
            print('Wrong command.')
    elif args.command == 'delete':
        delete(args.id)
    else:
        print('Wrong command.')


if __name__ == '__main__':
    main()