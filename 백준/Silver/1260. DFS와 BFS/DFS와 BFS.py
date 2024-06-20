from collections import deque

def bfs(graph, start_node):
    visited = []
    need_visited = deque()
    
    # 시작 노드 설정해주기
    need_visited.append(start_node)
    
    # 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        # 시작 노드를 지정하고
        node = need_visited.popleft()
        
        # 만약 방문한 리스트에 없다면
        if node not in visited:
            # 방문 리스트에 노드를 추가
            visited.append(node)
            
            # 인접 노드들을 방문 예정 리스트에 추가
            # 작은 번호의 노드부터 방문하기 위해 정렬된 순서로 추가
            need_visited.extend(sorted(graph[node]))
                
    return visited
def dfs(graph, start_node):
    visited = []
    need_visited = deque()
    
    # 시작 노드 설정해주기
    need_visited.append(start_node)
    
    # 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        # 시작 노드를 지정하고
        node = need_visited.pop()
        
        # 만약 방문한 리스트에 없다면
        if node not in visited:
            # 방문 리스트에 노드를 추가
            visited.append(node)
            
            # 인접 노드들을 방문 예정 리스트에 추가
            # 작은 번호의 노드부터 방문하기 위해 정렬된 순서로 추가
            need_visited.extend(sorted(graph[node], reverse=True))
                
    return visited
v, e, start = list(map(int,input().split()))
edge = []
adj_list = [[] for _ in range(v+1)]
for x in range(e):
    tmp = list(map(int,input().split()))
    edge.append(tmp[0])
    edge.append(tmp[1])
for i in range(e):
    num1, num2 = edge[2*i], edge[2*i+1]
    adj_list[num1].append(num2)
    adj_list[num2].append(num1)
visited = [False] * len(adj_list)
for d in dfs(adj_list, start):
    print(d, end=' ')
print()
for b in bfs(adj_list, start):
    print(b, end=' ') 

