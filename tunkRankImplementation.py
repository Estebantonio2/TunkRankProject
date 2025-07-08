def parent(i): return (i - 1) // 2
def left(i):   return 2 * i + 1
def right(i):  return 2 * i + 2

def heapify_down(arr, size, i):
    largest = i
    l = left(i)
    r = right(i)
    if l < size and arr[l] > arr[largest]:
        largest = l
    if r < size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_down(arr, size, largest)

def build_max_heap(arr):
    n = len(arr)
    # Comienza desde el último nodo no-hoja hasta la raíz
    for i in range((n // 2) - 1, -1, -1):
        heapify_down(arr, n, i)

def extract_max(arr, size):
    if size <= 0:
        return None, size
    max_val = arr[0]
    arr[0] = arr[size - 1]
    size -= 1
    heapify_down(arr, size, 0)
    return max_val, size

def top_k_tunkrank(T, k=3):
    # Convertir el diccionario T en una lista de tuplas (score, user_id)
    heap_arr = [(score, u) for u, score in T.items()]

    # Construir max-heap
    build_max_heap(heap_arr)

    # Extraer los k máximos
    topk = []
    size = len(heap_arr)
    for _ in range(min(k, size)):
        item, size = extract_max(heap_arr, size)
        topk.append(item)  # (score, user_id)

    return topk

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

    # Top 3 scores
    top3 = top_k_tunkrank(T2, k=3)
    print("Top 3 scores (user_id, score):")
    for score, user_id in top3:
        print(f"\t{names2[user_id]}: {score:.8f}")

    # Test 3
    with open('matrix_tw.txt', 'r') as f:
        content = f.read()
    local_vars = {}
    exec(content, {}, local_vars)
    matrix3 = local_vars['matrix']

    T3 = tunkrank(matrix3, p=0.4, max_iter=1000, tol=1e-8)
    # print_scores(T3)
    
    # Top 5 scores
    top5 = top_k_tunkrank(T3, k=5)
    print("Top 5 scores (id, score):")
    for score, id in top5:
        print(f"\t{id}: {score:.8f}")


main()