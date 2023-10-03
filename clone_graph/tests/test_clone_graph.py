import unittest

from clone_graph.graph_cloner import clone, Node

class CloneGraphTest(unittest.TestCase):

    def test_one_node_graph(self):
        node_0 = Node("0", [])
        graph = [node_0]
        src_map = {node.name:node for node in graph}

        map_test : set[Node] = set()
        def dfs_test(node:Node):
            if node in map_test:
                return True
            self.assertFalse(src_map[node.name] is node)
            self.assertTrue(src_map[node.name] == node)
            self.assertEqual(len(src_map[node.name].neighbors), len(node.neighbors))
            map_test.add(node)
            for clone_neighbors in node.neighbors:
                dfs_test(clone_neighbors)

        clone_node_0 = clone(node_0)
        dfs_test(clone_node_0) 

    def test_two_nodes_graph(self):
        node_0 = Node("0", [])
        node_1 = Node("1", [node_0])
        node_0.neighbors.append(node_1)
        graph = [node_0, node_1]
        src_map = {node.name:node for node in graph}

        map_test : set[Node] = set()
        def dfs_test(node:Node):
            if node in map_test:
                return True
            self.assertFalse(src_map[node.name] is node)
            self.assertTrue(src_map[node.name] == node)
            self.assertEqual(len(src_map[node.name].neighbors), len(node.neighbors))
            map_test.add(node)
            for clone_neighbors in node.neighbors:
                dfs_test(clone_neighbors)

        clone_node_0 = clone(node_0)
        dfs_test(clone_node_0) 

    def test_recursion_nodes_graph(self):
        node_0 = Node("0", [])
        node_0.neighbors.append(node_0)
        
        graph = [node_0]
        src_map = {node.name:node for node in graph}

        map_test : set[Node] = set()
        def dfs_test(node:Node):
            if node in map_test:
                return True
            self.assertFalse(src_map[node.name] is node)
            self.assertTrue(src_map[node.name] == node)
            self.assertEqual(len(src_map[node.name].neighbors), len(node.neighbors))
            map_test.add(node)
            for clone_neighbors in node.neighbors:
                dfs_test(clone_neighbors)

        clone_node_0 = clone(node_0)
        dfs_test(clone_node_0)   
    
    def test_case_0(self):
        node_0 = Node("0", [])
        node_1 = Node("1", [])
        node_2 = Node("2", [])
        node_3 = Node("3", [])
        node_4 = Node("4", [])

        node_0.neighbors.extend([node_1, node_2, node_4])
        node_1.neighbors.extend([node_3, node_0])
        node_2.neighbors.extend([node_0])
        node_3.neighbors.extend([node_4, node_1])
        node_4.neighbors.extend([node_0, node_3])
        
        graph = [node_0, node_1, node_2, node_3, node_4]
        src_map = {node.name:node for node in graph}
        
        
        map_test : set[Node] = set()
        def dfs_test(node:Node):
            if node in map_test:
                return True
            self.assertFalse(src_map[node.name] is node)
            self.assertTrue(src_map[node.name] == node)
            self.assertEqual(len(src_map[node.name].neighbors), len(node.neighbors))
            map_test.add(node)
            for clone_neighbors in node.neighbors:
                dfs_test(clone_neighbors)

        clone_node_0 = clone(node_0)
        dfs_test(clone_node_0)   