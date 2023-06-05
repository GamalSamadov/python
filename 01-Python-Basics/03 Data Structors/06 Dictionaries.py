"""
--------------------------------------------------
------------------ Dictionaries ------------------
--------------------------------------------------
Dictionaries are iterable
Dictionaries are mutable and changeable
get() ==> get value from key
item() ==> get all items
key() ==> get keys
value() ==> get value

More information:
https://academy.hsoub.com/programming/python/%D9%81%D9%87%D9%85-%D8%A7%D9%84%D9%82%D9%88%D8%A7%D9%85%D9%8A%D8%B3-%D9%81%D9%8A-%D8%A8%D8%A7%D9%8A%D8%AB%D9%88%D9%86-3-r743/
https://wiki.hsoub.com/Python/dict
"""

dictionariy = {
    'id': 1,
    'title': 'Go to the store',
    'done': True
}

print(dictionariy)
print(type(dictionariy))

print(dict([('id', 1), ('title', 'Go to the store'), ('done', True)]))

task = dict(id=1, title='Go to the store', done=True)
print(task)

print(task['id'])
print(task['title'])
print(task['done'])

task = {
    'id': 1,
    'title': 'Go to the store',
    'done': True
}
task['title'] = 'Finish the home work'
task['done'] = False

print(task)

task['due_date'] = 'Today'  # Add new key
print(task)

task = {}

task['id'] = 0
task['title'] = 'Write a lesson abaut python dictionary'
task['done'] = False
task["priority"] = ['None', 'Low', 'Medium', 'Hight']
task['notes'] = {'id': 0, 'text': 'Talk abaut builtin method'}
task['due_date'] = ('Today', 'Tmorrow', 'Date')
print(task)

task_prioritiy = task['priority'][2]
print(f'Task Priority: {task_prioritiy}')

print('id' in task)
print('comment' in task)
print('notes' in task)

print(len(task))

del task['notes']
print(task)

# task.clear()
# print(task)
#
# print(task.get('title'))
# print(task.items())
# print(task.keys())
# print(task.values())

task['comment'] = 'Dictionaries are cool'
print(task.items(), 'Items')
print(task.keys())
print(task.values())

print(list(task.keys()))
print(list(task.values()))
print(list(task.items()))

task.pop('comment')
print(list(task.keys()))
print(list(task.values()))
print(list(task.items()))
print(task.get('title'))
#
#
#
#