import sys
import random

def normal_distribution(numbers):
    pr_sum = 0
    for i in range(1,101):
        pr_sum = pr_sum + 1/100
        numbers.append([i,pr_sum])
def harmonic_distribution(numbers):
    harmonic_100th = 1
    pr_sum = 0
    for i in range(2,101):
        harmonic_100th = harmonic_100th + 1/i
    for i in range(1,101):
        pr_sum = pr_sum + 1/(i*harmonic_100th)
        numbers.append([i,pr_sum])
def double_harmonic_distribution(numbers):
    double_harmonic_100th = 1
    pr_sum = 0
    for i in range(2,101):
        double_harmonic_100th = double_harmonic_100th + 1/(i*i)
    for i in range(1,101):
        pr_sum = pr_sum + 1/(i*i*double_harmonic_100th)
        numbers.append([i,pr_sum])
def geometric_distribution(numbers):
    pr_sum = 0
    for i in range(1,101):
        pr_sum = pr_sum + 1/2**i
        if(i==100):
            pr_sum = pr_sum + 1/2**99
        numbers.append([i,pr_sum])

def access(test_array, index):
    seen = 0
    if index not in test_array:
        seen = len(test_array)
        test_array.append(index)
    else:
        seen = test_array.index(index)
    return seen

def get_index(array):
    rand = random.uniform(0,1)
    for index in array:
        if rand <= index[1]:
            break
    return index


def raw_array(numbers,test_array,n):
    access_sum = 0
    for _ in range(n):
        index = get_index(numbers)
        access_sum = access_sum + access(test_array,index[0])
    access_sum = access_sum / n
    print(access_sum)

def move_to_front(numbers,test_array,n):
    access_sum = 0
    for _ in range(n):
        index = get_index(numbers)
        access_sum = access_sum + access(test_array,index[0])
        element_to_move = test_array.index(index[0])
        #print(test_array)
        test_array.insert(0, test_array.pop(element_to_move))
        #print(test_array)
    access_sum = access_sum / n
    print(access_sum)
def transpose(numbers,test_array,n):
    access_sum = 0
    for _ in range(n):
        index = get_index(numbers)
        access_sum = access_sum + access(test_array,index[0])
        element_to_move = test_array.index(index[0])
        #print(test_array)
        if(element_to_move>0):
            test_array[element_to_move-1], test_array[element_to_move] = test_array[element_to_move], test_array[element_to_move-1]
        #print(test_array)
    access_sum = access_sum / n
    print(access_sum)
def count(numbers,test_array,n):
    access_sum = 0
    frequencies = []
    for _ in range(n):
        index = get_index(numbers)
        if index[0] not in test_array:
            frequencies.append(1)
        else:
            index_value = test_array.index(index[0])
            #print(index_value)
            frequencies[index_value] = frequencies[index_value] + 1
        access_sum = access_sum + access(test_array,index[0])
        #print(test_array)
        #print(frequencies)
        test_array = [x for _,x in sorted(zip(frequencies,test_array),reverse=True)]
        frequencies.sort(reverse=True)
        #print(test_array)
        #print(frequencies)
    access_sum = access_sum / n
    print(access_sum)



        




def main():
    numbers = []
    n = int(sys.argv[1])
    test_array = []
    #normal_distribution(numbers) ##dziala
    #harmonic_distribution(numbers) ##dziala
    double_harmonic_distribution(numbers) ##dziala
    #geometric_distribution(numbers) ##dziala
    #raw_array(numbers,test_array,n)
    move_to_front(numbers,test_array,n)
    #transpose(numbers,test_array,n)
    #count(numbers,test_array,n)
    #print(test_array)
    #print(numbers)
    #print(numbers[len(numbers)-1][1])


if __name__ == '__main__':
    main()