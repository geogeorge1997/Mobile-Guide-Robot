import direction_change_head as dir_chg_head

#set_r_path funtion defintion

def set_row_path(direction_list,current_index,next_index,head):

     if(current_index>next_index):

          direction_list,head=dir_chg_head.change_head(direction_list,head,"west")

     else:
          
          direction_list,head=dir_chg_head.change_head(direction_list,head,"east")

     return direction_list,head

#set_column_path funtion defintion

def set_column_path(direction_list,current_index,next_index,head):

     if(current_index>next_index):
          
          direction_list,head=dir_chg_head.change_head(direction_list,head,"north")

     else:
          
          direction_list,head=dir_chg_head.change_head(direction_list,head,"south")

     return direction_list,head
