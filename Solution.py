# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(' '.join([str(i) for i in list(product(A,B))]))
