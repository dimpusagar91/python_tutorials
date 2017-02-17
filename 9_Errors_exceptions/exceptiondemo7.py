
#Using finally to clean up after an exception

 
def divlog(x, y):
    try:
        f = open('C:/files/divlog.txt', 'a')
        f.write('{0}/{1} = {2}\n'.format(x, y, (x/y)))
    except ZeroDivisionError:
        f.write('Error: Zero division not allowed\n')

    finally:
        f.close()


divlog(40,20)
