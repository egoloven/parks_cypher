import math

from os import stat
from Pyro4 import expose

class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.workers = workers

    def solve(self):
        words = self.read_input()
        keyword = words[0]
        words = words[1:]

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        letter2number = {v: k for k,v in enumerate(letters)}


        table = [[(j + i) % len(letters) for j in range(len(letters))] for i in range(len(letters))]


        n = len(words)
        step = n / len(self.workers)

        cyphered = []
        for i in xrange(0, len(self.workers)):
            cyphered.append(self.workers[i].cypher(i * step, (i + 1) * step, words, keyword, table, letters, letter2number))

        reduced = self.myreduce(cyphered)
        self.write_output(reduced)

    @staticmethod
    @expose
    def cypher(a, b, words, keyword, table, letters, letter2number):
        print(a, b)
        res = []
        for i in xrange(a, b):
            word = words[i]
            while len(word) > len(keyword):
                keyword += keyword

            cyp_word = ''

            for n, letter in enumerate(word):
                cyp_word += letters[table[letter2number[keyword[n]]][letter2number[letter]]]
            res.append(cyp_word)

        return res

    @staticmethod
    @expose
    def myreduce(mapped):
        res = []
        for chunk in mapped:
            for s in chunk.value:
                res.append(s)
        
        return res

    def read_input(self):
        f = open(self.input_file_name, 'r')
        return [line.strip() for line in f.readlines()]

    def write_output(self, output):
        f = open(self.output_file_name, 'w')

        for s in output:
            f.write(str(s) + '\n')

        f.close()