"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
"""
def count_substring(string, sub_string):
    count_rec=0
    for i in range(0, len(string)):
        substr = string[i:i+len(sub_string)]
        if substr == sub_string:
            count_rec = count_rec+1    
    return count_rec

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count