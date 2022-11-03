class BellmanFord():
    """BellmanFord"""
    def __init__(self, graph):
        """
        Constructor.
        :param graph: the graph to traverse
        """
        self.graph = graph
        self.size = len(graph)  # number of vertices

    def shortest_paths(self, start_vertex, tolerance=0):
        """
        Find the shortest paths from start_vertex to every other vertex.
        Store each vertex's previous vertex from start_vertex.
        Also detect if there is any negative cycle and report the first one found.

        :param start_vertex: start of all paths
        :param tolerance: only if a path is more than tolerance better will be relaxed
        :return: distances, predecessors, negative-cycle
            distance:       dictionary keyed by vertex of shortest distance from start_vertex to that vertex
            predecessor:    dictionary keyed by vertex of previous vertex in shortest path from start_vertex
            negative_cycle: None if no negative cycle, otherwise an edge, (u,v), in one such cycle
        """

        distances = {}  # {key: vertex; value: shortest distance from start_vertex)
        predecessors = {}  # {key: vertex, value: prev vertex in shortest path}

        # initialize the shortest distance to infinity and previous vertex to None
        for vertex in self.graph:
            distances[vertex] = float("Inf")
            predecessors[vertex] = None

        # initialize distance from origin to itself as 0
        distances[start_vertex] = 0

        # relax all edges n - 1 times
        for i in range(self.size - 1):
            for node in self.graph:
                for neighbor in self.graph[node]:
                    edge_wt = self.graph[node][neighbor]["price"]
                    new_distance = distances[node] + edge_wt
                    # if new path is shorter than the previous distance
                    # update distance and predecessor
                    if distances[neighbor] - new_distance > tolerance:
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = node

        # check for negative cycle by running the algorithm one more time
        # if we can find any shorter path, means there is a negative cycle
        for node in self.graph:
            for neighbor in self.graph[node]:
                edge_wt = self.graph[node][neighbor]["price"]
                new_distance = distances[node] + edge_wt

                # if new path is shorter than the previous distance
                if distances[neighbor] - new_distance > tolerance:
                    # set neighbor's predecessor to node
                    predecessors[neighbor] = node

                    # calculate sum of weights of the cycle from "node -> neighbor -> ... -> node"
                    # to determine if cycle weight is negligible
                    # only report negative cycle if cycle weight is more than tolerance
                    sum_n_cycle_wt = self.calculate_cycle_weight(predecessors, node)
                    if sum_n_cycle_wt < -1 * tolerance:
                        print("\nSum of negative cycle weight is: ", sum_n_cycle_wt)
                        return distances, predecessors, (node, neighbor)
                    else:
                        print("\nSum of negative cycle weight negligible.")

        # no negative cycle found, return None
        return distances, predecessors, None

    def calculate_cycle_weight(self, predecessors, n_cycle_access_node):
        """
        Calculate the sum of weights of the negative cycle that starts at n_cycle_origin.
        :param predecessors: predecessor dictionary
        :param n_cycle_access_node: negative cycle access node
        :return: total weight of the negative cycle
        """
        total_weight = 0

        # use 2 pointers to help traverse the cycle to add weights
        curr_node = n_cycle_access_node
        prev_node = predecessors[curr_node]

        # stop looping one node prior to access node
        while prev_node != n_cycle_access_node:
            total_weight += self.graph[curr_node][prev_node]["price"]
            curr_node = prev_node
            prev_node = predecessors[curr_node]

        # add final distance between stopped node and access node to complete the cycle
        total_weight += self.graph[curr_node][prev_node]["price"]
        return -1 * total_weight
