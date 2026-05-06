from .point import Point

class Graph:
    def __init__(self, eps, minPts):
        self._graph = dict()
        self._eps = eps
        self._minPts = minPts

    def __str__(self):
        str = ''
        for key in self._graph:
            str += f"{key}: "
            for elem in self._graph[key]:
                str += f"  {elem}"
            str += '\n'
        return str

    def push_point(self, point):
        if point in self._graph:
            return
            
        self._graph[point] = []
        for elem in self._graph:
            if point.dist(elem) <= self._eps and elem != point:
                self._graph[elem].append(point)
                self._graph[point].append(elem)
                
        self._recalc_graph()

    def _recalc_graph(self):
        core_nodes = set()
        for p, neigbors in self._graph.items():
            if len(neigbors) + 1 >= self._minPts:
                core_nodes.add(p)
        visited = set()
        claster_id = 0
        for p in core_nodes:
            if p not in visited:
                claster_id += 1
                stack = [p]
                while stack:
                    node = stack.pop()
                    if node in visited or node not in core_nodes:
                        continue
                    node.set_color(claster_id)
                    visited.add(node)
                    stack.extend(self._graph[node])
        for p in self._graph:
            if p not in core_nodes:
                flag = False
                for neigbour in self._graph[p]:
                    if neigbour.get_color != 0:
                        flag = True
                        p.set_color(neigbour.get_color())
                        break
                if flag == False:
                    p.set_color(0)


        
    
    def get_graph(self):
        return self._graph
    
    def get_keys(self):
        return [*self._graph]
    
