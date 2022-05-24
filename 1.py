graph = {
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

visited=[]
queue=[]

def bfs(visited,graph,node):
    
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m,end=" ")
        if m==f:
            break
        
        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

def dfs(visited, graph, node,n):  
    if node not in visited:
        print (node,end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            elem = visited.pop()
            visited.append(elem)
            if elem==n:
                break
            else:
                dfs(visited, graph, neighbour,n)
                
a=1

if(a):
    print("Press 1: BFS, 2: DFS")
    b=input()

    if(b=='1'):
        f = input("Enter the number to search : ")
        print("The bfs for the searching element is :")
        bfs(visited,graph,'5')
    
    elif(b=='2'):
        n=input("Enter the no. to be searched:")
        print("Following is the Depth-First Search")
        dfs(visited, graph, '5',n)
        print(" ")

    else:
        print("Invalid Input")

print("")
print("Do you want to continue ? : Press Y/N")
g=input()

while(g=='Y'):
    visited=[]
    queue=[]

    print("Press 1: BFS, 2: DFS")
    b=input()

    if(b=='1'):
        f = input("Enter the number to search : ")
        print("The bfs for the searching element is :")
        bfs(visited,graph,'5')
        if f not in visited:
            print("Not found")
    
    elif(b=='2'):
        n=input("Enter the no. to be searched:")
        print("Following is the Depth-First Search")
        dfs(visited, graph, '5',n)
        print(" ")
        if f not in visited:
            print("Not found")

    else:
        print("Invalid Input")

    print(" ")
    print("Do you want to continue ? : Press Y/N")
    g=input()

    v=0
    while v==0:
        if(g!='Y' or g!='Y'):
            g=input()
        else:
            v=1