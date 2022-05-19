# when graph like this [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def BFS(graph,start):
    visit = []
    q = []

    q.append(start)

    while(q):
        node = q.pop(0)
        if(node not in visit):
            visit.append(node)
            linked = [i for i in graph if(node in i)]
            for new in linked:
                q.append(new[new.index(node)^1])
    return visit
