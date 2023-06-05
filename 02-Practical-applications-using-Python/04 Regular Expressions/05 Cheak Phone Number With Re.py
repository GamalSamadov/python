import re

def isPhoneNumber(text):
    is_phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
    return True if is_phone else False



