N,M,T = map(int, input().split(" ",3))

bw = list(map(int,input().strip().split()))[:N]


graph = {}
num = 1
for i in range (0,N):
    graph[num] = []
    num +=1

for i in range(0,M):
    x1,x2 = map(int, input().split(" ",2))
    graph[x1].append(x2)
    graph[x2].append(x1)

def bfs (graph, bw, node1, node2, news1, news2):
    state = [0] * N
    visited1 = []
    visited2 = []
    queue1 = []
    queue2 = []
    visited1.append(node1)
    visited2.append(node2)
    queue1.append(node1)
    queue2.append(node2)
    state[node1-1] = news1
    state[node2-1] = news2

    while queue1 or queue2 :
        if queue1 :
            s1 = queue1.pop(0)
            for neighbour in graph[s1]:
                if neighbour not in visited1:
                    if state[neighbour-1] == 0 :
                        if bw[s1-1] == -1 or bw[neighbour-1] == -1 :
                            state[neighbour-1] = state[s1-1]

                        else:
                            state[neighbour-1] = -(state[s1-1])
                    else:
                        if bw[s1-1] == -1 or bw[neighbour-1] == -1 :
                            if state[neighbour-1] is not state[s1-1] :
                                return False
                        else:
                            if state[neighbour-1] is not -(state[s1-1]) :
                                return False
                    visited1.append(neighbour)
                    queue1.append(neighbour)
        if queue2 :
            s2 = queue2.pop(0)
            for neighbour in graph[s2]:
                if neighbour not in visited2:
                    if state[neighbour-1] == 0 :
                        if bw[s2-1] == -1 or bw[neighbour-1] == -1 :
                            state[neighbour-1] = state[s2-1]

                        else:
                            state[neighbour-1] = -(state[s2-1])
                    else:
                        if bw[s2-1] == -1 or bw[neighbour-1] == -1 :
                            if state[neighbour-1] is not state[s2-1] :
                                return False
                        else:
                            if state[neighbour-1] is not -(state[s2-1]) :
                                return False
                    visited2.append(neighbour)
                    queue2.append(neighbour) 
    return True
t = []
for i in range (0,T):
    n1,n2,news1,news2 = map(int, input().split(" ",4))
    o = bfs(graph, bw, n1, n2, news1, news2)
    t.append(o)

for i in range (0,T):
    if t[i]:
        print("YES")
    else:
        print("NO")
