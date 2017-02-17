import atexit

try:
    _count = int(open("counter").read())
except IOError:
    _count = 0

def incrcounter(n):
    global _count
    _count = _count + n

def savecounter():
    open("counter","w").write("%d" % _count)

print('Registering...')
atexit.register(savecounter)
print('Registered..')
