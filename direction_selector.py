# List of Direction

def selector(dir_list):

    num_list=["north","east","south","west"]
    selector_list=[]

    for i in dir_list:

        tag_one=num_list.index(i[0])
        tag_two=num_list.index(i[1])

        selector_num=tag_one-tag_two

        if(selector_num==0):
            selector_list.append("straight")
            
        elif(selector_num==-1 or selector_num==3):
            selector_list.append("right")
            
        elif(selector_num==-3 or selector_num==1):
            selector_list.append("left")
            
        else:
            selector_list.append("reverse")

    return selector_list
            
