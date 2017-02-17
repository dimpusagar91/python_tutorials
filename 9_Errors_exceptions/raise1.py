def mistake(name):
    if 1 < 2:
        raise Exception(name + " caused exception")

# Call method.
mistake("hello Python")
