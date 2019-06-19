import codecs
import sys

filename ='test.txt'

print('Writing to', filename)
with codecs.open(filename, mode='w') as f:
    f.write('Chris') # Only str type can be writen

print('File contents:')
with open(filename,mode='r') as f:
    print(f.read())



    