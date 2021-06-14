GRAPH = {
    's': {
      'name': 's',
      'adj': ['r', 'w'],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    },
    'r': {
      'name': 'r',
      'adj': ['s', 'v'],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    },
    'v': {
      'name': 'v',
      'adj': [],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    },
    'w': {
      'name': 'w',
      'adj': ['s', 't', 'x'],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    },
    't': {
      'name': 't',
      'adj': ['w', 'x', 'u'],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    },
    'x': {
      'name': 'x',
      'adj': ['w', 't', 'u', 'y'],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    },
    'u': {
      'name': 'u',
      'adj': ['t', 'x', 'y'],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    },
    'y': {
      'name': 'y',
      'adj': ['u', 'x'],
      'color': "",
      'pie': "",
      'd': "",
      'f': ""
    }
}


Time = 0


def DFS(G):
  for name in G:
    vertex = G[name]
    vertex['color'] = "WHITE"
    vertex['pie'] = "NIL"
  for name in G:
    vertex = G[name]
    if vertex['color'] == "WHITE":
      DFS_Visit(vertex)
      

def DFS_Visit(vertex):
  global Time
  Time += 1
  vertex['d'] = Time
  vertex['color'] = "GRAY"
  for adj_v in vertex['adj']:
    if GRAPH[adj_v]['color'] == "WHITE":
      GRAPH[adj_v]['pie'] = vertex['name']
      DFS_Visit(GRAPH[adj_v])
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