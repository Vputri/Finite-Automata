def start(c): 
    if (c == '0'): 
        dfa = 1 
    else: 
        dfa = -1
    return dfa 
  
def state1(c):  
    if (c == '1'): 
        dfa = 2
    else: 
        dfa = -1
    return dfa 
  
def state2(c): 
    if (c == '1'): 
        dfa = 4
    elif (c == 'a'): 
        dfa = 3
    else: 
        dfa = -1
    return dfa 
   
def state3(c): 
    if (c == 'b'): 
        dfa = 2
    else: 
        dfa = -1
    return dfa 
  
def state4(c): 
    if (c == '0'): 
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

    if (dfa == 0) : 
        print(String, "ACCEPTED") 
    else: 
        print(String, "NOT ACCEPTED")
   
cek("0110") 
cek("01a10") 
cek("01b10") 
cek("01ab10") 
cek("01aba10") 
cek("01abb10") 
cek("01abab10") 
