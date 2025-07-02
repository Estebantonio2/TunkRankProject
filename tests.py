def compute_tunkrank(following, p=0.1, max_iter=100, tol=1e-6):
    """
    Calcula TunkRank para cada nodo de la red.
    - following: dict usuario -> lista de usuarios que sigue.
    - p: probabilidad constante de retweet.
    - max_iter: iteraciones máximas.
    - tol: umbral de convergencia (máximo cambio permitido).
    Devuelve: dict usuario -> puntaje TunkRank.
    """
    # 1. Construyo la lista de followers
    followers = {u: [] for u in following}
    for u, neighs in following.items():
        for v in neighs:
            # asumo que v está en following keys; si no, inicializarlo
            followers.setdefault(v, []).append(u)

    # 2. Inicializo TunkRank en cero
    T = {u: 0.0 for u in followers}

    # 3. Itero hasta convergencia
    for it in range(max_iter):
        delta = 0.0
        T_new = {}
        for x in T:
            rank = 0.0
            for y in followers.get(x, []):
                deg = len(following.get(y, []))
                if deg > 0:
                    rank += (1.0 / deg) * (1.0 + p * T[y])
            T_new[x] = rank
            delta = max(delta, abs(rank - T[x]))
        T = T_new
        # debug output
        print(f"Iteración {it+1}:")
        for u, score in T.items():
            print(f"{u:>5} → {score:.8f}")
        print()
        
        if delta < tol:
            print(f"Convergió en {it+1} iteraciones (δ={delta:.2e})")
            break
    else:
        print(f"No convergió tras {max_iter} iteraciones (δ={delta:.2e})")

    return T

if __name__ == "__main__":
    # Ejemplo de prueba
    following = {
        'Alice': ['Bob', 'Carol'],
        'Bob':   ['Carol'],
        'Carol': ['Alice'],
        'Dave':  ['Alice', 'Bob', 'Carol']
    }
    scores = compute_tunkrank(following, p=0.2, max_iter=1000, tol=1e-8)
    for user, score in scores.items():
        print(f"{user:>5} → {score:.4f}")
     # scores: numero esperado de lecturas
