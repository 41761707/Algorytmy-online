import sys
import random
import math
from distributions import normal_distribution,harmonic_distribution,double_harmonic_distribution,geometric_distribution

def get_index(array):
    rand = random.uniform(0,1)
    for index in array:
        if rand <= index[1]:
            break
    return index

def next_fit(seq):
    bins = []  # lista przechowująca kubełki
    current_bin = []  # aktualny kubełek
    
    for item in seq:
        if sum(current_bin) + item <= 1.0:  # jeśli ciąg zmieści się w aktualnym kubełku
            current_bin.append(item)  # dodaj ciąg do aktualnego kubełka
        else:
            bins.append(current_bin)  # dodaj aktualny kubełek do listy kubełków
            current_bin = [item]  # utwórz nowy kubełek z obecnym ciągiem
        
    bins.append(current_bin)  # dodaj ostatni kubełek do listy kubełków
    
    return len(bins) #zwracamy liczbę kubełków

def random_fit(seq):
    bins = []  # lista kubełków
    for item in seq:
        random.shuffle(bins)  # losowe przemieszanie kolejności kubełków
        for bin in bins:
            if sum(bin) + item <= 1.0:  # sprawdzamy, czy item zmieści się w kubełku
                bin.append(item)  # dodajemy item do kubełka
                break
        else:
            bins.append([item])  # tworzymy nowy kubełek i dodajemy do listy kubełków
    return len(bins)  # zwracamy liczbę kubełków

def first_fit(seq):
    bins = []  # lista kubełków
    for item in seq:
        for bin in bins:
            if sum(bin) + item <= 1.0:  # sprawdzamy, czy item zmieści się w kubełku
                bin.append(item)  # dodajemy item do kubełka
                break
        else:
            bins.append([item])  # tworzymy nowy kubełek i dodajemy do listy kubełków
    return len(bins)  # zwracamy liczbę kubełków

def best_fit(seq):
    bins = []  # lista kubełków
    for item in seq:
        best_bin_index = -1
        min_remaining_space = float('inf')
        for i, bin in enumerate(bins):
            remaining_space = 1.0 - sum(bin)
            if remaining_space >= item and remaining_space < min_remaining_space:
                best_bin_index = i
                min_remaining_space = remaining_space
        if best_bin_index != -1:
            bins[best_bin_index].append(item)
        else:
            bins.append([item])
    return len(bins)  # zwracamy liczbę kubełków

def worst_fit(items):
    bins = []  # lista kubełków
    for item in items:
        worst_bin_index = -1
        max_remaining_space = -1
        for i, bin in enumerate(bins):
            remaining_space = 1.0 - sum(bin)
            if remaining_space >= item and remaining_space > max_remaining_space:
                worst_bin_index = i
                max_remaining_space = remaining_space
        if worst_bin_index != -1:
            bins[worst_bin_index].append(item)
        else:
            bins.append([item])
    return len(bins)  # zwracamy liczbę kubełków


def main():
    seq = []
    numbers = []
    dist = sys.argv[1]
    if(dist=="NORMAL"):
        normal_distribution(numbers,10) ##dziala
    elif(dist=="HARMONIC"):
        harmonic_distribution(numbers,10) ##dziala
    elif(dist=="DOUBLE_HARMONIC"):
        double_harmonic_distribution(numbers,10) ##dziala
    elif(dist=="GEOMETRIC"):
        geometric_distribution(numbers,10) ##dziala
        
    while(len(seq)<=100):
        value = random.uniform(0,1)
        rep_los = get_index(numbers)
        seq.extend([value for x in range(rep_los[0])])
    seq = seq[:100]
    print(seq)
    print("Optymalna liczba koszyczków: {}".format(math.ceil(sum(seq))))
    print("Next fit wykorzystał: {} koszyczków".format(next_fit(seq)))
    print("Random fit wykorzystał: {} koszyczków".format(random_fit(seq)))
    print("First fit wykorzystał: {} koszyczków".format(first_fit(seq)))
    print("Best fit wykorzystał: {} koszyczków".format(best_fit(seq)))
    print("Worst fit wykorzystał: {} koszyczków".format(worst_fit(seq)))



if __name__ == "__main__":
    main()