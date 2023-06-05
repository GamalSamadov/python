import re

def isEmail(email):
    is_email = re.search(r'^[A-z0-9]+[\.-]?[A-z0-9]+@\w+\.\w{2,3}$', email)

    if is_email:
        print(f'The {email} is the valid Email.')
    else:
        print(f'The {email} is not the valid Email.')


email = 'hsoub.academy@gmail'
isEmail(email)