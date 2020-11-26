import graph_path_calculation_file as graph_path

# function of dijsktras

def dijsktras_main_fun(graph,current_vertex,target_vertex):


     current_vertex_a=int(current_vertex)
     
     #Shortest path 

     #previous_vertex_list contain previous node information

     previous_vertex_list=[5,5,5,5,5]
     #previous_vertex_list=[9,9,9,9,9,9,9,9,9]
     
     sptSet=[]
     #Distance Values is initilized for all vertices
     #100 ... INFINITY

     distane_values_list=[100,100,100,100,100]
     #distane_values_list=[100,100,100,100,100,100,100,100,100]

     sptSet.append(current_vertex)

     #temp_List contain all vertices connected to current_vertex
     temp_list=[]
     temp_list=graph[current_vertex]

     distane_values_list[int(current_vertex)]=0

     current_value=distane_values_list[int(current_vertex)]


     while(len(sptSet)!=5):
       
       for i in temp_list:
    
         if(distane_values_list[int(i)]>current_value+1):
              
           distane_values_list[int(i)]=current_value+1
           previous_vertex_list[int(i)]=int(current_vertex)

       #Next Vertex is selected which is not present in sptSet
       i=1
       temp_distane_values_list=[]
       temp_distane_values_list=list(distane_values_list)
       while(i==1):
    
         shortest_num_position=temp_distane_values_list.index(min(temp_distane_values_list))
         if(str(shortest_num_position) in sptSet):
           temp_distane_values_list[shortest_num_position]=100
      
         else:
           i=0
  
       sptSet.append(str(shortest_num_position))

       #Next source vertex is initilized
       current_vertex=str(shortest_num_position)
       current_value=distane_values_list[int(current_vertex)]
       temp_list=[]
       temp_list=graph[current_vertex]

#next conatin distance Values and Previous Vertex Lists

     '''

     print("Final Set : ",disVal)
     print("Final Set : ",a_List)

     '''

     shortest_path_list=graph_path.shortest_path_fun(previous_vertex_list,current_vertex_a,int(target_vertex))

     return(shortest_path_list)
