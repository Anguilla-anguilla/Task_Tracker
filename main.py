from time import sleep
import datetime as dt
from CRUD import create, read, update, delete, create_file


def main():
    create_file()
    while True:
        print('----------')
        print('Main menu:')
        print('1. View tasks')
        print('2. Update task')
        print('3. Add task')
        print('4. Delete task')
        print('5. Exit')
        print('----------')

        choice = int(input('Choose an option:'))

        if choice == 1:
            print('-View tasks')
            print('1. All tasks')
            print('2. In progress')
            print('3. Not done')
            print('4. Done')

            sub_choice_1 = int(input('Choose an option:'))

            if sub_choice_1 == 1:
                print('-All tasks:')
                read(sub_choice_1)
                sleep(5)

            if sub_choice_1 == 2:
                print('-In progress:')
                read(sub_choice_1)
                sleep(5)

            if sub_choice_1 == 3:
                print('-Not done:')
                read(sub_choice_1)
                sleep(5)

            if sub_choice_1 == 4:
                print('-Done:')
                read(sub_choice_1)
                sleep(5)

        if choice == 2:
            print('-Update task:')
            id = int(input('Enter task id: '))
            updated_at = dt.datetime.now().strftime('%d.%m.%Y')

            print('1. Update status')
            print('2. Update description')
            sub_choice_2 = int(input('Choose an option:'))

            if sub_choice_2 == 1:
                print('Set status to:')
                print('1. Done')
                print('2. In progress')
                print('3. Not done')
                change_status = int(input('Choose an option:'))
                update(id, updated_at, change_status=change_status)

            if sub_choice_2 == 2:
                change_description = input('Enter new description: ')
                update(id, updated_at, change_description=change_description)

        if choice == 3:
            print('-Add task:')
            description = input('Description: ')
            created_at = dt.datetime.now().strftime('%d.%m.%Y')
            create(description, created_at)

        if choice == 4:
            print('-Delete task:')

        if choice == 5:
            print('Thanks for using Task_Tracker!')
            break


if __name__ == '__main__':
    main()