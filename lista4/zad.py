import random
import heapq
import sys
import networkx as nx # Biblioteka implementująca graf

# Implementacja algorytmów
def move_to_min(graph, sequence):
    total_cost = 0
    #page_position = random.randint(0,num_vertices-1)
    page_position = 0
    #print("PAGE POSITION: ",page_position)
    current_sequence = []
    for a in range(len(sequence)):
        #print("PAGE POSITION: ",page_position)
        current_sequence.append(sequence[a])
        if (a+1) % 32 == 0:
            #print(current_sequence)
            values = []
            for j in range(graph.number_of_nodes()):
                values.append(sum(nx.shortest_path_length(graph, source=current, target=j) for current in current_sequence))
            #print(values)
            tmp_page_position = current_sequence.index(min(current_sequence))
            server_swap_cost = nx.shortest_path_length(graph, source=tmp_page_position, target=page_position)
            total_cost = total_cost +  (32 * server_swap_cost)
            #print(f"SWAP {tmp_page_position} - {page_position}, dystans: {server_swap_cost}")
            page_position = tmp_page_position
            current_sequence.clear()
        if page_position == sequence[a]:
            continue
        dist = nx.shortest_path_length(graph, source=sequence[a], target=page_position)
       # print(f"{sequence[a]} - {page_position}, dystans: {dist}")
        total_cost = total_cost +  dist
    return total_cost



def flip(graph, sequence):
    num_vertices = graph.number_of_nodes()
    #page_position = random.randint(0,num_vertices-1)
    page_position = 0
    total_cost = 0

    for request in sequence:
        #print("POZYCJA STRONY: ", page_position)
        #print("POZYCJA ZAPYTANIA: ", request)
        if page_position == request:
            continue
        else:
            dist = nx.shortest_path_length(graph, source=request, target=page_position)
            do_swap = random.uniform(0,1)
            #print(do_swap)
            #print(1/(2*D))
            if do_swap < 1/(2*32):
                #print("SWAP")
                page_position = request
                total_cost = total_cost +  (32 * dist)
                #print(f"KOSZT TEJ RUNDY: {32} * {dist} = {total_cost}")
            else:
                #print("NIE SWAP")
                #print(f"KOSZT TEJ RUNDY: {dist}")
                total_cost = total_cost +  dist
    return total_cost
        


# Funkcja generująca ciąg żądań z jednostajnym rozkładem
def generate_uniform_sequence(length, num_vertices):
    return [random.randint(0, num_vertices - 1) for _ in range(length)]

# Funkcja generująca ciąg żądań z harmonicznym rozkładem
def generate_harmonic_sequence(length, num_vertices):
    harmonic_numbers = [1 / i for i in range(1, num_vertices + 1)]
    harmonic_sum = sum(harmonic_numbers)
    probabilities = [num / harmonic_sum for num in harmonic_numbers]
    return random.choices(range(num_vertices), probabilities, k=length)

# Funkcja generująca ciąg żądań z dwuharmonicznym rozkładem
def generate_two_harmonic_sequence(length, num_vertices):
    two_harmonic_numbers = [1 / (i ** 2) for i in range(1, num_vertices + 1)]
    two_harmonic_sum = sum(two_harmonic_numbers)
    probabilities = [num / two_harmonic_sum for num in two_harmonic_numbers]
    return random.choices(range(num_vertices), probabilities, k=length)

# Parametry grafów
num_vertices = 64
D = 32
# Inicjalizacja grafów
torus_graph = nx.Graph()
hypercube_graph = nx.Graph()

# Dodawanie krawędzi do grafu torusa trójwymiarowego
'''for i in range(num_vertices):
    torus_graph.add_edge(i, (i + 1) % num_vertices)
    torus_graph.add_edge(i, (i - 1) % num_vertices)
    torus_graph.add_edge(i, (i + 8) % num_vertices)
    torus_graph.add_edge(i, (i - 8) % num_vertices)
    torus_graph.add_edge(i, (i + 16) % num_vertices)
    torus_graph.add_edge(i, (i - 16) % num_vertices)
    '''
'''
side_length = int(num_vertices ** (1/3))
for i in range(num_vertices):
    x = i % side_length
    y = (i // side_length) % side_length
    z = (i // (side_length * side_length)) % side_length

    # Krawędzie wzdłuż osi x
    torus_graph.add_edge(i, (x + 1) % side_length + y * side_length + z * side_length * side_length)
    torus_graph.add_edge(i, (x - 1 + side_length) % side_length + y * side_length + z * side_length * side_length)

    # Krawędzie wzdłuż osi y
    torus_graph.add_edge(i, x + ((y + 1) % side_length) * side_length + z * side_length * side_length)
    torus_graph.add_edge(i, x + ((y - 1 + side_length) % side_length) * side_length + z * side_length * side_length)

    # Krawędzie wzdłuż osi z
    torus_graph.add_edge(i, x + y * side_length + ((z + 1) % side_length) * side_length * side_length)
    torus_graph.add_edge(i, x + y * side_length + ((z - 1 + side_length) % side_length) * side_length * side_length)
'''

# Dodawanie krawędzi do grafu hiperkostki
for i in range(num_vertices):
    for j in range(i + 1, num_vertices):
        if bin(i ^ j).count('1') == 1:
            #print(f"{i} - {j}")
            hypercube_graph.add_edge(i, j)
# Parametry eksperymentu
sequence_length = 1024
num_trials = 100

for graph_type in [torus_graph,hypercube_graph]:
    # Eksperyment dla grafu torusa trójwymiarowego
    if graph_type == torus_graph:
        print("Eksperyment dla grafu torusa trójwymiarowego:")
        print("--------------------------------------------------")
    else:
        # Eksperyment dla grafu hiperkostki
        print("Eksperyment dla grafu hiperkostki:")
        print("--------------------------------------------------")

    # Jednostajny rozkład
    print("Jednostajny rozkład:")
    uniform_costs_move_to_min = 0
    all_uniform_costs_move_to_min = []
    uniform_costs_flip = 0
    all_uniform_costs_flips = []
    for _ in range(num_trials):
        uniform_sequence = generate_uniform_sequence(sequence_length, num_vertices)
        uniform_costs_move_to_min = uniform_costs_move_to_min + move_to_min(torus_graph, uniform_sequence)
        uniform_costs_move_to_min = uniform_costs_move_to_min / sequence_length
        all_uniform_costs_move_to_min.append(uniform_costs_move_to_min)
        uniform_costs_flip = uniform_costs_flip + flip(graph_type, uniform_sequence)
        uniform_costs_flip = uniform_costs_flip / sequence_length
        #print("UNI COSTS FLIP: ", uniform_costs_flip)
        all_uniform_costs_flips.append(uniform_costs_flip)

    print("MOVE-TO-MIN (średni koszt):", sum(all_uniform_costs_move_to_min) / num_trials)
    print("FLIP (średni koszt):", sum(all_uniform_costs_flips) / num_trials)
    print()
    # Harmoniczny rozkład
    print("Harmoniczny rozkład:")
    harmonic_costs_move_to_min = 0
    all_harmonic_costs_move_to_min = []
    harmonic_costs_flip = 0
    all_harmonic_costs_flips = []
    for _ in range(num_trials):
        harmonic_sequence = generate_harmonic_sequence(sequence_length, num_vertices)
        harmonic_costs_move_to_min = harmonic_costs_move_to_min + move_to_min(torus_graph, harmonic_sequence)
        harmonic_costs_move_to_min = harmonic_costs_move_to_min / sequence_length
        all_harmonic_costs_move_to_min.append(harmonic_costs_move_to_min)
        
        harmonic_costs_flip = harmonic_costs_flip + flip(graph_type, harmonic_sequence)
        harmonic_costs_flip = harmonic_costs_flip / sequence_length
        #print("HARMONIC COSTS FLIP: ", harmonic_costs_flip)
        all_harmonic_costs_flips.append(harmonic_costs_flip)

    print("MOVE-TO-MIN (średni koszt):", sum(all_harmonic_costs_move_to_min) / num_trials)
    print("FLIP (średni koszt):", sum(all_harmonic_costs_flips) / num_trials)
    print()

    # Dwuharmoniczny rozkład
    print("Dwuharmoniczny rozkład:")
    two_harmonic_costs_flip = 0
    two_harmonic_costs_move_to_min = 0
    all_two_harmonic_costs_move_to_min = []
    all_two_harmonic_costs_flips = []
    for _ in range(num_trials):
        two_harmonic_sequence = generate_two_harmonic_sequence(sequence_length, num_vertices)
        two_harmonic_costs_move_to_min = two_harmonic_costs_move_to_min + move_to_min(torus_graph, two_harmonic_sequence)
        two_harmonic_costs_move_to_min = two_harmonic_costs_move_to_min / sequence_length
        all_two_harmonic_costs_move_to_min.append(two_harmonic_costs_move_to_min)

        two_harmonic_costs_flip = two_harmonic_costs_flip + flip(graph_type, two_harmonic_sequence)
        two_harmonic_costs_flip = two_harmonic_costs_flip / sequence_length
        all_two_harmonic_costs_flips.append(two_harmonic_costs_flip)

    print("MOVE-TO-MIN (średni koszt):", sum(all_two_harmonic_costs_move_to_min) / num_trials)
    print("FLIP (średni koszt):", sum(all_two_harmonic_costs_flips) / num_trials)
    print()