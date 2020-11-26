import direction_select_head as dir_sele_head

#structure of graph is initialized

set_row=[[3,1,4]]

set_column=[[2,1,0]]

'''
set_row=[[6,7,8],[5,4,3],[0,1,2]]

set_column=[[6,5,0],[7,4,1],[8,3,2]]
'''

#funtion which is called from p2_main

def search_set_fun(direction_list,current_vertex,next_vertex,head):
          
     val,direction_list,head=set_row_search(direction_list,current_vertex,next_vertex,head)

     if(val==0):
          direction_list,head=set_column_search(direction_list,current_vertex,next_vertex,head)

     return direction_list,head

#funtion defintion for row sets

def set_row_search(direction_list,current_vertex,next_vertex,head):

     val=0
     
     for temp_list in set_row:
          
          if(temp_list.count(current_vertex) and temp_list.count(next_vertex)):

               #index of current and next vertex is selected
               current_index=temp_list.index(current_vertex)
               next_index=temp_list.index(next_vertex)

               #print(current_vertex,next_vertex)
               val=1
               
               #call next fun
               direction_list,head=dir_sele_head.set_row_path(direction_list,current_index,next_index,head)
               
               break
          
     return val,direction_list,head
     

#funtion defintion for coloumn sets          

def set_column_search(direction_list,current_vertex,next_vertex,head):

     for temp_list in set_column:
          
          if(temp_list.count(current_vertex) and temp_list.count(next_vertex)):

               #index of current and next vertex is selected
               current_index=temp_list.index(current_vertex)
               next_index=temp_list.index(next_vertex)

               #print(current_vertex,next_vertex)
               
               #call next fun
               direction_list,head=dir_sele_head.set_column_path(direction_list,current_index,next_index,head)
               
               break

     return direction_list,head
