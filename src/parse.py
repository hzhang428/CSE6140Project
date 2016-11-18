import networkx as nx
import math
import csv

class parser:

    def __init__(self):
        '''
        Initialize an instance of parser.
        '''
        self.matrix = None
        self.info = {}

    def readData(self, fn):
        '''
        Loads parameters of data and a matrix of data
        '''
        f = open(fn, 'r')
        csvreader = csv.reader(f)
        for x in csvreader:
            print(x)


p = parser()
p.readData('Atlanta.tsp')
