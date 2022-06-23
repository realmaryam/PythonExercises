n = int(input())
arr = list(map(int,input().strip().split()))[:n]
station = {}
num = 1
for i in range (0,n):
    station[num] = []
    num +=1
num = 2
for i in range (0,n-1):
    station[arr[i]].append(num)
    num+=1

visited = set()
way = [1]
counter = 0

def dfs(visited, station, node, done):  #function for dfs 
    if done ==1 :
        return
    if not station[node] and way[len(way)-1] is not n :
        way.pop()
    counter = len(station[node])
    for children in station[node]: 
        counter -= 1
        if children not in visited:
            if way[len(way)-1] is not n :
                way.append(children)
            visited.add(children)
            dfs(visited, station, children,done)
        if children is n :
            done = 1
        if counter == 0 and done == 0 and way[len(way)-1] is not n :
            way.pop()
dfs(visited, station, 1, 0)

print(*way)