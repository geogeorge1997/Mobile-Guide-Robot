import direction_structure as dir_struct

#p2_main_fun defintion

def dir_main_fun(path_list,head,direction_list):

     i=0
     
     while(i+1!=len(path_list)):

          current_vertex=path_list[i]
          next_vertex=path_list[i+1]

          direction_list,head=dir_struct.search_set_fun(direction_list,current_vertex,next_vertex,head)

          i=i+1
          
     return direction_list,head
