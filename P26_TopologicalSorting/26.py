from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, frm, to):
        self.graph[frm].append(to)

        if self.directed is False:
            self.graph[to].append(frm)
        else:
            self.graph[to] = self.graph[to]

    def topoSortvisit(self, s, visited, sortlist):
        visited[s] = True

        for i in self.graph[s]:
            if not visited[i]:
                self.topoSortvisit(i, visited, sortlist)

        sortlist.insert(0, s)

    def topoSort(self):
        visited = {i: False for i in self.graph}

        sortlist = []

        for v in self.graph:
            if not visited[v]:
                self.topoSortvisit(v, visited, sortlist)

        # print(sortlist)
        print(' '.join(map(str, sortlist)))


if __name__ == '__main__':
    g = Graph(directed=True)
    with open('rosalind_ts.txt', 'r') as f:
        for i in f.readlines():
            V1, V2 = list(map(int, i.split()))
            g.addEdge(V1, V2)
    g.topoSort()

