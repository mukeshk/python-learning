"""
Input Format

The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

"""
if __name__ == '__main__':
    N = int(raw_input())
    dataArray = []
    while(N>0):
        N = N-1
        inputparam = raw_input().split()
        if inputparam[0]=="print" :
            print(dataArray)
        elif inputparam[0]=="insert" :
            dataArray.insert(int(inputparam[1]),int(inputparam[2]))
        elif inputparam[0]=="append" :
            dataArray.append(int(inputparam[1]))
        elif inputparam[0]=="sort" :
            dataArray.sort()
        elif inputparam[0]=="reverse" :
            dataArray.reverse()
        elif inputparam[0]=="pop" :
            dataArray.pop()    
        elif inputparam[0]=="remove" :
            dataArray.remove(int(inputparam[1])) 