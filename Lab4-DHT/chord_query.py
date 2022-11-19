"""
STUDENT: Antonio Santana
FILE: chord_query.py

DESCRIPTION:
    This program demonstrates chord_query takes a port number of
    an existing node and a key (any value from column 1+4 of the file).

USAGE:
    python3 chord_query.py "Node_Port_Number" "Player_Id" "year"
    python3 chord_query.py 12517 steveramsey/2523725 1970

"""
import hashlib

class ChordQuery():
    """ Performs a query. """
    def find_player(self, node_port_number, player_id, year):
        """
        Creates a key from the user input.
        Player Id,Name,Position,Year
        """
        search_key = self.hash(player_id, year)
        # To find the node that stores the data, use the node’s key a sha1-hash
        # made from the string of its endpoint address IP + port number
        # node_port_number = port_number
        node_ip = "localhost"
        # node_address = f"{node_ip}{node_port_number}"
        # node_id = node_port_number - 4000
        # node’s key is a sha1-hash made from the string of its (endpoint address (IP, port number) + node_id)
        # node_key = self.hash(node_address, node_id)
        # rpc to find query the node using the node key and the data key
        # player_data_dictionary = get_data_from_node(node_ip, node_port_number, search_key)
        self.find_data(node_ip, node_port_number, search_key)

    def find_data(self, node_ip, node_port_number, search_key):
        """
        RPC to query for player data. Find data is an rpc to
        find query the node using the node key and the data key
        """
        print(f"RPC using {node_ip} {node_port_number} {search_key}")
        # Make an RPC here and remove the fake player data.
        player_data_dictionary = dict({'Player Id': 'steveramsey/2523725', 'Name': 'Ramsey, Steve', 'Position': '', 'Year': '1970', 'Team': 'New Orleans Saints', 'Games Played': '1', 'Passes Attempted': '2', 'Passes Completed': '0', 'Completion Percentage': '0.0', 'Pass Attempts Per Game': '2.0', 'Passing Yards': '0', 'Passing Yards Per Attempt': '0.0', 'Passing Yards Per Game': '0.0', 'TD Passes': '0', 'Percentage of TDs per Attempts': '0.0', 'Ints': '0', 'Int Rate': '0.0', 'Longest Pass': '--', 'Passes Longer than 20 Yards': '0', 'Passes Longer than 40 Yards': '0', 'Sacks': '0', 'Sacked Yards Lost': '0', 'Passer Rating': '39.6', 'Node Id': 8517, 'Node Port': 12517})
        print(player_data_dictionary)

    def hash(self, first_value, second_value):
        """
        Treat the first_value concatenated with the second_value
        as the key and use SHA-1 to hash it.
        """
        key = hashlib.sha1()
        key.update(f'{first_value}'.encode('ASCII'))
        key.update(f'{second_value}'.encode('ASCII'))
        return key.hexdigest()

if __name__ == '__main__':
    chord_query = ChordQuery()
    port_number = 12517
    player_id = 'steveramsey/2523725'
    year = 1970
    print("chord_query.py <Node_Port_Number> <Player_Id> <year>")
    print(f"chord_query.py {port_number} {player_id} {year} This is test data for now.\n")
    chord_query.find_player(port_number, player_id, year)
