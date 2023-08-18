#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    n = 10
    while n>0:
        print(n)
        n-=1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    squaredlist = [num*num for num in int_list]
    return squaredlist


def fizzbuzz():
    # code goes here!
    for i in range(100):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%5 == 0:
            print("Buzz")
        elif i%3 == 0:
            print("Fizz")
        else:
            print(i)

# happy_new_year()
# lista = (8,5,6,3,4)
# print(square_integers(lista))
fizzbuzz()