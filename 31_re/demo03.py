

import re
line = "He is a German called Mayer."
if re.search("M[aeq][iy]er",line):
    print("I found one!")
else:
    print("I found nothing..!!")
 
