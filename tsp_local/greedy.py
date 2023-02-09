import numpy as np

def greedy(A, start):
    """
    The nearest neighbor heuristic starts at one city and connects with the closest unvisited city. 
    It repeats until every city has been visited. It then returns to the starting city.

    :param A: A is an NxN array indicating distance between N locations
    :param start: Start is the index of the starting location
    :return: The found solution
    """      
    N = A.shape[0]
    visited = [False for _ in range(N)]
    current = start
    tour = [current]
    visited[current] = True
    for _ in range(N - 1):
        distances = np.array([A[current][j] if not visited[j] else np.inf for j in range(N)])
        nearest = np.argmin(distances)
        current = nearest
        tour.append(current)
        visited[current] = True
    return tour