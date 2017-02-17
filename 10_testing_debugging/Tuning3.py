#!/usr/bin/python

# Avoid exceptions for common cases
# Approach 1 : Perform a lookup and catch an exception

items = { "Giridhar" : 9550712233 , "Vamsi":929051001,
          "Sohan":1234598765,"Lasya":7654398763,
          "Dhruvin":9866502268,"Rao":1234567876}


key = "Giri"

import time
start_cpu = time.clock()
start_real = time.time()

try:
    value = items[key]
except KeyError:
    value = None

end_cpu = time.clock()
end_real = time.time()

tmp2 = end_cpu - start_cpu
tmp1 = end_real - start_real
print("%f Real Seconds" %(tmp1))
print("%f CPU Seconds" %(tmp2))


