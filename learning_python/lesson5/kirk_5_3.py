#/usr/bin/env python3

def func_mac_norm(mac_addr):
    if '.' in mac_addr:
        my_mac = mac_addr[:2]+':'+mac_addr[2:4]+':'+mac_addr[5:7]+':'+mac_addr[7:9]+':'+mac_addr[10:12]+':'+mac_addr[12:14]
        my_string = (my_mac.upper())
        print(my_string)

    if '-' in mac_addr:
        my_mac = mac_addr[:2]+':'+mac_addr[3:5]+':'+mac_addr[6:8]+':'+mac_addr[9:11]+':'+mac_addr[12:14]+':'+mac_addr[15:17]
        my_string = (my_mac.upper())
        print(my_string)


#func_mac_norm('0000.aaaa.bbbb')
func_mac_norm('00-00-aa-aa-bb-bb')
