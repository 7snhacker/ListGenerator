print("""  _     ___ ____ _____ ____ _____ _   _ 
 | |   |_ _/ ___|_   _/ ___| ____| \ | |
 | |    | |\___ \ | || |  _|  _| |  \| |
 | |___ | | ___) || || |_| | |___| |\  |
 |_____|___|____/ |_| \____|_____|_| \_|
                                        """)
print("instagram : 7snhacker")
import string
import random
letters = string.ascii_lowercase
r = open("list.txt", "w")
li = 0
while li == 0:
    r.write( ''.join(random.choice(letters) for i in range(4))+'\r\n')
    

        
r.close()
 
    
