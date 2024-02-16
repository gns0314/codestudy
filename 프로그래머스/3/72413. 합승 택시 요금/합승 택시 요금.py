import heapq

def dijkstra(graph, start):
    n = len(graph)
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    queue = [(0, start)]
    
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for neighbor, cost in graph[node].items():
            new_dist = dist + cost
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))
    
    return distance

def solution(n, s, a, b, fares):
    answer = float('inf')
    graph = {i:{} for i in range(1,n+1)}
    for j in fares:
        for k in range(1, n+1):
            if k == j[0]:
                graph[k][j[1]] = j[2]
            if k == j[1]:
                graph[k][j[0]] = j[2]
                
    start = dijkstra(graph, s)
    a_distance = dijkstra(graph, a)
    b_distance = dijkstra(graph, b)
    
    for i in range(1,n+1):
        if start[i] != float('inf') and a_distance[i] != float('inf')and b_distance[i] != float('inf'):
            answer = min(answer, start[i] + a_distance[i] + b_distance[i])
        
    return answer
