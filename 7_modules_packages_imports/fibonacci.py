#!/usr/bin/python

def fibo(num):
    # write finonacci series up to num
    vara,varb = 0,1
    while varb < num:
        print(varb, end = ' ')
        vara , varb = varb, vara + varb
    print()

def fibolist(num):  # return fibonacci series up to num
    result = []
    vara,varb = 0,1
    while varb < num:
        result.append(varb)
        vara, varb = varb, vara + varb
    return result
