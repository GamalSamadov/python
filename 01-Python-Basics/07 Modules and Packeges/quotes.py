from random import choice

quotes_list = [
    'For every complex problem there is an answer that is clear, simple, and wrong',
    "You can't be succsessful in buisnes whitout taking risk. It's really that simple",
    "Only great minds can afford a simple style"
]

def get_quotes():
    return '\n'.join(quotes_list)


def add_quote(quote):
    if isinstance(quote, str):
        quotes_list.append(quote)
    else:
        return 'The quote must be str'

def get_random_quote():
    return choice(quotes_list)


if __name__ == '__main__':
    print(get_random_quote())

    add_quote('You only live once, but if you do it right, once is enough')

    print(get_quotes())