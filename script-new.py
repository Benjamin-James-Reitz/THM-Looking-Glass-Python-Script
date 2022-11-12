#!/usr/bin/env python3
# These sites were used as references: https://stackabuse.com/executing-shell-commands-wi>
# https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the->

#set up initial conditions for the target port search
import subprocess
low_port=9000
high_port=13790
targetIP = "10.10.252.52"
print(targetIP)
#initialize loop_key variable:
loop_key="higher"

while loop_key=="Higher" or "Lower":
    print('low = '  + str(low_port) + ', high = ' + str(high_port))
#a good place to use floor division to cut off the extra digit
    mid_port=(high_port+low_port)//2
    print('Trying port ' + str(mid_port))
    #attempt to connect to the mid port
    result = subprocess.run(['ssh', 'root@' + str(targetIP), '-oHostKeyAlgorithms=+ssh-rsa', '-p', str(mid_port)], stdout=subprocess.PIPE)
    # prep the decoded output variable
    msg = result.stdout
    decoded_msg = msg.decode('utf-8')
    # print result of attempted ssh connection
    print(decoded_msg)

    if "Higher" in decoded_msg:
        #print("yes I see the words Higher")
        high_port=mid_port
        print(high_port)
        loop_key="Higher"
    elif "Lower" in decoded_msg:
        low_port=mid_port
        print(low_port)
        loop_key="Lower"
    else:
        print("You found the secret port - " + str(mid_port))
        exit()
