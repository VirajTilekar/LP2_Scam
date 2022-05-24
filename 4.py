def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
          
    return list

def check(v,color):
    for neighbour in graph.get(v):
        color_of_neighbour = color_of_vertex.get(neighbour)
        if color_of_neighbour == color:
            return False
    return True

def findColor(v):
    for color in colors:
        if check(v,color):
            return color

graph = {
  'A' : ['B','C'],
  'B' : ['E', 'D'],
  'C' : ['D'],
  'E' : [],
  'D' : [],
}
colors = ['Red','Yellow','Blue','Violet','Green','Orange','Brown']
color_of_vertex = {}

vertex = getList(graph)
        
for v in vertex:
    color_of_vertex[v] = findColor(v)
    
print(color_of_vertex)