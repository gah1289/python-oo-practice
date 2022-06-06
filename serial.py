"""Python serial number generator."""

from tkinter import N
from tracemalloc import start


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        '''Set the start value'''
        self.start=self.next=start


    def generate(self):
        '''return next sequential number'''
        self.next+=1
        return self.next-1
    
    def reset(self):
        self.next=self.start
        

