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
            print('11. All tasks')
            print('12. In progress')
            print('13. Not done')
            print('14. Done')

            choice = int(input('Choose an option:'))

            if choice == 11:
                print('-All tasks:')
                read(choice)
                sleep(5)

            if choice == 12:
                print('-In progress:')
                read(choice)
                sleep(5)

            if choice == 13:
                print('-Not done:')
                read(choice)
                sleep(5)

            if choice == 14:
                print('-Done:')
                read(choice)
                sleep(5)

        if choice == 2:
            print('-Update task:')

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