def two_opt(A, tour):
    """
    2-opt is a local search algorithm for solving the traveling salesman problem.
    The main idea behind it is to take a route that crosses over itself and reorder it,
    so that it does not cross over itself.

    :param A: 2D matrix representing the distances between cities
    :param tour: List of integers representing the order in which the cities should be visited.
    :return: The best tour found
    """
    improved = True
    best_tour = tour[:]
    best_length = tour_length(A, tour)
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1:
                    continue
                new_tour = swap(tour, i, j)
                new_length = tour_length(A, new_tour)
                if new_length < best_length:
                    improved = True
                    best_tour = new_tour[:]
                    best_length = new_length
        tour = best_tour
    return tour

def swap(tour, i, j):
    """
    Performs a 2-opt swap by reversing the order of the cities between indices i and j in the tour list,
    until no further improvements can be made

    :param tour: A list of integers representing the order in which the cities should be visited.
    :param i: The start index of the swap
    :param j: The end index of the swap
    :return: The new tour after the 2-opt swap.
    """  
    return tour[:i] + list(reversed(tour[i:j])) + tour[j:]


def tour_length(A, tour):
    """
    calculates the total distance of a tour by summing the distances 
    between consecutive cities in the tour and adding the distance between 
    the first and last city to complete the loop.

    :param A: 2D matrix representing the distances between cities
    :param tour: List of integers representing the order in which the cities should be visited.
    :return: Total distance of a tour
    """
    length = 0
    for i in range(len(tour) - 1):
        length += A[tour[i]][tour[i + 1]]
    length += A[tour[-1]][tour[0]]
    return length