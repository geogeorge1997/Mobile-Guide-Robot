#Shortest Path Calculation

def shortest_path_fun(previous_vertex_list,current_vertex,target_vertex):
    
     sPath_ans_list=[]

     #previous_vertex indicates the Previous Node
     previous_vertex=target_vertex
     
     while(previous_vertex!=current_vertex):

     #Previous Node is added to the list
          
          sPath_ans_list.append(previous_vertex)
          previous_vertex=previous_vertex_list[previous_vertex]

     sPath_ans_list.append(previous_vertex)

     sPath_ans_list.reverse()
     
     return(sPath_ans_list)
     

