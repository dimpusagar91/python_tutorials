


#Using finally to clean up after an exception



def divlog(x, y):
    try:
        f = open('C:/files/divlog.txt', 'a')
        f.write('{0:g} / {1:g} = {2:g}\n'.format(x, y, (x/y)))
    except ZeroDivisionError:
        f.write('Error: Zero division not allowed\n')
        raise
    finally:
        f.close()

divlog(100,21)
divlog(20,5)
divlog(10,0)



