#!/usr/bin/python

#A manager returned by Manager() will support types list, dict, Namespace
#Locl,Rlock,Semaphore, BoundedSemaphore, Condition,Event, Barrier,
#Queue, Value and Array

from multiprocessing import Process, Manager


def display(dictionaryObj,listObj):
    dictionaryObj[1] = '1'
    dictionaryObj['2'] = 2
    dictionaryObj[0.25] = None
    listObj.reverse()
    print("Dictionary  :", dictionaryObj)
    print("List        :", listObj)

if __name__ == '__main__':
    with Manager() as manager:
        dictionaryObj = manager.dict()
        listObj = manager.list(range(10))

        # process objects represent activity that is run in a sperate process
        processObj = Process( target=display, args=(dictionaryObj, listObj))

        # start the process's activity
        processObj.start()

        # block until all items in the queue have been processsed
        processObj.join()

