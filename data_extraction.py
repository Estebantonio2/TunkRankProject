def build_adjacency_matrix(edge_file, n=None):
    following = {}
    nodes = set()
    count = 0

    with open(edge_file, 'r') as f:
        for line in f:
            if n is not None and count >= n:
                break
            edges = line.strip().split()
            if len(edges) == 2:
                u, v = edges
                following.setdefault(u, []).append(v)
                nodes.add(u)
                nodes.add(v)
                count += 1

    nodes = list(nodes)
    node_to_idx = {node: idx for idx, node in enumerate(nodes)}
    size = len(nodes)
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    for u, v_list in following.items():
        for v in v_list:
            i = node_to_idx[u]
            j = node_to_idx[v]
            matrix[i][j] = 1

    with open('matrix3.txt', 'w') as f:
        f.write('matrix = [\n')
        for i, row in enumerate(matrix):
            row_str = ', '.join(str(x) for x in row)
            if i < size - 1:
                f.write(f'\t[{row_str}],\n')
            else:
                f.write(f'\t[{row_str}]\n')
        f.write(']\n')
    print('Matriz guardada en matrix_tw.txt con formato de lista de listas')

build_adjacency_matrix('twitter_combined.txt', 100000) # Numero de lineas a leer del archivo