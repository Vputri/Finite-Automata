def start(c):
    if (c == 'A' or c == 'M' or c == 'N'): 
        dfa = 1 
    elif (c == 'B' or c == 'C' or c == 'D' or c == 'F' or c == 'L' or c == 'V' or c == 'Y'): 
        dfa = 2
    elif (c == 'K'): 
        dfa = 3
    elif (c == 'G' or c == 'Z'): 
        dfa = 4
    elif (c == 'R' or c == 'S'): 
        dfa = 5
    else: 
        dfa = -1
    return dfa 
  
def state1(c):  
    if (c == 'I'): 
        dfa = 0
    elif (c == 'R' or c == 'D' or c == 'H'): 
        dfa = 1
    elif (c == 'L' or c == 'A'): 
        dfa = 3
    else: 
        dfa = -1
    return dfa 
  
def state2(c): 
    if (c == 'S' or c == 'D' or c == 'H'): 
        dfa = 0
    elif (c == 'L' or c == 'Y' or c == 'E'): 
        dfa = 1
    elif (c == 'I' or c == 'A' or c == 'T' or c == 'R' or c == 'Z'): 
        dfa = 2
    elif (c == 'C' or c == 'U' or c == 'O'): 
        dfa = 3
    elif (c == 'K'): 
        dfa = 6
    else: 
        dfa = -1
    return dfa 
  
   
def state3(c): 
    if (c == 'L' or c == 'I' or c == 'K'): 
        dfa = 0
    elif (c == 'R'): 
        dfa = 2
    elif (c == 'N' or c == 'H' or c == 'T' or c == 'F' or c == 'U'): 
        dfa = 3
    elif (c == 'A'): 
        dfa = 4
    else: 
        dfa = -1
    return dfa 
  
def state4(c): 
    if (c == 'O' or c == 'F'): 
        dfa = 0
    elif (c == 'L' or c == 'I'): 
        dfa = 4
    elif (c == 'D'): 
        dfa = 5
    else:
        dfa = -1
    return dfa 

def state5(c): 
    if (c == 'Y' or c == 'F' or c == 'N'): 
        dfa = 0
    elif (c == 'I' or c == 'F' or c == 'Q' or c == 'A' or c == 'E' or c == 'K'): 
        dfa = 5
    elif (c == 'S'): 
        dfa = 6
    else:
        dfa = -1
    return dfa

def state6(c): 
    if (c == 'A' or c == 'Y'): 
        dfa = 0
    else:
        dfa = -1
    return dfa 
  
def cek(String): 
    l = len(String) 
    dfa = 0
    for i in range(l):  
        if (dfa == 0):  
            dfa = start(String[i])  
        elif (dfa == 1):  
            dfa = state1(String[i])  
        elif (dfa == 2) : 
            dfa = state2(String[i])  
        elif (dfa == 3) : 
            dfa = state3(String[i])  
        elif (dfa == 4) : 
            dfa = state4(String[i]) 
        elif (dfa == 5) : 
            dfa = state5(String[i])  
        elif (dfa == 6) : 
            dfa = state6(String[i])  
 

    if (dfa == 0) : 
        print(String,"ACCEPTED") 
    else: 
        print(String,"NOT ACCEPTED")
   
cek("NADA")
cek("HANIF")
cek("ARDI")
cek("BILI") 
cek("BILAL")  
cek("CICI")
cek("DATUL")
cek("DIYANK") 
cek("FARELL") 
cek("FATONI")
cek("FATTAH") 
cek("GIO") 
cek("KHALIF") 
cek("LUTHFI") 
cek("MAUL")
cek("NARIS") 
cek("REKSA")
cek("RAY") 
cek("SISY") 
cek("VIKA")
cek("YAZID") 
cek("ZIDAN") 
