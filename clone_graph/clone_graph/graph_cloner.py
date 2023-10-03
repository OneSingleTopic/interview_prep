from dataclasses import dataclass, field

@dataclass(frozen=True)
class Node:
    name:str
    neighbors: list['Node'] = field(default_factory=list, hash=False)

    def __eq__(self, another_node):
        if self.name != another_node.name:
            return False
        for neighbor in self.neighbors:
            if neighbor.name not in [node.name for node in another_node.neighbors]:
                return False
        return True

def clone(node:Node) -> list[Node]:
    clone_map = {}

    def dfs(node: Node) -> bool:
        if node in clone_map:
            return clone_map[node]
        else:
            clone_map[node] = Node(node.name)
            for neighbor in node.neighbors:
                clone_map[node].neighbors.append(dfs(neighbor))
        return clone_map[node] 
    
    return dfs(node)
