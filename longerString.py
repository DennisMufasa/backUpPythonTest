# a function accepting 2 arguments
def longString(a, b):

    # if len(a) > len(b):
    #     return a
    # else:
    #     return b

    if len(a) == len(b):
        return a + '\n' + b
    elif len(a) > len(b):
        return a
    else:
        return b




