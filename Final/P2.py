Time = 0
GRAPH = {
    's': {
      'adj': ['r', 'w'],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    },
    'r': {
      'adj': ['s', 'v'],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    },
    'v': {
      'adj': [],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    },
    'w': {
      'adj': ['s', 't', 'x'],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    },
    't': {
      'adj': ['w', 'x', 'u'],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    },
    'x': {
      'adj': ['w', 't', 'u', 'y'],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    },
    'u': {
      'adj': ['t', 'x', 'y'],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    },
    'y': {
      'adj': ['u', 'x'],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    }
}


def DFS(G):
  for node_name in G:
    vertex = G[node_name]
    vertex['color'] = "WHITE"
    vertex['pie'] = "NIL"
  for node_name in G:
    vertex = G[node_name]
    if vertex['color'] == "WHITE":
      DFS_Visit(node_name)
      

def DFS_Visit(node_name):
  vertex = GRAPH[node_name]
  global Time
  Time += 1
  vertex['d'] = Time
  vertex['color'] = "GRAY"
  for adj_v in vertex['adj']:
    if GRAPH[adj_v]['color'] == "WHITE":
      GRAPH[adj_v]['pie'] = node_name
      DFS_Visit(adj_v)
  vertex['color'] = "BLACK"
  Time += 1
  vertex['f'] = Time


def print_d_and_pie():
  for name in GRAPH:
    print("Vertex", name, ": d=", GRAPH[name]['d'], "𝜋=", GRAPH[name]['pie'])


def main():
  DFS(GRAPH)
  print_d_and_pie()


if __name__ == "__main__":
    main()