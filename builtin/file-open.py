"""Open a file and write some text to it
"""
import sys
filename = sys.argv[1] 
string = 'Chris'
print('File contents:')
with open(filename,mode='w+') as f:
    print(f.write(string))