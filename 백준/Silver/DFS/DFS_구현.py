# 앞으로 찾아서 가야할 노드 & 이미 방문한 노드에 대해서 생각하기 
# 찾아서 가야할 노드면 검색 & 이미 방문한 노드면 무시 

# 스택 활용한 구현
def dfs(graph, start_node):
    # 기본 : 두 개의 리스트를 별도로 관리해줌
    need_visited, visited = list(), list()

    # 시작 노드 결정하기
    need_visited.append(start_node)

    # 만약 아직 방문이 필요한 노드가 있다면, 
    while need_visited:
        # 그 중 가장 마지막 데이터 추출 (스택)
        node = need_visited.pop()
        # 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
            # 방문 목록에 추가 
            visited.append(node)
            # 그 노드에 연결된 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])
    
    return visited

# 큐 활용한 구현
def dfs2(graph, start_node):
    from collections import deque
    # 이번엔 방문이 필요한 원소들을 덱에 담음
    visited = list()
    need_visited = deque()

    # 시작 노드 결정하기
    need_visited.append(start_node)

    # 만약 아직 방문이 필요한 노드가 있다면,
    while need_visited:
        # 그 중 가장 마지막 데이터 추출 (덱)
        node = need_visited.pop()
        # 만약 그 노드가 방문 리스트에 없다면
        if node not in visited:
            # 방문 목록에 추가
            visited.append(node)
            # 그 노드에 연결된 노드들을 방문 예정 덱에 추가
            need_visited.extend(graph[node])
    
    return visited

# 재귀함수 이용한 구현
def dfs_recursive(graph,start,visited=[]):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph,node,visited)
    
    return visited