import sys
import random
from distributions import normal_distribution,harmonic_distribution,double_harmonic_distribution,geometric_distribution

def get_index(array):
    rand = random.uniform(0,1)
    for index in array:
        if rand <= index[1]:
            break
    return index

def fifo(cache,index):
    new_cache = cache[1:]
    new_cache.append(index)
    return new_cache


def fwf(cache,index):
    new_cache = []
    new_cache.append(index)
    return new_cache

def lru(cache,index,flag):
    #print("CACHE IN : ",cache)
    if(flag == "F"):
        del cache[len(cache)-1]
        cache.insert(0,index)
    else:
        cache.insert(0, cache.pop(cache.index(index)))
    #print("CACHE OUT: ",cache)
    return cache
    

def lfu(cache,index,numbers):
    lowest_index = 0
    lowest_index_value = numbers[cache[0]-1][2]
    for i in range(1,len(cache)):
        if(numbers[cache[i]-1][2] < lowest_index_value):
            lowest_index = i
            lowest_index_value = numbers[cache[i]-1][2]
    cache.pop(lowest_index)
    cache.append(index[0])
    return cache

def rand(cache,index):
    del cache[random.randint(0,len(cache)-1)]
    cache.append(index)
    return cache

def rma(cache,index,numbers):
    unmarked = []
    for i in range(len(cache)):
        if(numbers[cache[i]-1][3] == 0):
            unmarked.append(i)
    if(len(unmarked) == 0):
        for i in range(len(cache)):
            numbers[cache[i]-1][3] = 0
            unmarked.append(i)
    to_remove = random.choice(unmarked)
    cache.pop(to_remove)
    cache.append(index[0])
    return cache
    


def access(numbers,test_array, index, max_len,func):
    seen = 0
    index[2] = index[2] + 1
    index[3] = 1
    if index[0] not in test_array:
        seen = 1
        if len(test_array) == max_len:
            if(func=="FIFO"):
                test_array = fifo(test_array,index[0]) #fifo
            elif(func=="FWF"):
                test_array = fwf(test_array,index[0]) #fwf
            elif(func=="RAND"):
                test_array = rand(test_array,index[0]) #rand
            elif(func=="LRU"):
                test_array = lru(test_array,index[0],"F") #lru
            elif(func=="LFU"):
                test_array = lfu(test_array,index,numbers) #lfu
            elif(func=="RMA"):
                test_array = rma(test_array,index,numbers) #rma
            
            '''
            test_array = fifo(test_array,index[0]) #fifo
            test_array = fwf(test_array,index[0]) #fwf
            test_array = rand(test_array,index[0]) #rand
            
            '''
        else:
            test_array.append(index[0])
            if(func=="LRU"):
                test_array = lru(test_array,index[0],"N") #lru
    return seen, test_array

def cache_handler(numbers, n, max_len, reps,func):
    access_sum = 0
    access_current = 0
    cache = []
    for _ in range(reps):
        #print("Cache: ",cache)
        index = get_index(numbers)
        #print("Index: ",index)
        access_current,cache = access(numbers,cache,index,max_len,func)
        access_sum = access_sum + access_current
        #print("Access_curent: ",access_current)
    return access_sum

def main():
    numbers = []
    n = int(sys.argv[1])
    k = int(sys.argv[2]) #max_len
    queries = int(sys.argv[3])
    repetitions = int(sys.argv[4])
    dist = sys.argv[5]
    func = sys.argv[6]
    access_sum = 0
    if(dist=="NORMAL"):
        normal_distribution(numbers,n) ##dziala
    elif(dist=="HARMONIC"):
        harmonic_distribution(numbers,n) ##dziala
    elif(dist=="DOUBLE_HARMONIC"):
        double_harmonic_distribution(numbers,n) ##dziala
    elif(dist=="GEOMETRIC"):
        geometric_distribution(numbers,n) ##dziala
    for _ in range(repetitions):
        access_sum = access_sum + cache_handler(numbers, n, k, queries,func)
    print("{};{};{}".format(n,k,access_sum/repetitions))
    '''
    ns = [20,30,40,50,60,70,80,90,100]
    repetitions = 1000
    f=""
    for n in ns:
        for dis in dist:
            access_sum = 0
            normal_distribution(numbers,n) ##dziala
            harmonic_distribution(numbers,n) ##dziala
            double_harmonic_distribution(numbers,n) ##dziala
            geometric_distribution(numbers,n) ##dziala
            queries = 100
            for f in func:
                for k in range(int(n/10),int(n/5)+1):
                    for _ in range(repetitions):
                        access_sum = access_sum + cache_handler(numbers, n, k, queries,f)
                    print("{};{};{}".format(n,k,access_sum/repetitions))
                    access_sum = 0
            numbers = []
    '''
    

if __name__ == '__main__':
    main()