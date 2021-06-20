import heapq # For 


GRAPH = {
  's': {'adj': {'t': 3, 'y': 5}, 'd': "", 'pie': ""},
  't': {'adj': {'x': 6, 'y': 2}, 'd': "", 'pie': ""},
  'x': {'adj': {'z': 2}, 'd': "", 'pie': ""},
  'y': {'adj': {'t': 1, 'x': 4, "z": 6}, 'd': "", 'pie': ""},
  'z': {'adj': {'s': 3, 'x': 7}, 'd': "", 'pie': ""}
}


def initialize(G):
  for node_name in G:
    GRAPH[node_name]['d'] = float("INF")
    GRAPH[node_name]['pie'] = "NIL"
  GRAPH['s']['d'] = 0


def Dijkstra(G, s):
  initialize(G)
  S = []
  Queue = [node for node in G]
  while Queue:
    u = heapq.heappop(Queue)
    S.append(u)
    for vertex in GRAPH[u]['adj']:
      relax(u, vertex)
  
  
def relax(u, v):
  if GRAPH[v]['d'] > GRAPH[u]['d'] + GRAPH[u]['adj'][v]:
      GRAPH[v]['d'] = GRAPH[u]['d'] + GRAPH[u]['adj'][v]
      GRAPH[v]['pie'] = u


def print_shortest_path(destination):
  path = [destination]
  while True:
    pie = GRAPH[destination]['pie']
    if pie == "NIL":
      break
    path.append(pie)
    destination = pie
  path.reverse()
  for index in range(len(path)):
    if index == len(path) - 1:
      print(path[index])
      break
    print(path[index], end='→')

def main():
  Dijkstra(GRAPH, 's')
  print("Vertex s to y :", end='')
  print_shortest_path('y')
  print("Total costs from s to y :", GRAPH['y']['d'])
  print("Vertex s to z :", end='')
  print_shortest_path('z')
  print("Total costs from s to z :", GRAPH['z']['d'])


if __name__ == "__main__":
    main()