from argparse import ArgumentParser
from .taskController import TaskController


def main():
    parser = ArgumentParser(description='Simple CIL Task Manager')
    subparsers = parser.add_subparsers()

    # add
    add_task = subparsers.add_parser('add', help='Add the given task')
    add_task.add_argument('title', help='Title of  the task', type=str)
    add_task.add_argument(
        '-d', '--description', help='Short description of the task', type=str, default=None)
    add_task.add_argument('-s', '--start_date',
                          help='Date to begin the task', type=str, default=None)
    add_task.add_argument('-e', '--end_date',
                          help='Date to end the task', type=str, default=None)
    add_task.add_argument(
        '--done', help='Cheak whather the task is done or not', type=str, default=False)
    add_task.set_defaults(func=TaskController.add_task)

    # list
    list_tasks = subparsers.add_parser('list', help='List unifinished tasks')
    list_tasks.add_argument(
        '-a', '--all', help='List all the tasks', action='store_true')
    list_tasks.set_defaults(func=TaskController.display)

    # cheak
    check_task = subparsers.add_parser('cheak', help='Cheak the given task')
    check_task.add_argument(
        '-t', '--task', help='Number of the task to be done. If not specified, last number will be removed.', type=int)
    check_task.set_defaults(func=TaskController.check_task)

    # remove
    remove = subparsers.add_parser('remove', help='Remove a task')
    remove.add_argument(
        '-t', '--task', help='The task to be removed (Number).', type=int)
    remove.set_defaults(func=TaskController.remove)

    # reset
    reset = subparsers.add_parser('reset', help='Remove all tasks')
    reset.set_defaults(func=TaskController.reset)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
