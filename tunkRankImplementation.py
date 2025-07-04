# Convierte una matriz de adyacencia en un diccionario de usuarios y sus seguidos
def adjacency_to_following(adj):
    following = {}
    for i, row in enumerate(adj):
        for j, values in enumerate(row):
            if values == 1:
                following[i] = following.get(i, []) + [j]
            else:
                following[i] = following.get(i, [])

    # print("Following:", following)
    return following

# Convierte una matriz de adyacencia en un diccionario de usuarios y sus seguidores
def adjacency_to_followers(adj):
    followers = {}
    for i, row in enumerate(adj):
        for j, values in enumerate(row):
            if values == 1:
                followers[j] = followers.get(j, []) + [i]
            else:
                followers[i] = followers.get(i, [])

    # print("Followers:", followers)
    return followers

# Imprime los scores de los nodos en cada iteración
def print_T_iteration(i, T_it):
    print(f"Iteration {i+1}:")
    for j in range(len(T_it)):
        print(f"\t{j}: {T_it[j]:.8f}")
        pass

# Imprime los scores finales de los nodos
def print_scores(T, names=None):
    print("Final scores:")
    for u, score in T.items():
        if names is not None:
            u = names[u]
        print(f"\t{u}: {score:.8f}")
    print()

# Implementación del algoritmo TunkRank
def tunkrank(adj, p=0.25, max_iter=100, tol=1e-6):
    following = adjacency_to_following(adj)
    followers = adjacency_to_followers(adj)

    n = len(adj)
    T = {u : 0.0 for u in range(n)}

    for it in range(max_iter):
        delta = 0.0
        T_new = {u : 0.0 for u in range(n)}
        for x in T:
            for y in followers.get(x, []):
                deg = len(following.get(y, []))
                if deg > 0:
                    # algoritmo TunkRank -> influence(x) = sum((1 + p * influence(y)) / ||following(y)||)
                    T_new[x] += (1.0 + p * T[y]) / deg
            delta = max(delta, abs(T_new[x] - T[x]))
        T = T_new

        # print_T_iteration(it, list(T.values()))
        
        if delta < tol:
            print(f"Convergió en {it+1} iteraciones (δ={delta:.2e})")
            break
    else:
        print(f"No convergió tras {max_iter} iteraciones (δ={delta:.2e})")

    return T

def main():
    # Test 1
    names1 = ["Alice", "Bob", "Carol", "Dave"]
    matrix1 = [ [0, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 1, 0, 1],
                [0, 0, 1, 0] ]
    
    T1 = tunkrank(matrix1, p=0.2, max_iter=1000, tol=1e-8)
    print_scores(T1, names=names1)
    
    # Test 2
    names2 = ['Juan', 'Mathias', 'Santiago', 'Gael', 'Gabriel']
    matrix2 = [
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
    ]
    T2 = tunkrank(matrix2, p=0.4, max_iter=1000, tol=1e-8)
    print_scores(T2, names=names2)

main()
