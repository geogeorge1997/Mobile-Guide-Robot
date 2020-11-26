
# Turn Selection and Calling its Function

import m_black_drive as m_b_d
import m_turn_left as m_t_l
import m_turn_right as m_t_r
import m_white_drive as m_w_d
import m_reverse as m_r

import time

def driver(drive_list):

    for i in drive_list:
        
        print("\n")
        print "Current Direction - ",i

        if(i=="straight"):

            time.sleep(1)
            m_w_d.white_drive()
            m_b_d.black_drive()
            
        elif(i=="right"):

            time.sleep(1)
            m_w_d.white_drive()
            m_t_r.turn_right()
            m_b_d.black_drive()

        elif(i=="left"):

            time.sleep(1)
            m_w_d.white_drive()
            m_t_l.turn_left()
            m_b_d.black_drive()

        else:
            
            time.sleep(1)
            m_r.reverse()
            m_b_d.black_drive()
