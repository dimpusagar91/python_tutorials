#import pickle
import pickle

 
# write python dict to a file
mydict = {"perl":10,"python":20}

output = open('myfile.pkl', 'wb')
pickle.dump(mydict, output)
output.close()

 

# read python dict back from the file
pkl_file = open('myfile.pkl', 'rb')
mydict2 = pickle.load(pkl_file)
pkl_file.close()


print (mydict2)



