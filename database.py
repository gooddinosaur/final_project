# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv
import os
import copy


class Read:
    def __init__(self, filename):
        self.info = []
        self.name = filename
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def insert(self):
        with open(os.path.join(self.__location__, self.name)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.info.append(dict(r))

# add in code for a Database class

# add in code for a Table class

# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated
