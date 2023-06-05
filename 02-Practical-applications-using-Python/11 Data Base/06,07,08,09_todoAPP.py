import sqlite3
from pathlib import Path as pth

message = """----------------------------------------
----------------------------------------
--------- "a" ==> Add New Task ---------
-------- "d" ==> Delete a Task ---------
-------- "s" ==> Show All Tasks --------
-------- "u" ==> Update a Task ---------
----------- "q" ==> Quit App -----------
----------------------------------------
----------------------------------------

>>> Please choose an option: 
>>> """

user_input = input(message).strip().lower()

# Command list
commands_list = ['a', 'd', 's', 'u', 'q']
user_id = 1
try:
    path = pth.home() / pth('OneDrive', 'Desktop', 'Curces', 'Hsoub Academy',
                            'The Code', '02 Practical applications using Python', '11 Data Base')
    sqLiteConnection = sqlite3.connect(path / 'todoApp.db')
    crsr = sqLiteConnection.cursor()
except:
    print('>>> Connection Error!')

finally:
    if sqLiteConnection:
        sqlCommand = """CREATE TABLE if not exists tasks(
                        user_id INTEGER, 
                        task_name VARCHAR(20),
                        description TEXT)"""
        crsr.execute(sqlCommand)


        def show_tasks():
            crsr.execute(f"SELECT * FROM tasks WHERE user_id='{user_id}'")
            result = crsr.fetchall()
            print(f'>>> You have {len(result)} tasks.')
            if len(result) > 0:
                for task in result:
                    print(f">>> Task Name: {task[1]} And", end=' ')
                    print(f"Task Description: {task[2]}")
            sqLiteConnection.commit()


        def add_task():
            task_name = input('>>> Write Task Name: ').strip()
            des = input(">>> Enter the task description: ").strip()
            crsr.execute(
                f'''INSERT INTO tasks (user_id, task_name, description) VALUES ('{user_id}', '{task_name}', '{des}')''')
            sqLiteConnection.commit()


        def delete_task():
            task_name = input('>>> Write Task Name: ').strip()
            crsr.execute(f"DELETE FROM tasks WHERE task_name='{task_name}' and user_id='{user_id}'")
            sqLiteConnection.commit()


        def update_task():
            task_name = input('>>> Write Task Name: ').strip()
            crsr.execute(f"SELECT * FROM tasks WHERE task_name = '{task_name}' AND user_id='{user_id}'")
            result = crsr.fetchall()

            if not result:
                print('>>> There is no tasks with this name')
            else:
                des = input(">>> Enter a new task description: ").strip()
                crsr.execute(
                    f"UPDATE tasks SET description = '{des}' WHERE task_name= '{task_name}' AND user_id='{user_id}'")
                sqLiteConnection.commit()

        def end_app():
            print('>>> The app is closed!')
            exit()


        if user_input in commands_list:
            if user_input == 's':
                show_tasks()
            elif user_input == 'a':
                add_task()
            elif user_input == 'd':
                delete_task()
            elif user_input == 'u':
                update_task()
            else:
                end_app()
        else:
            print('>>> Sorry this command Is Not Found!!!\n>>> Please type right command...')
    sqLiteConnection.close()
