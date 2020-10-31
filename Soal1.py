def start(c): 
    if (c == '0' or c == '2' or c == '4' or c == '6' or c == '8'): 
        dfa = 0
    elif (c == '1' or c == '3' or c == '5' or c == '7' or c == '9'): 
        dfa = 1
    else: 
        dfa = -1
    return dfa 
  
def state1(c):  
    if (c == '0' or c == '2' or c == '4' or c == '6' or c == '8'): 
        dfa = 0
    elif (c == '1' or c == '3' or c == '5' or c == '7' or c == '9'): 
        dfa = 1
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

    if (dfa == 0) : 
        print(String,"ACCEPTED") 
    else: 
        print(String,"NOT ACCEPTED")
   
cek("a")  
cek("b") 
cek("1")
cek("2")
cek("11")
cek("12")
cek("21")
cek("22")
cek("111")  
cek("112") 
cek("121")
cek("222")
cek("1111")
cek("1211")
cek("1121")
cek("1112")
cek("2222")
cek("2122")
cek("2212")
