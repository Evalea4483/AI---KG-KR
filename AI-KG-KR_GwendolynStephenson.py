import networkx as nx
import matplotlib.pyplot as plt

# Sets up the structure of the knowledge graph
class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    # add each new facts to the knowledge Graph
    def add_fact(self, subject, relation, obj):
        self.graph.add_node(subject)
        self.graph.add_node(obj)
        self.graph.add_edge(subject, obj, relation=relation)

    # return information
    def query(self, subject, relation):
        results = []
        for successor in self.graph.successors(subject):
            edge_data = self.graph.get_edge_data(subject, successor)
            if edge_data and edge_data['relation'] == relation:
                results.append(successor)
        return results
    
    def visualize(self):
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'relation')
        nx.draw(self.graph, pos, with_labels=True, node_size=700, node_color = 'skyblue', font_size = 8, font_color = 'black')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels = labels)
        plt.show()

kg = KnowledgeGraph()

kg.add_fact("James", "was_a", "Writer")
kg.add_fact("James", "died_in", "France")
kg.add_fact("James", "is_a_friend_of", "Nikki Giovanni")
kg.add_fact("Octavia", "wrote", "Science Fiction")
kg.add_fact("Octavia", "advocated_for", "Libraries")
kg.add_fact("Octavia", "is_a_friend_of", "James")

# Retrieve information 
print("Jame's friend: ", kg.query("James", "is_a_friend_of"))
print("Octavia's friend: ", kg.query("Octavia", "is_a_friend_of"))
print("Genre of books by Octavia: ", kg.query("Octavia", "wrote"))

kg.visualize()