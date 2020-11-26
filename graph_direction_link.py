import graph_creation_file as graph_create
import direction_main_file as dir_main
import direction_selector as dir_select
import rob_driver as r_drive

#call addEdge fun in graph file 
graph_create.addEdge_fun()

#call dijsktras_call in graph file
continue_value=1

current_vertex=0
head="north"
direction_list=[]

while(continue_value==1):

     target_vertex=raw_input("Enter Destination : ")
     shortest_path_list=graph_create.dijsktras_fun_call(current_vertex,target_vertex)
     current_vertex=shortest_path_list[len(shortest_path_list)-1]
     
     direction_list,head=dir_main.dir_main_fun(shortest_path_list,head,direction_list)

     print("\n")
     print "Path List - ",shortest_path_list
     #print("Direction List - ",direction_list)

     turn_list=dir_select.selector(direction_list)
     print "Direction List - ",turn_list

     r_drive.driver(turn_list)
     
     direction_list=[]
     print("\nDestination Reached\n")
     
     continue_value=int(raw_input("Enter 1 to Continue : "))
     

#After visting all required places

current_vertex=shortest_path_list[len(shortest_path_list)-1]         
shortest_path_list=graph_create.dijsktras_fun_call(current_vertex,0)

direction_list,head=dir_main.dir_main_fun(shortest_path_list,head,direction_list)

print("\n")
print "Path List - ",shortest_path_list
#print("Direction List - ",direction_list)

turn_list=dir_select.selector(direction_list)
print "Direction List - ",turn_list

r_drive.driver(turn_list)


print("\nDestination Reached\n")
