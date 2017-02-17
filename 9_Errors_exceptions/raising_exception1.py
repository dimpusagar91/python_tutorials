# Raising exception
print("\nExample program 2\n")
# The raise statement allows the programmer to
# force a specified exception to occur

# If you need to determine whether an exception was raised but don't intend to have a
# simpler form of the raise statement allows you to re-raise the exception

try:
    print("Initial statement")
    raise NameError('Hi There')
except NameError as e:
    print('An exception flew by!',e)
    raise 
