INFILE = 'rosalind_ddeg.txt'

try:
    with open(INFILE) as f:
        '''
                read data in edgelist format:
                1st line: number of vertices, number of edges
                subsequent lines:
                edge given by two vertices
                '''
        for i in f.readlines():
            input_list = list(map(int, i.split()))

        V, E = map(int, f.readline().rstrip().split())
        e = [map(int, line.rstrip().split()) for line in f]
        res = []

        # Neighbors dict with vertices as keys,
        # lists of adjacent vertices as values
        neighbors = {k: [] for k in range(1, V + 1)}
        for v1, v2 in e:
            neighbors[v1].append(v2)
            neighbors[v2].append(v1)

        # Degree of a vertex is the number of edges that connect to it
        # BUT double degree of a vertex is the number of edges that are
        # connected to ADJACENT vertices

        degree = {k: 0 for k in neighbors.keys()}
        for v in neighbors:
            for n in neighbors[v]:
                degree[v] += len(neighbors[n])

        for k, v in sorted(degree.items()):
            res.append(v)

    listToStr = ' '.join(map(str, res))
    print(listToStr)

except IOError as e:
    print('Operation failed: %s' % e.strerror)