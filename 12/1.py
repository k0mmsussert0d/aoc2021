if __name__ == '__main__':
    class Node:
        def __init__(self, name, vertices):
            self.name = name
            self.vert = vertices

    def get_node(name, nodes):
        for node in nodes:
            if node.name == name:
                return node
        new = Node(name, set())
        nodes.add(new)
        return new

    def add_node(name, vert, nodes):
        src = get_node(name, nodes)
        dst = get_node(vert, nodes)
        src.vert.add(dst)
        dst.vert.add(src)

    solutions = 0

    def dfs(start, end, current_path=None):
        global solutions
        if current_path is None:
            current_path = []

        if start.name.islower() and start in current_path:
            return

        current_path.append(start)

        if start == end:
            solutions += 1
            current_path.pop()
            return
        for node in start.vert:
            dfs(node, end, current_path)
        current_path.pop()

    nodes = set()
    with open('input', 'r') as file:
        for line in file.readlines():
            a, b = line.strip().split('-')
            add_node(a, b, nodes)
    dfs(get_node('start', nodes), get_node('end', nodes))
    print(solutions)
