import graph_dijsktras_file as graph_dij

# Python program for validation of a graph 
# Call Dijsktras Funtion

# import dictionary for graph 
from collections import defaultdict 

#graph is initailized
graph = defaultdict(list)

# function for adding edge to graph
def addEdge(graph,u,v):
    graph[u].append(v)
    
# declaration of graph as dictionary
def addEdge_fun():


    addEdge(graph,'0','1')
    addEdge(graph,'1','0')

    addEdge(graph,'1','2') 
    addEdge(graph,'2','1')

    addEdge(graph,'3','1')
    addEdge(graph,'1','3')

    addEdge(graph,'4','1') 
    addEdge(graph,'1','4')
'''
    addEdge(graph,'0','1')
    addEdge(graph,'1','0')

    addEdge(graph,'0','5') 
    addEdge(graph,'5','0')

    addEdge(graph,'1','4')
    addEdge(graph,'4','1')

    addEdge(graph,'1','2') 
    addEdge(graph,'2','1')

    addEdge(graph,'2','3') 
    addEdge(graph,'3','2')

    addEdge(graph,'3','4')
    addEdge(graph,'4','3')

    addEdge(graph,'3','8')
    addEdge(graph,'8','3')

    addEdge(graph,'4','5') 
    addEdge(graph,'5','4') 

    addEdge(graph,'4','7') 
    addEdge(graph,'7','4')

    addEdge(graph,'5','6')  
    addEdge(graph,'6','5')

    addEdge(graph,'6','7') 
    addEdge(graph,'7','6') 

    addEdge(graph,'7','8')
    addEdge(graph,'8','7')
'''

#call dijsktras fun
def dijsktras_fun_call(current_vertex,target_vertex):   
    
    shortest_path_list=graph_dij.dijsktras_main_fun(graph,current_vertex,target_vertex)
    return(shortest_path_list)       


#print vertex and its corresponding nodes

'''
nodes=['0','1','2','3','4','5','6','7','8']

for i in nodes:
  print(i," : ",graph[i])

'''

