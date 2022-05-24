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



import copy

def solution(n, edge):
    def BFS(graph,start):
        visit = []
        hierarchy = []
        way = [start]
        q = []

        while(len(visit)<n):
            hierarchy.append(list(set(way).difference(visit)))
            q = copy.deepcopy(hierarchy[-1])
            way = []
            while(q):
                node = q.pop(0)
                if(node not in visit):
                    visit.append(node)
                    link = [i for i in graph if(node in i)]
                    for new in link:
                        way.append(new[new.index(node)^1])
        return hierarchy
    return len(BFS(edge,1)[-1])



def solution(n, edge):
    visit = []
    way = [1]
    q = []

    while(len(visit)<n):
        last = way
        q = way[:]
        way = []
        while(q):
            node = q.pop()
            if(node not in visit):
                visit.append(node)
                way += [i[i.index(node)^1] for i in edge if(node in i)]
        way = list(set(way).difference(visit))
    return len(last)
