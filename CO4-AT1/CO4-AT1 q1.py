def p_mst(m):  #prism minimum spanning 
    n=len(m)
    visit=[False]*n
    key =[float('inf')]*n #initialsing 
    parent=[-1]*n
    key[0]=0
    tw=0

    for i in range(n):  #loop through all vertices 
          u = min((v for v in range(n) if not visit[v]),key=lambda v:key[v])
          visit[u]=True
          tw+=key[u]

          for v in range(n):  #update keys of adjucent vertices
                 if 0 <m[u][v] < key[v] and not visit[v]:
                      key[v]=m[u][v]
                      parent[v]=u
    return tw

matrix=[[0,2,3],[2,0,1],[3,1,0]]

print("Total weight =",p_mst(matrix))
