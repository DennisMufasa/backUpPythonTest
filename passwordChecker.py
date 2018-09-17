import re

# a program that checks passwords for A-Z a-z 0-9 #$@.
def passCheck(*args):
    if len(args) > 1 and len(args) != 0:
        newArgs = []
        for i in args:
            # if len(i) < 13 and len(i) > 5:
            if 5 < len(i) < 13:  # checking password length
                if re.search(r'[A-Z]', i):  # checking password for uppercase letters
                    if re.search(r'[a-z]', i):   # checking for lowercase
                        if re.search(r'[0-9]', i):   # checking for numerals
                            if re.search(r'[$#@]', i):  # checking for special characters
                                newArgs.append(i)
        return ', '.join(newArgs)  # re-factored to return a string

    else:
        password = ''.join(args)
        # if len(password) < 13 and len(password) > 5:
        if 5 < len(password) < 13:  # checking password length
            if re.search(r'[A-Z]', password):  # checking password for uppercase letters
                if re.search(r'[A-Z]', password):   # checking for lowercase
                    if re.search(r'[0-9]', password):   # checking for numerals
                        if re.search(r'[$#@]', password):  # checking for special characters
                            return password




