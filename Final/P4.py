import heapq


GRAPH = {
  's': {'adj': {'t': 3, 'y': 5}, 'd': "", 'pie': ""},
  't': {'adj': {'x': 6, 'y': 2}, 'd': "", 'pie': ""},
  'x': {'adj': {'z': 2}, 'd': "", 'pie': ""},
  'y': {'adj': {'t': 1, 'x': 4, "z": 6}, 'd': "", 'pie': ""},
  'z': {'adj': {'s': 3, 'x': 7}, 'd': "", 'pie': ""}
}


def Dijkstra(G, s):
  initialize(G)
  S = []
  Queue = [node for node in G]
  while Queue:
    u = heapq.heappop(Queue)
    S.append(u)
    for vertex in GRAPH[u]['adj']:
      relax(u, vertex)

def initialize(G):
  for node_name in G:
    GRAPH[node_name]['d'] = float("INF")
    GRAPH[node_name]['pie'] = "NIL"
  GRAPH['s']['d'] = 0
  
  
def relax(u, v):
  if GRAPH[v]['d'] > GRAPH[u]['d'] + GRAPH[u]['adj'][v]:
      GRAPH[v]['d'] = GRAPH[u]['d'] + GRAPH[u]['adj'][v]
      GRAPH[v]['pie'] = u


def main():
  Dijkstra(GRAPH, 's')
  for node in GRAPH:
    print("Node", node, "-> d:", GRAPH[node]['d'], "𝜋:", GRAPH[node]['pie'])


if __name__ == "__main__":
    main()