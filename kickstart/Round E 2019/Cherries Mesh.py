class VertexNode:
    def __init__(self):
        self.visited = 0 # 0 not visited 1 seen 2 done
        self.edge_list = []


def iterate_graph(vertex_list, vertex):
    sugar_count = 0
    for edge in vertex_list[vertex].edge_list: 
        if vertex_list[edge].visited == 0:
            sugar_count += 1
            vertex_list[edge].visited = 1
            sugar_count += iterate_graph(vertex_list, edge)
            vertex_list[edge].visited = 2
    return sugar_count


def bfs(vertex_list):
    sugar_count, flag = 0, False 
    for vertex in range(len(vertex_list)):        
        if vertex_list[vertex].visited == 0:
            if flag: 
                sugar_count += 2
            else:
                flag = True
            vertex_list[vertex].visited = 1
            sugar_count += iterate_graph(vertex_list, vertex)
            vertex_list[vertex].visited = 2    
    if sugar_count == 0:
        return 2
    else :
        return sugar_count


def main():
    T = int(input())
    for case in range(1, T + 1):
        the_string = input()
        N, M = the_string.split()
        N, M = int(N), int(M) # number of cheries2 # number of black sweet strands
        
        vertex_list = []
        for vertex in range(N):
            vertex_list.append(VertexNode())
        for vertex in range(M):
            the_string = input()
            v1, v2 = the_string.split()
            v1, v2 = int(v1) - 1, int(v2) - 1

            vertex_list[v1].edge_list.append(v2)
            vertex_list[v2].edge_list.append(v1)
        print("Case #", case, ": ", bfs(vertex_list))

if __name__ == '__main__':
    main()
