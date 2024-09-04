from time import sleep
import datetime as dt
from CRUD import create, read, update, delete, create_file


def main():
    create_file()
    while True:
        print('Main menu:')
        print('1. View tasks')
        print('2. Update task')
        print('3. Add task')
        print('4. Delete task')
        print('5. Exit')

        choice = int(input('Choose an option:'))

        if choice == 1:
            print('-View tasks')
            print('1. All tasks')
            print('2. In progress')
            print('3. Not done')
            print('4. Done')

            choice = int(input('Choose an option:'))

            if choice == 1:
                print('- All tasks:')
                sleep(5)
            
            if choice == 2:
                print('-In progress:')
                sleep(5)

            if choice == 3:
                print('-Not done:')
                sleep(5)

            if choice == 4:
                print('-Done:')
                sleep(5)

        if choice == 2:
            print('-Update task:')

        if choice == 3:
            print('-Add task:')
            description = input('Description: ')
            status = 'not done'
            created_at = dt.datetime.now().strftime('%d.%m.%Y')
            updated_at = '-'
            create(description, status, created_at, updated_at)

        if choice == 4:
            print('-Delete task:')

        if choice == 5:
            print('Thanks for using Task_Tracker!')
            break

if __name__ == '__main__':
    main()