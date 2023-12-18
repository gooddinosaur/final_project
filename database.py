"""Read, DB, Table class"""
import csv
import os
import copy


class Read:
    """Class for reading csv files"""

    def __init__(self, filename):
        self.info = []
        self.name = filename
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def insert(self):
        """Insert info into table"""
        with open(os.path.join(self.__location__, self.name),
                  encoding="utf-8") as file:
            rows = csv.DictReader(file)
            for row in rows:
                self.info.append(dict(row))


class DB:
    """Class for database interaction"""

    def __init__(self):
        self.database = []

    def insert(self, table):
        """For insert table into database"""
        self.database.append(table)

    def remove(self, table):
        """For remove table into database"""
        self.database.remove(table)

    def search(self, table_name):
        """For search table in database"""
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None


class Table:
    """Class for table interaction"""

    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def join(self, other_table, common_key):
        """Function for joining between table and table"""
        joined_table = Table(
            self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def insert(self, new_dic):
        """Function for add new dic into a table"""
        self.table.append(new_dic)

    def update(self, user_id, key, value):
        """Function to update information in a table"""
        for i in self.table:
            user_id_key = list(i.keys())[0]
            if i[user_id_key] == user_id:
                i[key] = value

    def remove(self, user_id):
        """Function to remove dic from a table"""
        for i in self.table:
            user_id_key = list(i.keys())[0]
            if i[user_id_key] == user_id:
                self.table.remove(i)

    def filter(self, condition):
        """Function to filter table from selected input"""
        filtered_table = Table(self.table_name + '_filtered', [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def aggregate(self, function, aggregation_key):
        """Function to make function to a table"""
        temps = []
        for item1 in self.table:
            temps.append(float(item1[aggregation_key]))
        return function(temps)

    def select(self, attributes_list):
        """Function to select key in a dic in a table and
        return all dic in table with only selected key."""
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps

    def find_from_id(self, _id):
        """Function to check that input id is in a table or not."""
        for i in self.table:
            user_id_key = list(i.keys())[0]
            if i[user_id_key] == _id:
                return True
        return False

    def search(self, _id):
        """Function to return information about that input id."""
        for i in self.table:
            user_id_key = list(i.keys())[0]
            if i[user_id_key] == _id:
                return i
        return None

    def __str__(self):
        return self.table_name + ':' + str(self.table)
