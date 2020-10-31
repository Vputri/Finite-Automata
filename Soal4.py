import sys

def main():
    transition = [[[0,1],[0]], [[4],[2]], [[4],[3]], [[4],[4]]]
    inputan = input("enter the string: ")
    inputan = list(inputan)
    for index in range(len(inputan)):
        if inputan[index]=='a':
            inputan[index]='0' 
        else:
            inputan[index]='1'

    final = "2"
    start = 0
    i=0 

    trans(transition, inputan, final, start, i)
    print ("rejected") 



def trans(transition, inputan, final, state, i):
    for j in range (len(inputan)):
        for each in transition[state][int(inputan[j])]:
            if each < 4:
                state = each
                if j == len(inputan)-1 and (str(state) in final):
                    print ("accepted") 
                    sys.exit()
                trans(transition, inputan[i+1:], final, state, i)
        i = i+1


main()