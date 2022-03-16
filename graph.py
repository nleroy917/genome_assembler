
class Graph:
    def __init__(self, *args):
        '''Create a directed graph from either a file or from a dictionary.

        This function accepts a filename or a dictionary as input. When a 
        filename is provided it expects the file to have a particular format. 
        The first line in the file should be something like
            Digraph {
        and the last line in the file should be 
            }
        Besides that, each row in the file encodes an edge. For example,
            A -> B
        denotes a directed edge from a node labeled 'A' to a node labeled 'B'

        When a dictionary is provided, it assumes that each node is key and its 
        values in the dictionary denotes all outgoing edges from the node. For
        example, the graph encoded by following python dictionary
            X = {"A":{"B":1}, "B":{"C":1}}

        has two edges A->B and B->C
        '''
        self.edges = {}

        if isinstance(args[0], dict):
            # the graph is provided as a python dictionary
            edges = args[0]
            for n1,n2s in edges.items():
                for n2,_ in n2s.items():
                    if n1 not in self.edges:
                        self.edges[n1] = {}
                    if n2 not in self.edges:
                        self.edges[n2] = {}
                    self.edges[n1][n2] = 1
        else:
            # the graph should be read from a file
            with open(args[0], 'r') as f:
                line = f.readline()
                assert line.startswith("Digraph ")
            
                for line in f:
                    if line.startswith("}"): break
                    n1, _, n2 = line.strip().split()
                    if n1 not in self.edges: 
                        self.edges[n1] = {}
                    if n2 not in self.nodes():
                        self.edges[n2] = {}
                    self.edges[n1][n2] = 1

    def nodes(self):
        '''Return a list of nodes in the graph.'''
        return self.edges.keys()

    def add_node(self, name):
        '''Add a node to the graph.

        This function expects that the node to be added does not exist in 
        the graph. An assert checks for that and will fail if the node exists
        '''
        assert name not in self.edges
        self.edges[name] = {}

    def add_edge(self, n1, n2):
        '''Add a directed edge from n1 to n2 in the graph.
        
        This function expects that the edge to be added does not exist in
        the graph. An assert checks for that and will fail if the edge is found
        before it is added
        '''
        assert n1 in self.edges and n2 not in self.edges[n1]
        self.edges[n1][n2] = 1

    def has_edge(self, n1, n2):
        '''Return True if an edge exists between n1 and n2.'''
        if n1 in self.edges and n2 in self.edges[n1]:
            return True
        return False

    def delete_edge(self, n1, n2):
        '''Delete the edge between n1 and n2.

        This function expects that the edge to be deleted exists. An assert
        checks for that and will fail if the edge is not found before deleting
        '''
        assert self.has_edge(n1, n2)
        del self.edges[n1][n2]

    def __eq__(self, other):
        '''The == operator for this class.

         To be equal:
           all node in one graph should be in the other AND
           all edges in one graph should be in the other 
        '''
        for n1, n2s in self.edges.items():
            if n1 not in other.edges.keys():
                return False
            for n2 in n2s:
                if n2 not in other.edges[n1]:
                    return False
        return True

    def __str__(self):
        '''String representation of the graph.
        '''
        string_repr = "Digraph G {\n"
        for n1,n2s in self.edges.items():
            for n2 in n2s:
                string_repr += f"\t{n1} -> {n2}\n"
        string_repr += "}"
        return string_repr
    
    def __repr__(self):
        '''memory representation of the graph.
        '''
        string_repr = "Digraph " + f"{self.__name__}" + "\{\n"
        for n1,n2s in self.edges.items():
            for n2 in n2s:
                string_repr += f"\t{n1} -> {n2}\n"
        string_repr += "}"
        return string_repr
