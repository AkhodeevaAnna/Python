N = int(input())
list = [i for i in range(20, N+1) if i% 20 == 0 or i % 21 == 0]
print(list)