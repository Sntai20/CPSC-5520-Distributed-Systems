"""
STUDENT: Antonio Santana
FILE: chord_populate.py

DESCRIPTION:
    This program demonstrates populates data from CSV file into network of nodes correctly.
    Support adding a new data value to the network, given (key, value) via any active node.
    Add must be efficient, make use of predecessor, successor, and finger tables as 
    appropriate using key SHA1 hash and recursive RPC.

    chord_populate takes a port number of an existing node and the filename of the data file.

USAGE:
    python3 chord_populate.py

REFERENCES:
    Read a csv file. https://docs.python.org/3/library/csv.html

"""

import csv
import hashlib
import os

class ChordPopulate:
    "Methods to interface with the data."
    def __init__(self):
        self.node_data_set_dictionary = dict()
        self.absolute_file_path = self.find_file()
        self.read_file()

    def find_file(self):
        """
        Find the files.
        Filename: Career_Stats_Passing.csv
        File path: ./Lab4-DHT/Career_Stats_Passing.csv
        Relative path: ~./repo/CPSC-5520-Distributed-Systems/Lab4-DHT/Career_Stats_Passing.csv
        """
        print(f'Current Working Directory: {os.getcwd()}')
        filename = 'Career_Stats_Passing.csv'
        absolute_file_path = f"{os.path.dirname(__file__)}/{os.path.basename(filename)}"
        print('File name :    ', os.path.basename(filename))
        print('Directory Name:     ', os.path.dirname(__file__))
        print(f"Absolute path of the {filename}:     {absolute_file_path}")
        return absolute_file_path

    def read_file(self):
        """
        Reads a file with the following fieldnames in the first row:
        Player Id,Name,Position,Year,Team,Games Played,Passes Attempted,Passes Completed,
        Completion Percentage,Pass Attempts Per Game,Passing Yards,Passing Yards Per Attempt,
        Passing Yards Per Game,TD Passes,Percentage of TDs per Attempts,Ints,Int Rate,
        Longest Pass,Passes Longer than 20 Yards,Passes Longer than 40 Yards,Sacks,
        Sacked Yards Lost,Passer Rating

        Create an object that operates like a regular reader but maps the information
        in each row to a dict whose keys are given by the optional fieldnames parameter.
        """
        with open(f"{self.absolute_file_path}", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            node_id = 0

            for row in reader:
                node_id +=1
                row['Node Id'] = node_id
                node_port_number = (node_id + 4000)
                row['Node Port'] = node_port_number
                node_key = self.hash_something(row['Player Id'], row['Year'])
                self.node_data_set_dictionary[node_key] = row

    def print_dictionary(self):
        for k, v in self.node_data_set_dictionary.items():
            print(f"Key {k} Node Id: {v['Node Id']} Node Port: {v['Node Port']} Player Id: {v['Player Id']} Year: {v['Year']}")

    def find_node(self):
        print(f'Find node d55607515a6c96f2ff50b87a62d26e5ce18e2e07 : {self.node_data_set_dictionary.get("d55607515a6c96f2ff50b87a62d26e5ce18e2e07")}')

    def hash_something(self, player_id, year):
        """
        Treat the value in the first column (playerid) concatenated
        with the fourth column (year) as the key and use SHA-1 to hash it.
        """
        key = hashlib.sha1()
        key.update(f'{player_id}'.encode('ASCII'))
        key.update(f'{year}'.encode('ASCII'))
        return key.hexdigest()
        # player_id_year = (player_id + year)
        # print(f"Sha1 Hash {key.hexdigest()} = Player Id + Year {player_id_year}")

if __name__ == '__main__':
    # Clearing the Screen
    os.system('clear')

    chord_populate = ChordPopulate()
    chord_populate.print_dictionary()
    chord_populate.find_node()
