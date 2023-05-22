num=int(input())
adjlist=[]
for _ in range(num):
    adjlist.append(list(map(int,input().split()[1:])))
n=3
adj_matrix = [[0] * num for _ in range(num)]

for v,ad_ver in enumerate(adjlist,1):
    for j in ad_ver:
        adj_matrix[v-1][j-1]=1
for r in adj_matrix:
    print(' '.join(map(str,r)))
