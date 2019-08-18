def swap_case(s):
    d=[]
    for i in range(0,len(s)):
        if(s[i].isupper()):
            d.append(s[i].lower())
        elif(s[i].islower()):
            d.append(s[i].upper())
        else:
            d.append(s[i])
    return ''.join(d)

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result