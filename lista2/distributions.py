def normal_distribution(numbers,n):
    pr_sum = 0
    for i in range(1,n+1):
        pr_sum = pr_sum + 1/n
        numbers.append([i,pr_sum,0,0])
def harmonic_distribution(numbers,n):
    harmonic= 1
    pr_sum = 0
    for i in range(2,n+1):
        harmonic = harmonic + 1/i
    for i in range(1,n+1):
        pr_sum = pr_sum + 1/(i*harmonic)
        numbers.append([i,pr_sum,0,0])
def double_harmonic_distribution(numbers,n):
    double_harmonic = 1
    pr_sum = 0
    for i in range(2,n+1):
        double_harmonic = double_harmonic + 1/(i*i)
    for i in range(1,n+1):
        pr_sum = pr_sum + 1/(i*i*double_harmonic)
        numbers.append([i,pr_sum,0,0])
def geometric_distribution(numbers,n):
    pr_sum = 0
    for i in range(1,n):
        pr_sum = pr_sum + 1/2**i
        numbers.append([i,pr_sum,0,0])
    numbers.append([n,pr_sum+1/2**(n-1),0,0])