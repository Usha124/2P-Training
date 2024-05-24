n,e=map(int,input().split())
adj=[]
for i in range(n+1):
    row=[0]*(n+1)
    adj.append(row)
for i in range(e):
    u,v=map(int,input().split())
    adj[u][v]=1
    adj[v][u]=1
print(adj)
